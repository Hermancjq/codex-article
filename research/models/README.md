# Intensity forecasting and conditional deployment models

`transition_models.py` contains importable functions and a CLI. It does not bundle observations, engine performance data, or calibrated scenario parameters. Source authenticity and statistical scope must be verified upstream. `year,i` rows are accepted, as are canonical `year,fuel_intensity_kg_tkm` columns; if a `verification_status` column exists, every row must say `verified`.

## Empirical forecast API

```python
from transition_models import load_intensity_csv, rolling_forecast, latest_forecast, run
rows = load_intensity_csv("source/verified_data.csv")
evaluation = rolling_forecast(rows, min_differences=8)
projection = latest_forecast(rows, min_differences=8)
results = run(rows)  # Includes prior and pandemic-training sensitivities.
```

The h=1 rolling comparison uses a minimum of eight valid, consecutive annual log differences. B0 keeps the latest intensity unchanged; B1 adds an unshrunk mean log drift; B2 uses a normal-inverse-gamma posterior for a shrunk drift. B2 reports a median and 80%/95% central predictive intervals on the intensity scale. Exponentiated Student-t predictions have no finite positive moments, so no original-scale predictive mean is claimed.

All models use the same eligible origins and training differences. MAE and MASE are reported; a zero training MASE denominator is left undefined. Every forecast stores origin, target, training maximum year, training difference count, and error. In pandemic sensitivity, any annual difference touching 2020, 2021, or 2022 is omitted from training; no gaps are bridged. Actual next-year test outcomes are retained.

For an eleven-year 2015–2025 series, only 2024 and 2025 meet the eight-difference rolling training threshold. These two folds are marked `diagnostic_only`, not evidence of robust model superiority. Pandemic-exclusion training has only six differences and is explicitly skipped. Nothing silently relaxes the threshold.

`NIGPrior` defaults to mu=0, kappa=1, alpha=2, beta=0.05². These are analyst assumptions. `run` also evaluates beta=0.02² and 0.10². No prior is claimed to measure engine technology or capability.

## Conditional deployment API

```python
from transition_models import fuel_ratio, required_deployment_rate, corner_bounds, sobol_stress_test
# config must be supplied after documenting parameter evidence and assumptions.
conditional = sobol_stress_test(config)
```

The configuration is an explicit dictionary/JSON with this schema (placeholders below are not runnable values):

```text
{
  "horizon": INTEGER_YEARS,
  "target_fuel_ratio": POSITIVE_TARGET_RELATIVE_TO_BASE_YEAR,
  "ranges": {
    "g": [ACTIVITY_LOG_GROWTH_LOW, ACTIVITY_LOG_GROWTH_HIGH],
    "b": [BASELINE_INTENSITY_LOG_DECLINE_LOW, BASELINE_INTENSITY_LOG_DECLINE_HIGH],
    "theta": [REALIZED_INCREMENTAL_BENEFIT_LOW, REALIZED_INCREMENTAL_BENEFIT_HIGH],
    "r": [ANNUAL_FUEL_WEIGHTED_ADOPTION_LOW, ANNUAL_FUEL_WEIGHTED_ADOPTION_HIGH]
  },
  "tau_values": [NONNEGATIVE_DEPLOYMENT_DELAYS],
  "parameter_evidence": {"each_parameter": "citation or explicitly labeled stress-test assumption"},
  "sobol_power": 12,
  "check_convergence": true,
  "seed": 20261016
}
```

No g, b, theta, r, or tau bounds are hard-coded. `theta` must lie in [0,1), r in [0,1], and tau must be nonnegative. Deployment refers to the fuel-use-weighted share, not aircraft counts. Incremental efficiency is relative to the baseline path, so historical efficiency improvements should not be double-counted.

The model is `R_h=exp[(g-b)h]*(1-theta*[1-(1-r)^max(h-tau,0)])`. `required_deployment_rate` returns analytic thresholds or explicit impossible/baseline-sufficient states. It never clips an infeasible required share into a feasible result. `corner_bounds` computes exact best/worst domain corners from model monotonicity. Cumulative future fuel sums h=1,...,H and uses base-year annual fuel as its unit.

Sobol points cover the supplied rectangular assumption domain, separately for each delay. Default resolution is 2^12 points, compared with 2^14 using the same scrambling seed. Output fractions and quantiles describe the chosen design space. They are not empirical probabilities, confidence intervals, or estimates of China's engine deployment capabilities. The routine does not claim variance-based Sobol sensitivity indices.

## CLI and validation

```bash
python models/transition_models.py source/verified_data.csv --output output/transition
python models/transition_models.py source/verified_data.csv --scenario-config documented_ranges.json --output output/transition --save-draws
python models/test_transition_models.py
```

Outputs are `transition_results.json`, `rolling_h1_forecasts.csv` when any folds are eligible, and optionally `conditional_scenario_design.csv`. Empirical forecasting and conditional scenarios occupy separate JSON blocks. Without a scenario configuration, the scenario block explicitly says it was skipped.

Eleven synthetic mathematical checks verify conjugate calculations, multi-step predictive variance, no future leakage, sample-size skips, no bridging of missing/excluded years, undefined zero-denominator MASE, adoption boundaries, analytic/numeric threshold agreement, model monotonicity, exact corner bounds, constant domains, and deterministic Sobol reproducibility. These checks contain synthetic inputs only and are not evidence of empirical findings.
