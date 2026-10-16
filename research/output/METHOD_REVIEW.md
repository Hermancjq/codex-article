# Internal technical methods check

Review date: 16 October 2026. This is an internal, same-platform technical check, not external peer review, an independent certification of the study, or a prediction of journal acceptance. The reviewer contributed to the transition-model implementation; the manuscript was checked separately against saved outputs and standalone arithmetic, but that contribution limits any claim of reviewer independence.

Reviewed manuscript snapshot: `/workspace/research/output/MANUSCRIPT.md`, SHA-256 `96eda33b596c8f97ee79e17c265c69579040fd2a4a8aff1342c97011844bd79a`. Line numbers below refer to that snapshot.

## Overall finding

No material numerical, unit-conversion, chain-versus-endpoint, scenario-configuration, or training-time inconsistency was found in the checked manuscript. Two small methods clarifications should be made before final assembly. The main 2017–2025 window, extended 2015–2025 diagnostic, and absence of eligible post-2017 forecast tests are represented correctly. No manuscript changes were made during this check.

## Wording to fix

1. **Line 100: qualify the predictive-distribution statement.** “Original-scale point predictions are medians of exponentiated Student-t distributions” should refer specifically to the Bayesian benchmark. B0 is a deterministic unchanged-intensity baseline and B1 is an unshrunk plug-in drift baseline; the implementation does not assign those two baselines the Bayesian Student-t distribution. Suggested wording: “The Bayesian benchmark’s original-scale point predictions are medians of exponentiated Student-t distributions, not means.” This does not change any reported value.

2. **Lines 70–78: state the domain of Equation (4).** The required-share formula divides by θ. The actual stress-test domain has θ between 0.10 and 0.30 and is therefore valid, but the general formula should say “For θ > 0”. For completeness, add that θ = 0 cannot change the baseline and therefore cannot meet an otherwise missed target. The code already handles this boundary explicitly. This is a domain clarification, not a failed numerical result.

## Checked and consistent

| Manuscript location | Technical check | Finding |
|---|---|---|
| Lines 27–33, 185 | Statistical processing and inference boundary | Main comparisons begin in 2017; no retrospective harmonisation is claimed; annual intensity coverage is presented as an official-anchor-supported interpretation, not enterprise-level matching. |
| Lines 37–52 | Fuel units | With Q in 10^8 tonne-km and I in kg/tonne-km, fuel is 0.1QI Mt. The analysis script's 10QI in 10,000-tonne units equals 0.1QI Mt. All eleven annual conversions match saved outputs. |
| Lines 54–60, 120–135 | LMDI, chain totals, endpoint sensitivity | Formula is an exact identity. Table 3 uses adjacent-year chain contributions, rather than the different endpoint allocations. Net changes and offsets match. The rounding envelope is explicitly for endpoint quantities, not a confidence interval. |
| Lines 110–112 | Historical changes | Turnover +51.4967%, intensity −11.2628%, and reconstructed fuel +34.4339% for 2017–2025 round as reported. The 33.95–34.92% fuel-growth envelope and 2019–2025 comparisons agree with saved calculations. |
| Lines 64–92 | Deployment definitions and rates | θ is incremental relative to baseline; r is fuel-use-weighted adoption; g and b use continuous rates converted from ordinary rates. H=15 means 2025 to 2040. No engine-only benefit, aircraft-count rate, or official fuel target is inferred. |
| Lines 143–145 | Analytic scenarios | Required full-adoption benefit is 0.354387409; full adoption of θ=0.30 yields R=1.084241556. Low-growth required share is 0.680440019; required rates for τ=0/3/8 are 0.073233858/0.090688468/0.150385786. Reported rounding and the “more than doubles” statement are correct. |
| Lines 94, 153–155 | Sobol and exact box bounds | The manuscript quotes the 2^14 resolution entries, not the initial 2^12 entries. Seeds, parameter ranges, domain weights, fractions, resolution differences and exact corners match the configuration and output. No variance-based sensitivity indices are claimed. |
| Lines 100, 157 | Priors and forecast folds | The NIG prior is μ0=0, κ0=1, α0=2, β0=0.05²; alternative β scales match the code. Forward-only extended-series origins are 2023 and 2024, targeting 2024 and 2025, using 8 and 9 differences. MAEs round to 0.0160/0.0147/0.0148 for B0/B1/B2. No superiority is asserted. |
| Line 157 | Post-2017 eligibility | 2017–2025 has eight total differences but no later observed target after the first eligible full training set. Thus zero out-of-sample folds is correct. It is distinct from a latest-origin 2026 projection that can be computed but is not empirically tested or used to calibrate scenarios. |
| Lines 100, 157 | Pandemic exclusion | The extended series has six valid annual differences after excluding any difference touching 2020–2022; post-2017 has four. No skipped year is bridged; the eight-difference threshold is not relaxed. |
| Lines 19–21, 171–189, 193 | Identification and climate boundaries | Aggregate efficiency is not presented as engine capability; causal attribution, rebound, lifecycle neutrality and investment optimality are explicitly excluded. Scenario fractions are design-space summaries, not empirical probabilities. |

## Standalone arithmetic recheck

The following checks were rerun directly from `source/verified_data.csv` and the root `scenario_config.json`, without importing the modelling or accounting functions under review:

- All eleven annual fuel conversions match `output/analysis/accounting_results.json`.
- Adjacent-year LMDI sums reproduce all four main manuscript periods:

| Period | Activity, Mt | Intensity, Mt | Sum, Mt |
|---|---:|---:|---:|
| 2017–2019 | 6.0593377721 | −0.9359567721 | 5.1233810000 |
| 2019–2022 | −20.8434543315 | 2.0840853315 | −18.7593690000 |
| 2022–2025 | 29.9311763624 | −5.3678523624 | 24.5633240000 |
| 2017–2025 | 15.1470598030 | −4.2197238030 | 10.9273360000 |

- The standalone conjugate posterior produces Bayesian medians 0.2917786193 for target 2024 and 0.2688013756 for target 2025. The 80% and 95% interval endpoints match saved outputs. These are medians, not original-scale expectations: exponentiated Student-t predictions do not have finite positive moments.
- Regenerating all three 2^14 Sobol sets gives domain fractions 0.0679321289, 0.0511474609 and 0.0260620117 for delays 0, 3 and 8. These agree exactly with the saved higher-resolution summaries.

## Delivery-package issue outside the manuscript calculation

`output/RESEARCH_STATUS.md` still describes the earlier network-blocked, no-data stage. If supplied beside the current completed manuscript without a prominent historical label, it contradicts the actual replication status. Update it, explicitly archive it as a dated progress record, or exclude it from the submission package. This is a packaging correction, not a numerical defect in the manuscript.

## Limits of this check

The review checked formulas, numerical consistency, saved configuration, sample eligibility, and interpretation boundaries. It did not re-authenticate every official PDF from the publisher, re-perform the literature search, verify author declarations, assess all journal policies, evaluate originality against every related article, or reproduce an external editor's judgement. The official-source intensity mapping remains a measurement assumption supported by documented anchors; this check does not turn it into a direct independent fuel-total observation. The study remains a descriptive accounting exercise plus explicitly conditional deployment analysis, and the small forecasting exercise remains diagnostic.
