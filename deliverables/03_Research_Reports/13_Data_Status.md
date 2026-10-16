# Official aviation data acquisition status

Status at 2026-10-16 UTC: **Official sources retrieved successfully. Core observed Q/I series: 2015–2025 (11 years).**

## What was verified

- Sixteen original CAAC annual Civil Aviation Industry Development Statistical Bulletin PDFs, covering 2010–2025, were downloaded from `www.caac.gov.cn`. Raw files, full SHA-256 digests, retrieval timestamps, exact excerpts and physical PDF page locators are archived.
- Total transport turnover is available for 2010–2025. The annual bulletin does not report a verifiable annual fuel-intensity value for 2010–2014; these cells remain missing and are excluded from the common sample. The 11-year intensity series is 0.294, 0.293, 0.293, 0.287, 0.285, 0.316, 0.309, 0.302, 0.292, 0.271 and 0.260 kg/tkm (2015–2025).
- NBS China Statistical Yearbook 2025 Table 16-29 was downloaded as the official JPG and visually checked. Its total-turnover values for 2010, 2020, 2022, 2023 and 2024 agree with CAAC annual-bulletin values within the bulletin's 0.01 hundred-million tonne-km rounding precision. See `nbs_crosscheck.csv`.
- All sixteen archived CAAC bulletin PDF SHA-256 digests were rechecked against the ledger. The canonical 11-row empirical input is `/workspace/research/source/verified_data.csv`; `verified_observation_ledger_2015_2025.json` preserves original evidence.

## Statistical population decision

Q is transport turnover of mainland-registered commercial air carriers on domestic (including Hong Kong/Macao/Taiwan routes) and international services, not airport throughput and not the statistics of Hong Kong/Macao/Taiwan-registered carriers.

I is interpreted as transport-aviation fuel per transport tonne-km using official anchors and continuity of the identically named, common-2005-baseline annual series. The independent source reviewer supported this bounded interpretation. It is **not** a claim that each annual bulletin repeats the denominator definition or that carrier microdata were matched year by year.

The supporting anchors are the CAAC 2020 press conference explicitly identifying 2019 **transport aviation** intensity as 0.285 kg/tkm, the 2022 policy/action page linking transport-fleet 2019 0.285 with 2021 0.309 in the same discussion, and the 2024 official survey system's item 126 transport-fuel/transport-turnover formula. See `scope_alignment_decision.json` and `/workspace/research/scope_audit/` for the independent audit.

- https://www.caac.gov.cn/XWZX/MHYW/202012/t20201222_205702.html
- https://www.caac.gov.cn/XWZX/MHYW/202209/t20220923_215418.html
- https://www.caac.gov.cn/XXGK/XXGK/TJSJ/202406/P020240604342006406114.pdf (physical p.84 = printed p.80, item 126; also physical p.33 = printed p.29, fuel survey table)

The 2024 system separately defines general-aviation and combined converted-turnover formulas. Those definitions are not silently substituted for transport turnover. Canonical rows mark `scope_match=true` only with the documented official-anchor-plus-series-continuity interpretation retained in every `coverage_definition` cell.

## Material limitations

- Q×I is a **reconstructed/implied fuel-use estimate**, not an independently observed or externally validated official fuel total. No independent aggregate fuel total was retrieved for cross-validation.
- I is rounded to three decimals; rounding intervals should be propagated. The fuel conversion is fuel in 10,000 tonnes = turnover in 100 million tonne-km × intensity in kg/tkm × 10.
- The 2017 bulletin explicitly reports changed production-data processing and audit rules after the comprehensive statistical system launched. Report this break and show sensitivity beginning in 2017.
- 2020–2022 are a structural disruption in demand, utilisation, load factors and traffic composition. They are not evidence that engine technology deteriorated.
- No observation identifies an indigenous-engine effect, engine manufacturing capability, non-CO2 aviation climate effects, or life-cycle emissions. Any engine R&D link must remain a conditional engineering interpretation.
- The official 2024 survey resource table uses 3.15 tCO2/t for aviation kerosene and 3.16 for other kerosene. A CO2 conversion must document its chosen factor and boundary. The main fuel accounting does not require an emissions factor.
- Do not smooth missing pre-2015 intensity or back-solve individual years from a five-year mean or a rounded percentage reduction.

## Reproduction files

- `collect_official_sources.py`: standard-library official source archival and excerpt extraction; `pdftotext -layout` for PDFs. Default discovery now follows the actual CAAC annual-report archive at `index_1214.html` and historical page `index_1214_1.html`.
- `raw/`, `extracted_text/`, `fetch_log.jsonl`, `excerpts.csv`: original files and candidate text extraction.
- `early_years/`: independent 2010–2017 retrieval, missingness decisions and supplementary official planning evidence.
- `official_aviation_2010_2025.csv`: raw observation ledger; missing early I values remain blank.
- `verified_observation_ledger_2015_2025.json`: source-excerpt audit for every core observation.
- `nbs_crosscheck.csv`: visually verified NBS yearbook values and rounding differences.
- `scope_alignment_decision.json`: statistical-population judgment and limitations.
- `validation_report.json`: successful source-hash and input verification report.

## Historical network issue (resolved)

Initial requests to CAAC/NBS failed with proxy CONNECT 403; the root agent saved a network-settings draft. After the user said to continue and network settings changed to unrestricted, official requests succeeded. No TLS verification was disabled. `network_attempts.json` records the earlier failure only; it is not the current readiness state. GitHub was used as a discovery fallback during the outage; no GitHub numerical observation entered the official dataset. A 2022 policy/action PDF exceeded the acquisition script's 25 MiB cap, so its successfully archived official HTML was used; no complete PDF download is claimed for that attachment.

## Analytical design suitable for this sample

With 11 common-sample national annual observations (2015–2025), a high-dimensional neural network, causal forest, or structural causal model cannot be justified simply because it is complex. A transparent accounting decomposition plus uncertainty-aware, constrained scenario model is defensible and reproducible.

Let Q denote transport turnover in tonne-kilometres; I fuel intensity in kg fuel/tkm; F fuel in kg; e the kg CO2/kg fuel factor; and C direct CO2 in kg. Then F = QI and C = QIe.

Exact additive LMDI between valid endpoints a and b uses L(Cb,Ca) = (Cb−Ca)/(ln Cb−ln Ca), with the equal-value continuous limit L(C,C)=C. Contributions are ΔC_Q=L ln(Qb/Qa), ΔC_I=L ln(Ib/Ia), and ΔC_e=L ln(eb/ea). With a fixed emission factor, ΔC_e=0. Report the exact closure residual and avoid causal language.

For a target terminal emissions ratio R=C_T/C_0, activity growth g, annual fuel-intensity reduction r and n years, the identity implies C_T/C_0=[(1+g)(1−r)]^n when e is fixed. The minimum annual intensity reduction is r_min=1−R^(1/n)/(1+g). This is an engineering requirement conditional on assumed demand, not a forecast of engine performance.

A cohort renewal extension can model fleet entry age, retirement survival, new-aircraft intensity advantage and operational utilisation, using explicit scenario parameters where data are unavailable. Label assumed distributions separately from official observations, solve a constrained replacement/allocation problem, and report Monte Carlo intervals as **scenario uncertainty**, not empirical confidence intervals. Test demand growth, survival lifetime, utilisation, improvement saturation and SAF life-cycle factors individually. SAF does not reduce tank-to-wake CO2 to zero and must be analysed with a separate life-cycle boundary.

Empirical validation should include exact identity closure, source rounding tolerance, same-definition turnover comparisons, sensitivity to 2019 versus latest-year baselines, and parameter stress tests. A paper can claim descriptive trends and conditional transition requirements; it cannot claim an identified causal effect of domestic engine R&D from these aggregates.
