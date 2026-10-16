"""Small-sample intensity forecasts and explicitly conditional deployment scenarios.

No observations or calibrated technology ranges are bundled. ``run`` accepts rows
with ``year`` and ``i`` (or the canonical ``fuel_intensity_kg_tkm``). Statistical
forecasts use only supplied historical observations. Deployment scenarios require
an explicit parameter configuration and never imply empirical adoption forecasts.

CLI:
    python transition_models.py verified_data.csv --output models/output
    python transition_models.py verified_data.csv --scenario-config ranges.json \
        --output models/output --save-draws

Scenario JSON requires horizon, ranges {g,b,theta,r}, and tau_values. The optional
fields are target_fuel_ratio (1), sobol_power (12), seed (20261016), and
check_convergence (true). Ranges and delays have no calibrated defaults.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
import json
import math
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import numpy as np
from scipy import stats
from scipy.stats import qmc


PANDEMIC_YEARS = frozenset({2020, 2021, 2022})
PARAMETER_NAMES = ("g", "b", "theta", "r")


@dataclass(frozen=True)
class NIGPrior:
    """Normal-inverse-gamma prior; beta is a scale, not a rate parameter."""

    mu: float = 0.0
    kappa: float = 1.0
    alpha: float = 2.0
    beta: float = 0.05 ** 2

    def __post_init__(self):
        if not all(math.isfinite(x) for x in asdict(self).values()):
            raise ValueError("Prior parameters must be finite")
        if self.kappa <= 0 or self.alpha <= 0 or self.beta <= 0:
            raise ValueError("Prior kappa, alpha, and beta must be positive")


@dataclass(frozen=True)
class NIGPosterior:
    n: int
    mu: float
    kappa: float
    alpha: float
    beta: float


def normalize_rows(rows: Iterable[Mapping]) -> list[dict]:
    """Validate supplied intensity observations; do not interpolate or verify sources."""
    output = []
    for source in rows:
        if "verification_status" in source and source["verification_status"] != "verified":
            raise ValueError("Supplied verification_status must equal 'verified'")
        value = source.get("i", source.get("fuel_intensity_kg_tkm"))
        if value is None:
            raise ValueError("Each row requires i or fuel_intensity_kg_tkm")
        raw_year = float(source["year"])
        if not math.isfinite(raw_year) or not raw_year.is_integer():
            raise ValueError("year must be a finite integer")
        intensity = float(value)
        if not math.isfinite(intensity) or intensity <= 0:
            raise ValueError("Intensity must be finite and strictly positive")
        output.append({"year": int(raw_year), "i": intensity})
    output.sort(key=lambda row: row["year"])
    if len({row["year"] for row in output}) != len(output):
        raise ValueError("Duplicate years require source reconciliation")
    return output


def load_intensity_csv(path: str | Path) -> list[dict]:
    """Read canonical verified input; provenance verification remains caller work.

    If verification_status metadata is supplied it is enforced. A two-column
    year/i extract is accepted for integration after upstream source verification;
    naming a CSV 'verified' is not treated as evidence of authenticity.
    """
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        return normalize_rows(csv.DictReader(handle))


def annual_differences(rows: Iterable[Mapping], exclude_years: Iterable[int] = ()) -> list[dict]:
    """Use adjacent calendar years only; never bridge gaps or omitted pandemic years."""
    data = normalize_rows(rows)
    excluded = frozenset(int(year) for year in exclude_years)
    differences = []
    for previous, current in zip(data, data[1:]):
        if current["year"] != previous["year"] + 1:
            continue
        if previous["year"] in excluded or current["year"] in excluded:
            continue
        differences.append({
            "start": previous["year"], "end": current["year"],
            "log_change": math.log(current["i"]) - math.log(previous["i"]),
            "absolute_naive_error": abs(current["i"] - previous["i"]),
        })
    return differences


def fit_nig(changes: Sequence[float], prior: NIGPrior | None = None) -> NIGPosterior:
    """Conjugate posterior for iid annual log-intensity increments."""
    prior = prior or NIGPrior()
    values = np.asarray(changes, dtype=float)
    if values.ndim != 1 or not np.all(np.isfinite(values)):
        raise ValueError("changes must be a one-dimensional finite sequence")
    n = len(values)
    if n == 0:
        raise ValueError("At least one annual log difference is needed")
    mean = float(values.mean())
    kappa = prior.kappa + n
    mu = (prior.kappa * prior.mu + n * mean) / kappa
    beta = (prior.beta + 0.5 * float(np.sum((values - mean) ** 2))
            + prior.kappa * n / (2 * kappa) * (mean - prior.mu) ** 2)
    return NIGPosterior(n=n, mu=mu, kappa=kappa,
                        alpha=prior.alpha + n / 2, beta=beta)


def predictive_intensity(latest_intensity: float, posterior: NIGPosterior,
                         horizon: int = 1, levels: Sequence[float] = (0.8, 0.95)) -> dict:
    """Student-t log-scale prediction; original-scale median and central intervals.

    No original-scale predictive mean is returned. Exponentiated Student-t draws
    do not have finite positive moments, so exp(location) is explicitly a median.
    """
    if not math.isfinite(latest_intensity) or latest_intensity <= 0:
        raise ValueError("latest_intensity must be finite and positive")
    if isinstance(horizon, bool) or int(horizon) != horizon or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    h = int(horizon)
    location = math.log(latest_intensity) + h * posterior.mu
    scale = math.sqrt(posterior.beta / posterior.alpha * (h + h * h / posterior.kappa))
    df = 2 * posterior.alpha
    result = {"point_summary": "median", "median": math.exp(location),
              "log_location": location, "log_scale": scale, "degrees_of_freedom": df,
              "horizon": h, "intervals": {}}
    for level in levels:
        if not 0 < level < 1:
            raise ValueError("Interval levels must be strictly between 0 and 1")
        quantile = float(stats.t.ppf((1 + level) / 2, df=df))
        lower, upper = math.exp(location - scale * quantile), math.exp(location + scale * quantile)
        result["intervals"][str(int(round(100 * level)))] = {"lower": lower, "upper": upper}
    return result


def _score_forecasts(forecasts: list[dict]) -> dict:
    scores = {}
    groups = {"all": forecasts,
              "pandemic_transition": [row for row in forecasts if row["pandemic_transition"]],
              "other_transition": [row for row in forecasts if not row["pandemic_transition"]]}
    for group_name, group in groups.items():
        scores[group_name] = {}
        for model in ("B0", "B1", "B2"):
            selected = [row for row in group if row["model"] == model]
            defined_mase = [row["scaled_absolute_error"] for row in selected
                            if row["scaled_absolute_error"] is not None]
            entry = {"n_test": len(selected),
                     "MAE": float(np.mean([row["absolute_error"] for row in selected])) if selected else None,
                     "MASE": float(np.mean(defined_mase)) if defined_mase else None,
                     "n_MASE": len(defined_mase),
                     "test_years": [row["target_year"] for row in selected]}
            if model == "B2":
                for level in ("80", "95"):
                    entry[f"coverage_{level}"] = float(np.mean([
                        row["intervals"][level]["lower"] <= row["actual"] <= row["intervals"][level]["upper"]
                        for row in selected])) if selected else None
                    entry[f"mean_width_{level}"] = float(np.mean([
                        row["intervals"][level]["upper"] - row["intervals"][level]["lower"]
                        for row in selected])) if selected else None
            scores[group_name][model] = entry
    return scores


def rolling_forecast(rows: Iterable[Mapping], min_differences: int = 8,
                     prior: NIGPrior | None = None,
                     exclude_years: Iterable[int] = ()) -> dict:
    """Strict rolling-origin h=1 comparison of no drift, drift, and shrunk drift.

    All three models share the same eligible origins and training differences.
    An excluded-year sensitivity omits differences with either endpoint excluded;
    it still evaluates actual next-year observations, including pandemic shocks.
    """
    if min_differences < 1 or int(min_differences) != min_differences:
        raise ValueError("min_differences must be a positive integer")
    data = normalize_rows(rows)
    prior = prior or NIGPrior()
    excluded = frozenset(int(year) for year in exclude_years)
    by_year = {row["year"]: row for row in data}
    forecasts, skips = [], []
    for origin in data:
        target = by_year.get(origin["year"] + 1)
        if target is None:
            continue
        training = [row for row in data if row["year"] <= origin["year"]]
        differences = annual_differences(training, excluded)
        if len(differences) < min_differences:
            skips.append({"origin_year": origin["year"], "target_year": target["year"],
                          "n_valid_differences": len(differences),
                          "reason": "insufficient_prior_annual_differences"})
            continue
        changes = [row["log_change"] for row in differences]
        posterior = fit_nig(changes, prior)
        predictive = predictive_intensity(origin["i"], posterior)
        points = {"B0": origin["i"],
                  "B1": math.exp(math.log(origin["i"]) + float(np.mean(changes))),
                  "B2": predictive["median"]}
        denominator = float(np.mean([row["absolute_naive_error"] for row in differences]))
        for model, point in points.items():
            error = abs(point - target["i"])
            result = {"model": model, "origin_year": origin["year"],
                      "target_year": target["year"], "training_max_year": origin["year"],
                      "n_valid_differences": len(differences), "horizon": 1,
                      "point_summary": "median_or_deterministic_point", "prediction": point,
                      "actual": target["i"], "absolute_error": error,
                      "mase_denominator": denominator,
                      "scaled_absolute_error": error / denominator if denominator > 0 else None,
                      "pandemic_transition": bool({origin["year"], target["year"]} & PANDEMIC_YEARS)}
            if model == "B2":
                result["intervals"] = predictive["intervals"]
            forecasts.append(result)
    n_origins = len(forecasts) // 3
    return {"analysis_type": "empirical_out_of_sample_forecast_evaluation",
            "status": "completed" if n_origins else "skipped_insufficient_valid_differences",
            "minimum_training_differences": int(min_differences),
            "excluded_training_endpoint_years": sorted(excluded), "prior": asdict(prior),
            "n_test_origins": n_origins,
            "evaluation_purpose": "diagnostic_only" if n_origins < 5 else "descriptive_rolling_evaluation",
            "small_test_sample_warning": n_origins < 5,
            "limitations": ["Predictive performance is descriptive in a small annual sample.",
                            "Priors are transparent analyst choices, not empirically calibrated engine parameters.",
                            "The log-increment model assumes constant drift and iid Gaussian increments.",
                            "No engine-technology or policy causal effect is identified."],
            "scores": _score_forecasts(forecasts), "forecasts": forecasts, "skipped_origins": skips}


def latest_forecast(rows: Iterable[Mapping], min_differences: int = 8,
                    prior: NIGPrior | None = None, exclude_years: Iterable[int] = (),
                    horizon: int = 1) -> dict:
    """Latest historical posterior/projection; explicit skip for inadequate data."""
    data = normalize_rows(rows)
    prior = prior or NIGPrior()
    excluded = frozenset(int(year) for year in exclude_years)
    differences = annual_differences(data, excluded)
    result = {"analysis_type": "empirical_conditional_statistical_projection",
              "n_valid_differences": len(differences), "prior": asdict(prior),
              "excluded_training_endpoint_years": sorted(excluded)}
    if not data or len(differences) < min_differences:
        return {**result, "status": "skipped_insufficient_valid_differences"}
    posterior = fit_nig([row["log_change"] for row in differences], prior)
    return {**result, "status": "completed", "origin_year": data[-1]["year"],
            "posterior": asdict(posterior),
            "forecast": predictive_intensity(data[-1]["i"], posterior, horizon=horizon)}


def _as_output(value):
    value = np.asarray(value)
    return float(value) if value.ndim == 0 else value


def _validate_finite(**values):
    for name, value in values.items():
        if not np.all(np.isfinite(np.asarray(value, dtype=float))):
            raise ValueError(f"{name} must be finite")


def adoption_share(h, r, tau):
    """Fuel-use-weighted adoption, not aircraft-count replacement."""
    _validate_finite(h=h, r=r, tau=tau)
    h, r, tau = np.broadcast_arrays(np.asarray(h, dtype=float), np.asarray(r, dtype=float),
                                    np.asarray(tau, dtype=float))
    if np.any(h < 0) or np.any(tau < 0) or np.any((r < 0) | (r > 1)):
        raise ValueError("h,tau must be nonnegative and r in [0,1]")
    elapsed = np.maximum(h - tau, 0)
    return _as_output(1 - np.power(1 - r, elapsed))


def fuel_ratio(h, g, b, theta, r, tau):
    """Conditional F_(T+h)/F_T; g,b are continuous log rates per year."""
    _validate_finite(g=g, b=b, theta=theta)
    theta = np.asarray(theta, dtype=float)
    if np.any((theta < 0) | (theta >= 1)):
        raise ValueError("theta must be in [0,1)")
    share = adoption_share(h, r, tau)
    ratio = np.exp((np.asarray(g) - np.asarray(b)) * np.asarray(h)) * (1 - theta * share)
    if not np.all(np.isfinite(ratio)):
        raise ValueError("Scenario produces nonfinite ratios; restrict the parameter domain")
    return _as_output(ratio)


def cumulative_fuel_ratio(horizon: int, g, b, theta, r, tau):
    """Sum annual future fuel/F_T, h=1,...,H, in baseline-year-fuel units."""
    if isinstance(horizon, bool) or int(horizon) != horizon or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    return _as_output(sum(np.asarray(fuel_ratio(h, g, b, theta, r, tau))
                          for h in range(1, int(horizon) + 1)))


def required_deployment_rate(horizon: int, g: float, b: float, theta: float,
                             tau: float, target_fuel_ratio: float = 1) -> dict:
    """Exact annual deployment threshold, with impossible cases left explicit."""
    if isinstance(horizon, bool) or int(horizon) != horizon or horizon < 0:
        raise ValueError("horizon must be a nonnegative integer")
    _validate_finite(g=g, b=b, theta=theta, tau=tau, target_fuel_ratio=target_fuel_ratio)
    if not 0 <= theta < 1 or tau < 0 or target_fuel_ratio <= 0:
        raise ValueError("Require theta in [0,1), tau>=0, and positive target")
    baseline = math.exp((g - b) * horizon)
    result = {"horizon": int(horizon), "target_fuel_ratio": target_fuel_ratio,
              "baseline_fuel_ratio": baseline, "required_share": None,
              "required_r": None, "analysis_type": "conditional_analytic_frontier"}
    if baseline <= target_fuel_ratio:
        return {**result, "status": "baseline_satisfies_target", "required_share": 0.0,
                "required_r": 0.0}
    if theta == 0:
        return {**result, "status": "impossible_zero_technical_benefit"}
    required_share = (1 - target_fuel_ratio / baseline) / theta
    result["required_share"] = required_share
    if required_share > 1 + 1e-12:
        return {**result, "status": "impossible_even_with_full_adoption"}
    if horizon <= tau:
        return {**result, "status": "impossible_before_deployment_begins"}
    share = min(required_share, 1.0)
    rate = 1.0 if share == 1 else -math.expm1(math.log1p(-share) / (horizon - tau))
    return {**result, "status": "deployment_threshold_exists", "required_r": rate}


def _validate_scenario_config(config: Mapping) -> dict:
    if "horizon" not in config or "ranges" not in config or "tau_values" not in config:
        raise ValueError("Scenario requires horizon, ranges {g,b,theta,r}, and tau_values")
    horizon = config["horizon"]
    if isinstance(horizon, bool) or int(horizon) != horizon or horizon < 1:
        raise ValueError("Scenario horizon must be a positive integer")
    ranges = config["ranges"]
    if set(ranges) != set(PARAMETER_NAMES):
        raise ValueError("Ranges must have exactly g,b,theta,r")
    normalized = {}
    for name in PARAMETER_NAMES:
        bounds = list(ranges[name])
        if len(bounds) != 2:
            raise ValueError(f"{name} must have [lower,upper]")
        low, high = map(float, bounds)
        _validate_finite(**{name: [low, high]})
        if low > high:
            raise ValueError(f"{name} lower bound exceeds upper bound")
        normalized[name] = [low, high]
    if not 0 <= normalized["theta"][0] <= normalized["theta"][1] < 1:
        raise ValueError("theta range must lie in [0,1)")
    if not 0 <= normalized["r"][0] <= normalized["r"][1] <= 1:
        raise ValueError("r range must lie in [0,1]")
    delays = sorted(set(float(value) for value in config["tau_values"]))
    if not delays or any(not math.isfinite(tau) or tau < 0 for tau in delays):
        raise ValueError("tau_values requires finite nonnegative delays")
    target = float(config.get("target_fuel_ratio", 1))
    if not math.isfinite(target) or target <= 0:
        raise ValueError("target_fuel_ratio must be finite and positive")
    power = config.get("sobol_power", 12)
    if isinstance(power, bool) or int(power) != power or not 1 <= power <= 20:
        raise ValueError("sobol_power must be an integer between 1 and 20")
    return {"horizon": int(horizon), "ranges": normalized, "tau_values": delays,
            "target_fuel_ratio": target, "sobol_power": int(power),
            "seed": int(config.get("seed", 20261016)),
            "check_convergence": bool(config.get("check_convergence", True)),
            "parameter_evidence": config.get("parameter_evidence", {})}


def corner_bounds(config: Mapping) -> dict:
    """Exact extrema over the supplied rectangular domain and delay list.

    R increases with g,tau and decreases with b,theta,r in this model. Extrema
    are therefore corners, not estimates from the sampled design points.
    """
    c = _validate_scenario_config(config)
    bounds = c["ranges"]
    worst = {"g": bounds["g"][1], "b": bounds["b"][0],
             "theta": bounds["theta"][0], "r": bounds["r"][0], "tau": max(c["tau_values"])}
    best = {"g": bounds["g"][0], "b": bounds["b"][1],
            "theta": bounds["theta"][1], "r": bounds["r"][1], "tau": min(c["tau_values"])}
    def evaluate(parameters):
        return {"parameters": parameters,
                "terminal_fuel_ratio": fuel_ratio(c["horizon"], **parameters),
                "cumulative_future_fuel_in_baseline_year_units": cumulative_fuel_ratio(c["horizon"], **parameters)}
    worst_result, best_result = evaluate(worst), evaluate(best)
    return {"analysis_type": "conditional_exact_box_bounds", "worst_corner": worst_result,
            "best_corner": best_result,
            "entire_domain_meets_target": worst_result["terminal_fuel_ratio"] <= c["target_fuel_ratio"],
            "no_point_in_domain_can_meet_target": best_result["terminal_fuel_ratio"] > c["target_fuel_ratio"]}


def _sobol_one_delay(c: dict, tau: float, power: int, seed: int, save_draws: bool) -> tuple[dict, list]:
    unit = qmc.Sobol(d=4, scramble=True, seed=seed).random_base2(power)
    low = np.array([c["ranges"][name][0] for name in PARAMETER_NAMES])
    high = np.array([c["ranges"][name][1] for name in PARAMETER_NAMES])
    design = low + (high - low) * unit
    g, b, theta, rate = design.T
    ratio = np.asarray(fuel_ratio(c["horizon"], g, b, theta, rate, tau))
    cumulative = np.asarray(cumulative_fuel_ratio(c["horizon"], g, b, theta, rate, tau))
    meets = ratio <= c["target_fuel_ratio"]
    quantiles = (0.05, 0.5, 0.95)
    summary = {"tau": tau, "sobol_power": power, "n_design_points": len(design), "seed": seed,
               "fraction_of_design_points_meeting_target": float(meets.mean()),
               "terminal_fuel_ratio_design_quantiles": {str(q): float(np.quantile(ratio, q)) for q in quantiles},
               "cumulative_fuel_design_quantiles_baseline_year_units": {
                   str(q): float(np.quantile(cumulative, q)) for q in quantiles},
               "sampled_terminal_min": float(ratio.min()), "sampled_terminal_max": float(ratio.max())}
    draws = []
    if save_draws:
        for values, final, total, meets_target in zip(design, ratio, cumulative, meets):
            draws.append({**dict(zip(PARAMETER_NAMES, map(float, values))), "tau": tau,
                          "terminal_fuel_ratio": float(final),
                          "cumulative_future_fuel_in_baseline_year_units": float(total),
                          "meets_target": bool(meets_target)})
    return summary, draws


def sobol_stress_test(config: Mapping, save_draws: bool = False) -> dict:
    """Explore an explicit assumption domain; fractions are not probabilities.

    Scrambled Sobol points have uniform design weights in each supplied range.
    This does not establish physical parameter distributions or independence.
    No variance-based sensitivity indices are claimed by this function.
    """
    c = _validate_scenario_config(config)
    summaries, convergence, draws = [], [], []
    for index, tau in enumerate(c["tau_values"]):
        seed = c["seed"] + index
        summary, sample = _sobol_one_delay(c, tau, c["sobol_power"], seed, save_draws)
        summaries.append(summary)
        draws.extend(sample)
        if c["check_convergence"]:
            higher_power = min(c["sobol_power"] + 2, 22)
            high, _ = _sobol_one_delay(c, tau, higher_power, seed, False)
            convergence.append({"tau": tau, "higher_resolution": high,
                                "change_in_design_target_fraction": high["fraction_of_design_points_meeting_target"]
                                - summary["fraction_of_design_points_meeting_target"],
                                "change_in_terminal_median": high["terminal_fuel_ratio_design_quantiles"]["0.5"]
                                - summary["terminal_fuel_ratio_design_quantiles"]["0.5"]})
    result = {"analysis_type": "conditional_uncalibrated_deployment_scenarios",
              "status": "completed_for_explicit_assumption_domain", "configuration": c,
              "interpretation": ["Parameter bounds are supplied assumptions unless independently documented.",
                                 "Design-space fractions and quantiles are not empirical probabilities or confidence intervals.",
                                 "No aircraft-count replacement rate, engine R&D capability, or causal effect is inferred.",
                                 "g and b are continuous log rates per year; r is fuel-use-weighted annual adoption.",
                                 "theta is realized incremental efficiency relative to the baseline path, avoiding double counting.",
                                 "tau is a deployment delay in years; cumulative fuel excludes the observed base year."],
              "delay_summaries": summaries, "exact_domain_bounds": corner_bounds(c),
              "resolution_comparison": convergence}
    if save_draws:
        result["design_points"] = draws
    return result


def run(rows: Iterable[Mapping], scenario_config: Mapping | None = None,
        min_differences: int = 8, prior: NIGPrior | None = None,
        prior_scales: Sequence[float] = (0.02, 0.10), save_draws: bool = False) -> dict:
    """Combined API with empirical and conditional outputs explicitly separated."""
    data = normalize_rows(rows)
    prior = prior or NIGPrior()
    empirical = {"observations": len(data),
                 "period": [data[0]["year"], data[-1]["year"]] if data else None,
                 "provenance_notice": "Official-source verification must be completed upstream; this module validates arithmetic inputs only.",
                 "main_rolling_h1": rolling_forecast(data, min_differences, prior),
                 "pandemic_training_exclusion_rolling_h1": rolling_forecast(
                     data, min_differences, prior, PANDEMIC_YEARS),
                 "latest_h1": latest_forecast(data, min_differences, prior),
                 "latest_h1_pandemic_training_exclusion": latest_forecast(
                     data, min_differences, prior, PANDEMIC_YEARS),
                 "prior_scale_sensitivity": {}}
    for scale in prior_scales:
        if not math.isfinite(scale) or scale <= 0:
            raise ValueError("prior_scales must be positive finite values")
        alternative = NIGPrior(mu=prior.mu, kappa=prior.kappa, alpha=prior.alpha, beta=scale ** 2)
        empirical["prior_scale_sensitivity"][str(scale)] = rolling_forecast(data, min_differences, alternative)
    conditional = (sobol_stress_test(scenario_config, save_draws) if scenario_config is not None else
                   {"analysis_type": "conditional_deployment_scenarios", "status": "skipped_no_explicit_scenario_configuration"})
    return {"empirical_forecast_analysis": empirical, "conditional_deployment_scenarios": conditional}


def _write_outputs(result: dict, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    draws = result["conditional_deployment_scenarios"].get("design_points")
    serializable = {**result, "conditional_deployment_scenarios": {
        key: value for key, value in result["conditional_deployment_scenarios"].items()
        if key != "design_points"}}
    (output / "transition_results.json").write_text(
        json.dumps(serializable, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    forecasts = result["empirical_forecast_analysis"]["main_rolling_h1"]["forecasts"]
    if forecasts:
        keys = [key for key in forecasts[0] if key != "intervals"]
        with (output / "rolling_h1_forecasts.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=keys)
            writer.writeheader()
            for row in forecasts:
                writer.writerow({key: row.get(key) for key in keys})
    if draws:
        with (output / "conditional_scenario_design.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(draws[0]))
            writer.writeheader()
            writer.writerows(draws)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Canonical CSV with year and i/fuel_intensity_kg_tkm")
    parser.add_argument("--scenario-config", type=Path, help="Explicit assumption-domain JSON; no ranges are inferred")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "output")
    parser.add_argument("--min-differences", type=int, default=8)
    parser.add_argument("--prior-scale", type=float, default=0.05, help="sqrt(beta), an analyst prior setting")
    parser.add_argument("--save-draws", action="store_true")
    args = parser.parse_args()
    if not math.isfinite(args.prior_scale) or args.prior_scale <= 0:
        parser.error("--prior-scale must be finite and positive")
    config = json.loads(args.scenario_config.read_text(encoding="utf-8")) if args.scenario_config else None
    result = run(load_intensity_csv(args.input), config, args.min_differences,
                 NIGPrior(beta=args.prior_scale ** 2), save_draws=args.save_draws)
    _write_outputs(result, args.output)
    evaluation = result["empirical_forecast_analysis"]["main_rolling_h1"]
    print(json.dumps({"forecast_status": evaluation["status"],
                      "n_test_origins": evaluation["n_test_origins"],
                      "scenario_status": result["conditional_deployment_scenarios"]["status"],
                      "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
