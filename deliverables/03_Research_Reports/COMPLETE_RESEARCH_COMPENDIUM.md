# 全部研究成果与核验报告汇编

本汇编收录英文论文、补充材料、中文说明、数据来源与口径核验、参考文献及内部审查报告。审查报告是修订前快照，对应问题的最终处置见“最终核验与审查问题处置”。末尾研究方案为历史归档，当前结论以英文论文和最终核验记录为准。完整数值表及代码另见Excel和复现压缩包。

# 01 英文论文全文

## Efficiency Gains, Growing Fuel Demand and Deployment Frontiers in China’s Commercial Aviation

### Abstract

Improving aircraft efficiency does not necessarily reduce aviation fuel demand when transport activity expands. This study links official Chinese aviation statistics to deployment-constrained transition scenarios. Eleven paired annual observations for 2015–2025 were assembled from Civil Aviation Administration of China publications; selected turnover observations were cross-checked against National Bureau of Statistics yearbooks. The principal analysis starts in 2017 because statistical processing changed that year. Chain-linked logarithmic-mean decomposition shows that, during 2017–2025, transport turnover increased by 51.5% and reported fuel intensity declined by 11.3%, while reconstructed fuel demand rose by 34.4%. Intensity improvements offset 27.9% of the activity-related increase. A nonlinear deployment model separates insufficient technical benefit from insufficient adoption speed. Under an illustrative 4% annual activity-growth and 1% baseline-efficiency-improvement scenario, even complete deployment requires an additional 35.4% efficiency advantage to hold 2040 fuel demand at its 2025 level. Under a lower-growth scenario, an eight-year delay more than doubles the required adoption rate. These are conditional feasibility results, not forecasts. The findings connect observed efficiency–activity mismatches to transparent technology-deployment requirements without attributing aggregate changes to domestic engine research or claiming climate neutrality.

**Keywords:** civil aviation; fuel efficiency; technology deployment; logarithmic-mean decomposition; quasi-Monte Carlo; sustainability transition

### 1. Introduction

Aviation sustainability depends on how rapidly operational improvements become effective across a growing transport system. Better engines, aircraft and operations can reduce fuel consumption per unit of transport, but their sector-wide effect depends on activity growth and adoption. Global transition studies consequently combine efficiency improvements with fuel substitution, demand assumptions and, in some pathways, carbon removals [1–3]. Their conclusions differ with their system boundaries and assumptions. A useful national analysis must therefore distinguish what has already been observed from what additional deployment would have to achieve.

This distinction matters for China-registered commercial air carriers. They operate domestic and international services, and their transport activity experienced a severe interruption and subsequent recovery around the COVID-19 pandemic. An intensity decline during recovery cannot automatically be interpreted as persistent technological progress. Conversely, a fall in aggregate fuel demand during a transport contraction does not establish a durable sustainability transition. The latest official statistics permit these changes to be examined through 2025, but they also require explicit attention to statistical coverage, rounding and a change in processing procedures.

China-specific aviation decomposition is established prior art. Liu and Zhang studied the drivers of decoupling between transport growth and carbon emissions over 1996–2015 [4]. Cui and Lei examined complementary mitigation pathways for China–foreign routes, a different operational boundary [5]. The present study does not claim to introduce aviation decomposition or to identify a new causal relationship between efficiency and demand. Its question is narrower: after updating the official record through 2025, what combination of additional efficiency benefit, deployment speed and deployment timing would be sufficient to prevent further fuel-demand growth?

Recent research makes the timing question especially relevant. Martulli et al. distinguish announced sustainable aviation fuel (SAF) production capacity from capacity realised on schedule [6]. Their global and European evidence motivates explicit treatment of implementation delays, but does not supply China-specific adoption parameters. Policy analyses also question reliance on future technical improvements without examining activity assumptions [7], while aviation scenarios published in this journal consider interactions among fuel transitions, operational efficiency and demand [8]. These studies suggest examining implementation constraints jointly with the size of the efficiency improvement, rather than assuming immediate fleet-wide availability.

Our conceptual starting point is the coordination of design, testing and manufacturing in aero-engine development. Technical potential has to pass through validation, certification, production and operational adoption before influencing fleet-wide fuel use. However, national fuel-intensity statistics cannot measure those capabilities separately or identify their causal effects. We retain this coordination perspective as a motivation for deployment constraints and replace untraceable capability indices with publicly documented operational statistics.

The study makes three connected contributions. First, it constructs a source-linked annual dataset with an explicit operator-based boundary and quantifies activity and intensity contributions across expansion, disruption and recovery. Second, it derives an analytical frontier distinguishing an inadequate efficiency benefit from an inadequate deployment rate. Third, it checks that frontier using nonlinear simulation, exact parameter-box bounds and scrambled Sobol scenario exploration. A small-sample Bayesian forecasting diagnostic is reported separately and is not used to claim predictive superiority or calibrate technology adoption. The resulting contribution is a reproducible assessment of transition requirements, rather than a long-term forecast or a causal estimate of engine innovation.

### 2. Data and Methods

#### 2.1. Official data, coverage and comparability

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

#### 2.2. Accounting and chain-linked decomposition

With Q measured in 10⁸ tonne-km and I in kg/tonne-km, reconstructed fuel demand in Mt is

$$F_t = 0.1 Q_t I_t. \tag{1}$$

For strictly positive quantities, the logarithmic mean is L(x,y) = (x − y)/(ln x − ln y), with the continuous limit L(x,x) = x. The additive logarithmic-mean Divisia index (LMDI) approach [17] gives the adjacent-year contributions

$$D_{Q,t}=L(F_t,F_{t-1})\ln(Q_t/Q_{t-1}), \qquad D_{I,t}=L(F_t,F_{t-1})\ln(I_t/I_{t-1}). \tag{2}$$

Their sum equals F_t − F_(t−1). We sum adjacent-year contributions within three periods: 2017–2019, 2019–2022 and 2022–2025. The dates are transparent descriptive groupings, not statistically estimated breakpoints. Direct endpoint decomposition is retained as a sensitivity analysis because a path containing a disruption and recovery can allocate contributions differently from a single endpoint comparison. No contribution is interpreted as a causal treatment effect.

We report the intensity offset as −ΣD_I/ΣD_Q only when the activity contribution is positive. An offset below one means that the net intensity contribution did not cancel the activity contribution. This accounting ratio does not identify a rebound effect, which would require evidence that efficiency changes caused demand changes [9]. Rounding sensitivity perturbs the start and end Q values by ±0.005 and I values by ±0.0005 at all sixteen endpoint corners. These are reporting-precision perturbations, not confidence intervals or estimates of systematic measurement error.

#### 2.3. A deployment-constrained transition model

We normalise future fuel demand to the 2025 reconstructed level. Let h denote years after 2025, g the continuous annual activity-growth rate, b the continuous baseline intensity-improvement rate, θ an additional realised efficiency advantage, r the annual fuel-use-weighted adoption rate among the remaining non-adopting share, and τ the delay before additional adoption starts. The adopted share and fuel ratio are

$$s_h=1-(1-r)^{\max(h-\tau,0)}, \qquad R_h=\frac{F_h}{F_{2025}}=\exp[(g-b)h](1-\theta s_h). \tag{3}$$

The additional advantage θ is relative to an already improving baseline, preventing double counting of baseline efficiency gains. It is not an engine test-bench efficiency or an estimate of any domestic engine’s effect. Likewise, r refers to the distribution of fuel use, not the percentage of aircraft replaced. Its conversion to aircraft numbers would require fleet-vintage, utilisation and engine-configuration data that are unavailable here. The delay represents a conditional deployment constraint; it is not estimated from the supplied capability framework.

For horizon H, target fuel ratio κ and θ > 0, the required adopted share is

$$s_{\mathrm{req}}=\frac{1-\kappa\exp[-(g-b)H]}{\theta}. \tag{4}$$

If the numerator is non-positive, the baseline already meets the target. If s_req > 1, even complete adoption is insufficient. If 0 < s_req ≤ 1 and H > τ, the required adoption rate is

$$r_{\mathrm{req}}=1-(1-s_{\mathrm{req}})^{1/(H-\tau)}. \tag{5}$$

If H ≤ τ and the baseline misses the target, the additional technology cannot help within that horizon. When θ = 0, additional adoption has no effect on the baseline path. These cases distinguish an efficiency-benefit constraint from a deployment-speed constraint. The full-adoption necessary condition is θ ≥ max{0, 1 − κ exp[−(g−b)H]}. Faster deployment cannot overcome a violation of that condition.

#### 2.4. Scenario domain and numerical verification

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

#### 2.5. A deliberately limited forecasting diagnostic

To assess whether the short historical series could defensibly supply a predictive baseline, we implemented a conjugate Bayesian benchmark for annual log-intensity changes: Δln I ~ N(μ,σ²), μ|σ² ~ N(0,σ²), and σ² ~ InvGamma(2,0.05²). Sensitivities used inverse-gamma scales 0.02² and 0.10². Predictions were evaluated against an unchanged-intensity baseline and an unshrunk historical-drift baseline using forward-only training and at least eight valid annual differences. The Bayesian benchmark’s original-scale point predictions are medians of exponentiated Student-t distributions, not means. Differences touching 2020–2022 were omitted in a separate training sensitivity without bridging excluded years. These diagnostics are documented in the supplementary material and do not calibrate the scenario ranges.

#### 2.6. Research-assistance transparency

OpenAI Codex assisted with source-search formulation, extraction workflows, code development and checking, and English manuscript drafting. The research-assistance workflow retrieved and compared source records and bibliographic metadata with official documents and publisher records, and generated the reported calculations through executed Python scripts. Independent verification and approval by the named human authors remain pending. This assistance does not establish authorship eligibility or institutional approval. Human authors must review the underlying records, interpretation and disclosure before submission. No survey responses, confidential engine-performance records or human-subject observations were used in this analysis.

### 3. Results

#### 3.1. Lower intensity coexisted with higher reconstructed fuel demand

Between 2017 and 2025, transport turnover increased from 1083.08 to 1640.83 × 10⁸ tonne-km, or 51.5%, while reported intensity fell from 0.293 to 0.260 kg/tonne-km, or 11.3%. Their product implies fuel demand increasing from 31.73 to 42.66 Mt, a rise of 34.4% (Figure 1). The endpoint rounding perturbations place this increase between 33.95% and 34.92%; reporting precision does not reverse the direction. This calculation establishes an activity–efficiency mismatch, not an engine-specific performance effect.

The recovery-period comparison is not solely a low-base phenomenon. Relative to 2019, turnover in 2025 was 26.9% higher and intensity 8.8% lower, yet reconstructed fuel demand remained 15.7% higher. Conversely, the 2019–2022 decline in reconstructed fuel demand coincided with sharply lower activity and higher intensity. That pattern is inconsistent with interpreting the aggregate contraction itself as evidence of technological improvement.

![Figure 1](/workspace/research/output/figures/figure1_historical_indices.png)

**Figure 1. Activity, intensity and reconstructed fuel demand in the extended official record.** All series are indexed to 2015 = 100 using eleven paired annual CAAC observations. The shaded interval identifies 2020–2022, and the vertical marker identifies the 2017 change in statistical processing. The main comparison begins in 2017. Fuel demand is derived from Q and I and is not an independent validation series. Lines connect annual observations; they do not represent additional measurements or fitted trends. Source data: `annual.csv` and the observation ledger supplied with the replication materials.

#### 3.2. The intensity contribution only partially offset expansion

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

![Figure 2](/workspace/research/output/figures/figure2_chain_lmdi.png)

**Figure 2. Contributions across expansion, disruption and recovery.** Bars show chain-linked LMDI activity and intensity contributions in Mt; diamonds show their net sum. Each contribution is computed from the annual official inputs and summed within the stated interval. These are deterministic accounting components, with no sampling-error bars or causal interpretation. Source data: `periods.csv` supplied with the replication materials.

#### 3.3. Technical potential and deployment speed impose different constraints

The analytical frontier identifies circumstances in which deployment acceleration alone cannot meet the fuel constraint. Under an illustrative 4% ordinary annual activity-growth rate and 1% baseline annual intensity reduction, the additional full-adoption advantage required by 2040 is 35.4%. Even a hypothetical 30% advantage deployed completely would yield a terminal fuel ratio of 1.084, or 8.4% above the 2025 benchmark. This is a conditional result about those assumptions; it is not a forecast of Chinese demand or an estimate of engine potential.

A lower-growth illustration exposes the timing constraint. With 2% annual activity growth, 1% baseline annual intensity reduction and an additional 20% advantage, at least 68.0% of fuel use must have adopted the incremental improvement by 2040. The required annual adoption rate is 7.3% with no delay, 9.1% with a three-year delay and 15.0% with an eight-year delay (Figure 3). The longest delay pushes the requirement above the 12% upper rate used in the exploratory domain. These rates refer to fuel-use-weighted diffusion of the additional benefit, not the share of aircraft that an airline should replace each year.

![Figure 3](/workspace/research/output/figures/figure3_deployment_thresholds.png)

**Figure 3. Conditional efficiency and deployment frontiers for a 2040 fuel constraint.** (a) The minimum additional advantage under complete adoption, with alternative assumed baseline intensity-improvement rates. (b) The annual fuel-use-weighted adoption rate required under the illustrative 2% activity-growth, 1% baseline-improvement and 20% additional-advantage case, as the delay increases. The 12% comparison is the exploration-domain upper bound, not an observed Chinese replacement rate. Ordinary percentage rates are converted to continuous rates before calculation. All curves are assumption-conditional calculations, not observations or official forecasts; source data are supplied for both panels.

#### 3.4. Global scenario exploration confirms a restricted feasible region

At 2¹⁴ design points per delay, 6.79%, 5.11% and 2.61% of the specified parameter combinations met the non-increasing-fuel constraint for delays of zero, three and eight years, respectively. These are shares of a chosen design space, not estimated success probabilities. Moving from 2¹² to 2¹⁴ points changed these shares by at most 0.24 percentage points. Scenario medians changed by at most 0.0013 in the terminal fuel ratio, indicating that the reported numerical summaries were not driven by the initial integration resolution.

Exact corner evaluation gave terminal ratios from 0.740 to 2.365 over the entire specified domain. Thus some combinations were feasible, but the benchmark was not satisfied throughout the uncertainty set. This range is an analytical bound for the stated assumptions, not an empirical prediction interval. The restricted feasible region is conditional on the selected growth and improvement domain; broadening or reweighting that domain would alter its design-space share.

The forecasting diagnostic does not justify replacing these transparent assumptions with a claimed accurate forecast. The extended eleven-year record supplies only two eligible one-year tests, 2024 and 2025. The Bayesian benchmark’s mean absolute error was 0.0148 kg/tonne-km, compared with 0.0160 for unchanged intensity and 0.0147 for unshrunk drift. Two tests cannot establish reliable superiority. The post-2017 record supplies no eligible out-of-sample test under the same eight-difference training rule, and pandemic-excluded training has insufficient differences. These limits are reported rather than relaxed after seeing the results.

### 4. Discussion

#### 4.1. Efficiency progress and a sustainability transition are different achievements

The observed record supports a limited but consequential conclusion: the reported efficiency improvement did not offset growth in the transport activity of China-registered air carriers. This complements earlier Chinese decomposition work [4] while extending observation through the latest verified 2025 bulletin. The result should not be interpreted as proof that efficiency caused traffic growth, nor as evidence that specific engines failed to improve. It concerns the aggregate balance between activity and reported fuel intensity.

The distinction helps reconcile apparently different aviation-transition narratives. Global studies identify multiple combinations of technology, fuel and demand levers [1–3]. Policy-document analysis questions technology-centred growth narratives [7], while economic analysis highlights interactions among efficiency standards, carbon pricing and demand responses [9]. Our model does not choose a universally necessary demand pathway. It states the growth-compatible efficiency and deployment conditions explicitly. Where technical benefit is inadequate, faster deployment cannot solve the accounting mismatch; where benefit is adequate, timing can still prevent its realisation within the target horizon.

The disruption and recovery further caution against reading an annual fuel-intensity series as a technological learning curve. Pandemic-era operational restructuring can change utilisation and the passenger/freight or route mix alongside technology. COVID-sensitive aviation-climate scenarios already recognise that activity shocks influence future pathways [20]. The present aggregate data cannot separate these mechanisms, and the small forecasting diagnostic provides no basis for extending the rapid recent intensity decline indefinitely.

#### 4.2. What the deployment frontier means for capability coordination

The design–testing–manufacturing perspective becomes operationally useful when framed as a constraint on when an improvement can enter service and how rapidly it can spread. Testing and certification can affect the waiting time, while manufacturing and fleet absorption can affect adoption. However, those are hypotheses about mechanisms, not effects estimated by this dataset. Neither a capability index nor a causal coefficient for domestic engine development is inferred from the aggregate fuel series.

Recent evidence about announced versus realised sustainable-fuel capacity illustrates why potential and deployment should remain separate [6]. The analogy is conceptual: fuel-production projects and aircraft/engine adoption have different physical and institutional processes. Importing a global SAF realisation rate into a Chinese fleet model would conceal that difference. The transparent frontier instead allows decision makers to insert independently documented assumptions when such data become available.

The implications for evaluation are concrete. A technology programme can be assessed against the additional operational benefit required at full adoption, the achievable fuel-use-weighted diffusion rate and the time remaining after validation and certification. A programme that passes only the first test may still miss an aggregate fuel objective. Conversely, a technical shortfall should not be disguised as a deployment-speed problem. These distinctions support integrated evaluation without claiming an investment optimum, which would require costs and resource constraints absent here.

#### 4.3. Fuel-demand feasibility is narrower than climate neutrality

This study deliberately reports fuel demand rather than convert it into a supposedly comprehensive climate metric. Fuel substitution, lifecycle greenhouse-gas emissions, contrails and air-quality effects require additional accounting. Route-based mitigation studies [5] and scenario work in Sustainability [8] evaluate levers beyond operational fuel intensity. Sacchi et al. further show why climate-neutrality definitions and resource constraints matter [3]. A pathway meeting the present non-increasing-fuel benchmark is therefore not necessarily climate-neutral, while an appropriately evidenced lifecycle fuel transition could change greenhouse-gas outcomes without reducing fuel mass by the same proportion.

The omitted effects are material boundaries. Contrail effects vary with flight and meteorological conditions [10], and recent modelling evaluates health impacts from aircraft-emission growth [11]. Neither can be recovered by multiplying this fuel series by an undifferentiated climate factor. The operator-based international-activity coverage also differs from a territorial national greenhouse-gas inventory. These distinctions constrain how the results can be used in policy comparisons.

#### 4.4. Limitations and a targeted extension

The first limitation is measurement. Official transport-aviation anchors support the intensity interpretation, but annual bulletins do not repeat all enterprise-level definitions. Reconstructed totals lack an independently observed fuel-total check. The 2017 processing change precludes assuming that the full 2015–2025 record is harmonised. Restricting the principal comparison to 2017–2025 and reporting rounding sensitivity reduce specific risks but do not remove systematic measurement uncertainty.

The second limitation is identification. Annual aggregates cannot distinguish engine improvements from airframe technology, operating conditions or transport composition. Consequently, the decomposition does not estimate policy effects, rebound elasticities or the causal value of capability coordination. Those questions require linked fleet, route, utilisation and technology-adoption data, rather than additional complexity fitted to eleven annual observations.

The third limitation is scenario calibration. The rectangular domain is a disclosed stress test, not an estimated joint distribution. Adoption is represented by a parsimonious diffusion function and omits fleet cohorts, heterogeneous utilisation and capacity bottlenecks beyond the stated delay and rate. A useful next extension would link aircraft/engine vintages and actual fuel-use shares to dated certification and delivery records. That would permit τ, r and θ to be constrained by observable deployment evidence and would test whether the simple frontier is adequate, rather than merely adding parameters.

### 5. Conclusions

Official activity and intensity statistics indicate that efficiency improvements did not offset the expansion of China-registered commercial air transport during 2017–2025: reconstructed fuel demand increased by 34.4%, and the net intensity contribution offset 27.9% of the activity contribution. Conditional deployment analysis shows why technical potential and deployment speed must be evaluated separately. An insufficient full-adoption benefit cannot be repaired by faster diffusion; a sufficient benefit can still miss a finite-horizon constraint when deployment is delayed. The practical value is an auditable set of growth, benefit and timing requirements. These results do not identify domestic aero-engine capability effects, predict a particular future pathway or establish climate neutrality.

### Data and Code Availability

The supplied Supplementary Replication Package (`REPLICATION_PACKAGE.zip`) includes the transcribed official observations, source URLs and page locators, SHA-256 source ledgers, NBS cross-publication checks, scenario configuration, Python analysis code, numerical outputs and figure source data. Original statistical documents are available from CAAC and NBS at the URLs in the source ledgers. No public repository DOI or GitHub release is claimed. A public archival link can be added after the authors deposit the verified package, or the package can be supplied as submission supplementary material subject to journal instructions.

### Author Declarations to Complete Before Submission

Author names, affiliations, corresponding-author details, contributions, funding and conflicts of interest must be supplied and verified by the human authors. No human participants were recruited for this study; the analysis uses public aggregate statistics. The relationship to any previously submitted or publicly available version of the underlying thesis must be checked and disclosed where applicable. These items are unresolved author information, not findings of this analysis.

### Acknowledgment of Generative Artificial Intelligence Assistance

OpenAI Codex was used for the research and drafting assistance described in Section 2.6. The human authors must review and revise the manuscript and underlying evidence, confirm the actual product/version information available to them, and declare substantive generative artificial intelligence use during submission in accordance with the journal’s current policy. No statement that human authors have already completed these checks is implied by this draft.

### References

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


# 02 补充材料全文

## Supplementary Information


### S1. Complete paired official record and provenance


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


### S2. Chain-linked and direct endpoint decomposition


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


### S3. Reporting-precision perturbations


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


### S4. Bayesian diagnostic, baselines and small-sample exclusions


Let d denote adjacent annual log-intensity changes. The conjugate model uses μ₀=0, κ₀=1, α₀=2 and β₀=0.05². For n changes with average d̄, κₙ=κ₀+n, μₙ=(κ₀μ₀+nd̄)/κₙ, αₙ=α₀+n/2, and βₙ=β₀+Σ(d−d̄)²/2+κ₀n(d̄−μ₀)²/(2κₙ). The h-step log-intensity predictive distribution is Student-t with 2αₙ degrees of freedom, location ln(I_T)+hμₙ and scale sqrt[(βₙ/αₙ)(h+h²/κₙ)]. Exponentiation supplies a median and central intervals; the exponentiated Student-t has no finite positive moments, so an original-scale predictive mean is not reported.


B0 is unchanged intensity. B1 adds the unshrunk training mean log change. B2 uses the shrunk posterior location. Every model uses the same eligible origin, with a minimum of eight prior valid annual differences; no target observation enters its training. MASE divides absolute prediction error by the mean absolute adjacent-year naive error in that origin’s training set. A zero denominator remains undefined.


| Model | Test years | n | MAE (kg/tonne-km) | MASE |
| --- | --- | --- | --- | --- |
| B0 | 2024, 2025 | 2 | 0.016000 | 1.894853 |
| B1 | 2024, 2025 | 2 | 0.014655 | 1.750015 |
| B2 | 2024, 2025 | 2 | 0.014790 | 1.764619 |


These two tests are diagnostics, not evidence of model superiority. The post-2017 series has no eligible out-of-sample test under the same rule. Excluding every training difference touching 2020–2022 leaves only six valid differences in the extended record, so the pandemic-exclusion forecast is skipped rather than formed by joining separated years. Prior scales 0.02² and 0.10² are retained in the machine-readable outputs. The forecasting diagnostic is not used to choose or calibrate the conditional scenario domain.


### S5. Conditional exploration, resolution and analytical bounds


The exact input configuration is `scenario_config.json`. g is uniform in the log-rate interval corresponding to ordinary growth of 2–6%; b is uniform in the continuous intensity-decline interval corresponding to ordinary reductions of 0–2%; θ and r have uniform design weights over 0.10–0.30 and 0.02–0.12, respectively. These are exploratory weights, not inferred parameter distributions. Delays are evaluated separately, not pooled into a probability mixture. H=15 and κ=1 define a 2040 non-increasing-fuel benchmark, not an asserted official target.


| Delay (years) | 2¹² design share meeting target (%) | 2¹⁴ share (%) | 2¹⁴ terminal-ratio median |
| --- | --- | --- | --- |
| 0.0 | 7.0312 | 6.7932 | 1.346867 |
| 3.0 | 5.2246 | 5.1147 | 1.370412 |
| 8.0 | 2.6367 | 2.6062 | 1.423835 |


The shares above describe only the stated design domain. They are not probabilities that China will meet a target. Scrambling seeds are 20261016, 20261017 and 20261018. No points are skipped or thinned. The higher-resolution results are stored with the resolution comparison; the initial individual design points are supplied in CSV. Re-running the documented code regenerates both.


By monotonicity, the lowest terminal ratio occurs at low g, high b, high θ, high r and the shortest delay; the highest occurs at the opposite corner. Exact bounds are 0.739640 and 2.364954. These are bounds for the assumed box, not empirical prediction limits. A cumulative-fuel diagnostic sums future years 1 through H, excluding the observed baseline year, in units of baseline annual fuel. It is retained in the numerical output but is not used to claim a carbon budget.


The analytical frontier explicitly distinguishes baseline-sufficient, full-adoption-insufficient and deployment-threshold cases. It does not truncate an impossible adopted share to one or interpret fuel-use-weighted adoption as aircraft-count replacement.


### S6. Reproduction and integrity boundaries


The replication README gives the offline reproduction command, exact software versions and input hashes. Eighteen deliberately synthetic arithmetic/mathematical checks cover accounting identities, unit conversion, Bayesian conjugacy and prediction variance, forward-only training, missing/excluded-year handling, adoption boundaries, analytic/numerical threshold agreement, monotonicity and exact scenario corners. These tests are not empirical observations. Official-document hashes, table transcriptions, coverage reasoning and figure-source values are separate evidence checks.


References were checked against DOI metadata and authoritative publisher records. Reading coverage differs by source: the Bergero and Dray papers were used at the official-abstract level; Ang (2005) was bibliographically verified but its full text was not retrieved. The decomposition equations and closure checks are self-contained. Current MDPI author instructions, scope and research-data/artificial-intelligence policies were read; these checks do not constitute a journal acceptance decision or human-author attestation.


No confidential thesis survey responses or unverified capability scores were reused. Public archive publication and formal submission have not been performed. Author details, contributions, funding, conflicts, prior-thesis relationship and human-author review remain to be completed by the authors.

# 03 作者说明与投稿前事项

## 英文研究稿交付说明

已完成英文全文、补充材料、三张可编辑矢量图及可复算代码。本文是根据附件研究主题重新建立公开数据实证的英文研究稿，不是原论文的逐章翻译。

### 研究主线

题目：*Efficiency Gains, Growing Fuel Demand and Deployment Frontiers in China’s Commercial Aviation*。

实证对象由原稿的“航空发动机研制能力”收窄到“中国境内注册航空运输企业的运输增长与燃油效率”，保留设计—试验—制造协同作为部署时滞与扩散约束的理论动机。未沿用原稿缺少可复核原始记录的问卷、能力指数、路径系数或仿真参数，也未用民航总体油耗推断国产发动机的因果效果。

### 实际完成的研究

- 采集并核验2015—2025年11组民航局官方周转量、吨公里油耗；早期缺失油耗未补造。国家统计局年鉴用于部分年份周转量的跨出版物核对，底层资料仍源自民航局，并不是第二套物理测量。
- 因2017年统计处理和审核规则变化，主分析采用2017—2025年；较早年份保留在扩展记录及补充分析中。
- 完成链式LMDI分解、舍入敏感性、非线性部署模型、解析可行边界、Sobol随机化准蒙特卡洛情景与精确参数角点检验。
- 实现并运行贝叶斯收缩漂移模型与两个基线，但扩展样本只有两个可评价年份，主窗口没有足够样本外检验。因此明确作为诊断，不宣称预测优势，也不据此校准未来技术参数。
- 核验并使用20条参考来源，包含2025—2026年研究，以及官方统计、政策和方法资料。对不同文献的实际阅读范围保留记录；Ang（2005）只完成书目核验，没有声称读取全文。

### 核心结果及解释

2017—2025年，运输周转量增长51.5%，吨公里油耗下降11.3%，按二者重构的燃油需求仍增长34.4%。链式分解中，强度改善抵消了活动扩张贡献的27.9%。燃油量是由官方四舍五入指标推算的估计，不是另行观测的官方燃油总量。

仿真将“收益不够”和“部署不够快”分开。例如在假设年活动增长4%、基线油耗强度每年下降1%的情况下，要在2040年不超过2025年的燃油需求，即使完全采用也需要额外35.4%的效率收益。这是给定假设下的解析结果，不是对中国需求或某型发动机的预测。

所有情景区间均已标为研究者压力测试假设。设计点达标占比不是现实达标概率；本文也没有得到完整生命周期减排、非二氧化碳气候影响或“气候中和”的结论。

### 已做核查及其限度

主要数值、单位、来源页面、11份核心公报哈希、引用编号及图表数据已由同平台工作流程交叉核对。18项合成算术/模型边界检查和离线复现已通过；这些检查不构成实证观测。三张图的文字大小、碰撞与适用面板对齐检查通过。

这些是辅助研究流程中的来源与技术核查，不是外部同行评审，也不能替代真实作者独立审阅。对Sustainability官网的核验支持范围和实质内容适配，但不能保证编辑初筛或录用。

### 投稿前仍须作者完成

1. 核实并补齐作者、单位、通讯作者、贡献、经费和利益冲突；不能由系统猜填。
2. 亲自审阅数据来源、统计口径、解释及引文，确认本文与既有学位论文/公开稿的关系，并作必要披露。
3. 根据期刊现行政策确认实质性生成式人工智能使用的披露及可核实的产品/版本信息。稿中没有替作者声明“已经完成独立核验”。
4. 将复现包作为补充材料，或先存入公共仓库后填写真实链接。当前没有替你上传GitHub、登记DOI、联系期刊或提交论文。

建议优先阅读英文摘要、Section 2.1统计边界、Table 3和Figure 3，确认研究对象和情景假设符合你的投稿意图。然后再完成作者声明和正式提交。


# 04 最终核验与审查问题处置

## Final verification and review dispositions

This is an internal consistency and provenance record for the delivered research draft. It is not external peer review, human-author approval, a journal acceptance assessment or an exhaustive proof of manuscript correctness. The method checker also contributed to the model implementation; shared platform/context and source records are retained rather than described as independent external review.

### Executed evidence

- Eleven official paired annual observations (2015–2025), with original-report SHA-256 digests, exact quotations and PDF page locators. All eleven source files were rehashed successfully. Selected NBS yearbook turnover values agree after conversion/rounding; their underlying statistics originate with CAAC.
- Main comparison restricted to 2017–2025 following the documented processing change. Reconstructed fuel is not an independent official measurement, a territorial inventory or a domestic-engine effect.
- All eleven annual fuel-unit conversions and all seven reported chain-period closures checked against the machine-readable results. Seven principal manuscript numerical bindings were mechanically compared with the results; additional scenario, posterior and source values were checked in the recorded technical reviews.
- Seven synthetic accounting assertions and eleven mathematical/model test cases passed. These checks do not create empirical observations.
- Offline reproduction completed from the frozen official extract and explicit scenario configuration. A newly extracted copy of the delivery archive was then rerun in a separate directory: accounting JSON, transition JSON, post-2017 diagnostic JSON, analytical-frontier JSON and supplementary tables matched the source outputs byte for byte. Limited Bayesian diagnostics, two resolutions of Sobol conditional scenarios and exact corner bounds were actually run. Forecasting remains diagnostic; scenario shares remain assumption-domain shares.
- Three figure sources and final PDFs passed the retained source, text-size and collision checks; the two-panel figure passed the 1.5 pt alignment gate. Every figure was visually inspected. Full figure notes and measured QA reports accompany the exports.
- Twenty reference entries were checked for numbered mapping and source identity. Literature reading coverage is recorded. Ang (2005) was bibliographically verified; no full-text reading is claimed. A follow-up OpenAlex/Semantic Scholar metadata query also did not identify accessible full text.
- The abstract contains 185 words under the recorded tokenisation check. Word delivery contains three embedded figures, three tables and five editable display-equation objects.
- The original supplied document’s hash is unchanged. No unpublished manuscript was sent to an external model, no journal was contacted, and no repository or article was publicly released.

### Review findings addressed

| Finding from reviewed snapshot | Final disposition |
|---|---|
| Ref. 15 named the wrong white paper | Corrected to the State Council Information Office transport-sustainability white-paper press conference; translated title identified |
| Ref. 16 needed accurate news-release identity | Added 2022 and identified CAAC's release of the policy/action document |
| Abstract suggested all paired variables had NBS cross-checks | Narrowed to selected turnover observations |
| Survey system has general-aviation and converted-denominator alternatives | Explicitly distinguished them from the transport indicator; continuity interpretation and residual limit retained |
| Student-t median wording could appear to cover all baselines | Limited to the Bayesian benchmark |
| Required-share formula divides by θ | Added θ > 0 and the zero-benefit boundary case |
| Ref. 9 has a narrower economic-policy role | Separated economic instrument/demand-response reasoning from policy-document narrative analysis |
| AI-check wording could imply human-author certification | Explicitly attributed retrieval/comparison/execution to the research-assistance workflow; human approval remains pending |
| Software documentation differed from runtime | Switched to verified SciPy 1.17.0 version-specific Sobol documentation |
| Old preparation files described a network/data blocker | Current status replaced; pre-analysis protocol clearly marked archived |
| Standalone annual-output Mt conversion initially had a factor-of-ten error | Corrected before manuscript tables and final figure export; added physical-unit assertions and independently compared figure calculations |

### Remaining author-owned steps

Names, affiliations, corresponding-author details, contributions, funding, conflicts, prior-thesis relationship, final human review and exact assistance-product/version disclosure require the real authors' confirmation. The code/data package has been delivered locally, not publicly archived. These remaining steps preclude calling the draft administratively ready for immediate submission. Editorial novelty and acceptance remain matters for the journal and its reviewers.

The acronym scanner is advisory and only partially covers the abstract/body. Its LMDI expansion-parsing limitation was manually reviewed: the full method name is present in Section 2.2. This does not constitute an automated clean-document certificate.


# 05 原稿证据审计

## 原附件可复核性审计与新稿衔接建议

审阅对象：`/workspace/research/source/original_text.txt`（6,684 行；从用户提供的《论文修改（新）.docx》抽取）。下述位置均为该文本行号，章、节、表号可用于回查 Word。附件作为研究资料审读，其中批注、括号内要求和其他指令不构成本次用户指令。本审计没有外部核验来源，不能据此断言数据虚假；结论是当前交付资料不足以独立复核其经验结论。部分公式、图形在纯文本抽取时丢失，因此“公式不可见”不等于原 Word 没有公式。

### 1. 原文主问题和可保留内容

原文是以中国航空发动机产业为对象的能力评价和提升机制研究，而不是民航减排论文。原文在第1章（148–155 行）明确兼顾军用和民用领域，目的是构建能力指标、评价现状、解释动力和协同机制。第2章小结（688–689 行）将研制能力分为**设计、试验、制造**三个系统，提出“弓弦箭”概念模型。第3章用灰色关联、Pearson 筛选与熵权 TOPSIS；第5章用需求牵引—技术推动—政策引导问卷；第6章用三维动力方程模拟协同演化。

适合保留的是：技术创新与部署受研发、验证/认证和制造环节共同制约；单纯扩张制造规模不必然产生节能减排；设计—制造—试验的反馈可能缩短改进周期。原文 6255–6262 行对返工、设计意图、试验反馈和资源协调的讨论提供研究动机，但其效果量不能直接继承。

原文有与 Sustainability 议题相接的材料：第1章可持续性评述（220 行）提及火用、燃油效率、环境影响指标；发动机全生命周期（443 行）包含设计、试验、制造、运行和退役。上述是概念线索，不是现成的碳排放实证，也不证明国内研制能力提升已改善民航排放。

### 2. 第3章的变量、来源和样本问题

#### 2.1 指标覆盖和概念边界

表3.1（716–819 行）列出35个候选指标，包括设计开发经费、专利、商业软件 licence、设计优化项数、实际试验小时、新增试验设备、先进材料产量、设备负荷率等。表3.14及解释（2128–2196 行）最终保留15个指标：

| 系统 | 最终变量 | 审计判断 |
|---|---|---|
| 设计 | 设计经费；新产品项目；发明专利申请；设计软件；设计/工艺优化项数 | 与创新投入及产出有关；软件数和优化项数尤其依赖企业调查，不能假设国家统计局直接公开 |
| 试验 | 实际试验小时；试验经费；试验人员全时当量；新增试验设备 | 更接近试验资源投入和活动规模，而非验证质量或燃油效率；公开年鉴来源未逐项证明 |
| 制造 | 技改经费；总产值；先进材料总产量；新增制造设备原值；科技人员；设备负荷率 | 主要体现规模和投入，不是绿色绩效；先进材料全行业产量不等于航空发动机专属投入 |

原文自己说明先进材料包含钛合金、高温合金和复合材料，并以“航空发动机制造是这些先进材料的主要销售市场”将材料总产量解释为发动机生产力（2190 行）。该归属比例没有原始证据；若新稿使用这些变量，必须确定行业边界及分配规则。第3章把所有指标作为正向指标（2244 行），但原文对设备负荷率又明确“太高”可能任务过重（2196 行）；这种非单调性不能靠统一正向标准化处理解决。

#### 2.2 2012–2021 原始来源未形成可追溯链

关键原文：

- 第3.5.1节，2275 行：“数据主要来源于现场调研数据，同时通过对2012-2021年《中国统计年鉴》、……《中国高技术统计年鉴》……《中国科技统计年鉴》的原始数据筛选和整理得到。”
- 第3.5.2节，2277 行：“利用SPSS软件对少数缺失数据进行了合理的替代。”
- 第3.2.1.2节，843 行：指标筛选数据却为“2010-2019年”，来源含现场调研和统计年鉴。
- 第2.3.3节，483 行：典型相关的资料时期又为“2005-2019年”，同样含企业现场调研。
- 第2章，504 行仍保留作者括注：“根据……相关数据（需要说明从哪来和列出具体数据吗）”。这是待完善的材料说明，不能当作已给出数据来源。

当前材料没有逐指标—逐年原始值—年鉴版本—表号/页码—统计口径—调查单位范围的映射，未列调查机构、数据获得日期、调查表或可共享原始记录。年鉴出版年份与统计数据年份的对应也未明确。“中国高技术统计年鉴”与前文“中国高技术产业统计年鉴”的书名不一致，需要实际来源确认。仅列官方年鉴名不足以证明15项国家航空发动机数据均可由该年鉴取得。

文中表3.16（2281 行起）等主要给出**无量纲化后数据**，例如2012年设计指标为0.78914、1.00466等；这些数值不能在缺少均值、单位和原始矩阵时还原为真实支出、专利或软件数量。后续大量权重/距离/贴近度表只能检验部分算法，不能追溯最初观测。

#### 2.3 经验识别风险

- 样本是10个全国年度，而非具有地区/企业横截面的面板。原文336、3584 行称“面板数据”，但第3章所展示的观测轴只有2012–2021年。不能扩大为省级或企业级样本。
- 缺失替代没有报告缺失位置、数量、机制、替代方法或敏感性。SPSS是软件名，不是插补方法。
- 表3.20（2495–2504 行）设计贴近度为0.253、0.132、0.352、0.267、0.485、0.485、0.494、0.588、0.788、0.872，存在下降；2509 行的“持续上升”应改为整体上升。综合指数也从2012年0.141降到2013年0.130（3530–3531 行）。
- 第3.5.2.5（3545–3576 行）将综合指数回归到其三个构成子指数，存在指标构成关系导致的机械关联，不能把系数解释为因果“驱动力”。样本仅10年，滞后1期后最多9条时间观测；未报告自相关、趋势、共线性和样本量。指数位于[0,1]不意味着观测被删失，不能仅凭有界性选择 Tobit。
- 将2016年前后趋势归因于集团成立或专项（2273、3544、3581 行）缺少对照、政策反事实、同期冲击控制或严谨识别。不能在新稿写成已识别的政策效果。

**处理建议：不把第3章数字、回归显著性或能力趋势当作新稿已核验实证。** 可以作为未发表附件提出的概念框架，在新稿中以公开资料重新构建可测研究对象；新数据不能伪装成对原15项能力指标的复刻。

### 3. 第5章问卷是否可复核

第5.4.1.1节（5556–5558 行）称向北京、天津、上海、陕西、四川、辽宁相关单位通过邮件发放452份、回收428份、剔除64份、有效364份（364/452约80.5%）。职务分布26+84+108+92+54=364；设计/试验/制造/综合单位分布98+85+124+57=364，汇总加总在算术上成立。

表5.1（5559–5605 行）给出22项7点量表，涉及需求牵引4项、技术推动4项、政策引导3项，以及设计/试验/制造能力11项。第5.4.1.2（5608–5609 行）报告CITC与Cronbach’s α，后文提供因子分析及中介/调节结果。

但是，抽取资料中未发现：调查开始/结束日期；受访单位和个人抽样框；邀请对象去重规则及各单位嵌套关系；64份无效问卷剔除标准；原始逐人逐题回答；脱敏数据文件；专家预调查规模/修改记录；成熟量表逐项原始出处及改编验证；知情同意/伦理审查或豁免说明；重现统计的代码。正文中的“成熟量表”或信效度汇总不能替代这些材料。

因此既不能确认问卷造假，也不能独立确认已完成的364人调查。当前不能将其人数、路径系数、显著性和研究过程直接写成新英文稿作者实施且已复核的研究；若要保留，须作者提供可核验脱敏数据、采集及伦理材料后再分析。新稿可以完全采用公开二手数据，使问卷不是本次完成研究的必要前置条件。

### 4. 第6章协同仿真输入和模型风险

第6.3.2节（6272–6297 行）把设计、试验、制造活动定为三个状态，环境规制定为控制参数。第6.4.1（6332 行）给出最终参数α=0.878、β=0.759、γ=0.748、θ=0.737，但追溯链不足：

1. 参数从前面能力得分和7项政策量表生成，未给输入逐年值、题项全表、归一化和权重的可复核记录，没有拟合过程、估计误差或样本外验证。6332 行说“第五章……评价研究”，实际能力评价在第三章，章次指向错误。
2. 表6.1（6292–6297 行）将β对应试验、γ对应制造；表6.2（6344–6349 行）却将调整参数2对应制造、参数3对应试验。状态与参数映射必须查原模型及代码后确认。
3. θ的题项举例包括国拨资金占比、R&D税收减免、企业减免税、政策文件（6332 行）。这些测量的是产业支持/治理环境，不能直接命名为environmental regulation并解释为污染或气候规制。
4. 至少两个动力方程系数被“本文假设=2”固定（6311 行），并非实测。这是可报告的结构假设，不能伪称数据估计结果。
5. 初始状态在[0,1]用0.1网格重复11³=1,331次（6351 行），只是情景网格，不构成1,331个真实样本。仿真结果与采集数据必须区分。
6. 线性稳定性讨论由某特征方程有负系数推到系统“肯定不满足”稳定条件，并进一步推到“不存在阈值条件”（6329 行），结论逻辑过强；须指定平衡点、Jacobian与局部/全局范围，不能直接继承。
7. 仿真称设计制造一体化优于设计制造试验一体化，进而主张试验相对独立（6370–6384 行附近）。在无参数估计、验证和充分敏感性分析时，这仅是设定方程下的条件性模拟结果，不是可直接用于产业制度建议的实证发现。

公式在纯文本中大量为空，必须用Word公式对象或原仿真代码复核精确形式后才谈复现；当前审计不尝试补写丢失公式，也不推断原图是否绘制正确。

### 5. 适合新英文稿的可验证衔接

建议将论文问题收窄为：**民用航空交通增长、燃油效率改进和技术部署滞后共同决定排放路径；如何在公开数据约束下评估改进速度与需求增长的匹配程度，以及何种可核算的技术部署情景能够降低排放。** 这保留原文关注的技术能力协调问题，但把可测结果明确转成民航部门的运营与减排绩效。

| 原文概念 | 可保留的理论关系 | 新实证必须重新取得的可测量变量 | 不能跨越的推断 |
|---|---|---|---|
| 设计能力 | 先进发动机/机体技术可能降低单位运输能耗 | 经独立权威来源验证的技术效率改进范围；或机队年龄/型号/实际燃油消耗 | 全国运营强度不能识别国内发动机设计能力 |
| 试验能力 | 验证、适航及认证产生部署时滞 | 有官方时间戳的认证/部署节点；情景模型中明确标为假设的部署时滞 | 不能把假定时滞叫做从问卷估计的参数 |
| 制造能力 | 机队更新和技术扩散影响效率实现 | 民航机队规模、引进/退出量、运输周转量、燃油使用或官方强度 | 机队扩张不等于国产发动机制造能力提升 |
| 协同机制 | 技术准备与部署速度存在匹配约束 | 有质量控制的年度公开序列与不确定性情景 | 条件性仿真不能证明组织协同的因果效果 |
| 政策支持 | 激励可能改变技术部署和燃料结构 | 可核验政策节点及情景假设，或具有识别条件的政策数据 | 产业支持指数不能称为已观察到的气候规制效果 |

可采用有约束的状态空间/变点模型描述历史强度轨迹，加上透明的机队/技术扩散或需求—强度情景核算。模型复杂度应服务明确问题及可验证数据；20年左右的全国年度序列不足以支持深度神经网络、大量自由参数、未经识别的因果森林或声称精准长期预测。若输出使用未来轨迹，必须称为assumption-conditional scenarios，报告历史验证、参数敏感性和不确定性，不能当作官方预测。

新稿必须区分燃油燃烧CO₂、生命周期温室气体和非CO₂气候效应；官方燃油强度乘以运输量只能按对应口径得到燃油/燃烧CO₂核算，不得自动扩展为全生命周期排放。公众统计口径（航空公司运输、民航全行业、国内/国际、客货周转量）必须全程一致。

### 6. 结论供主稿使用

原附件可以贡献研究背景、设计—制造—验证协同的理论动机和研究缺口，不能在目前材料条件下直接贡献已经独立复核的能力面板、问卷或仿真参数。最稳妥的完成路线是：基于公开官方民航/统计数据重建一个范围清晰的新实证，明确发动机技术只是效率改进的机制之一，保留能力协调为理论解释和部署情景，而不是把部门减排结果声称为对国产航空发动机能力的直接因果测量。


# 06 统计口径核验

## Official-source coverage and turnover cross-check

The evidence supports a **transport-aviation interpretation** of the annual CAAC fuel-intensity series, with an explicit continuity qualification. This is sufficient for a transparent derived fuel-use estimate; it is not proof that annual operator-level microdata have been matched or that an independent national fuel total has been obtained. The structured evidence, exact URLs, retrieval times, full SHA-256 hashes and printed/physical PDF page locators are in `scope_evidence.json`. Original official files are retained in `raw/`.

### Transport activity covers operators, including international services

CAAC's 2024 statistical system, aviation-company transport table, printed p.9 (PDF p.13), requires reporting by enterprises registered in China operating scheduled or nonscheduled civil transport. Domestic services (with Hong Kong/Macao/Taiwan routes separately identified as a subset) and international services are included, and the operating carrier reports the activity. The 2024 annual bulletin, note [3], printed p.20 (PDF p.22), explicitly states that turnover and related activity data are carried by domestic airlines. The NBS 2025 yearbook chapter explanation independently republishes the same scope and explicitly excludes foreign airlines operating in China.

Thus this is an **operator-based statistical boundary**. It is not all flights departing/arriving at Chinese airports, territorial emissions, only domestic routes, or only fuel sold in China. It excludes the energy used by airports, air-traffic control, manufacturing and other civil-aviation establishments. Neither an international flight's full distance nor the related fuel should be labelled a domestic aviation national-inventory quantity.

NBS identifies CAAC among the underlying official data suppliers. Its publication provides a useful transcription, unit and cross-publication consistency check, not statistically independent original measurement.

### NBS numerical cross-check

Values were manually transcribed from the original official NBS table images, which have been downloaded and visually inspected. CSV provenance is in `nbs_turnover_crosscheck.csv`.

| Observation year | NBS table | NBS original total, 10,000 tonne-km | Converted total, 100 million tonne-km | CAAC annual bulletin | Comparison |
|---|---|---:|---:|---:|---|
| 2019 | China Statistical Yearbook 2020, 16-30 | 12,932,530 | 1293.2530 | 1293.25 | Same after rounding |
| 2023 | China Statistical Yearbook 2024, 16-30 | 11,883,381 | 1188.3381 | 1188.34 | Same after rounding |
| 2023 | China Statistical Yearbook 2025, 16-29 | 11,883,381 | 1188.3381 | 1188.34 | Unchanged across these two NBS editions |
| 2024 | China Statistical Yearbook 2025, 16-29 | 14,851,708 | 1485.1708 | 1485.17 | Same after rounding |

No substantive revision or conflict was found for these checks. The differences before rounding reflect the NBS table's finer display precision. No versions were averaged. CAAC says that formal annual reports supersede previously released preliminary figures where they differ. The NBS 2026 yearbook index was not available at its standard URL during retrieval (404), so no NBS 2025-year numerical cross-check is claimed. The separately downloaded CAAC 2025 annual bulletin is available, but is not an NBS confirmation.

### Fuel-intensity interpretation: why it is supported and what remains uncertain

The 2019 CAAC bulletin reports 0.285 kg/tonne-km. A separate CAAC report of the 22 December 2020 State Council Information Office white-paper press conference explicitly states: “2019年，我国运输航空每吨公里油耗和碳排放分别为0.285千克和0.898千克”. This is a direct same-year, same-value identification of the statistic as **transport aviation**.

The CAAC release of *2022 Policies and Actions of China Civil Aviation Green Development* explicitly calls the 2019 value “中国运输机队燃效”, again 0.285 kg/tonne-km, and in the same paragraph reports the 2021 identically named national intensity, 0.309. The official January 2022 announcement of the Fourteenth Five-Year Green Civil Aviation Plan describes the continuing indicator as “运输航空单位吨公里油耗”. These sources support continuity of the named official transport-aviation indicator rather than interpreting the series as airport or general-aviation energy use.

The 2024 statistical system provides the required mathematical definition in item 126, printed pp.80–81 (PDF pp.84–85): transport fuel intensity is actual transport-flight fuel in tonnes divided by transport tonne-km, multiplied by 1,000 to yield kg/tonne-km. Item 17 defines total transport tonne-km as passenger tonne-km plus freight tonne-km plus mail tonne-km. Passenger mass conversion uses 90 kg per adult including baggage, with half and one-tenth weights for children and infants; a simple multiplication of all passenger-km by 0.09 cannot independently recreate the official total without passenger composition.

The same item 126 also lists **separate** general-aviation converted-tonne-km and combined average-converted-tonne-km measures; the collection form covers both transport and general aviation. The distinction initially prevented treating the bulletin's abbreviated label alone as complete scope proof. The explicit official 2019 transport mapping, later semantic anchors and continuing common series now support a transport interpretation. They do not constitute a newly recovered annual microdata match. No separate official same-year wording was retrieved that repeats “transport aviation” beside the exact latest 2024 value 0.271 or 2025 value 0.260; this limitation must not be disguised as a confirmed yearly definition.

Recommended analytical status is therefore `supported_transport_interpretation_with_continuity_caveat`. A boolean scope flag may be true **only if its documented meaning is this supported interpretive alignment**, not a claim that every annual numerator and denominator population has independently been audited. The multiplicative output should be called **derived/implied transport fuel-use estimate**, not “independently observed official fuel consumption”. Annual fuel intensity is rounded to three decimal places, so reconstruction and confidence statements must account for display rounding, in addition to any statistical uncertainty.

Suggested manuscript disclosure:

> We interpret the consistently named CAAC fuel-intensity series as referring to transport aviation. This interpretation is anchored by a separate official statement identifying the 2019 bulletin value explicitly as transport-aviation fuel intensity, subsequent official descriptions of the same indicator, and the transport fuel-intensity formula in CAAC's statistical system. Annual bulletins do not repeat an operator-level denominator specification each year. Fuel use reconstructed from turnover and intensity is therefore a derived estimate under this documented continuity interpretation, rather than an independently observed national fuel total. The operator boundary includes international services by China-registered carriers and excludes foreign-carrier activity and airport energy use.

### Airport throughput cannot replace transport turnover

CAAC's airport table instructions, printed p.22 (PDF p.26), explicitly include foreign airlines and aggregate passengers and cargo entering and leaving the airport. An airport passenger is a handling event; turnover is weight times actual flown distance. A domestic airport pair may record the same passenger at both ends, while long-haul and short-haul movements have different distance weights. Airport passenger or cargo throughput therefore cannot be multiplied by airline kg/tonne-km fuel intensity, used as its denominator, or pooled with the activity series without an entirely different accounting model.

No original manuscript data, original survey responses, unpublished engine-development indicators or invented official observations were used in this audit.


# 07 内部方法核对（修订前快照）

## Internal technical methods check

Review date: 16 October 2026. This is an internal, same-platform technical check, not external peer review, an independent certification of the study, or a prediction of journal acceptance. The reviewer contributed to the transition-model implementation; the manuscript was checked separately against saved outputs and standalone arithmetic, but that contribution limits any claim of reviewer independence.

Reviewed manuscript snapshot: `/workspace/research/output/MANUSCRIPT.md`, SHA-256 `96eda33b596c8f97ee79e17c265c69579040fd2a4a8aff1342c97011844bd79a`. Line numbers below refer to that snapshot.

### Overall finding

No material numerical, unit-conversion, chain-versus-endpoint, scenario-configuration, or training-time inconsistency was found in the checked manuscript. Two small methods clarifications should be made before final assembly. The main 2017–2025 window, extended 2015–2025 diagnostic, and absence of eligible post-2017 forecast tests are represented correctly. No manuscript changes were made during this check.

### Wording to fix

1. **Line 100: qualify the predictive-distribution statement.** “Original-scale point predictions are medians of exponentiated Student-t distributions” should refer specifically to the Bayesian benchmark. B0 is a deterministic unchanged-intensity baseline and B1 is an unshrunk plug-in drift baseline; the implementation does not assign those two baselines the Bayesian Student-t distribution. Suggested wording: “The Bayesian benchmark’s original-scale point predictions are medians of exponentiated Student-t distributions, not means.” This does not change any reported value.

2. **Lines 70–78: state the domain of Equation (4).** The required-share formula divides by θ. The actual stress-test domain has θ between 0.10 and 0.30 and is therefore valid, but the general formula should say “For θ > 0”. For completeness, add that θ = 0 cannot change the baseline and therefore cannot meet an otherwise missed target. The code already handles this boundary explicitly. This is a domain clarification, not a failed numerical result.

### Checked and consistent

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

### Standalone arithmetic recheck

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

### Delivery-package issue outside the manuscript calculation

`output/RESEARCH_STATUS.md` still describes the earlier network-blocked, no-data stage. If supplied beside the current completed manuscript without a prominent historical label, it contradicts the actual replication status. Update it, explicitly archive it as a dated progress record, or exclude it from the submission package. This is a packaging correction, not a numerical defect in the manuscript.

### Limits of this check

The review checked formulas, numerical consistency, saved configuration, sample eligibility, and interpretation boundaries. It did not re-authenticate every official PDF from the publisher, re-perform the literature search, verify author declarations, assess all journal policies, evaluate originality against every related article, or reproduce an external editor's judgement. The official-source intensity mapping remains a measurement assumption supported by documented anchors; this check does not turn it into a direct independent fuel-total observation. The study remains a descriptive accounting exercise plus explicitly conditional deployment analysis, and the small forecasting exercise remains diagnostic.


# 08 内部来源核对（修订前快照）

## Internal source and boundary review

This is an internal source audit conducted within the same Codex platform. It is not external peer review, journal review, human-author verification or acceptance assessment. No manuscript text was changed.

Reviewed file: `/workspace/research/output/MANUSCRIPT.md`, 228-line snapshot, SHA-256 `96eda33b596c8f97ee79e17c265c69579040fd2a4a8aff1342c97011844bd79a`. Line numbers below refer to that snapshot.

### Corrections needed

1. **Reference 15 misidentifies the white paper (line 223; cited at line 31).** The actual official page is titled `民航局参加国新办《中国交通的可持续发展》白皮书新闻发布会`, not a press conference on a civil-aviation green-development policy/action white paper. The present title conflates the December 2020 transport white paper with the September 2022 aviation publication. Replace the reference title with an accurate translation, for example: *CAAC Participates in the State Council Information Office Press Conference on the White Paper “Sustainable Development of Transport in China”*; retaining the exact Chinese title in brackets would remove translation ambiguity. The existing date, URL and transport-intensity quotation are correct. Source: `scope_audit/raw/53d7e6bd0a7262a76c6618c045b0a998f367efabcdcbd02228599b640e86225b.html`, title and main paragraph beginning `《中国交通的可持续发展》白皮书中对绿色发展用了专门章节进行描述`.

2. **Abstract wording can imply all eleven annual pairs were checked against NBS (line 5).** The documented NBS numerical checks concern turnover in 2019, 2023 and 2024, not all eleven Q/I pairs and not the fuel-intensity series. Change to: “Eleven annual observations for 2015–2025 were assembled from CAAC publications; selected turnover observations were cross-checked against NBS yearbooks.” Section 2.1, line 29, otherwise states the scope and non-independence correctly. Evidence: `scope_audit/nbs_turnover_crosscheck.csv`.

3. **Make the remaining denominator ambiguity explicit in the methods (line 31; related limitation at line 185).** The existing continuity qualification is substantially accurate. However, the cited 2024 statistical system also defines general-aviation converted-tonne-km and combined average-converted-tonne-km intensities, alongside transport-only intensity. The current text mentions only the transport formula, making the reason for the inferential qualification less visible. Add a short sentence such as: “The survey system separately defines general-aviation and combined converted-tonne-kilometre measures; our transport-only interpretation relies on the official transport-aviation anchors and continuity of the annual indicator.” This does not require abandoning the documented scope decision or treating the derived product as unusable. It prevents readers mistaking a located formula for direct proof that each annual bulletin independently restated that same denominator. Source: 2024 statistical survey system, item 126, printed pp.80–81 / physical PDF pp.84–85; `scope_audit/scope_evidence.json`.

### Small editorial source clarification

At line 19, “replace untraceable capability indices” describes the revision process and can be read as an unreferenced criticism of prior research. Prefer “use publicly documented operational statistics to examine deployment requirements”. The underlying manuscript audit established insufficient traceability in the supplied materials, not that every capability index in the field is untraceable. This wording issue does not contaminate the empirical data or recreate the original unsupported questionnaire results.

Reference 16 (line 224) could also identify the year and distinguish the release page from the document: the linked page is `中国民航局发布《2022中国民航绿色发展政策与行动》`; the underlying official PDF is archived at `scope_audit/raw/24d537035bc4c214d1b0fab89e7b5298d462d180464316e294eebdb52a41f8be.pdf`. Calling the linked item an official policy release in line 31 would be maximally precise, although the release faithfully reproduces the relevant policy-document figures.

### Empirical values independently checked: no numerical corrections needed

All eleven original report files in `data_agent/verified_observation_ledger_2015_2025.json` were rehashed; each full SHA-256 matches the saved ledger. I independently extracted the cited physical PDF pages with `pdftotext` and confirmed the reported Q and I values for every year. The source ledger, `source/verified_data.csv` and `output/analysis/annual.csv` agree for all eleven pairs. Recomputed annual fuel values also agree with `annual.csv` using F = 0.1 QI in Mt. Table 1, lines 39–44, correctly rounds the selected annual observations and derived totals.

| Check | Independently recomputed value | Manuscript value | Finding |
|---|---:|---:|---|
| 2017–2025 turnover change | +51.49665768% | +51.5% | Correct |
| 2017–2025 intensity change | −11.26279863% | −11.3% | Correct |
| 2017 derived fuel | 31.734244 Mt | 31.734 Mt / 31.73 Mt | Correct |
| 2025 derived fuel | 42.661580 Mt | 42.662 Mt / 42.66 Mt | Correct |
| 2017–2025 derived fuel change | +34.43389419% | +34.4% | Correct |
| Endpoint reporting-precision bounds | +33.94576281% to +34.92369837% | +33.95% to +34.92% | Correct |
| 2019–2025 turnover change | +26.87647400% | +26.9% | Correct |
| 2019–2025 intensity change | −8.77192982% | −8.8% | Correct |
| 2019–2025 derived fuel change | +15.74695874% | +15.7% | Correct |
| 2017–2025 chain activity contribution | +15.14705980 Mt | +15.15 Mt | Correct |
| 2017–2025 chain intensity contribution | −4.21972380 Mt | −4.22 Mt | Correct |
| Sum / actual derived change | +10.92733600 Mt | +10.93 Mt | Correct |
| Intensity offset of positive activity contribution | 27.85836894% | 27.9% | Correct |

Table 3 also reproduces the independently recomputed chain-linked contributions:

| Period | Activity, Mt | Intensity, Mt | Net, Mt |
|---|---:|---:|---:|
| 2017–2019 | +6.05933777 | −0.93595677 | +5.12338100 |
| 2019–2022 | −20.84345433 | +2.08408533 | −18.75936900 |
| 2022–2025 | +29.93117636 | −5.36785236 | +24.56332400 |

The 15.4% and 17.9% period offsets at line 133 are correctly rounded from 15.4465% and 17.9340%. The 27.9% full-period offset is a ratio of summed chain contributions; it is correctly distinguished from direct endpoint decomposition, whose allocation differs.

### Boundary checks passed

- **No independent fuel-total claim:** lines 31, 46, 110, 116 and 185 consistently identify F as reconstructed. They do not treat QI identity closure as independent empirical validation.
- **Operator versus territorial scope:** lines 13, 29, 181 and 193 correctly refer to mainland China-registered carriers, include international services, exclude foreign carriers and distinguish national territorial inventory coverage.
- **NBS reuses CAAC-source data:** line 29 correctly limits the check to transcription and cross-publication consistency. None of the three NBS values conflicts with the respective CAAC rounded number; no averaging of different official versions was performed.
- **2017 change is appropriately handled:** line 27 accurately reflects the 2017 bulletin's statement: `2017年度行业综合统计系统正式上线后，由于航空公司生产数据处理流程和审核规则发生变化，2017年度相关数据和增速按照最新的口径进行计算。` The original is at physical PDF p.18, note [1]. The post-2017 principal analysis and the warning against assuming full-record harmonisation are appropriate. This does not establish that all possible later revisions have independently been ruled out, and the manuscript does not claim that.
- **Original questionnaire and capability results are not inherited:** lines 19, 68, 104, 171 and 187 use the original design–testing–manufacturing perspective only as conceptual motivation. The paper does not report the original 364-person questionnaire as a newly conducted survey, reuse its coefficients as causal estimates, or invent confidential engine-development observations.
- **Scenario inputs remain assumptions:** lines 64–94 and the relevant Results/Discussion paragraphs distinguish fuel-use-weighted adoption from aircraft replacement, baseline and incremental benefit, hypothetical ranges from observations, and scenario-design shares from real-world probabilities. No official-data provenance is falsely attached to the future parameter ranges.
- **No climate-neutrality overclaim:** lines 179–181 correctly distinguish fuel mass, lifecycle greenhouse gases, contrails, health effects and territorial-inventory coverage.

This audit checks empirical input traceability, principal accounting numbers and the stated research boundary. It does not independently verify every cited scholarly paper's substantive claim, validate all scenario code or establish readiness for journal acceptance; those are separate review tasks.


# 09 引用与期刊政策核对（修订前快照）

## Internal citation and publication-policy check

**Reviewed file:** `MANUSCRIPT.md`, snapshot read on 16 October 2026. This is an internal source-and-policy check, not external peer review or an acceptance assessment. The manuscript was not edited. Line locators below refer to this snapshot.

**Main finding:** The scientific literature citations map to real sources and mostly support the narrowly worded claims. The 2025–2026 citations do not import international results as Chinese estimated parameters. One official-source title is factually wrong and should be corrected: reference 15 describes a different white paper from the one at its URL. The manuscript remains a research draft with explicit human-author and submission declarations pending; it should not be labelled fully submission-ready.

### 1. Corrections and targeted improvements

#### Required: correct reference 15's document identity

- **Location:** reference 15; the associated source discussion is Section 2.1, line 31.
- **Current reference:** *Press Conference on China’s Civil Aviation Green Development Policy and Action White Paper*.
- **Actual official page title:** `民航局参加国新办 《中国交通的可持续发展》白皮书新闻发布会`.
- **Actual date:** 22 December 2020. The body says the State Council Information Office held a press conference about `《中国交通的可持续发展》`; CAAC Deputy Administrator Dong Zhiyi answered questions there. It is not a press conference on a civil-aviation green-development policy white paper.
- **The numerical support remains valid:** the page explicitly states `2019年，我国运输航空每吨公里油耗和碳排放分别为0.285千克和0.898千克`. Thus the 2019 transport-aviation intensity anchor in Section 2.1 is supported; only source identity/attribution needs correction.
- **Suggested accurate reference, explicitly a translation:**

  Civil Aviation Administration of China. *CAAC Participates in the State Council Information Office Press Conference on the White Paper “Sustainable Development of Transport in China”* [English translation of Chinese news-release title]; 22 December 2020 (in Chinese). https://www.caac.gov.cn/XWZX/MHYW/202012/t20201222_205702.html (accessed 16 October 2026).

- **Suggested body wording:** “An official CAAC report of the State Council Information Office press conference on the transport-sustainability white paper explicitly identifies the 2019 value …” This avoids calling it a CAAC white paper.
- **Saved evidence:** `/workspace/research/scope_audit/raw/53d7e6bd0a7262a76c6618c045b0a998f367efabcdcbd02228599b640e86225b.html`, together with `scope_evidence.json` and `SCOPE_FINDINGS.md` in that directory. The English wording above is identified as a translation, not asserted to be the official page's English title.

#### Recommended: identify reference 16 as the actual news release

Reference 16 is a real CAAC page, dated 23 September 2022, headed `中国民航局发布《2022中国民航绿色发展政策与行动》`. Its present English title omits “2022” and makes the news page look like the policy document itself. The source supports the shared 2019/2021 intensity-series statement. For precision use:

> Civil Aviation Administration of China. *CAAC Releases “2022 Policies and Actions for Green Development of China’s Civil Aviation”* [English translation of Chinese news-release title]; 23 September 2022 (in Chinese). https://www.caac.gov.cn/XWZX/MHYW/202209/t20220923_215418.html (accessed 16 October 2026).

Alternatively cite the attached policy PDF as a separate document after checking its title page and publication identity. Do not imply an official English title has been found when only the Chinese webpage has been checked.

#### Recommended: make reference 9's narrower role clearer

- **Location:** Section 4.1, line 165, “policy analyses question the adequacy of technology-centred growth strategies [7,9]”.
- **Assessment:** reference 7 directly critiques a technology-centred climate-neutral-growth narrative using EU/Finland policy documents. Reference 9 is an economic analysis of aviation policy instruments, international coordination and efficiency standards, including rebound/instrument interactions. It is not the same kind of narrative/content analysis and should not be read as independent evidence of the EU/Finland document finding.
- **Suggested narrow wording:** “Policy-document analysis questions technology-centred growth narratives [7], while economic analysis highlights interactions among efficiency standards, carbon pricing and demand responses [9].”
- Reference 9's use in Section 2.2 to contextualise rebound is reasonable, provided the manuscript continues to say its own decomposition does **not** estimate a causal rebound effect. No Chinese rebound elasticity should be inferred from Proost (2026).

#### Recommended: state who/what completed the checks without implying human-author verification

- **Location:** Section 2.6, line 104.
- **Current wording:** “source records and bibliographic metadata were checked against official documents and publisher records.”
- **Assessment:** the next sentences explicitly state that human-author verification remains pending, which preserves the draft boundary. Nevertheless, the passive completed-check wording could be read out of context as an author certification.
- **Suggested wording:** “The research-assistance workflow retrieved and compared source records and bibliographic metadata with official documents and publisher records, and generated the calculations through executed Python scripts. Independent verification and approval by the named human authors remain pending.”
- Only retain statements of completed retrieval, execution and comparison for which the package contains records. Do not replace the pending status with “the authors independently verified all sources” until real authors actually do so.

#### Recommended: bind the DAS to the actual delivered replication package

- **Location:** Data and Code Availability, line 197.
- **Assessment:** it correctly avoids claiming a public DOI, a GitHub release or public archiving. Supplementary files are an allowed route under the current policy. The present text says the materials are “supplied”; this must be true of the final delivery/submission rather than a future intention.
- **Action:** once the package is assembled, name its actual ZIP or supplementary-file identifier and its source ledgers. Example: “Data and code are available in the accompanying replication package, [actual filename], including [actual ledger filenames].” Do not add a public URL until public deposit has actually occurred.
- Do not use “No new data were created or analysed”: this study transcribes, transforms and analyses public observations and generates simulation outputs.

#### Recommended: pin reference 19 to the runtime's official documentation

The manuscript transparently distinguishes documentation 1.18.0 from analysis runtime 1.17.0; this is not a false statement. A version-matched official URL was also successfully retrieved during this review:

https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.stats.qmc.Sobol.html

It confirms `random_base2`, power-of-two balance, LMS+shift scrambling and `float64` behavior for 1.17.0. Replacing the unversioned reference-19 URL with this pinned URL removes the mismatch. Saved HTML/text: `/workspace/research/literature_agent/policy/scipy_qmc_1_17_0_sobol.html` and `.txt` (HTTP 200). Do not change the runtime version merely to match current documentation.

#### Access limitation to preserve: reference 17

Ang (2005) has verified Crossref and RePEc bibliographic identity, but no abstract or full text was obtained: Crossref has no abstract, RePEc explicitly has none, and ScienceDirect remained blocked. The manuscript's self-contained decomposition equations and numerical closure do not require claiming original-paper full-text appraisal. Keep this access limitation in the source-review ledger; authors should consult the original method before submission where possible. Do not add a quotation or a detailed property attributed to a supposedly read Ang full text. No fabricated method citation was found.

#### Pending author/provenance information should remain pending

The author-declaration and AI-acknowledgment sections correctly mark unresolved information. Actual authors must complete names, affiliations, corresponding author, contributions, funding and conflicts, and confirm the source thesis's authorship and prior-publication/submission status. If the supplied thesis is publicly available or needs an unpublished-work acknowledgment, give it an appropriate citation or provenance acknowledgment after confirming those facts. Do not invent a thesis repository, DOI, publication status, ethics approval, “no conflicts,” “no funding,” all-author approval, originality declaration or absence of simultaneous submission.

### 2. Numbered-citation and metadata audit

All numbers **1–20** appear in the body, each resolves to the intended reference, and no reference is orphaned. No range expands to a nonexistent entry. All scholarly DOI references correspond to the saved records. No paper's year or author identity is materially wrong.

First-use order is `1,2,3,4,5,6,7,8,12,13,15,16,14,17,9,19,18,20,10,11`, so the list is not currently ordered by first appearance. This is a presentation issue, not a semantic mapping failure. The user waived formatting; if preparing an actual MDPI submission, renumber citations and references together as a final mechanical step.

| Ref | Metadata identity / current claim support | Review result |
|---|---|---|
| 1 | Bergero et al.; 2023; *Nature Sustainability* 6, 404–414; DOI `10.1038/s41893-022-01046-9` | Official abstract read, metadata matched. Supports combining demand, efficiency, alternative fuels and removals in global pathways. Do not treat its global scenario shares as China data. |
| 2 | Dray et al.; 2022; *Nature Climate Change* 12, 956–962; DOI `10.1038/s41558-022-01485-4` | Official abstract read, metadata matched. Supports a contrasting pathway combining efficiency/fuels with continued demand growth; the manuscript acknowledges assumption-dependent conclusions. |
| 3 | Sacchi et al.; 2023; *Nature Communications* 14, 3989; DOI `10.1038/s41467-023-39749-y` | Abstract and selected open methods/results read. Supports lifecycle/resource and CO2/non-CO2 boundaries; manuscript does not import Europe-specific results as China estimates. |
| 4 | Xiao Liu and Yancai Zhang; 2023; *PLOS ONE* 18, e0282025; DOI `10.1371/journal.pone.0282025` | Official full-text scope confirms 1996–2015 and prior decomposition/decoupling. Correctly used as prior art. |
| 5 | Qiang Cui and Yi-lin Lei; 2023; *npj Climate Action* 2, 15; DOI `10.1038/s44168-023-00047-4` | Official abstract/methods support China–foreign-route mitigation and ETS/SAF complementarity. Correctly distinguished from the operator-based national boundary. “Y.L.” versus “Y.-L.” is only an initials-style choice. |
| 6 | Martulli, Brandt, Allroggen and Malina; 2025; *Nature Communications* 16, 11619; DOI `10.1038/s41467-025-66686-9` | Official 25 November 2025 paper is real; abstract and selected methods/results read. Distinguishes announced SAF capacity from realised capacity. Current text explicitly treats adoption analogy as conceptual and does not copy global realisation rates into China. Supports the sentences as written. |
| 7 | Emilia Suomalainen; 2025; *npj Climate Action* 4, 54; DOI `10.1038/s44168-025-00261-2` | Official 10 June 2025 paper, author and title verified. Directly supports EU/Finland policy narrative and Avoid–Shift–Improve discussion. It is document analysis, not a demand-effect estimate. |
| 8 | Igor Davydenko and Hans Hilbers; 2024; *Sustainability* 16, 950; DOI `10.3390/su16030950` | Official text supports interaction of technological/operational efficiency, fuel transition, prices and demand. Its presence in this journal is accurately stated; it does not imply this manuscript will be accepted. |
| 9 | Stef Proost; 2026; *Journal of Shipping and Trade* 11, 14; DOI `10.1186/s41072-026-00230-w` | Official 4 April 2026 paper, title and author verified. Instrument-interaction/rebound support is sound; narrow the shared “technology-centred growth strategies” sentence as recommended above. The 2026 annual issue metadata may display December while online publication was April; this does not invalidate the publication year. |
| 10 | Teoh, Engberg, Schumann, Voigt, Shapiro, Rohs and Stettler; 2024; *Atmospheric Chemistry and Physics* 24, 6071–6093; DOI `10.5194/acp-24-6071-2024` | Official abstract and selected full text support meteorological/flight heterogeneity and non-CO2 boundaries. Manuscript uses it appropriately without a universal fuel-to-climate multiplier. |
| 11 | Quadros, Nelen, Snellen and Dedoussi; 2026; *Communications Earth & Environment* 7, 806; DOI `10.1038/s43247-026-03732-4` | Official 16 June 2026 paper is real; abstract and selected methods read. Supports the statement that recent modelling evaluates growing aviation emissions' health impacts. No global mortality numbers are improperly assigned to China. |
| 12 | CAAC annual 2015–2025 bulletins; releases 2016–2026 | Real official source series recorded with eleven annual PDF URLs and page/hash evidence. English collective title is a translated description, not a single monograph. Retain exact per-year identifiers in the replication ledger; the landing-page URL alone is insufficient for reconstructing each observation. |
| 13 | NBS; *China Statistical Yearbook* 2020/2024/2025; tables 16-30/16-30/16-29 | Real official yearbooks and table images. Saved scope-audit cross-checks support the quoted 2019, 2023 and 2024 numbers. Correctly described as CAAC-derived cross-publication checks rather than independent physical measurement. Prefer exact table URLs in the ledger. |
| 14 | CAAC; `民航综合统计调查制度`; title page dated May 2024; official PDF | Corporate author/year and mathematical denominator claim are supported. English title is a reasonable translation; label translations consistently. Printed pp.80–81 correspond to physical PDF pp.84–85 for item 126. |
| 15 | CAAC news report of a State Council Information Office white-paper press conference; 22 December 2020 | URL and date real and numerical quote valid. **Current translated title identifies the wrong white paper; correct as above.** |
| 16 | CAAC news release `中国民航局发布《2022中国民航绿色发展政策与行动》`; 23 September 2022 | URL/date and intensity-series support valid. Add 2022 and distinguish the news page from the attached policy document; current English title is a paraphrase. |
| 17 | B. W. Ang; 2005; *Energy Policy* 33, 867–871; DOI `10.1016/j.enpol.2003.10.010` | Correct bibliographic identity. Original abstract/full text not read; retain access limitation. |
| 18 | Virtanen et al. and SciPy 1.0 Contributors; 2020; *Nature Methods* 17, 261–272; DOI `10.1038/s41592-019-0686-2` | Official abstract/full text retrieved; software citation correct. It does not document Sobol/QMC, and the manuscript correctly uses ref19 for that claim instead. |
| 19 | SciPy official `stats.qmc.Sobol` documentation | Real official page, current 1.18.0 page and pinned 1.17.0 page both readable. Power-of-two balance statement is supported. Runtime/documentation distinction currently explicit; pinning recommended. |
| 20 | Grewe et al.; 2021; *Nature Communications* 12, 3841; DOI `10.1038/s41467-021-24091-y` | Official abstract and selected scenario/methods text read. Supports COVID-recovery sensitivity and technology/climate-scenario framing. Manuscript does not cite it for current CORSIA policy. |

### 3. Journal substantive-content check

The authoritative policy snapshot is `/workspace/research/literature_agent/policy/sustainability_policy_verified_2026-10-16.md`, backed by official HTML and access logs. Scope includes sustainability measurement, air pollution and climate change; the study's explicit fuel/activity/deployment question has a defensible scope connection. No claim that complexity guarantees novelty or acceptance appears.

- **Research structure:** Introduction, reproducible methods, results, discussion, conclusions, figures/tables and reference list are present. Abstract is approximately **176 whitespace-delimited words**, within the retrieved “about 200 words maximum” guidance; six keywords meet the stated 3–10 range.
- **Scientific boundaries:** observed data, deterministic accounting, conditional scenarios and a limited forecasting diagnostic are separated. No fake forecast superiority, inferred engine-capability effect, causal rebound estimate, lifecycle accounting or climate-neutrality outcome is claimed. Literature supports the modest motivation rather than replacing empirical evidence.
- **Reproducibility:** software versions, seeds, parameter ranges, conversion equations and scenario target are described. Public sources and derived inputs are distinguished. A final delivered package must actually contain the promised files, and authors must check the calculations and figures.
- **Data/code statement:** present and does not falsely claim public deposit. Concrete package identifiers remain desirable, and publication-time availability must match the actual deposit/supplement route. A DOI is not invented or required to exist at drafting time.
- **AI disclosure:** substantive assistance is disclosed in Methods and Acknowledgments, matching the policy's placement and submission-declaration direction. Actual product/version details and human responsibility certification still require real authors. Current pending-language is appropriate for a draft.
- **Authorship/funding/conflicts/provenance:** deliberately unresolved, not falsely negative. These are required submission-completion items and cannot be supplied by inference. A cover letter, originality/all-author approval and no-concurrent-submission assurances must likewise wait for author confirmation.
- **Editorial boundary:** this check does not establish “meets acceptance requirements,” novelty by editorial standards or a probability of acceptance. Scientific soundness and substantial new information remain editorial/reviewer judgments.

### 4. Evidence used and actions intentionally not taken

The review compared the manuscript with the saved Crossref/publisher records, `verified_references.json`, `claim_evidence_mapping.md`, official source/scope ledgers, and retrieved MDPI/SciPy documents. It did not change the manuscript, upload it to an external service, publish the code, contact a journal, submit the work, certify human authorship, or simulate an editor's decision. Scientific result replication and figure QA are outside this citation-policy review and should rely on the separate executed-analysis checks.


# 10 Sustainability官方政策核验

## Sustainability / MDPI 官方政策核验

实际访问：2026-10-16 04:31:55–04:32:00 UTC（北京时间 12:31:55–12:32:00）。本报告只陈述该次访问可读内容，不推断网页发布日期或后续变更。

### 访问及证据状态

| 来源 | 实际结果 | 已保存证据 |
|---|---|---|
| https://www.mdpi.com/journal/sustainability/about | HTTP 200 | sustainability_aims.html / .txt |
| https://www.mdpi.com/journal/sustainability/instructions | HTTP 200 | sustainability_instructions.html / .txt |
| https://www.mdpi.com/ethics | HTTP 200 | mdpi_ethics.html / .txt |
| https://www.mdpi.com/ethics#_bookmark21 | HTTP 200（同一 ethics 页面；不据此认定该 fragment 对应数据章节） | mdpi_data.html / .txt |
| https://www.mdpi.com/editorial_process | HTTP 200 | mdpi_editorial.html / .txt |

本轮没有 403。此前记录中的 403 是历史环境观察，不能再用来表示本轮政策无法核验。访问元数据见 access_log.json；原始文件 SHA-256 见 source_checksums.json。

### 经核验的要求与准确解释

#### 1. 选题范围与研究价值

来源：Aims & Scope，https://www.mdpi.com/journal/sustainability/about （本地文本第 149–190 行）。

短摘录："Air pollution and climate change"；"Measuring and monitoring sustainability"；"full experimental and methodological details so that results can be reproduced and assessed"。

解释：能源、排放、需求变化、技术采用与政策情景等议题可与期刊环境和经济可持续性范围建立直接联系。可计算、可复现、与可持续发展问题直接相关，是可论证的匹配依据。官方范围并未要求方法越复杂越好，也不把模型复杂度等同于创新。

#### 2. Article 的科学性、创新和文献

来源：Instructions for Authors，https://www.mdpi.com/journal/sustainability/instructions#submission （本地文本第 1139–1141 行）。

短摘录："scientifically sound experiments"；"a substantial amount of new information"；"the most recent and relevant references"。

解释：本任务适合 original research Article。必须提供真实资料和可检查结果；最新且相关的文献应由实际检索与核验支持。不能以未验证引文、编造数据、未经执行的复杂模型代替研究结果。会计分解、预测和情景仿真应各自表述，不可在没有识别设计时写成因果估计。

#### 3. 用户不要求格式时仍需保留内容要素

来源：Instructions，https://www.mdpi.com/journal/sustainability/instructions#freeformatsub （本地文本第 1152–1156、1180–1183、1221–1224 行）。

短摘录："Sustainability now accepts free format submission"；"about 200 words maximum"。

解释：初投允许自由格式、文献格式一致即可；这不豁免作者信息、摘要、关键词、Introduction、Methods、Results、Conclusions、图表说明、经费、作者贡献、利益冲突等内容。研究文章类型说明另列 Discussion，宜保留。摘要约 200 词以内，单段，依次给问题、方法、主要结果和结论；关键词 3–10 个。可不在本任务花时间套版，但实证论文的内容要素需要完整。

#### 4. 可复现方法、数据和代码

来源：Instructions，https://www.mdpi.com/journal/sustainability/instructions#manuscript 、#data 、#computer （本地文本第 1228、1245–1246、1294–1340 行）；Research Data Policies，https://www.mdpi.com/ethics （“MDPI Research Data Policies”章节）。

短摘录："Data Availability Statement (DAS)"（该节的强制声明要求）；"include all the parameters used"；"authors should release the code"。

解释：DAS 对本类研究是强制项；应说明支持结果的数据实际在哪里取得、哪些是公开资源，以及分析产生的数据可在哪里取得。MDPI 鼓励 FAIR 数据和可信仓库。新开发的代码应通过公开仓库（官方举例 GitHub）或补充材料释放，并说明软件版本、全部分析参数。公开统计资料的原始数据来源、下载日期、单位、口径、计算式、处理后表格、随机种子和情景参数应进入可复现材料。不得先写“已在 GitHub/Zenodo 公开”而实际尚未公开；本地交付不等于公共存档。对公共数据进行重新整理和分析的本研究不适合声称“No new data were created or analyzed”。

#### 5. AI 使用披露

来源：MDPI Publication Ethics，https://www.mdpi.com/ethics （Artificial Intelligence → Manuscript preparation）；期刊 Instructions 第 1228 行。

短摘录："authors are required to declare this during the submission process"；"disclose details ... in the Materials and Methods section"；"product details in the Acknowledgments section"。

解释：仅语法、拼写、标点或格式等表层编辑可免披露。本任务涉及研究设计、检索辅助、分析代码、结果解释和实质写作，因此不属于豁免，应在投稿过程申报，在 Methods 交代用途，并在 Acknowledgments 给出实际产品/版本信息。AI 不能署名作者；人类作者对原创性、有效性、完整性负责，并需核对输出和每一条引文。工具名称、版本不可猜写。

建议披露草案（只在作者核对实际用途后采用）：

Methods: “Generative AI assistance was used for research planning, literature-search formulation, development and checking of analysis code, and manuscript drafting. All source records, analytical inputs and outputs, and cited references were checked against the underlying sources and reproducible analysis files by the authors.”

Acknowledgments: “During the preparation of this manuscript, the authors used [actual product name and version] for [verified description of use]. The authors have reviewed and edited the output and take full responsibility for the content of this publication.”

最后两句对“作者已检查/承担责任”的陈述须由真实作者在提交前亲自完成和确认；不能把本草案视为检查已经发生的证据。

#### 6. 其他投稿和录用边界

来源：Instructions #coverletter；https://www.mdpi.com/editorial_process （本地文本第 100–106、124–130 行）。

短摘录："fits the journal’s scope and meets the expected standards of scientific soundness"；"At least two review reports"；"made exclusively by the assigned Academic Editor"。

解释：初筛看范围和科学可靠性；通过后仍须同行评议和学术编辑决定。Cover letter 必须解释意义和范围适配，作者批准、原创/非一稿多投等声明只能在作者确认后成立。满足可核验的投稿要求不等于达到可保证的录用标准；不应承诺录用。无需未经用户授权实际投稿、发邮件或公开发布。

### 对主稿的具体落实清单

- 把目标写成可检验的可持续性问题，并给出具有现实解释的增量发现。
- 用可追溯官方数据完成真实分析；明确描述年度、地区/行业边界、单位、口径和缺失值。
- 分离观察结果、分解结果与前瞻情景假设；报告敏感性和模型适用边界。
- 通过真实执行产出结果、图表和代码；只在实施完成时使用“we estimated / simulated”。
- 保留 DAS、软件/参数、GenAI 实质用途和产品详情披露草案；留空真实作者/基金/冲突信息供作者确认。
- 准备可公开的数据和代码包，但公共发布及投稿由用户另行执行或明确授权。


# 11 已核验参考文献目录

## Verified reference list

Verified against Crossref and official publisher pages on 16 October 2026. Eleven items are from 2023–2026 and two are older foundational comparisons. Access levels and boundaries appear in the evidence map. This is a targeted search, not a systematic review.

1. Bergero, C.; Gosnell, G.; Gielen, D.; Kang, S.; Bazilian, M.; Davis, S. J. (2023). Pathways to net-zero emissions from aviation. Nature Sustainability, 6(4), 404–414. https://doi.org/10.1038/s41893-022-01046-9

2. Sacchi, R.; Becattini, V.; Gabrielli, P.; Cox, B.; Dirnaichner, A.; Bauer, C.; Mazzotti, M. (2023). How to make climate-neutral aviation fly. Nature Communications, 14(1), 3989. https://doi.org/10.1038/s41467-023-39749-y

3. Martulli, A.; Brandt, K.; Allroggen, F.; Malina, R. (2025). The potential scale-up of sustainable aviation fuels production capacity to meet global and EU policy targets. Nature Communications, 16(1), 11619. https://doi.org/10.1038/s41467-025-66686-9

4. Teoh, R.; Engberg, Z.; Schumann, U.; Voigt, C.; Shapiro, M.; Rohs, S.; Stettler, M. E. J. (2024). Global aviation contrail climate effects from 2019 to 2021. Atmospheric Chemistry and Physics, 24(10), 6071–6093. https://doi.org/10.5194/acp-24-6071-2024

5. Cui, Q.; Lei, Y. L. (2023). Pathways analysis to reducing aircraft emissions for China-Foreign routes. npj Climate Action, 2(1), 15. https://doi.org/10.1038/s44168-023-00047-4

6. Liu, X.; Zhang, Y. (2023). What drives the decoupling progress of China’s civil aviation transportation growth from carbon emissions? A new decomposition analysis. PLOS ONE, 18(3), e0282025. https://doi.org/10.1371/journal.pone.0282025

7. Suomalainen, E. (2025). Growth over climate or aviation climate policy in the Avoid–Shift–Improve framework. npj Climate Action, 4(1), 54. https://doi.org/10.1038/s44168-025-00261-2

8. Davydenko, I.; Hilbers, H. (2024). Decarbonization Paths for the Dutch Aviation Sector. Sustainability, 16(3), 950. https://doi.org/10.3390/su16030950

9. Proost, S. (2026). What role for aviation in climate policy? Journal of Shipping and Trade, 11(1), 14. https://doi.org/10.1186/s41072-026-00230-w

10. Quadros, F. D. A.; Nelen, R.; Snellen, M.; Dedoussi, I. C. (2026). Global air quality and human health impacts of growing aircraft emissions. Communications Earth & Environment, 7(1), 806. https://doi.org/10.1038/s43247-026-03732-4

11. Gössling, S.; Humpe, A.; Leitão, J. C. (2024). Private aviation is making a growing contribution to climate change. Communications Earth & Environment, 5(1), 666. https://doi.org/10.1038/s43247-024-01775-z

12. Dray, L.; Schäfer, A. W.; Grobler, C.; Falter, C.; Allroggen, F.; Stettler, M. E. J.; Barrett, S. R. H. (2022). Cost and emissions pathways towards net-zero climate impacts in aviation. Nature Climate Change, 12(10), 956–962. https://doi.org/10.1038/s41558-022-01485-4

13. Grewe, V.; Gangoli Rao, A.; Grönstedt, T.; Xisto, C.; Linke, F.; Melkert, J.; Middel, J.; Ohlenforst, B.; Blakey, S.; Christie, S.; Matthes, S.; Dahlmann, K. (2021). Evaluating the climate impact of aviation emission scenarios towards the Paris agreement including COVID-19 effects. Nature Communications, 12(1), 3841. https://doi.org/10.1038/s41467-021-24091-y


# 12 论断与文献证据映射

## Claim–evidence map

Each item has a saved Crossref record and official publisher page. “Full text retrieved” is distinguished from actual reading; reading was selective, not an exhaustive appraisal. Exact evidence snippets are short; see the raw files for surrounding context.

| Ref | Source / role | Reading level | Support | Limits |
|---|---|---|---|---|
| 1 | Bergero et al. (2023); Core | Abstract read; publisher full text paywalled. | Global pathways combine demand, efficiency, fuel substitution and removals; their relative potential depends on assumptions. | Do not transfer global scenario percentages to China or describe them as observed effects. |
| 2 | Sacchi et al. (2023); Core | Abstract and selected open full-text introduction/methods/results paragraphs read. | European aviation LCA highlights resource constraints and different CO2/non-CO2 neutrality definitions. | European modeling, not a Chinese empirical estimate; its large non-CO2 share is scenario/scope specific. |
| 3 | Martulli et al. (2025); Core | Abstract and selected open full-text introduction/methods/results paragraphs read. | SAF project announcements need deployment-realization and delay analysis; stochastic diffusion is an evidenced modeling approach. | Production capacity is not actual fuel output or uptake. Global/EU realization rates are not estimated China parameters. |
| 4 | Teoh et al. (2024); Core | Abstract and selected open full-text methods/discussion paragraphs read. | Non-CO2 aviation impacts are spatially heterogeneous and sensitive to meteorology and engine particle emissions. | Do not use global/region RF numbers as CO2 inventory multipliers or infer Chinese operational CO2 from them. |
| 5 | Cui et al. (2023); Core | Abstract and selected open full-text methods paragraphs read. | China-foreign-route scenario evidence models complementary fuel and market instruments. | Routes and modeled atmospheric impacts differ from the national CAAC operator-based fuel/turnover boundary. |
| 6 | Liu et al. (2023); Essential prior art | Abstract and open full-text data scope/conclusions read. | China aviation decoupling and decomposition already studied using 1996–2015 commercial passenger/freight data. | Updating years alone is not sufficient novelty; do not claim the first China decoupling/decomposition study or equate accounting with causality. |
| 7 | Suomalainen et al. (2025); Core | Abstract and selected open full-text framework/methods paragraphs read. | Avoid–Shift–Improve content analysis questions technology-centered climate-neutral-growth narratives. | Qualitative document analysis of EU/Finland; it is not a Chinese causal demand estimate. |
| 8 | Davydenko et al. (2024); Journal-specific comparator | Abstract and selected open full-text methods/conclusions read. | Sustainability has published aviation scenarios combining fuel transition, operational efficiency, ticket prices and demand elasticity. | Dutch assumptions and elasticity values are not automatically valid in China; policy-neutrality wording in that paper does not remove LCA requirements. |
| 9 | Proost et al. (2026); Recent economic context | Abstract and selected open full-text conclusions read. | Economic analysis shows instrument interactions and potential rebound effects should be considered when interpreting fuel-efficiency policy. | A theoretical/economic policy analysis; it does not identify an aggregate Chinese rebound elasticity. |
| 10 | Quadros et al. (2026); Recent boundary context | Abstract and selected open full-text scenarios/atmospheric-model methods read. | Aviation sustainability includes air-quality/health impacts beyond a CO2-only inventory. | Do not sum PM2.5- and ozone-attributable deaths without considering overlap; do not label its global modeled impacts Chinese observed outcomes. |
| 11 | Gössling et al. (2024); Optional demand/distribution context | Official publisher abstract read; open full text retrieved. | Private aviation has distinct growth and distribution patterns, reinforcing the need for explicit aviation coverage. | Private aviation is outside a commercial transport-operator study unless explicitly included. Prefer omit if word-limited. |
| 12 | Dray et al. (2022); Older foundational counterpoint | Official publisher abstract read; full text paywalled. | Under its modeled pathways, large lifecycle CO2 reductions can coexist with demand growth, but residual non-CO2 impacts remain. | Use alongside Sacchi rather than implying consensus that demand reduction is always mathematically necessary; assumptions differ. |
| 13 | Grewe et al. (2021); Older foundational context | Abstract and selected open full-text scenario/methods paragraphs read. | Bottom-up technology/SAF and COVID-recovery scenarios distinguish emissions targets from temperature outcomes. | Older scenario assumptions/CORSIA descriptions should not be cited as current policy. Use only for method/climate-boundary context. |

### Short evidence excerpts

1. [Pathways to net-zero emissions from aviation](https://doi.org/10.1038/s41893-022-01046-9): “ambitious reductions in demand for air transport and improvements in the energy efficiency of aircraft”

2. [How to make climate-neutral aviation fly](https://doi.org/10.1038/s41467-023-39749-y): “with a continuous increase in air traffic, synthetic jet fuel produced with electricity from renewables would exert excessive pressure”

3. [The potential scale-up of sustainable aviation fuels production capacity to meet global and EU policy targets](https://doi.org/10.1038/s41467-025-66686-9): “only 24% (26% in the EU) of the announced capacity was realized on time by 2024”

4. [Global aviation contrail climate effects from 2019 to 2021](https://doi.org/10.5194/acp-24-6071-2024): “only 2 % of all flights caused 80 % of the annual contrail energy forcing”

5. [Pathways analysis to reducing aircraft emissions for China-Foreign routes](https://doi.org/10.1038/s44168-023-00047-4): “the best way is to combine SAFs and ETS”

6. [What drives the decoupling progress of China’s civil aviation transportation growth from carbon emissions? A new decomposition analysis](https://doi.org/10.1371/journal.pone.0282025): “the relationship between carbon emissions and transport turnover is dominated by the expansive coupling”

7. [Growth over climate or aviation climate policy in the Avoid–Shift–Improve framework](https://doi.org/10.1038/s44168-025-00261-2): “the current focus on (future) technological solutions”

8. [Decarbonization Paths for the Dutch Aviation Sector](https://doi.org/10.3390/su16030950): “the growth rate will be significantly lower than before 2019”

9. [What role for aviation in climate policy?](https://doi.org/10.1186/s41072-026-00230-w): “efficiency measures are expensive and are to some extent compensated by lower carbon taxes and by the rebound effect”

10. [Global air quality and human health impacts of growing aircraft emissions](https://doi.org/10.1038/s43247-026-03732-4): “use an atmospheric chemistry transport model to estimate their air quality and human health impacts”

11. [Private aviation is making a growing contribution to climate change](https://doi.org/10.1038/s43247-024-01775-z): “Emissions increased by 46% between 2019-2023”

12. [Cost and emissions pathways towards net-zero climate impacts in aviation](https://doi.org/10.1038/s41558-022-01485-4): “our pathways reduce aviation CO2-equivalent emissions by only 46–69%”

13. [Evaluating the climate impact of aviation emission scenarios towards the Paris agreement including COVID-19 effects](https://doi.org/10.1038/s41467-021-24091-y): “a bottom-up analysis of potential technical improvements”


### Contribution positioning

Prior China-specific work already decomposes the relationship between aviation growth and carbon emissions (Liu and Zhang, 2023, studying 1996–2015), and route-based work evaluates fuel/market-policy combinations (Cui and Lei, 2023, with 2014–2021 emissions). A credible new contribution must specify what a newer observed period, revised accounting boundary, threshold analysis or deployment-lag simulation adds. Do not claim that decomposition or Chinese aviation decoupling is itself new. Global pathway studies emphasize interacting demand, efficiency and fuel levers, with differing conclusions under different assumptions (Bergero et al., 2023; Dray et al., 2022; Sacchi et al., 2023). The recent SAF realization-gap evidence (Martulli et al., 2025) supports explicit treatment of deployment delay and uncertainty, without supplying China-specific causal parameters.

### Excluded metadata-only recent candidates

Crossref confirms the existence of Bardon et al. (2025), DOI 10.1016/j.jenvman.2024.123943; Jiang et al. (2024), DOI 10.1016/j.trd.2024.104055; and Abulibdeh (2026), DOI 10.1016/j.jclepro.2026.149589. ScienceDirect/Elsevier API remained blocked and no authoritative abstract was read. Their findings are not used as support. PubMed query redirects led to challenge pages, not readable abstracts.


# 13 方法与软件文献核验

## Method and software source verification

Retrieved 16 October 2026 (Asia/Shanghai). These are additional methods sources, separate from the 13 aviation-content references.

### Ang (2005): bibliography verified, full text and abstract not read

**Reference:** Ang, B. W. (2005). The LMDI approach to decomposition analysis: a practical guide. *Energy Policy*, **33**(7), 867–871. https://doi.org/10.1016/j.enpol.2003.10.010

- Crossref DOI record retrieved successfully and saved as `raw/ang2005_crossref.json`; title, author, publication year, volume, issue and pages match the candidate supplied by the parent.
- Publisher page `https://www.sciencedirect.com/science/article/pii/S0301421503003136` returned proxy 403. Its `/abs/` equivalent also returned 403.
- RePEc bibliographic page `https://ideas.repec.org/a/eee/enepol/v33y2005i7p867-871.html` was successfully read and independently confirms these bibliographic details. It explicitly reports: “No abstract is available for this item.” Original page and text are saved as `raw/ang2005_repec.html` and `.txt`.
- **Access boundary:** this is a verified bibliographic method reference, not an original-paper content appraisal. Do not attribute detailed properties, robustness claims or a quotation to a full text that was not read. The manuscript's stated decomposition equations and zero-residual numerical checks should be self-contained and independently verified. The author may consult the full original paper before submission.

### Virtanen et al. (2020): official abstract and open full text available

**Reference:** Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J., et al.; SciPy 1.0 Contributors (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nature Methods*, **17**(3), 261–272. https://doi.org/10.1038/s41592-019-0686-2

- Crossref record and official Nature Methods article successfully retrieved; full author metadata are retained in `raw/scipy2020_crossref.json`.
- Official source: https://www.nature.com/articles/s41592-019-0686-2
- Original page and extracted text: `raw/scipy2020_publisher.html` and `.txt`.
- The official abstract identifies SciPy as an open-source Python scientific-computing library and describes an overview of its capabilities and development practices. This supports the software citation.
- **Boundary:** this 2020 paper does not discuss `stats.qmc` or Sobol sampling in its visible text. It should not be used as evidence for current Sobol API defaults or balance properties; use current official API documentation for those details and report the version actually run.

### Current Sobol API

See `policy/scipy_qmc_verified_2026-10-16.md` (verification complete) and its saved official documentation. Use the actual analyzed SciPy version and actual constructor arguments, sample count, scrambling flag and random generator/seed in the manuscript and code. A quasi-Monte Carlo share across chosen parameter bounds is not an observed probability or a data-estimated probability distribution.

The official documentation retrieved is labeled SciPy 1.18.0. It states that `random_base2(m)` generates 2^m points with balance properties; skipping the first point, thinning, or using arbitrary non-power-of-two sample counts loses these properties. `scramble=True` applies LMS followed by digital random shift. `bits` defaults to 30 when `None` and is limited to 64; it controls sequence length 2^B, while output dtype is `numpy.float64`. Sobol sequence sampling does not itself constitute Sobol sensitivity analysis.


# 14 Sobol官方文档核验

## SciPy Sobol randomized quasi–Monte Carlo 方法核验

### 官方证据与访问状态

- URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.Sobol.html
- 实际访问：2026-10-16 04:36:37 UTC（北京时间 12:36:37），HTTP 200。
- 页面自身的 `docsearch:version` 与版本切换元数据均为 **SciPy 1.18.0**。这只标识所访问文档，不能用来代替实际分析环境所安装的 SciPy 版本。
- 保存：`scipy_qmc_sobol.html`（原始 HTML）；`scipy_qmc_sobol.txt`（解析文本）；`scipy_qmc_access_log.json`（URL、访问时间、HTTP 状态、字节数、SHA-256）。

### 精确短摘录与解释

| 要点 | 官方短摘录 | 正确解释 |
|---|---|---|
| 序列与点数 | “Sobol’ sequences are low-discrepancy, quasi-random numbers.” | Sobol 是低差异积分/设计点序列，不是独立同分布的普通伪随机观测样本。 |
| `random_base2` | “guarantees the balance properties of the sequence.” | `random_base2(m)` 用于生成 n = 2^m 个点。应从新引擎生成完整的 2^m 点设计，保留全部点，避免把任意长度采样描述为同样具有平衡保证。 |
| `scramble` | “If True, use LMS+shift scrambling.” | 默认 `scramble=True`；实现为 left linear matrix scramble 加 digital random shift。固定并记录随机种子/生成器状态能复现同一随机化设计。 |
| 失去平衡的情形 | “a sample size that is not a power of 2, or skips the first point, or thins the sequence” | 不能随意删除第一个点、抽稀或取非 2 的幂次的样本数后仍宣称保留官方 Sobol 平衡属性。扩大设计时应采用更大的 2^M；不是在原样本后任意补点。 |
| 独立随机化重复 | “the number R of independent replicates does not have to be a power of 2.” | 每个重复设计内保持 n = 2^m；可用多个独立 scramble 的重复比较结果，考察数值误差与收敛。重复次数 R 不要求是 2 的幂。 |
| `bits` | “Control the maximum number of points ... 2**bits. Maximal value is 64.” | `bits` 控制生成器周期上限；默认 `None` 对应 30，即最多 2^30 个点。显式最大值为 64。耗尽 2^B 点后本应重复，因此实现抛出错误。 |
| 返回精度 | “return type, which is always np.float64” | `bits` 不等于输出数据类型或任意精度。返回是 float64；IEEE 754 双精度通常有 53 位二进制有效精度。增大 `bits` 不能解释成提高结果的浮点数值精度。 |
| 事后优化 | “does not guarantee that all properties of the sample will be conserved.” | 若目标是保留标准 Sobol 设计性质，使用 `optimization=None`；不能做事后优化后无条件声称所有原有属性仍成立。 |

以上摘录对应本地文本第 59–103、116–137 行。摘录中的省略号只省略无关连接文字；完整原句以原 HTML/解析文本为准。

### 论文表述边界

建议称 **randomized quasi–Monte Carlo (RQMC) scenario sampling using scrambled Sobol sequences**。由 n = 2^m 个设计点经参数映射得到的情景集合，可以衡量在给定参数范围、变换与依赖设定下，哪些组合达到目标。若参数只定义为探索范围，满足某条件的点比例应称 **scenario share** / **fraction of evaluated scenarios**，不能写成观察到的事件频率、预测事件发生概率或经经验校准的风险概率。

即使采用了均匀、三角等参数分布，此比例也仅对应所选分布下的模型条件结果；分布不由实证识别时，不得将其解释为实际世界发生概率。Sobol 的 scramble 不会自动给输入假设赋予经验概率意义。独立 scramble 重复之间的差异反映数值积分/采样误差，也不包含结构性模型误差、数据偏差或输入分布不确定性。

建议 Methods 文案（按实际执行修改）：

“Parameter scenarios were generated using randomized quasi–Monte Carlo sampling with scrambled Sobol sequences implemented in SciPy [actual installed version]. Each design contained n = 2^m points generated with `random_base2(m)`, with `scramble=True`, `optimization=None`, and a recorded random-generator seed. Scenario coordinates were mapped to the prespecified parameter ranges [and transformations]. Reported attainment shares describe the fraction of evaluated scenarios satisfying the criterion under this sampling design; they are not empirically calibrated probabilities.”

应在补充材料记录实际 m、维度 d、bits、种子/生成器、重复次数、边界、参数映射、相关性假设、SciPy/NumPy版本。只有真的执行独立 scramble 重复或收敛检验时，才能声称进行了相应误差检查。该采样器自身也不构成 Sobol sensitivity-index analysis；若未计算相应敏感度估计量，不应把场景采样写成 Sobol 全局敏感性分析。


# 15 官方数据获取与口径记录

## Official aviation data acquisition status

Status at 2026-10-16 UTC: **Official sources retrieved successfully. Core observed Q/I series: 2015–2025 (11 years).**

### What was verified

- Sixteen original CAAC annual Civil Aviation Industry Development Statistical Bulletin PDFs, covering 2010–2025, were downloaded from `www.caac.gov.cn`. Raw files, full SHA-256 digests, retrieval timestamps, exact excerpts and physical PDF page locators are archived.
- Total transport turnover is available for 2010–2025. The annual bulletin does not report a verifiable annual fuel-intensity value for 2010–2014; these cells remain missing and are excluded from the common sample. The 11-year intensity series is 0.294, 0.293, 0.293, 0.287, 0.285, 0.316, 0.309, 0.302, 0.292, 0.271 and 0.260 kg/tkm (2015–2025).
- NBS China Statistical Yearbook 2025 Table 16-29 was downloaded as the official JPG and visually checked. Its total-turnover values for 2010, 2020, 2022, 2023 and 2024 agree with CAAC annual-bulletin values within the bulletin's 0.01 hundred-million tonne-km rounding precision. See `nbs_crosscheck.csv`.
- All sixteen archived CAAC bulletin PDF SHA-256 digests were rechecked against the ledger. The canonical 11-row empirical input is `/workspace/research/source/verified_data.csv`; `verified_observation_ledger_2015_2025.json` preserves original evidence.

### Statistical population decision

Q is transport turnover of mainland-registered commercial air carriers on domestic (including Hong Kong/Macao/Taiwan routes) and international services, not airport throughput and not the statistics of Hong Kong/Macao/Taiwan-registered carriers.

I is interpreted as transport-aviation fuel per transport tonne-km using official anchors and continuity of the identically named, common-2005-baseline annual series. The independent source reviewer supported this bounded interpretation. It is **not** a claim that each annual bulletin repeats the denominator definition or that carrier microdata were matched year by year.

The supporting anchors are the CAAC 2020 press conference explicitly identifying 2019 **transport aviation** intensity as 0.285 kg/tkm, the 2022 policy/action page linking transport-fleet 2019 0.285 with 2021 0.309 in the same discussion, and the 2024 official survey system's item 126 transport-fuel/transport-turnover formula. See `scope_alignment_decision.json` and `/workspace/research/scope_audit/` for the independent audit.

- https://www.caac.gov.cn/XWZX/MHYW/202012/t20201222_205702.html
- https://www.caac.gov.cn/XWZX/MHYW/202209/t20220923_215418.html
- https://www.caac.gov.cn/XXGK/XXGK/TJSJ/202406/P020240604342006406114.pdf (physical p.84 = printed p.80, item 126; also physical p.33 = printed p.29, fuel survey table)

The 2024 system separately defines general-aviation and combined converted-turnover formulas. Those definitions are not silently substituted for transport turnover. Canonical rows mark `scope_match=true` only with the documented official-anchor-plus-series-continuity interpretation retained in every `coverage_definition` cell.

### Material limitations

- Q×I is a **reconstructed/implied fuel-use estimate**, not an independently observed or externally validated official fuel total. No independent aggregate fuel total was retrieved for cross-validation.
- I is rounded to three decimals; rounding intervals should be propagated. The fuel conversion is fuel in 10,000 tonnes = turnover in 100 million tonne-km × intensity in kg/tkm × 10.
- The 2017 bulletin explicitly reports changed production-data processing and audit rules after the comprehensive statistical system launched. Report this break and show sensitivity beginning in 2017.
- 2020–2022 are a structural disruption in demand, utilisation, load factors and traffic composition. They are not evidence that engine technology deteriorated.
- No observation identifies an indigenous-engine effect, engine manufacturing capability, non-CO2 aviation climate effects, or life-cycle emissions. Any engine R&D link must remain a conditional engineering interpretation.
- The official 2024 survey resource table uses 3.15 tCO2/t for aviation kerosene and 3.16 for other kerosene. A CO2 conversion must document its chosen factor and boundary. The main fuel accounting does not require an emissions factor.
- Do not smooth missing pre-2015 intensity or back-solve individual years from a five-year mean or a rounded percentage reduction.

### Reproduction files

- `collect_official_sources.py`: standard-library official source archival and excerpt extraction; `pdftotext -layout` for PDFs. Default discovery now follows the actual CAAC annual-report archive at `index_1214.html` and historical page `index_1214_1.html`.
- `raw/`, `extracted_text/`, `fetch_log.jsonl`, `excerpts.csv`: original files and candidate text extraction.
- `early_years/`: independent 2010–2017 retrieval, missingness decisions and supplementary official planning evidence.
- `official_aviation_2010_2025.csv`: raw observation ledger; missing early I values remain blank.
- `verified_observation_ledger_2015_2025.json`: source-excerpt audit for every core observation.
- `nbs_crosscheck.csv`: visually verified NBS yearbook values and rounding differences.
- `scope_alignment_decision.json`: statistical-population judgment and limitations.
- `validation_report.json`: successful source-hash and input verification report.

### Historical network issue (resolved)

Initial requests to CAAC/NBS failed with proxy CONNECT 403; the root agent saved a network-settings draft. After the user said to continue and network settings changed to unrestricted, official requests succeeded. No TLS verification was disabled. `network_attempts.json` records the earlier failure only; it is not the current readiness state. GitHub was used as a discovery fallback during the outage; no GitHub numerical observation entered the official dataset. A 2022 policy/action PDF exceeded the acquisition script's 25 MiB cap, so its successfully archived official HTML was used; no complete PDF download is claimed for that attachment.

### Analytical design suitable for this sample

With 11 common-sample national annual observations (2015–2025), a high-dimensional neural network, causal forest, or structural causal model cannot be justified simply because it is complex. A transparent accounting decomposition plus uncertainty-aware, constrained scenario model is defensible and reproducible.

Let Q denote transport turnover in tonne-kilometres; I fuel intensity in kg fuel/tkm; F fuel in kg; e the kg CO2/kg fuel factor; and C direct CO2 in kg. Then F = QI and C = QIe.

Exact additive LMDI between valid endpoints a and b uses L(Cb,Ca) = (Cb−Ca)/(ln Cb−ln Ca), with the equal-value continuous limit L(C,C)=C. Contributions are ΔC_Q=L ln(Qb/Qa), ΔC_I=L ln(Ib/Ia), and ΔC_e=L ln(eb/ea). With a fixed emission factor, ΔC_e=0. Report the exact closure residual and avoid causal language.

For a target terminal emissions ratio R=C_T/C_0, activity growth g, annual fuel-intensity reduction r and n years, the identity implies C_T/C_0=[(1+g)(1−r)]^n when e is fixed. The minimum annual intensity reduction is r_min=1−R^(1/n)/(1+g). This is an engineering requirement conditional on assumed demand, not a forecast of engine performance.

A cohort renewal extension can model fleet entry age, retirement survival, new-aircraft intensity advantage and operational utilisation, using explicit scenario parameters where data are unavailable. Label assumed distributions separately from official observations, solve a constrained replacement/allocation problem, and report Monte Carlo intervals as **scenario uncertainty**, not empirical confidence intervals. Test demand growth, survival lifetime, utilisation, improvement saturation and SAF life-cycle factors individually. SAF does not reduce tank-to-wake CO2 to zero and must be analysed with a separate life-cycle boundary.

Empirical validation should include exact identity closure, source rounding tolerance, same-definition turnover comparisons, sensitivity to 2019 versus latest-year baselines, and parameter stress tests. A paper can claim descriptive trends and conditional transition requirements; it cannot claim an identified causal effect of domestic engine R&D from these aggregates.


# 16 离线复现说明

## Replication materials

The accompanying English manuscript analyses official Chinese commercial-air-transport activity and fuel intensity, then evaluates explicitly assumed deployment scenarios. It does not estimate domestic engine capabilities or causal policy effects.

### Contents and provenance

- `source/verified_data.csv`: eleven paired annual CAAC observations, 2015–2025, with source URLs, full hashes, page locators and coverage explanations. Main comparison: 2017–2025 because of the documented 2017 processing change.
- `data_agent/verified_observation_ledger_2015_2025.json`: source quotations, publication/PDF locators and hash metadata. Original PDFs are retrieved from the listed official URLs; the public documents are not reproduced in this compact package.
- `data_agent/nbs_crosscheck.csv` and `scope_audit/nbs_turnover_crosscheck.csv`: selected cross-publication checks. NBS republishes CAAC-origin statistics; this is not independent physical measurement.
- `scope_audit/scope_evidence.json`: transport-intensity mapping evidence and residual statistical-scope limitations.
- `scenario_config.json`: explicit analyst-defined stress domain, not fitted Chinese parameter distributions or official forecasts.
- `analyze_official_data.py`, `run_accounting.py`, `models/transition_models.py`: accounting, LMDI, limited Bayesian diagnostics and deployment scenarios.
- `output/analysis/`, `output/transition/`: executed machine-readable results.
- `figure_work/build_figures.py`, `output/figures/`: figure code, editable exports, source CSVs and rendered QA reports. Bundled QA helpers come from the invoked Nature Skills figure workflow; they inspect geometry rather than establish scientific validity.
- `output/MANUSCRIPT.md`, `output/SUPPLEMENTARY_INFORMATION.md`: manuscript and supplementary text.
- `literature_agent/`: verified reference metadata, citation–evidence map, reading coverage and journal-policy audit. Full publisher articles are not bundled.

### Offline reproduction

Use Python 3.12.14 with the exact package versions in `requirements_research.txt`. A fresh virtual environment can be created outside any existing project and populated with `python -m pip install -r requirements_research.txt`. Installation requires access to the normal package registry; reproducing the analysis with installed dependencies requires no network.

From the extracted package root:

```bash
python reproduce.py
```

The command checks frozen input hashes, runs seven accounting arithmetic checks and eleven model/boundary checks, reproduces the accounting and conditional scenarios, writes the limited forecast diagnostics and rebuilds supplementary tables and figures. Logs preserve command outputs and failure status. The model checks use explicitly synthetic examples, not empirical observations.

The reproduction command also runs `figure_work/audit_figures.py` on the regenerated exports. Equivalent QA commands are recorded in `output/figures/QA_notes.md`. Source/geometry audits do not verify empirical authenticity or manuscript conclusions. Manuscript DOCX conversion used Pandoc; the supplied Word files already contain the three figures and editable equations.

### Statistical and interpretive boundary

Q is operator-based turnover of mainland China-registered carriers, including international services; it is not airport throughput or a territorial inventory. I is interpreted as transport-aviation intensity based on official same-value anchors and statistical continuity, not year-by-year enterprise matching. F = 0.1 Q I in Mt is reconstructed from rounded official inputs, not independently observed total fuel. The main data begin in 2017; earlier observations remain visible but are not treated as harmonised across the processing change.

The Bayesian benchmark has only two eligible tests in the extended series and none in the principal post-2017 period. It does not calibrate the scenario domain or establish model superiority. QMC design shares are not probabilities. Additional efficiency is relative to an improving baseline; adoption is fuel-use-weighted, not the fraction of aircraft replaced. No lifecycle, contrail, health, domestic-engine causal or comprehensive climate-neutrality result is claimed.

### Public release and author review

This is a local delivery package, not a GitHub release, Zenodo deposit or journal submission. The human authors must verify their authorship, declarations, evidence and interpretation and provide an archival location or attach the package as supplementary material before submission. The official policy audit is a source-based checklist, not an acceptance guarantee.


# 17 图表质量检查记录

## Figure QA record

All figures were drawn and exported with Python/matplotlib. Width: 183 mm.
PDF and SVG contain editable text; PNG previews are 300 dpi. Figure-specific
JSON sidecars retain glyph audit, collision verdict, source-data SHA-256 and
image dimensions. The retained plotting source is reproducible after running
the accounting workflow. No graphical content was generated by an image model.

### Evidence and data handling

Figure 1 includes all 11 annual observations, 2015–2025, without dropping or
interpolating a year. It shows all three requested series. Only an explicitly
labelled index normalization (2015 = 100) is applied. Reconstructed fuel is
distinct from the two official inputs. The official 2017 reporting-programme
change is marked without claiming a detected physical discontinuity.

Figure 2 displays all three requested primary phases after the reporting
change. Other computed periods are retained by the accounting workflow, not
represented as additional independent observations. No missing values were
removed. Chain contributions were independently recomputed from annual Q and
I in Mt: reconstructed fuel = Q × I / 10, where Q is in 100 million tonne-km
and I in kg per tonne-km. This agrees with the accounting output's conversion
from 10,000-tonne units by division by 100. The 2025 reconstructed quantity is
42.66158 Mt.

| Phase | Activity effect (Mt) | Intensity effect (Mt) | Net change (Mt) |
|---|---:|---:|---:|
| 2017–2019 | 6.0593377721 | −0.9359567721 | 5.123381 |
| 2019–2022 | −20.8434543315 | 2.0840853315 | −18.759369 |
| 2022–2025 | 29.9311763624 | −5.3678523624 | 24.563324 |

Figure 3 uses exact analytic model functions and explicit illustrative inputs.
There are 161 activity-growth grid points for each of three baseline-improvement
curves and 101 deployment-delay points. A grid point is a deterministic design
point, not an observed replicate. No claim of calibration, sampling uncertainty,
frequency probability or official forecasting is made. Ordinary annual growth
and improvement are converted as g = log(1 + a) and b = −log(1 − e). The deployment
rate is a conversion parameter for remaining fuel-use-weighted adoption
potential, not an annual aircraft-count replacement rate.

### Statistical and panel audit

| Figure/panel | Unique evidence role | Summary and uncertainty | Unit | Labels and layout | QA |
|---|---|---|---|---|---|
| 1 | Historical divergence of activity and intensity and their product | All annual official inputs and deterministic reconstructed indices; no inferred interval | Calendar year | Three series differentiated by colour, markers and line style; pandemic shade and reporting change disclosed | Visually inspected; one-panel alignment not applicable; collisions PASS |
| 2 | Separate activity and intensity accounting contributions | Exact chain sum from rounded annual inputs; no statistical CI | Phase composed of consecutive annual changes | Grouped bars and distinct net diamond; zero baseline visible | Visually inspected; one-panel alignment not applicable; collisions PASS |
| 3a | Full-adoption technical feasibility boundary | Exact conditional curve; grey band is assumed range, not uncertainty | Deterministic scenario point | All three baseline rates identified; normalizations and rates stated | Visually inspected; alignment PASS; collisions PASS |
| 3b | Delay-dependent deployment-rate requirement | Exact conditional threshold with fixed case; no statistical interval | Deterministic scenario point | Hypothetical ceiling differentiated by line style and legend | Visually inspected; alignment PASS; collisions PASS |

There are no independent experimental replicates, hypothesis tests,
multiple-comparison corrections, p-values, train/test splits or fitted
uncertainty bands in these figures. The absence of such elements reflects the
deterministic accounting and conditional-analytic design. Their uncertainty
must be discussed as data-definition, rounding and model-assumption limits.

### Automated and visual checks

Source validator: 18 PASS, 3 WARN, 0 FAIL. Reviewed warnings are resolved as
follows: the requested raster deliverable is PNG at 300 dpi, while PDF/SVG are
the vector masters, so TIFF and a 600 dpi raster are unnecessary for this
delivery; the static source parser cannot identify the dynamic width constant,
but exported PDF width is 518.74015748 pt (183 mm).

All three final PDFs pass the glyph-size check with a minimum of 7 pt against
a 5 pt requirement, and every final collision audit reports 0 FAIL and 0 WARN.
Early footer collisions were corrected through layout spacing, followed by
fresh exports and repeat audits. Figure 3's final render-time alignment JSON
passes the 1.5 pt tolerance with zero failures, warnings or exemptions. Both
panels have identical plot-area heights, widths and top/bottom edges, with
aligned panel-label anchors.

Each final PNG was inspected through the image viewer, including each Figure 3
panel and the assembled figure. Text is legible, source notes are separated from
axis labels, no data are clipped, and line styles/markers permit interpretation
without colour alone. The shaded bands are distinct from the series and are
described in captions. Collision overlays and alignment SVG are diagnostic QA
files, not submission figures.

### Reproduction

After generating the frozen annual and period accounting CSVs, run:

```bash
python figure_work/build_figures.py
python figure_work/audit_figures.py
```

The plotting script records the render-time alignment result before Figure 3
export. The audit script preserves current source, PDF text and collision
reports. Every later visual change requires another export and QA run.


# 18 当前研究状态

## 当前研究状态：英文研究稿与复现材料已完成

此前官方站点被网络白名单拦截的限制已经解除，不能再将旧的403记录作为当前阻碍。

已完成：2015—2025年11组官方数据采集与核验、2017—2025年主分析、链式LMDI与舍入检验、部署可行前沿、Sobol条件情景、小样本贝叶斯诊断、三张图、英文全文和补充材料。数据的官方口径与残余限制已写入正文。

主要结果：2017—2025年周转量增长51.5%，强度下降11.3%，重构燃油需求增长34.4%；强度贡献抵消活动贡献的27.9%。未来情景是假设条件下的可行性计算，不是官方预测或因果估计。

当前成稿：MANUSCRIPT_EN.docx；补充材料：SUPPLEMENTARY_INFORMATION.docx；详细中文说明：AUTHOR_NOTES_ZH.md。完整数据和代码随REPLICATION_PACKAGE.zip交付。

实际作者仍须完成作者信息、贡献、经费、利益冲突、原论文关系及最终独立审阅，并确认人工智能披露。尚未公开发布代码、登记DOI或投稿；不保证期刊录用。

审查文件记录的是早一快照的问题；最终修订及对应处理见FINAL_VERIFICATION.md。原始附件保持不变。


# 19 归档：分析前英文研究方案

> Archived pre-analysis protocol. Network access was restored and the analyses were subsequently completed. The final research draft is `MANUSCRIPT.md` / `MANUSCRIPT_EN.docx`; its scope and executed methods supersede this prospective document. Statements below describing pending work refer to the earlier preparation stage.

## Can Efficiency Gains Offset Growth in China’s Civil Aviation?

### An official-data decomposition and deployment-constrained scenario analysis

**Status: prospective research protocol; not a completed empirical manuscript. No official annual observations or new empirical results have yet been verified.**

#### Research question and contribution to be tested

The study will examine whether improvements in the fuel intensity of Chinese civil air transport have been sufficient to offset changes in transport activity. A second question concerns the intensity improvements required under alternative, explicitly assumed activity and deployment trajectories. The contribution to be evaluated is an auditable link between historical accounting, growth-compatible efficiency thresholds, and conditional deployment scenarios. Novelty relative to recent studies remains to be established through source-verified literature searches.

The supplied Chinese manuscript motivates the importance of coordination among aero-engine design, testing and manufacturing. That framework will inform the discussion of deployment constraints. Aggregate air-transport statistics do not measure domestic aero-engine development capability. The proposed study therefore will not estimate the causal effect of domestic engine development, industrial reorganisation, certification policy or organisational coordination.

#### Evidence and statistical boundary

The primary sources will be annual statistical bulletins published by the Civil Aviation Administration of China, supplemented where appropriate by National Bureau of Statistics publications. The intended period begins in 2010 and ends with the latest complete, compatible and verifiable year. This is a target window, not a claim of data availability. Every included observation will retain the original document, official URL, observation year, publication year, table or page locator, unit, coverage definition and source-file SHA-256 digest.

The minimum paired inputs are total transport turnover, Q, in units of 100 million tonne-kilometres, and fuel intensity, I, in kilograms per tonne-kilometre. They may be multiplied only after confirming that their statistical populations and geographical and operational boundaries match. Passenger-kilometres cannot substitute for total tonne-kilometres. An intensity indicator for transport airlines cannot automatically be combined with activity covering all civil aviation. Definitions or conversions used by the statistical authority will be documented rather than inferred.

Where compatible fuel use is independently reported, it will be used as an external accounting check. A fuel series reconstructed from turnover and intensity is mathematically derived from those inputs and is not an independent validation dataset. Missing years will remain missing unless an explicitly justified sensitivity analysis is undertaken. No missing observation will be represented as an official reported value.

#### Accounting and exact decomposition

With the units above, reconstructed fuel use F in units of 10,000 tonnes satisfies:

**F(t) = 10 × Q(t) × I(t).**

For two positive observations, define the logarithmic mean L(a,b) = (a−b)/(ln(a)−ln(b)), with L(a,a)=a. The change in fuel use can then be written exactly as:

**ΔF(activity) = L(F(1),F(0)) × ln[Q(1)/Q(0)]**

**ΔF(intensity) = L(F(1),F(0)) × ln[I(1)/I(0)].**

The two components sum to observed or consistently reconstructed fuel change, subject to numerical rounding. The analysis will report both effects in physical fuel units and verify the identity for every interval. The published source for the decomposition method will be checked before manuscript citation.

This decomposition is descriptive. An intensity component can reflect fleet composition, load factors, route structure, operational practices and technology, among other influences. It cannot be labelled an engine innovation effect without additional identification. Similarly, a temporary fall in activity during a disruption is not evidence of a durable technological transition.

#### Growth-compatible improvement thresholds

If activity grows by g and intensity declines by e over the same interval, the fuel-use ratio is (1+g)(1−e). Fuel use does not increase when:

**e ≥ 1 − 1/(1+g), for g > −1.**

For a cumulative activity ratio A and a specified fuel-use target ratio R, the required terminal intensity ratio is at most R/A. These are accounting conditions, not fitted policy effects. When g is negative, the threshold may also be negative; it should not be misreported as a required positive efficiency improvement. Historical activity and fuel changes will be shown alongside any decoupling classification, since a ratio alone can be unstable near zero activity growth or misleading during contraction.

#### Dynamic modelling and validation rule

The final forecasting or filtering model will be selected only after the length, gaps and coverage of the verified series are known. Candidate models may include a constant-intensity baseline, an exponential trend and a parsimonious local-level or local-linear-trend state-space model. Pandemic-related disruptions will be explicitly examined. A separate free parameter for every event or transition is inappropriate when the annual sample is short.

Any fitted dynamic model will be compared with simple baselines using forward-chaining historical evaluation. Training observations will precede validation observations. Parameter tuning, transformations and break selection will use the training window only. Forecast errors, number of evaluation origins and uncertainty coverage will be disclosed. If there are too few usable origins or unstable estimates, the model will be omitted from inferential claims, and transparent accounting and conditional scenarios will carry the analysis.

The study will not use a complex machine-learning model merely to create an appearance of novelty. It will not treat simulated paths as additional empirical observations or describe in-sample fit as independent predictive validation.

#### Deployment-constrained scenarios

Scenarios will distinguish activity growth, realised efficiency improvement and the timing of technology adoption. A deployment delay can shift the date at which an improvement begins; an adoption constraint can limit its rate of diffusion. Such parameters require independent evidence if presented as calibrated estimates. Otherwise they will be openly labelled analyst-defined assumptions and explored over a stated range.

The scenario analysis will evaluate fuel outcomes and threshold violations under combinations of these inputs. Monte Carlo sampling may propagate specified parameter uncertainty, but the distributions and dependence assumptions will be reported. Scenario probabilities will not be described as real-world probabilities unless their calibration can be defended. Robust comparisons will ask which conclusions survive the full stated range of plausible assumptions, rather than select a favourable single trajectory.

No national causal effect of design–testing–manufacturing coordination will be inferred from these scenarios. The relationship to the original manuscript will remain a mechanism-based interpretation and a source of deployment hypotheses.

#### Sensitivity and limitations

The analysis will examine pre-pandemic and pandemic/recovery intervals separately while retaining the full observed record. Other checks will concern endpoints, alternative compatible official revisions, rounding, assumed activity growth, intensity trajectories, deployment lags and dependence between uncertain inputs. Annual official aggregates may not support attribution among aircraft technology, engine technology, airline operations and network composition.

Fuel use, combustion CO2, lifecycle greenhouse gases and non-CO2 climate effects are different quantities. The primary analysis can remain in fuel units. Any conversion to combustion CO2 requires a verified emission factor, consistent coverage and a documented calculation. That conversion does not estimate lifecycle emissions or total aviation warming, and a change in fuel mix requires a separate treatment.

#### Planned manuscript evidence chain

The eventual article will open with the specific sustainability question established by the verified literature. The data and methods section will define the official statistical boundary and accounting identities. Results will proceed from historical activity and intensity changes to the decomposition, improvement thresholds, model validation where justified and conditional scenarios. Discussion will relate these findings to deployment constraints and to the supplied manuscript's coordination framework without elevating that framework into an empirically identified mechanism.

The abstract, final title and conclusions will be written after the results. Data and code availability, source limitations and the actual role of AI assistance will be stated accurately. Authorship, affiliations, funding and applicable declarations require author-supplied facts; none will be invented. Current Sustainability policies and recent references remain unverified until external access is restored.

#### Evidence status

The original Word manuscript has been preserved and audited. The accounting implementation has passed seven deliberately synthetic arithmetic checks. Those checks establish a limited numerical property of the implementation; they establish neither the authenticity of future input data nor the empirical validity of the proposed study. Official data retrieval, current literature verification, empirical estimation, scenario calibration and English manuscript drafting remain pending.


# 20 归档：方法设计方案

> 历史研究方案：此文件写于正式数据取得前。后续官方数据、实证和英文研究稿已完成；以 output/MANUSCRIPT.md 及实际代码/结果为准。以下“尚未取得数据/尚未实现”等状态属于准备阶段记录。脚本弹性定义后已统一为对数弹性。

## 可执行方法设计：航空运输增长、燃油效率与技术部署约束

**状态（2026-10-16）**：本文件是研究设计，不包含实证结果。当前尚无完成官方来源核验的真实数据，任何估计值、样本期间、显著性或情景输出都必须等数据取得后再写。下面的数值（如模型先验和仿真样本量）是预先声明的分析设置，并非观测事实。

### 1. 建议收窄的研究问题与贡献

建议英文题目：**When Efficiency Cannot Outrun Growth: Fuel-Use Decomposition and Deployment-Constrained Sustainability Pathways for Chinese Civil Aviation**。

可以回答的问题：
1. 在口径一致的官方年度资料中，运输活动扩张和单位周转量油耗变化分别贡献了多少燃油用量变化？这种关系在疫情前、疫情期和恢复期有何差异？
2. 仅根据历史燃油强度形成的简约预测，在逐年留后检验中是否优于强度不变和无收缩漂移基线？
3. 在明确声明的活动增长、基础强度趋势、技术实际收益、投用延迟和部署速度范围内，哪些组合能够满足燃油总量约束？其必要条件与最不利条件是什么？

原稿的“设计—试验—制造协同”用于解释研发收益转化为服役效率时存在的准备期、认证/验证和规模部署约束。不能把航空运输总量或宏观燃油强度称为航空发动机研制能力的直接测量，也不能用本文核算识别国产发动机、研制协同或特定政策的实际效果。若没有可复核的企业/机队微观数据，应撤去原稿能力综合指数、问卷结构方程和三系统耦合估计中的经验结论。

可辩护的潜在贡献是：将**可审计的官方活动—效率核算、经外推检验的简约动态基准、具有解析可行边界的部署约束情景**结合起来；把“技术效率改善”与“行业总量下降”之间的缺口转化为清晰的速度和时滞条件。该组合是否具有文献新意必须待最新文献检索后判断，不宜声称使用了从未有人提出的模型。

### 2. 最低数据要求与严格口径检查

优先来源：中国民用航空局（CAAC）年度《民航行业发展统计公报》及环境/绿色发展相关官方统计；统计年鉴可用于核对周转量、单位和修订，不应把不同覆盖范围数据直接拼接。国家统计局数据可用于交叉核对行业活动，不能用全社会航空煤油消费替代同范围运输航空油耗。

| 字段 | 最低要求 | 核验要点 |
|---|---|---|
| `year` | 连续年份，理想至少 15 年；实际范围待核验 | 不预先虚构起止年；最新公报年份以已发布且可核验为准 |
| `transport_turnover` | 年度运输总周转量，优先原表单位“亿吨公里” | 国内/国际、地区航线、境内航空公司/境内机场覆盖必须与油耗强度一致；不能混用机场吞吐量 |
| `fuel_intensity` | 运输航空吨公里油耗，保留原始单位和小数位 | 是否为 kg/(tonne·km)、是否为换算周转量、是否对货邮/客运采用同一换算标准；若定义不一致则暂停乘积推算 |
| `reported_fuel` | 如官方提供，同范围年度燃油总量 | 优先使用直接值，并以乘积值核验；如无直接值，清楚标成“由官方活动量和四舍五入强度推算” |
| `scope_note` | 原文统计范围及定义 | 对口径变更逐年标记，不能直接插值跨越 |
| `source_url`, `document_title`, `publication_date`, `page_or_table`, `retrieval_date`, `local_file`, `sha256` | 每项观测可追溯 | 原始 PDF/HTML 和提取表均保存；数据值对应到具体页/表 |
| `revision_status`, `original_unit`, `rounding_resolution` | 每字段记录 | 同一资料后续修订采用一致规则；保存原始值与标准化值 |

如还要把燃油换算成直接燃烧 CO2：需取得并核验适用航空煤油的官方燃烧排放因子及单位，说明只是直接燃烧 CO2，不是生命周期温室气体、净零指标或航空非 CO2 气候效应。未核验时，燃油用量足以作为主结果；排放因子不能凭记忆填入。

**单位恒等式**：若 Q 的原单位为亿吨公里，I 为 kg/(tonne·km)，则推算燃油吨数 `F_t = Q_t * I_t * 10^5`，以“万吨”为单位则为 `F_t(万吨) = 10 * Q_t * I_t`。实施时首先转换为标准单位，再计算。不要把“亿”理解成百万。

**不兼容即停止对应分析**：如果两个指标未通过范围一致性检查，仍可分别描述，但不能推出燃油、分解燃油或制造碳排放结果。如果只能获得少数年份，仅做端点核算和透明情景，取消时间序列预测。

### 3. 模块 A：精确 LMDI 核算与增长—效率脱钩

设标准化周转量为 Q_t，燃油强度为 I_t，燃油为 F_t = Q_t I_t。所有变量必须严格为正。

对任意两个年份 a、b，定义对数平均：

    L(x,y) = (x-y)/(ln x-ln y),   x != y;
    L(x,x) = x.

活动与强度贡献分别为：

    D_Q(a,b) = L(F_b,F_a) ln(Q_b/Q_a)
    D_I(a,b) = L(F_b,F_a) ln(I_b/I_a)
    F_b - F_a = D_Q(a,b) + D_I(a,b).

这是**核算恒等式**，不需要回归，不产生因果识别。恒定排放因子 K 下，直接燃烧 CO2 的两项贡献直接乘 K；如果燃料构成导致 K 变化，就要有可核验 K_t 并增加独立因子，不能暗中设为常数。

**报告方案**：以逐年链式分解为主，全年贡献相加仍与起终点燃油差完全一致；预先定义的阶段报告链式贡献之和。端点直接分解只用于敏感性对照，两种分解可能分配不同的阶段贡献，不能混淆。以绝对燃油吨数为主，避免净变化接近零时“贡献率”爆炸。

**脱钩度量**：使用年度增长率 `g_Q = Q_t/Q_(t-1)-1`、`g_F = F_t/F_(t-1)-1`；当活动增长时，`g_F<0` 表示绝对脱钩，`0<=g_F<g_Q` 表示相对脱钩，`g_F>=g_Q` 表示燃油增长不慢于活动增长。活动下降年份另设“收缩”类，不把疫情下降称作技术驱动的可持续转型。若报告弹性，明确采用 `epsilon = Δln F / Δln Q`，而非同时混用百分比弹性；当 |Δln Q| 极小时不报告弹性，直接报告增长率。

`D_Q/(-D_I)` 仅在 `D_Q>0, D_I<0` 时可作为“增长抵消强度改善的核算比率”。不要称为需求反弹效应或 Jevons 效应，因为没有识别效率改善对出行需求的因果影响。

**四舍五入敏感性**：若强度原文保留 p 位小数，以原值 ± 0.5×10^(-p) 为可取区间，其他原表数据同理；在端点区间内计算 F、D_Q、D_I 的包络或透明独立均匀舍入扰动。后者只是舍入误差敏感性，不是统计置信区间，不反映系统测量误差。除四舍五入精度外，不凭空设定“官方数据±5%误差”。

### 4. 模块 B：小样本动态预测与诚实基线

#### 4.1 预测定位

预测只为约束基础效率趋势和量化短期外推局限服务，不承担创新性主张。年度序列通常不足以可靠估计深度学习、GNN、多层 DML、复杂 VAR 或带大量解释变量的因果模型。不得以同一样本上的高拟合度证明先进性。

使用 `z_t = ln I_t`，每次训练仅使用当时已观测数据。主模型为**贝叶斯收缩漂移随机游走**：

    d_t = z_t-z_(t-1) ~ N(mu, sigma^2)
    mu | sigma^2 ~ N(mu0, sigma^2/kappa0)
    sigma^2 ~ InvGamma(alpha0,beta0).

这只是少参数的动态概率基准，并非发动机性能或技术学习机制模型。可预先设置 `mu0=0, kappa0=1, alpha0=2, beta0=0.05^2`（先验年度对数变动的尺度是研究者选择；0.05 非数据事实），并把尺度改为 0.02 和 0.10 作为必要敏感性分析。所有先验和候选模型必须在查看样本外得分前固定。

对 n 个有效年度差分：

    kappan = kappa0+n
    mun = (kappa0*mu0+n*dbar)/kappan
    alphan = alpha0+n/2
    betan = beta0 + 0.5*sum((d-dbar)^2)
            + kappa0*n/(2*kappan)*(dbar-mu0)^2.

h 步预测的 `z_(T+h)` 为自由度 `2*alphan` 的 Student-t，位置 `z_T+h*mun`，尺度平方 `betan/alphan * (h+h^2/kappan)`。按预测抽样在原始强度尺度报告中位数和区间；不能把 `exp(E[z])` 称作强度均值。若正态年度差分明显不合适，优先承认区间不足与报告敏感性，不在小样本上迭代搜索复杂模型。

#### 4.2 必须比较的基线与检验

- B0：强度维持最新观测值（随机游走无漂移）。
- B1：随机游走加无收缩历史平均漂移，同样训练年份。
- B2：上述收缩漂移主模型。

滚动起点逐年向前，以至少 8 个有效连续年度差分作为最小训练要求，主检验 h=1；若产生至少 5 个可评价起点再报告 h=3，否则只说明样本不足。不得把同一序列随机打乱做交叉验证；不得用全样本估计漂移后倒回生成“样本外预测”。

主点预测误差报告 MAE（原始 I 单位）与 MASE（各训练集的一步朴素误差为分母）；概率预测报告 80% 和 95% 区间覆盖率及平均宽度，样本足够才报告区间得分。每个得分均报告测试年份和数量。小样本不做声称有充分功效的模型优越性检验；如主模型没有稳定优于基线，保留无漂移情景，不掩盖失败结果。

#### 4.3 疫情与结构变化

以预先声明的日历分组展示疫情前、2020—2022 年冲击期、2023 年以后恢复期。这个分组是描述用的外部事件划分，不是估计出的最优断点。

主预测评估保留所有可评价年份，并另列冲击期和其余年份得分，以显示外推失败。一个敏感性版本在估计长期漂移时删除任何端点属于 2020—2022 的年度差分；绝不把 2019 和 2023 之间的跨年差额当作一个年度差分。删除后的训练/测试规则必须逐起点执行；疫情期样本外预测仍需如实记录。不能用已知未来恢复值修正过去预测。

最新水平 I_T 是情景起点，历史漂移只用于形成可解释的基础趋势范围。若漂移结论对疫情处理、先验或样本窗口不稳健，主情景用保守区间，不能称某一技术改善率已得到稳健估计。

### 5. 模块 C：部署约束仿真与解析可行边界

#### 5.1 最小机制模型

设 h 为距最后观测年份的年数，g 为年度活动对数增长率，b 为**不包含新增技术方案**的基础强度下降对数率。θ 为新增技术在实际运行中相对该基础路径的燃油强度优势（包括实现损失后的收益，0<=θ<1）；r 为每年尚未采用部分的**燃油使用权重部署率**，0<=r<=1；tau 为首次额外部署前的等待年数。所有参数来源必须区分“历史估计”“经核验文献范围”和“分析者压力测试范围”。

新技术燃油权重采用率：

    s_h = 1-(1-r)^max(h-tau,0),   s_0=0.

燃油路径：

    Q_h = Q_T exp(g*h)
    I_base,h = I_T exp(-b*h)
    I_h = I_base,h (1-theta*s_h)
    F_h = Q_h I_h
    R_h = F_h/F_T = exp((g-b)*h) (1-theta*s_h).

r 不是直接可观测的飞机架数替换比例，不同机型飞行量/燃油用量不同；没有机队年龄、飞行利用率和配置数据就不能把它写成中国机队实际更新率。θ 不代表国产/某型号发动机本体台架效率。若分别引入工程效率优势与实现系数，它们仅以乘积进入该式，在宏观数据下不可分别识别，因此主模型只用一个实际收益 θ。

原稿设计—试验—制造体系可以解释 tau 和 r 受到研发准备、认证、生产爬坡及机队吸收的约束。这是机制解释，**不能从 Q、I 反推出三种能力、三系统参数或时滞真实分布**。若没有可靠外部证据，tau 与 r 必须标为假设变量。

#### 5.2 解析可行前沿

给定终点燃油目标 `F_H/F_T <= kappa`，需要：

    s_req = [1-kappa*exp(-(g-b)*H)]/theta.

- 若分子<=0，基础路径已满足目标；新增方案不是满足该目标的必要条件。
- 若 theta=0 且基础路径未达标，无额外收益可使目标达标。
- 若 `s_req>1`，即使全部部署也不足，技术收益与活动需求设定不相容。
- 若 `0<s_req<=1` 且 H>tau，所需部署率为

      r_req = 1-(1-s_req)^[1/(H-tau)].

- 若 H<=tau 且基础路径未达标，部署尚未开始，目标不可达。

即使没有新增技术，也有直观的一年必要条件：若活动普通增长率为 `a`、强度普通下降率为 `e`，燃油不增需 `e >= a/(1+a)`；使用对数率时是 `b>=g`。不要把普通百分比率与连续对数率混用。

这些前沿比“复杂模型给出一个预测数字”更有价值：让可行性由显式条件决定，并允许读者替换假设。

#### 5.3 不确定性和全局敏感性

**把统计预测与深度不确定性分开**。B 模块的概率区间来自明确随机过程；C 模块尚无可识别参数分布时采用探索性情景设计，不把区间或达标组合占比称为客观达标概率。

1. 预先建立参数范围表：g、b、θ、r 和 tau 的下限/上限、依据、单位、适用地域、证据质量。文献技术潜力不能未经解释直接充当中国机队已实现收益；没有可核验范围的参数可以用清楚标记的政策压力测试范围，但不能称为经验估计。
2. 对 tau 取少数预设离散情景，对连续的 g、b、θ、r 使用 scrambled Sobol 低差异序列。初始用 `2^12` 个组合/时滞，种子固定，再以 `2^14` 核查结果数值稳定性。Sobol 序列是覆盖参数空间的方法，不能让未经证据支持的参数变成“真实分布”。
3. 输出终点 `R_H`、累计燃油 `sum(F_h)`、是否满足目标、以及达到目标的 r/θ/tau 前沿；报告最不利角点和目标能否在整个预设参数集合内满足。蒙特卡洛分位数标成“情景设计空间分位数”。
4. 如报告 Sobol 一阶/总效应指数，必须明确假设参数在预设区间内独立、采用指定设计权重，使用 A/B 与逐列替换矩阵估计，并做多次 scrambling 数值稳定性分析；这些是**对假设空间的输出敏感度**，不是对现实机制的重要性排名。g 与 b 的关联若有可靠依据，应另设联合情景；不能把相关输入直接套进独立 Sobol 解释。
5. 因模型多数方向单调，优先用解析前沿和边界检验检验数值仿真；无需把全局敏感性作为额外“先进算法”堆叠。主文可用前沿图，详细敏感性置补充材料。

条件情景不能证明新技术引发需求反弹、政策增加研发能力、协同提升效率或某条路线会在某年实现。没有财务成本和约束数据，就不做最优投资分配或福利最优宣称。

### 6. 最低有效性检查（应写入实际脚本）

- 逐条观测检查来源、年份唯一性、正值、单位及范围一致性；不自动填补缺失。
- 如可取得同口径直接燃油值，比较乘积值与直接值，解释可由原表精度产生的差异；不强制调数配平。
- 每段 LMDI 检查 `D_Q+D_I == F_b-F_a`，使用与量纲相称的浮点容差；年链式贡献之和与总变化相等。
- 舍入包络不跨越零；接近相同燃油值时使用稳定 log-mean 实现（`log1p`/`expm1`），不得用任意 epsilon 改写观测。
- 预测检查训练最大年份早于测试年份；只用训练数据估计先验敏感性、MASE 分母和漂移；预测区间经指数变换保持正值。
- 情景检查 r=0 或 H<=tau 时 s=0；theta=0 时回到基础路径；r=1 时等待期后 s=1；theta 增、r 增不应增加燃油，g 增、tau 增不应降低燃油。
- 解析 r_req 代回仿真应恰好达到目标（边界容差内）；不可行区域不强行裁切成看似可行的 0—1 比例。
- 图表的数据来源是实际脚本输出；摘要、结果表、图注和结论与同一 results_summary 绑定。禁止以演示数据填充主文结果。

### 7. 建议文章结构与真实完成门槛

摘要应在真实分析后写；引言明确航空增长与部署时滞的冲突；文献分为航空效率/气候约束、技术扩散/机队更新、分解与稳健决策；数据章节公开官方来源和统计边界；方法保持上述三模块；结果依次核算、外推检验、可行前沿；讨论说明设计—验证—制造协同的现实含义与不能识别的边界。

完成可投稿经验论文至少需要：已核验的真实观测及来源快照；可运行代码与机器可读结果；经核验的近期关键文献；与结果一致的英文正文；对口径/疫情/部署假设的局限说明。仅有研究设计和假设仿真不能标成已经完成了正式数据实证，更不能保证 Sustainability 录用。

### 8. AERS 技能加载记录

已成功读取根路由 `c4/auto-empirical-research-skills`。按根说明尝试以下完整资源均返回 `failed to read skill resource`：

- `skill://plugins_6ad19a2ef7d08191901e54e1a6391ef6/auto-empirical-research-skills/skills/69-Paper-WorkFlow/SKILL.md`
- `skill://plugins_6ad19a2ef7d08191901e54e1a6391ef6/auto-empirical-research-skills/skills/00.1-Full-empirical-analysis-skill_Python/SKILL.md`
- `skill://plugins_6ad19a2ef7d08191901e54e1a6391ef6/auto-empirical-research-skills/catalog/skills.json`

因此未声称执行不可读取的嵌套技能，也未依据未见原文的“门禁”要求阻断可独立完成的研究设计工作。

### 9. 已有核算脚本审核与当前交付状态

已阅读 `/workspace/research/analyze_official_data.py`：`f0,f1 = 10*q*i` 的结果单位是万吨，换算正确。脚本将来源核验和范围匹配设为先决输入，正值/有限性/重复年份检查合理；缺年不冒充一个年度变化。`--self-check` 中的数字是明确标识的合成算术例子，不是官方观测。

需在实际正文与脚本之间统一一个小差异：当前脚本 `fuel_activity_elasticity = gf/gq` 是普通百分比弹性；本方法设计选择的是 `ln(F1/F0)/ln(Q1/Q0)`。两者不是同一数值。推荐正文统一采用对数弹性、脚本用 `log1p(gf)/log1p(gq)`；也可以保留原脚本，正文明确标为百分比弹性并彻底删除对数口径。

当前脚本只实现模块 A 和不增油耗的阈值核算。模块 B 的滚动预测、模块 C 的部署仿真、全局敏感性、参数范围核验均尚未实现或运行，不能把方法文件中的拟议步骤写成既成研究结果。官方数据模板当前为空，故不能声称已经完成任何实证估计。

最低样本决策：不足两个连续且范围一致的年度观测时不做年度分解；未取得至少 8 个可用连续年度差分时不估计漂移模型；不足可评价样本外起点时不比较模型表现。预测基线的 MASE 分母若为零，应标记不可定义，不以任意小常数制造得分。只有活动和强度数据而没有技术参数证据时，可以绘制清楚标注的假设前沿，不能把仿真参数称为中国航空发动机实际研制/部署能力。

仅靠核算恒等式通常不足以构成高水平创新；研究价值取决于可信数据、参数证据、可检验的部署约束和与现有文献的真实差异。本文不建议以算法名称堆叠替代这些证据。
