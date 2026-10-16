> Archived pre-analysis protocol. Network access was restored and the analyses were subsequently completed. The final research draft is `MANUSCRIPT.md` / `MANUSCRIPT_EN.docx`; its scope and executed methods supersede this prospective document. Statements below describing pending work refer to the earlier preparation stage.

# Can Efficiency Gains Offset Growth in China’s Civil Aviation?

## An official-data decomposition and deployment-constrained scenario analysis

**Status: prospective research protocol; not a completed empirical manuscript. No official annual observations or new empirical results have yet been verified.**

### Research question and contribution to be tested

The study will examine whether improvements in the fuel intensity of Chinese civil air transport have been sufficient to offset changes in transport activity. A second question concerns the intensity improvements required under alternative, explicitly assumed activity and deployment trajectories. The contribution to be evaluated is an auditable link between historical accounting, growth-compatible efficiency thresholds, and conditional deployment scenarios. Novelty relative to recent studies remains to be established through source-verified literature searches.

The supplied Chinese manuscript motivates the importance of coordination among aero-engine design, testing and manufacturing. That framework will inform the discussion of deployment constraints. Aggregate air-transport statistics do not measure domestic aero-engine development capability. The proposed study therefore will not estimate the causal effect of domestic engine development, industrial reorganisation, certification policy or organisational coordination.

### Evidence and statistical boundary

The primary sources will be annual statistical bulletins published by the Civil Aviation Administration of China, supplemented where appropriate by National Bureau of Statistics publications. The intended period begins in 2010 and ends with the latest complete, compatible and verifiable year. This is a target window, not a claim of data availability. Every included observation will retain the original document, official URL, observation year, publication year, table or page locator, unit, coverage definition and source-file SHA-256 digest.

The minimum paired inputs are total transport turnover, Q, in units of 100 million tonne-kilometres, and fuel intensity, I, in kilograms per tonne-kilometre. They may be multiplied only after confirming that their statistical populations and geographical and operational boundaries match. Passenger-kilometres cannot substitute for total tonne-kilometres. An intensity indicator for transport airlines cannot automatically be combined with activity covering all civil aviation. Definitions or conversions used by the statistical authority will be documented rather than inferred.

Where compatible fuel use is independently reported, it will be used as an external accounting check. A fuel series reconstructed from turnover and intensity is mathematically derived from those inputs and is not an independent validation dataset. Missing years will remain missing unless an explicitly justified sensitivity analysis is undertaken. No missing observation will be represented as an official reported value.

### Accounting and exact decomposition

With the units above, reconstructed fuel use F in units of 10,000 tonnes satisfies:

**F(t) = 10 × Q(t) × I(t).**

For two positive observations, define the logarithmic mean L(a,b) = (a−b)/(ln(a)−ln(b)), with L(a,a)=a. The change in fuel use can then be written exactly as:

**ΔF(activity) = L(F(1),F(0)) × ln[Q(1)/Q(0)]**

**ΔF(intensity) = L(F(1),F(0)) × ln[I(1)/I(0)].**

The two components sum to observed or consistently reconstructed fuel change, subject to numerical rounding. The analysis will report both effects in physical fuel units and verify the identity for every interval. The published source for the decomposition method will be checked before manuscript citation.

This decomposition is descriptive. An intensity component can reflect fleet composition, load factors, route structure, operational practices and technology, among other influences. It cannot be labelled an engine innovation effect without additional identification. Similarly, a temporary fall in activity during a disruption is not evidence of a durable technological transition.

### Growth-compatible improvement thresholds

If activity grows by g and intensity declines by e over the same interval, the fuel-use ratio is (1+g)(1−e). Fuel use does not increase when:

**e ≥ 1 − 1/(1+g), for g > −1.**

For a cumulative activity ratio A and a specified fuel-use target ratio R, the required terminal intensity ratio is at most R/A. These are accounting conditions, not fitted policy effects. When g is negative, the threshold may also be negative; it should not be misreported as a required positive efficiency improvement. Historical activity and fuel changes will be shown alongside any decoupling classification, since a ratio alone can be unstable near zero activity growth or misleading during contraction.

### Dynamic modelling and validation rule

The final forecasting or filtering model will be selected only after the length, gaps and coverage of the verified series are known. Candidate models may include a constant-intensity baseline, an exponential trend and a parsimonious local-level or local-linear-trend state-space model. Pandemic-related disruptions will be explicitly examined. A separate free parameter for every event or transition is inappropriate when the annual sample is short.

Any fitted dynamic model will be compared with simple baselines using forward-chaining historical evaluation. Training observations will precede validation observations. Parameter tuning, transformations and break selection will use the training window only. Forecast errors, number of evaluation origins and uncertainty coverage will be disclosed. If there are too few usable origins or unstable estimates, the model will be omitted from inferential claims, and transparent accounting and conditional scenarios will carry the analysis.

The study will not use a complex machine-learning model merely to create an appearance of novelty. It will not treat simulated paths as additional empirical observations or describe in-sample fit as independent predictive validation.

### Deployment-constrained scenarios

Scenarios will distinguish activity growth, realised efficiency improvement and the timing of technology adoption. A deployment delay can shift the date at which an improvement begins; an adoption constraint can limit its rate of diffusion. Such parameters require independent evidence if presented as calibrated estimates. Otherwise they will be openly labelled analyst-defined assumptions and explored over a stated range.

The scenario analysis will evaluate fuel outcomes and threshold violations under combinations of these inputs. Monte Carlo sampling may propagate specified parameter uncertainty, but the distributions and dependence assumptions will be reported. Scenario probabilities will not be described as real-world probabilities unless their calibration can be defended. Robust comparisons will ask which conclusions survive the full stated range of plausible assumptions, rather than select a favourable single trajectory.

No national causal effect of design–testing–manufacturing coordination will be inferred from these scenarios. The relationship to the original manuscript will remain a mechanism-based interpretation and a source of deployment hypotheses.

### Sensitivity and limitations

The analysis will examine pre-pandemic and pandemic/recovery intervals separately while retaining the full observed record. Other checks will concern endpoints, alternative compatible official revisions, rounding, assumed activity growth, intensity trajectories, deployment lags and dependence between uncertain inputs. Annual official aggregates may not support attribution among aircraft technology, engine technology, airline operations and network composition.

Fuel use, combustion CO2, lifecycle greenhouse gases and non-CO2 climate effects are different quantities. The primary analysis can remain in fuel units. Any conversion to combustion CO2 requires a verified emission factor, consistent coverage and a documented calculation. That conversion does not estimate lifecycle emissions or total aviation warming, and a change in fuel mix requires a separate treatment.

### Planned manuscript evidence chain

The eventual article will open with the specific sustainability question established by the verified literature. The data and methods section will define the official statistical boundary and accounting identities. Results will proceed from historical activity and intensity changes to the decomposition, improvement thresholds, model validation where justified and conditional scenarios. Discussion will relate these findings to deployment constraints and to the supplied manuscript's coordination framework without elevating that framework into an empirically identified mechanism.

The abstract, final title and conclusions will be written after the results. Data and code availability, source limitations and the actual role of AI assistance will be stated accurately. Authorship, affiliations, funding and applicable declarations require author-supplied facts; none will be invented. Current Sustainability policies and recent references remain unverified until external access is restored.

### Evidence status

The original Word manuscript has been preserved and audited. The accounting implementation has passed seven deliberately synthetic arithmetic checks. Those checks establish a limited numerical property of the implementation; they establish neither the authenticity of future input data nor the empirical validity of the proposed study. Official data retrieval, current literature verification, empirical estimation, scenario calibration and English manuscript drafting remain pending.
