# Efficiency Gains, Growing Fuel Demand and Deployment Frontiers in China’s Commercial Aviation

## Abstract

Improving aircraft efficiency does not necessarily reduce aviation fuel demand when transport activity expands. This study links official Chinese aviation statistics to deployment-constrained transition scenarios. Eleven paired annual observations for 2015–2025 were assembled from Civil Aviation Administration of China publications; selected turnover observations were cross-checked against National Bureau of Statistics yearbooks. The principal analysis starts in 2017 because statistical processing changed that year. Chain-linked logarithmic-mean decomposition shows that, during 2017–2025, transport turnover increased by 51.5% and reported fuel intensity declined by 11.3%, while reconstructed fuel demand rose by 34.4%. Intensity improvements offset 27.9% of the activity-related increase. A nonlinear deployment model separates insufficient technical benefit from insufficient adoption speed. Under an illustrative 4% annual activity-growth and 1% baseline-efficiency-improvement scenario, even complete deployment requires an additional 35.4% efficiency advantage to hold 2040 fuel demand at its 2025 level. Under a lower-growth scenario, an eight-year delay more than doubles the required adoption rate. These are conditional feasibility results, not forecasts. The findings connect observed efficiency–activity mismatches to transparent technology-deployment requirements without attributing aggregate changes to domestic engine research or claiming climate neutrality.

**Keywords:** civil aviation; fuel efficiency; technology deployment; logarithmic-mean decomposition; quasi-Monte Carlo; sustainability transition

## 1. Introduction

Aviation sustainability depends on how rapidly operational improvements become effective across a growing transport system. Better engines, aircraft and operations can reduce fuel consumption per unit of transport, but their sector-wide effect depends on activity growth and adoption. Global transition studies consequently combine efficiency improvements with fuel substitution, demand assumptions and, in some pathways, carbon removals [1–3]. Their conclusions differ with their system boundaries and assumptions. A useful national analysis must therefore distinguish what has already been observed from what additional deployment would have to achieve.

This distinction matters for China-registered commercial air carriers. They operate domestic and international services, and their transport activity experienced a severe interruption and subsequent recovery around the COVID-19 pandemic. An intensity decline during recovery cannot automatically be interpreted as persistent technological progress. Conversely, a fall in aggregate fuel demand during a transport contraction does not establish a durable sustainability transition. The latest official statistics permit these changes to be examined through 2025, but they also require explicit attention to statistical coverage, rounding and a change in processing procedures.

China-specific aviation decomposition is established prior art. Liu and Zhang studied the drivers of decoupling between transport growth and carbon emissions over 1996–2015 [4]. Cui and Lei examined complementary mitigation pathways for China–foreign routes, a different operational boundary [5]. The present study does not claim to introduce aviation decomposition or to identify a new causal relationship between efficiency and demand. Its question is narrower: after updating the official record through 2025, what combination of additional efficiency benefit, deployment speed and deployment timing would be sufficient to prevent further fuel-demand growth?

Recent research makes the timing question especially relevant. Martulli et al. distinguish announced sustainable aviation fuel (SAF) production capacity from capacity realised on schedule [6]. Their global and European evidence motivates explicit treatment of implementation delays, but does not supply China-specific adoption parameters. Policy analyses also question reliance on future technical improvements without examining activity assumptions [7], while aviation scenarios published in this journal consider interactions among fuel transitions, operational efficiency and demand [8]. These studies suggest examining implementation constraints jointly with the size of the efficiency improvement, rather than assuming immediate fleet-wide availability.

Our conceptual starting point is the coordination of design, testing and manufacturing in aero-engine development. Technical potential has to pass through validation, certification, production and operational adoption before influencing fleet-wide fuel use. However, national fuel-intensity statistics cannot measure those capabilities separately or identify their causal effects. We retain this coordination perspective as a motivation for deployment constraints and replace untraceable capability indices with publicly documented operational statistics.

The study makes three connected contributions. First, it constructs a source-linked annual dataset with an explicit operator-based boundary and quantifies activity and intensity contributions across expansion, disruption and recovery. Second, it derives an analytical frontier distinguishing an inadequate efficiency benefit from an inadequate deployment rate. Third, it checks that frontier using nonlinear simulation, exact parameter-box bounds and scrambled Sobol scenario exploration. A small-sample Bayesian forecasting diagnostic is reported separately and is not used to claim predictive superiority or calibrate technology adoption. The resulting contribution is a reproducible assessment of transition requirements, rather than a long-term forecast or a causal estimate of engine innovation.

## 2. Data and Methods

### 2.1. Official data, coverage and comparability

Annual transport turnover, Q, and reported fuel intensity, I, were transcribed from the Civil Aviation Administration of China (CAAC) statistical bulletins [12]. Complete paired observations were available for 2015–2025. Earlier turnover observations were retained in the source ledger, but missing fuel intensities were not interpolated. The principal decomposition begins in 2017 because that year’s bulletin states that production-data processing and audit rules changed following the introduction of a statistical information system. The 2015–2016 observations remain visible in the extended record; they are not assumed to have been retrospectively harmonised with the later procedure.

The activity boundary comprises mainland China-registered air carriers and includes their domestic, Hong Kong/Macao/Taiwan and international services. It excludes foreign carriers operating in China. It is therefore neither a territorial fuel inventory nor a measure of all flights arriving at Chinese airports. Airport throughput is not interchangeable with carrier transport turnover. National Bureau of Statistics (NBS) yearbook tables were used for cross-publication checks [13]. For example, the yearbook values for 2019, 2023 and 2024 convert to 1293.2530, 1188.3381 and 1485.1708 × 10⁸ tonne-km, respectively, agreeing with the CAAC bulletin values after rounding. NBS republishes CAAC-source statistics, so this checks transcription and publication consistency rather than providing independent physical measurement.

The annual energy sections call I “Chinese civil aviation fuel consumption per tonne-kilometre” without repeating the full denominator definition. We interpret this as the continuous transport-aviation indicator using three official anchors. A CAAC statement at the State Council Information Office press conference on the white paper *Sustainable Development of Transport in China* explicitly identifies the 2019 value, 0.285 kg/tonne-km, as transport-aviation intensity [15]. A subsequent official policy document places that transport-fleet value and the 2021 value, 0.309 kg/tonne-km, in the same series [16]. The 2024 statistical survey system defines transport fuel per tonne-kilometre as transport-flight fuel divided by transport turnover [14]. It separately defines general-aviation and combined converted-tonne-kilometre indicators, which cannot be substituted for the transport indicator. These anchors support the interpretation, but do not provide year-by-year matching of enterprise microdata. That remaining limitation is carried into the interpretation of reconstructed fuel demand.

Each paired observation retains its official PDF URL, publication identity, exact source quotation, physical page locator, retrieval date and SHA-256 digest. All eleven paired-report file hashes were checked. Documents were accessed on 16 October 2026. I is published to 0.001 kg/tonne-km and Q to 0.01 × 10⁸ tonne-km. Selected official values and derived fuel estimates are shown in Table 1; the complete record is supplied with the replication files.

**Table 1. Selected official observations and reconstructed fuel demand.**

| Year | Transport turnover, 10⁸ tonne-km | Reported intensity, kg/tonne-km | Reconstructed fuel, Mt |
|---|---:|---:|---:|
| 2017 | 1083.08 | 0.293 | 31.734 |
| 2019 | 1293.25 | 0.285 | 36.858 |
| 2020 | 798.51 | 0.316 | 25.233 |
| 2022 | 599.28 | 0.302 | 18.098 |
| 2024 | 1485.17 | 0.271 | 40.248 |
| 2025 | 1640.83 | 0.260 | 42.662 |

Source: CAAC annual bulletins [12]. Fuel is calculated from the rounded official activity and intensity observations; it is not an independently reported fuel total. Mt denotes one million tonnes.

### 2.2. Accounting and chain-linked decomposition

With Q measured in 10⁸ tonne-km and I in kg/tonne-km, reconstructed fuel demand in Mt is

$$F_t = 0.1 Q_t I_t. \tag{1}$$

For strictly positive quantities, the logarithmic mean is L(x,y) = (x − y)/(ln x − ln y), with the continuous limit L(x,x) = x. The additive logarithmic-mean Divisia index (LMDI) approach [17] gives the adjacent-year contributions

$$D_{Q,t}=L(F_t,F_{t-1})\ln(Q_t/Q_{t-1}), \qquad D_{I,t}=L(F_t,F_{t-1})\ln(I_t/I_{t-1}). \tag{2}$$

Their sum equals F_t − F_(t−1). We sum adjacent-year contributions within three periods: 2017–2019, 2019–2022 and 2022–2025. The dates are transparent descriptive groupings, not statistically estimated breakpoints. Direct endpoint decomposition is retained as a sensitivity analysis because a path containing a disruption and recovery can allocate contributions differently from a single endpoint comparison. No contribution is interpreted as a causal treatment effect.

We report the intensity offset as −ΣD_I/ΣD_Q only when the activity contribution is positive. An offset below one means that the net intensity contribution did not cancel the activity contribution. This accounting ratio does not identify a rebound effect, which would require evidence that efficiency changes caused demand changes [9]. Rounding sensitivity perturbs the start and end Q values by ±0.005 and I values by ±0.0005 at all sixteen endpoint corners. These are reporting-precision perturbations, not confidence intervals or estimates of systematic measurement error.

### 2.3. A deployment-constrained transition model

We normalise future fuel demand to the 2025 reconstructed level. Let h denote years after 2025, g the continuous annual activity-growth rate, b the continuous baseline intensity-improvement rate, θ an additional realised efficiency advantage, r the annual fuel-use-weighted adoption rate among the remaining non-adopting share, and τ the delay before additional adoption starts. The adopted share and fuel ratio are

$$s_h=1-(1-r)^{\max(h-\tau,0)}, \qquad R_h=\frac{F_h}{F_{2025}}=\exp[(g-b)h](1-\theta s_h). \tag{3}$$

The additional advantage θ is relative to an already improving baseline, preventing double counting of baseline efficiency gains. It is not an engine test-bench efficiency or an estimate of any domestic engine’s effect. Likewise, r refers to the distribution of fuel use, not the percentage of aircraft replaced. Its conversion to aircraft numbers would require fleet-vintage, utilisation and engine-configuration data that are unavailable here. The delay represents a conditional deployment constraint; it is not estimated from the supplied capability framework.

For horizon H, target fuel ratio κ and θ > 0, the required adopted share is

$$s_{\mathrm{req}}=\frac{1-\kappa\exp[-(g-b)H]}{\theta}. \tag{4}$$

If the numerator is non-positive, the baseline already meets the target. If s_req > 1, even complete adoption is insufficient. If 0 < s_req ≤ 1 and H > τ, the required adoption rate is

$$r_{\mathrm{req}}=1-(1-s_{\mathrm{req}})^{1/(H-\tau)}. \tag{5}$$

If H ≤ τ and the baseline misses the target, the additional technology cannot help within that horizon. When θ = 0, additional adoption has no effect on the baseline path. These cases distinguish an efficiency-benefit constraint from a deployment-speed constraint. The full-adoption necessary condition is θ ≥ max{0, 1 − κ exp[−(g−b)H]}. Faster deployment cannot overcome a violation of that condition.

### 2.4. Scenario domain and numerical verification

The principal stress test asks whether 2040 fuel demand can be held at its 2025 level: H = 15 and κ = 1. This is an analytical benchmark, not an asserted Chinese policy target. Table 2 defines the exploratory domain. All ranges are analyst-defined assumptions. Historical observations contextualise the activity and baseline-intensity rates, but do not estimate the future parameter distributions. Recent literature motivates treating deployment as uncertain [6]; its international project-realisation statistics are not imported as Chinese adoption parameters.

**Table 2. Explicit assumptions for the conditional scenario domain.**

| Input | Exploration range | Interpretation |
|---|---|---|
| Activity growth | 2–6% per year | Ordinary annual rate; converted to g = ln(1 + growth) |
| Baseline intensity improvement | 0–2% per year | Ordinary reduction; converted to b = −ln(1 − reduction) |
| Additional realised advantage, θ | 10–30% | Relative to the improving baseline; hypothetical package, not engine-only performance |
| Fuel-use-weighted adoption, r | 2–12% per year | Fraction of the remaining non-adopting share; not aircraft-count replacement |
| Deployment delay, τ | 0, 3 or 8 years | Alternative timing assumptions |

Scrambled Sobol sequences were generated separately for each delay, initially with 2¹² points and then with 2¹⁴ points as a resolution check. Sampling used uniform design weights in continuous g, b, θ and r; those weights are not claims about real-world distributions or independence. Seeds were 20261016, 20261017 and 20261018 for the three delays. The quoted scenario fractions use the higher resolution. We do not compute or claim variance-based Sobol sensitivity indices. The power-of-two construction follows the software’s documented balance requirements [19].

Because R increases with g and τ and decreases with b, θ and r, best and worst parameter-box corners can be evaluated directly. Analytical adoption thresholds were substituted back into Equation (3), and boundary cases and monotonicity were checked numerically. The implementation also verifies decomposition closure and physical-unit conversion. Computation used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 [18], pandas 2.2.3 and Matplotlib 3.10.8.

### 2.5. A deliberately limited forecasting diagnostic

To assess whether the short historical series could defensibly supply a predictive baseline, we implemented a conjugate Bayesian benchmark for annual log-intensity changes: Δln I ~ N(μ,σ²), μ|σ² ~ N(0,σ²), and σ² ~ InvGamma(2,0.05²). Sensitivities used inverse-gamma scales 0.02² and 0.10². Predictions were evaluated against an unchanged-intensity baseline and an unshrunk historical-drift baseline using forward-only training and at least eight valid annual differences. The Bayesian benchmark’s original-scale point predictions are medians of exponentiated Student-t distributions, not means. Differences touching 2020–2022 were omitted in a separate training sensitivity without bridging excluded years. These diagnostics are documented in the supplementary material and do not calibrate the scenario ranges.

### 2.6. Research-assistance transparency

OpenAI Codex assisted with source-search formulation, extraction workflows, code development and checking, and English manuscript drafting. The research-assistance workflow retrieved and compared source records and bibliographic metadata with official documents and publisher records, and generated the reported calculations through executed Python scripts. Independent verification and approval by the named human authors remain pending. This assistance does not establish authorship eligibility or institutional approval. Human authors must review the underlying records, interpretation and disclosure before submission. No survey responses, confidential engine-performance records or human-subject observations were used in this analysis.

## 3. Results

### 3.1. Lower intensity coexisted with higher reconstructed fuel demand

Between 2017 and 2025, transport turnover increased from 1083.08 to 1640.83 × 10⁸ tonne-km, or 51.5%, while reported intensity fell from 0.293 to 0.260 kg/tonne-km, or 11.3%. Their product implies fuel demand increasing from 31.73 to 42.66 Mt, a rise of 34.4% (Figure 1). The endpoint rounding perturbations place this increase between 33.95% and 34.92%; reporting precision does not reverse the direction. This calculation establishes an activity–efficiency mismatch, not an engine-specific performance effect.

The recovery-period comparison is not solely a low-base phenomenon. Relative to 2019, turnover in 2025 was 26.9% higher and intensity 8.8% lower, yet reconstructed fuel demand remained 15.7% higher. Conversely, the 2019–2022 decline in reconstructed fuel demand coincided with sharply lower activity and higher intensity. That pattern is inconsistent with interpreting the aggregate contraction itself as evidence of technological improvement.

![Figure 1](figures/figure1_historical_indices.png)

**Figure 1. Activity, intensity and reconstructed fuel demand in the extended official record.** All series are indexed to 2015 = 100 using eleven paired annual CAAC observations. The shaded interval identifies 2020–2022, and the vertical marker identifies the 2017 change in statistical processing. The main comparison begins in 2017. Fuel demand is derived from Q and I and is not an independent validation series. Lines connect annual observations; they do not represent additional measurements or fitted trends. Source data: `annual.csv` and the observation ledger supplied with the replication materials.

### 3.2. The intensity contribution only partially offset expansion

Chain-linked decomposition attributes a 15.15 Mt activity contribution and a −4.22 Mt intensity contribution to the 2017–2025 change, summing to the 10.93 Mt increase. The net intensity contribution therefore offset 27.9% of the activity contribution. Table 3 and Figure 2 show why the intervening path matters.

**Table 3. Chain-linked decomposition of reconstructed fuel-demand changes, Mt.**

| Period | Activity contribution | Intensity contribution | Net change |
|---|---:|---:|---:|
| 2017–2019 | 6.06 | −0.94 | 5.12 |
| 2019–2022 | −20.84 | 2.08 | −18.76 |
| 2022–2025 | 29.93 | −5.37 | 24.56 |
| 2017–2025 | 15.15 | −4.22 | 10.93 |

Contributions use adjacent-year chains, not separate endpoint allocations. Rounding of displayed values can affect the last decimal.

During 2017–2019, the intensity contribution offset 15.4% of the activity contribution. During 2019–2022, declining activity reduced the reconstructed total, while the net intensity contribution increased it. During 2022–2025, the intensity contribution offset 17.9% of the much larger recovery-related activity contribution. These are descriptive accounting patterns; operational conditions, route composition and technology are not separately identified.

Direct endpoint decomposition also assigns a negative intensity contribution and a positive activity contribution to 2017–2025, although their magnitudes differ from the chain-linked allocation. The extended 2015–2025 record likewise shows rising reconstructed fuel demand, but crosses the documented processing change. It is retained as a supplementary comparison rather than used to override the post-2017 result.

![Figure 2](figures/figure2_chain_lmdi.png)

**Figure 2. Contributions across expansion, disruption and recovery.** Bars show chain-linked LMDI activity and intensity contributions in Mt; diamonds show their net sum. Each contribution is computed from the annual official inputs and summed within the stated interval. These are deterministic accounting components, with no sampling-error bars or causal interpretation. Source data: `periods.csv` supplied with the replication materials.

### 3.3. Technical potential and deployment speed impose different constraints

The analytical frontier identifies circumstances in which deployment acceleration alone cannot meet the fuel constraint. Under an illustrative 4% ordinary annual activity-growth rate and 1% baseline annual intensity reduction, the additional full-adoption advantage required by 2040 is 35.4%. Even a hypothetical 30% advantage deployed completely would yield a terminal fuel ratio of 1.084, or 8.4% above the 2025 benchmark. This is a conditional result about those assumptions; it is not a forecast of Chinese demand or an estimate of engine potential.

A lower-growth illustration exposes the timing constraint. With 2% annual activity growth, 1% baseline annual intensity reduction and an additional 20% advantage, at least 68.0% of fuel use must have adopted the incremental improvement by 2040. The required annual adoption rate is 7.3% with no delay, 9.1% with a three-year delay and 15.0% with an eight-year delay (Figure 3). The longest delay pushes the requirement above the 12% upper rate used in the exploratory domain. These rates refer to fuel-use-weighted diffusion of the additional benefit, not the share of aircraft that an airline should replace each year.

![Figure 3](figures/figure3_deployment_thresholds.png)

**Figure 3. Conditional efficiency and deployment frontiers for a 2040 fuel constraint.** (a) The minimum additional advantage under complete adoption, with alternative assumed baseline intensity-improvement rates. (b) The annual fuel-use-weighted adoption rate required under the illustrative 2% activity-growth, 1% baseline-improvement and 20% additional-advantage case, as the delay increases. The 12% comparison is the exploration-domain upper bound, not an observed Chinese replacement rate. Ordinary percentage rates are converted to continuous rates before calculation. All curves are assumption-conditional calculations, not observations or official forecasts; source data are supplied for both panels.

### 3.4. Global scenario exploration confirms a restricted feasible region

At 2¹⁴ design points per delay, 6.79%, 5.11% and 2.61% of the specified parameter combinations met the non-increasing-fuel constraint for delays of zero, three and eight years, respectively. These are shares of a chosen design space, not estimated success probabilities. Moving from 2¹² to 2¹⁴ points changed these shares by at most 0.24 percentage points. Scenario medians changed by at most 0.0013 in the terminal fuel ratio, indicating that the reported numerical summaries were not driven by the initial integration resolution.

Exact corner evaluation gave terminal ratios from 0.740 to 2.365 over the entire specified domain. Thus some combinations were feasible, but the benchmark was not satisfied throughout the uncertainty set. This range is an analytical bound for the stated assumptions, not an empirical prediction interval. The restricted feasible region is conditional on the selected growth and improvement domain; broadening or reweighting that domain would alter its design-space share.

The forecasting diagnostic does not justify replacing these transparent assumptions with a claimed accurate forecast. The extended eleven-year record supplies only two eligible one-year tests, 2024 and 2025. The Bayesian benchmark’s mean absolute error was 0.0148 kg/tonne-km, compared with 0.0160 for unchanged intensity and 0.0147 for unshrunk drift. Two tests cannot establish reliable superiority. The post-2017 record supplies no eligible out-of-sample test under the same eight-difference training rule, and pandemic-excluded training has insufficient differences. These limits are reported rather than relaxed after seeing the results.

## 4. Discussion

### 4.1. Efficiency progress and a sustainability transition are different achievements

The observed record supports a limited but consequential conclusion: the reported efficiency improvement did not offset growth in the transport activity of China-registered air carriers. This complements earlier Chinese decomposition work [4] while extending observation through the latest verified 2025 bulletin. The result should not be interpreted as proof that efficiency caused traffic growth, nor as evidence that specific engines failed to improve. It concerns the aggregate balance between activity and reported fuel intensity.

The distinction helps reconcile apparently different aviation-transition narratives. Global studies identify multiple combinations of technology, fuel and demand levers [1–3]. Policy-document analysis questions technology-centred growth narratives [7], while economic analysis highlights interactions among efficiency standards, carbon pricing and demand responses [9]. Our model does not choose a universally necessary demand pathway. It states the growth-compatible efficiency and deployment conditions explicitly. Where technical benefit is inadequate, faster deployment cannot solve the accounting mismatch; where benefit is adequate, timing can still prevent its realisation within the target horizon.

The disruption and recovery further caution against reading an annual fuel-intensity series as a technological learning curve. Pandemic-era operational restructuring can change utilisation and the passenger/freight or route mix alongside technology. COVID-sensitive aviation-climate scenarios already recognise that activity shocks influence future pathways [20]. The present aggregate data cannot separate these mechanisms, and the small forecasting diagnostic provides no basis for extending the rapid recent intensity decline indefinitely.

### 4.2. What the deployment frontier means for capability coordination

The design–testing–manufacturing perspective becomes operationally useful when framed as a constraint on when an improvement can enter service and how rapidly it can spread. Testing and certification can affect the waiting time, while manufacturing and fleet absorption can affect adoption. However, those are hypotheses about mechanisms, not effects estimated by this dataset. Neither a capability index nor a causal coefficient for domestic engine development is inferred from the aggregate fuel series.

Recent evidence about announced versus realised sustainable-fuel capacity illustrates why potential and deployment should remain separate [6]. The analogy is conceptual: fuel-production projects and aircraft/engine adoption have different physical and institutional processes. Importing a global SAF realisation rate into a Chinese fleet model would conceal that difference. The transparent frontier instead allows decision makers to insert independently documented assumptions when such data become available.

The implications for evaluation are concrete. A technology programme can be assessed against the additional operational benefit required at full adoption, the achievable fuel-use-weighted diffusion rate and the time remaining after validation and certification. A programme that passes only the first test may still miss an aggregate fuel objective. Conversely, a technical shortfall should not be disguised as a deployment-speed problem. These distinctions support integrated evaluation without claiming an investment optimum, which would require costs and resource constraints absent here.

### 4.3. Fuel-demand feasibility is narrower than climate neutrality

This study deliberately reports fuel demand rather than convert it into a supposedly comprehensive climate metric. Fuel substitution, lifecycle greenhouse-gas emissions, contrails and air-quality effects require additional accounting. Route-based mitigation studies [5] and scenario work in Sustainability [8] evaluate levers beyond operational fuel intensity. Sacchi et al. further show why climate-neutrality definitions and resource constraints matter [3]. A pathway meeting the present non-increasing-fuel benchmark is therefore not necessarily climate-neutral, while an appropriately evidenced lifecycle fuel transition could change greenhouse-gas outcomes without reducing fuel mass by the same proportion.

The omitted effects are material boundaries. Contrail effects vary with flight and meteorological conditions [10], and recent modelling evaluates health impacts from aircraft-emission growth [11]. Neither can be recovered by multiplying this fuel series by an undifferentiated climate factor. The operator-based international-activity coverage also differs from a territorial national greenhouse-gas inventory. These distinctions constrain how the results can be used in policy comparisons.

### 4.4. Limitations and a targeted extension

The first limitation is measurement. Official transport-aviation anchors support the intensity interpretation, but annual bulletins do not repeat all enterprise-level definitions. Reconstructed totals lack an independently observed fuel-total check. The 2017 processing change precludes assuming that the full 2015–2025 record is harmonised. Restricting the principal comparison to 2017–2025 and reporting rounding sensitivity reduce specific risks but do not remove systematic measurement uncertainty.

The second limitation is identification. Annual aggregates cannot distinguish engine improvements from airframe technology, operating conditions or transport composition. Consequently, the decomposition does not estimate policy effects, rebound elasticities or the causal value of capability coordination. Those questions require linked fleet, route, utilisation and technology-adoption data, rather than additional complexity fitted to eleven annual observations.

The third limitation is scenario calibration. The rectangular domain is a disclosed stress test, not an estimated joint distribution. Adoption is represented by a parsimonious diffusion function and omits fleet cohorts, heterogeneous utilisation and capacity bottlenecks beyond the stated delay and rate. A useful next extension would link aircraft/engine vintages and actual fuel-use shares to dated certification and delivery records. That would permit τ, r and θ to be constrained by observable deployment evidence and would test whether the simple frontier is adequate, rather than merely adding parameters.

## 5. Conclusions

Official activity and intensity statistics indicate that efficiency improvements did not offset the expansion of China-registered commercial air transport during 2017–2025: reconstructed fuel demand increased by 34.4%, and the net intensity contribution offset 27.9% of the activity contribution. Conditional deployment analysis shows why technical potential and deployment speed must be evaluated separately. An insufficient full-adoption benefit cannot be repaired by faster diffusion; a sufficient benefit can still miss a finite-horizon constraint when deployment is delayed. The practical value is an auditable set of growth, benefit and timing requirements. These results do not identify domestic aero-engine capability effects, predict a particular future pathway or establish climate neutrality.

## Data and Code Availability

The supplied Supplementary Replication Package (`REPLICATION_PACKAGE.zip`) includes the transcribed official observations, source URLs and page locators, SHA-256 source ledgers, NBS cross-publication checks, scenario configuration, Python analysis code, numerical outputs and figure source data. Original statistical documents are available from CAAC and NBS at the URLs in the source ledgers. No public repository DOI or GitHub release is claimed. A public archival link can be added after the authors deposit the verified package, or the package can be supplied as submission supplementary material subject to journal instructions.

## Author Declarations to Complete Before Submission

Author names, affiliations, corresponding-author details, contributions, funding and conflicts of interest must be supplied and verified by the human authors. No human participants were recruited for this study; the analysis uses public aggregate statistics. The relationship to any previously submitted or publicly available version of the underlying thesis must be checked and disclosed where applicable. These items are unresolved author information, not findings of this analysis.

## Acknowledgment of Generative Artificial Intelligence Assistance

OpenAI Codex was used for the research and drafting assistance described in Section 2.6. The human authors must review and revise the manuscript and underlying evidence, confirm the actual product/version information available to them, and declare substantive generative artificial intelligence use during submission in accordance with the journal’s current policy. No statement that human authors have already completed these checks is implied by this draft.

## References

1. Bergero, C.; Gosnell, G.; Gielen, D.; Kang, S.; Bazilian, M.; Davis, S.J. Pathways to net-zero emissions from aviation. *Nature Sustainability* **2023**, *6*, 404–414. https://doi.org/10.1038/s41893-022-01046-9
2. Dray, L.; Schäfer, A.W.; Grobler, C.; Falter, C.; Allroggen, F.; Stettler, M.E.J.; Barrett, S.R.H. Cost and emissions pathways towards net-zero climate impacts in aviation. *Nature Climate Change* **2022**, *12*, 956–962. https://doi.org/10.1038/s41558-022-01485-4
3. Sacchi, R.; Becattini, V.; Gabrielli, P.; Cox, B.; Dirnaichner, A.; Bauer, C.; Mazzotti, M. How to make climate-neutral aviation fly. *Nature Communications* **2023**, *14*, 3989. https://doi.org/10.1038/s41467-023-39749-y
4. Liu, X.; Zhang, Y. What drives the decoupling progress of China’s civil aviation transportation growth from carbon emissions? A new decomposition analysis. *PLOS ONE* **2023**, *18*, e0282025. https://doi.org/10.1371/journal.pone.0282025
5. Cui, Q.; Lei, Y.L. Pathways analysis to reducing aircraft emissions for China-Foreign routes. *npj Climate Action* **2023**, *2*, 15. https://doi.org/10.1038/s44168-023-00047-4
6. Martulli, A.; Brandt, K.; Allroggen, F.; Malina, R. The potential scale-up of sustainable aviation fuels production capacity to meet global and EU policy targets. *Nature Communications* **2025**, *16*, 11619. https://doi.org/10.1038/s41467-025-66686-9
7. Suomalainen, E. Growth over climate or aviation climate policy in the Avoid–Shift–Improve framework. *npj Climate Action* **2025**, *4*, 54. https://doi.org/10.1038/s44168-025-00261-2
8. Davydenko, I.; Hilbers, H. Decarbonization Paths for the Dutch Aviation Sector. *Sustainability* **2024**, *16*, 950. https://doi.org/10.3390/su16030950
9. Proost, S. What role for aviation in climate policy? *Journal of Shipping and Trade* **2026**, *11*, 14. https://doi.org/10.1186/s41072-026-00230-w
10. Teoh, R.; Engberg, Z.; Schumann, U.; Voigt, C.; Shapiro, M.; Rohs, S.; Stettler, M.E.J. Global aviation contrail climate effects from 2019 to 2021. *Atmospheric Chemistry and Physics* **2024**, *24*, 6071–6093. https://doi.org/10.5194/acp-24-6071-2024
11. Quadros, F.D.A.; Nelen, R.; Snellen, M.; Dedoussi, I.C. Global air quality and human health impacts of growing aircraft emissions. *Communications Earth & Environment* **2026**, *7*, 806. https://doi.org/10.1038/s43247-026-03732-4
12. Civil Aviation Administration of China. *Statistical Bulletins on the Development of the Civil Aviation Industry, 2015–2025*; annual releases, 2016–2026 (in Chinese). Official documents and exact annual PDF URLs are listed in the accompanying observation ledger. https://www.caac.gov.cn/XXGK/XXGK/TJSJ/TJSJ_1/ (accessed 16 October 2026).
13. National Bureau of Statistics of China. *China Statistical Yearbook 2020*, Table 16-30; *China Statistical Yearbook 2024*, Table 16-30; *China Statistical Yearbook 2025*, Table 16-29 (in Chinese). https://www.stats.gov.cn/sj/ndsj/ (accessed 16 October 2026).
14. Civil Aviation Administration of China. *Comprehensive Civil Aviation Statistical Survey System*, 2024; fuel-consumption reporting table and indicator 126 (in Chinese). https://www.caac.gov.cn/XXGK/XXGK/TJSJ/202406/P020240604342006406114.pdf (accessed 16 October 2026).
15. Civil Aviation Administration of China. *CAAC Participates in the Press Conference on the White Paper Sustainable Development of Transport in China*, 22 December 2020 (title translated from Chinese). https://www.caac.gov.cn/XWZX/MHYW/202012/t20201222_205702.html (accessed 16 October 2026).
16. Civil Aviation Administration of China. *CAAC Releases 2022 China’s Civil Aviation Green Development Policy and Action*, 23 September 2022 (title translated from Chinese). https://www.caac.gov.cn/XWZX/MHYW/202209/t20220923_215418.html (accessed 16 October 2026).
17. Ang, B.W. The LMDI approach to decomposition analysis: a practical guide. *Energy Policy* **2005**, *33*, 867–871. https://doi.org/10.1016/j.enpol.2003.10.010
18. Virtanen, P.; Gommers, R.; Oliphant, T.E.; Haberland, M.; Reddy, T.; Cournapeau, D.; et al.; SciPy 1.0 Contributors. SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nature Methods* **2020**, *17*, 261–272. https://doi.org/10.1038/s41592-019-0686-2
19. SciPy Developers. *scipy.stats.qmc.Sobol: Official API Documentation, Version 1.17.0*. https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.stats.qmc.Sobol.html (accessed 16 October 2026; analysis runtime 1.17.0).
20. Grewe, V.; Gangoli Rao, A.; Grönstedt, T.; Xisto, C.; Linke, F.; Melkert, J.; et al. Evaluating the climate impact of aviation emission scenarios towards the Paris agreement including COVID-19 effects. *Nature Communications* **2021**, *12*, 3841. https://doi.org/10.1038/s41467-021-24091-y
