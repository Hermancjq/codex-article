# Supplementary Information


## S1. Complete paired official record and provenance


The table preserves all eleven paired observations. No fuel-intensity value was interpolated before 2015. The main comparison begins in 2017 because that bulletin documents a change in production-data processing and audit rules. Reconstructed fuel is not independently observed total consumption.


| Year | Q (10⁸ tonne-km) | I (kg/tonne-km) | Reconstructed fuel (Mt) |
| --- | --- | --- | --- |
| 2015 | 851.65 | 0.294 | 25.038510 |
| 2016 | 962.51 | 0.293 | 28.201543 |
| 2017 | 1083.08 | 0.293 | 31.734244 |
| 2018 | 1206.53 | 0.287 | 34.627411 |
| 2019 | 1293.25 | 0.285 | 36.857625 |
| 2020 | 798.51 | 0.316 | 25.232916 |
| 2021 | 856.75 | 0.309 | 26.473575 |
| 2022 | 599.28 | 0.302 | 18.098256 |
| 2023 | 1188.34 | 0.292 | 34.699528 |
| 2024 | 1485.17 | 0.271 | 40.248107 |
| 2025 | 1640.83 | 0.260 | 42.661580 |


The canonical `source/verified_data.csv` contains separate source URLs, full SHA-256 digests, physical PDF page locators and the coverage interpretation for every pair. The official-source observation ledger adds exact Chinese quotations and source-file metadata. Transport-aviation interpretation is anchored to the CAAC 2019 transport-intensity statement, the 2022 policy/action series and indicator 126 in the 2024 survey system. This is a documented continuity interpretation rather than enterprise-level matching in every year. NBS cross-publication checks are retained separately; they reuse CAAC-origin statistics and are not independent original measurements. The 2025 observation was obtained from CAAC, not an unverified NBS 2026 yearbook.


## S2. Chain-linked and direct endpoint decomposition


The chain calculation sums adjacent-year LMDI components. Direct endpoint allocation can differ, particularly through contraction and recovery; both sum exactly to the same endpoint fuel change. The following table reports Mt, retaining three decimals. All underlying calculations retain floating-point precision.


| Period | Chain activity | Chain intensity | Endpoint activity | Endpoint intensity | Net |
| --- | --- | --- | --- | --- | --- |
| 2017–2019 | 6.059 | -0.936 | 6.071 | -0.948 | 5.123 |
| 2019–2022 | -20.843 | 2.084 | -20.287 | 1.528 | -18.759 |
| 2022–2025 | 29.931 | -5.368 | 28.853 | -4.290 | 24.563 |
| 2017–2025 | 15.147 | -4.220 | 15.340 | -4.413 | 10.927 |
| 2019–2025 | 9.088 | -3.284 | 9.448 | -3.644 | 5.804 |
| 2015–2019 | 12.846 | -1.027 | 12.769 | -0.950 | 11.819 |
| 2015–2025 | 21.933 | -4.310 | 21.687 | -4.064 | 17.623 |


The extended 2015–2025 comparison crosses the 2017 processing change and is not presented as a harmonised main estimate. Contributions remain accounting allocations; they do not identify technology, policy or rebound effects.


## S3. Reporting-precision perturbations


At every combination of low/high starting and ending values, Q was perturbed by ±0.005 (10⁸ tonne-km) and I by ±0.0005 kg/tonne-km. Sixteen corners were evaluated per period. This examines source rounding only, not systematic measurement error, population coverage or a statistical confidence interval.


| Period | Fuel growth, central (%) | Fuel-growth corner range (%) |
| --- | --- | --- |
| 2017–2019 | 16.145 | 15.742 to 16.548 |
| 2019–2022 | -50.897 | -51.065 to -50.729 |
| 2022–2025 | 135.722 | 134.877 to 136.570 |
| 2017–2025 | 34.434 | 33.946 to 34.924 |
| 2019–2025 | 15.747 | 15.321 to 16.174 |
| 2015–2019 | 47.204 | 46.695 to 47.715 |
| 2015–2025 | 70.384 | 69.766 to 71.004 |


## S4. Bayesian diagnostic, baselines and small-sample exclusions


Let d denote adjacent annual log-intensity changes. The conjugate model uses μ₀=0, κ₀=1, α₀=2 and β₀=0.05². For n changes with average d̄, κₙ=κ₀+n, μₙ=(κ₀μ₀+nd̄)/κₙ, αₙ=α₀+n/2, and βₙ=β₀+Σ(d−d̄)²/2+κ₀n(d̄−μ₀)²/(2κₙ). The h-step log-intensity predictive distribution is Student-t with 2αₙ degrees of freedom, location ln(I_T)+hμₙ and scale sqrt[(βₙ/αₙ)(h+h²/κₙ)]. Exponentiation supplies a median and central intervals; the exponentiated Student-t has no finite positive moments, so an original-scale predictive mean is not reported.


B0 is unchanged intensity. B1 adds the unshrunk training mean log change. B2 uses the shrunk posterior location. Every model uses the same eligible origin, with a minimum of eight prior valid annual differences; no target observation enters its training. MASE divides absolute prediction error by the mean absolute adjacent-year naive error in that origin’s training set. A zero denominator remains undefined.


| Model | Test years | n | MAE (kg/tonne-km) | MASE |
| --- | --- | --- | --- | --- |
| B0 | 2024, 2025 | 2 | 0.016000 | 1.894853 |
| B1 | 2024, 2025 | 2 | 0.014655 | 1.750015 |
| B2 | 2024, 2025 | 2 | 0.014790 | 1.764619 |


These two tests are diagnostics, not evidence of model superiority. The post-2017 series has no eligible out-of-sample test under the same rule. Excluding every training difference touching 2020–2022 leaves only six valid differences in the extended record, so the pandemic-exclusion forecast is skipped rather than formed by joining separated years. Prior scales 0.02² and 0.10² are retained in the machine-readable outputs. The forecasting diagnostic is not used to choose or calibrate the conditional scenario domain.


## S5. Conditional exploration, resolution and analytical bounds


The exact input configuration is `scenario_config.json`. g is uniform in the log-rate interval corresponding to ordinary growth of 2–6%; b is uniform in the continuous intensity-decline interval corresponding to ordinary reductions of 0–2%; θ and r have uniform design weights over 0.10–0.30 and 0.02–0.12, respectively. These are exploratory weights, not inferred parameter distributions. Delays are evaluated separately, not pooled into a probability mixture. H=15 and κ=1 define a 2040 non-increasing-fuel benchmark, not an asserted official target.


| Delay (years) | 2¹² design share meeting target (%) | 2¹⁴ share (%) | 2¹⁴ terminal-ratio median |
| --- | --- | --- | --- |
| 0.0 | 7.0312 | 6.7932 | 1.346867 |
| 3.0 | 5.2246 | 5.1147 | 1.370412 |
| 8.0 | 2.6367 | 2.6062 | 1.423835 |


The shares above describe only the stated design domain. They are not probabilities that China will meet a target. Scrambling seeds are 20261016, 20261017 and 20261018. No points are skipped or thinned. The higher-resolution results are stored with the resolution comparison; the initial individual design points are supplied in CSV. Re-running the documented code regenerates both.


By monotonicity, the lowest terminal ratio occurs at low g, high b, high θ, high r and the shortest delay; the highest occurs at the opposite corner. Exact bounds are 0.739640 and 2.364954. These are bounds for the assumed box, not empirical prediction limits. A cumulative-fuel diagnostic sums future years 1 through H, excluding the observed baseline year, in units of baseline annual fuel. It is retained in the numerical output but is not used to claim a carbon budget.


The analytical frontier explicitly distinguishes baseline-sufficient, full-adoption-insufficient and deployment-threshold cases. It does not truncate an impossible adopted share to one or interpret fuel-use-weighted adoption as aircraft-count replacement.


## S6. Reproduction and integrity boundaries


The replication README gives the offline reproduction command, exact software versions and input hashes. Eighteen deliberately synthetic arithmetic/mathematical checks cover accounting identities, unit conversion, Bayesian conjugacy and prediction variance, forward-only training, missing/excluded-year handling, adoption boundaries, analytic/numerical threshold agreement, monotonicity and exact scenario corners. These tests are not empirical observations. Official-document hashes, table transcriptions, coverage reasoning and figure-source values are separate evidence checks.


References were checked against DOI metadata and authoritative publisher records. Reading coverage differs by source: the Bergero and Dray papers were used at the official-abstract level; Ang (2005) was bibliographically verified but its full text was not retrieved. The decomposition equations and closure checks are self-contained. Current MDPI author instructions, scope and research-data/artificial-intelligence policies were read; these checks do not constitute a journal acceptance decision or human-author attestation.


No confidential thesis survey responses or unverified capability scores were reused. Public archive publication and formal submission have not been performed. Author details, contributions, funding, conflicts, prior-thesis relationship and human-author review remain to be completed by the authors.