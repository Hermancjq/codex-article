"""Assemble supplementary tables from executed outputs, never manual results."""
import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |', '| '+' | '.join(['---']*len(headers))+' |']
                     +['| '+' | '.join(map(str,r))+' |' for r in rows])


def main():
    out=BASE/'output'
    accounting=json.loads((out/'analysis/accounting_results.json').read_text())
    transition=json.loads((out/'transition/transition_results.json').read_text())
    empirical=transition['empirical_forecast_analysis']
    scenario=transition['conditional_deployment_scenarios']
    s=['# Supplementary Information',
       '\n## S1. Complete paired official record and provenance',
       '\nThe table preserves all eleven paired observations. No fuel-intensity value was interpolated before 2015. The main comparison begins in 2017 because that bulletin documents a change in production-data processing and audit rules. Reconstructed fuel is not independently observed total consumption.',
       '\n'+table(['Year','Q (10⁸ tonne-km)','I (kg/tonne-km)','Reconstructed fuel (Mt)'],
         [[r['year'],f"{r['turnover_100m_tkm']:.2f}",f"{r['fuel_intensity_kg_tkm']:.3f}",f"{r['implied_fuel_mt']:.6f}"] for r in accounting['annual']]),
       '\nThe canonical `source/verified_data.csv` contains separate source URLs, full SHA-256 digests, physical PDF page locators and the coverage interpretation for every pair. The official-source observation ledger adds exact Chinese quotations and source-file metadata. Transport-aviation interpretation is anchored to the CAAC 2019 transport-intensity statement, the 2022 policy/action series and indicator 126 in the 2024 survey system. This is a documented continuity interpretation rather than enterprise-level matching in every year. NBS cross-publication checks are retained separately; they reuse CAAC-origin statistics and are not independent original measurements. The 2025 observation was obtained from CAAC, not an unverified NBS 2026 yearbook.',
       '\n## S2. Chain-linked and direct endpoint decomposition',
       '\nThe chain calculation sums adjacent-year LMDI components. Direct endpoint allocation can differ, particularly through contraction and recovery; both sum exactly to the same endpoint fuel change. The following table reports Mt, retaining three decimals. All underlying calculations retain floating-point precision.',
       '\n'+table(['Period','Chain activity','Chain intensity','Endpoint activity','Endpoint intensity','Net'],
         [[f"{p['start']}–{p['end']}",f"{p['chain_activity_effect_10kt']/100:.3f}",f"{p['chain_intensity_effect_10kt']/100:.3f}",f"{p['activity_effect_10kt']/100:.3f}",f"{p['intensity_effect_10kt']/100:.3f}",f"{p['change_10kt']/100:.3f}"] for p in accounting['periods']]),
       '\nThe extended 2015–2025 comparison crosses the 2017 processing change and is not presented as a harmonised main estimate. Contributions remain accounting allocations; they do not identify technology, policy or rebound effects.',
       '\n## S3. Reporting-precision perturbations',
       '\nAt every combination of low/high starting and ending values, Q was perturbed by ±0.005 (10⁸ tonne-km) and I by ±0.0005 kg/tonne-km. Sixteen corners were evaluated per period. This examines source rounding only, not systematic measurement error, population coverage or a statistical confidence interval.',
       '\n'+table(['Period','Fuel growth, central (%)','Fuel-growth corner range (%)'],
         [[f"{p['start']}–{p['end']}",f"{100*(p['fuel_ratio']-1):.3f}",f"{100*(p['endpoint_rounding_corner_envelope']['fuel_ratio'][0]-1):.3f} to {100*(p['endpoint_rounding_corner_envelope']['fuel_ratio'][1]-1):.3f}"] for p in accounting['periods']]),
       '\n## S4. Bayesian diagnostic, baselines and small-sample exclusions',
       '\nLet d denote adjacent annual log-intensity changes. The conjugate model uses μ₀=0, κ₀=1, α₀=2 and β₀=0.05². For n changes with average d̄, κₙ=κ₀+n, μₙ=(κ₀μ₀+nd̄)/κₙ, αₙ=α₀+n/2, and βₙ=β₀+Σ(d−d̄)²/2+κ₀n(d̄−μ₀)²/(2κₙ). The h-step log-intensity predictive distribution is Student-t with 2αₙ degrees of freedom, location ln(I_T)+hμₙ and scale sqrt[(βₙ/αₙ)(h+h²/κₙ)]. Exponentiation supplies a median and central intervals; the exponentiated Student-t has no finite positive moments, so an original-scale predictive mean is not reported.',
       '\nB0 is unchanged intensity. B1 adds the unshrunk training mean log change. B2 uses the shrunk posterior location. Every model uses the same eligible origin, with a minimum of eight prior valid annual differences; no target observation enters its training. MASE divides absolute prediction error by the mean absolute adjacent-year naive error in that origin’s training set. A zero denominator remains undefined.',
       '\n'+table(['Model','Test years','n','MAE (kg/tonne-km)','MASE'],
         [[name,', '.join(map(str,v['test_years'])),v['n_test'],f"{v['MAE']:.6f}",f"{v['MASE']:.6f}"] for name,v in empirical['main_rolling_h1']['scores']['all'].items()]),
       '\nThese two tests are diagnostics, not evidence of model superiority. The post-2017 series has no eligible out-of-sample test under the same rule. Excluding every training difference touching 2020–2022 leaves only six valid differences in the extended record, so the pandemic-exclusion forecast is skipped rather than formed by joining separated years. Prior scales 0.02² and 0.10² are retained in the machine-readable outputs. The forecasting diagnostic is not used to choose or calibrate the conditional scenario domain.',
       '\n## S5. Conditional exploration, resolution and analytical bounds',
       '\nThe exact input configuration is `scenario_config.json`. g is uniform in the log-rate interval corresponding to ordinary growth of 2–6%; b is uniform in the continuous intensity-decline interval corresponding to ordinary reductions of 0–2%; θ and r have uniform design weights over 0.10–0.30 and 0.02–0.12, respectively. These are exploratory weights, not inferred parameter distributions. Delays are evaluated separately, not pooled into a probability mixture. H=15 and κ=1 define a 2040 non-increasing-fuel benchmark, not an asserted official target.',
       '\n'+table(['Delay (years)','2¹² design share meeting target (%)','2¹⁴ share (%)','2¹⁴ terminal-ratio median'],
         [[low['tau'],f"{100*low['fraction_of_design_points_meeting_target']:.4f}",f"{100*high['higher_resolution']['fraction_of_design_points_meeting_target']:.4f}",f"{high['higher_resolution']['terminal_fuel_ratio_design_quantiles']['0.5']:.6f}"] for low,high in zip(scenario['delay_summaries'],scenario['resolution_comparison'])]),
       '\nThe shares above describe only the stated design domain. They are not probabilities that China will meet a target. Scrambling seeds are 20261016, 20261017 and 20261018. No points are skipped or thinned. The higher-resolution results are stored with the resolution comparison; the initial individual design points are supplied in CSV. Re-running the documented code regenerates both.',
       '\nBy monotonicity, the lowest terminal ratio occurs at low g, high b, high θ, high r and the shortest delay; the highest occurs at the opposite corner. Exact bounds are '+f"{scenario['exact_domain_bounds']['best_corner']['terminal_fuel_ratio']:.6f} and {scenario['exact_domain_bounds']['worst_corner']['terminal_fuel_ratio']:.6f}. "+'These are bounds for the assumed box, not empirical prediction limits. A cumulative-fuel diagnostic sums future years 1 through H, excluding the observed baseline year, in units of baseline annual fuel. It is retained in the numerical output but is not used to claim a carbon budget.',
       '\nThe analytical frontier explicitly distinguishes baseline-sufficient, full-adoption-insufficient and deployment-threshold cases. It does not truncate an impossible adopted share to one or interpret fuel-use-weighted adoption as aircraft-count replacement.',
       '\n## S6. Reproduction and integrity boundaries',
       '\nThe replication README gives the offline reproduction command, exact software versions and input hashes. Eighteen deliberately synthetic arithmetic/mathematical checks cover accounting identities, unit conversion, Bayesian conjugacy and prediction variance, forward-only training, missing/excluded-year handling, adoption boundaries, analytic/numerical threshold agreement, monotonicity and exact scenario corners. These tests are not empirical observations. Official-document hashes, table transcriptions, coverage reasoning and figure-source values are separate evidence checks.',
       '\nReferences were checked against DOI metadata and authoritative publisher records. Reading coverage differs by source: the Bergero and Dray papers were used at the official-abstract level; Ang (2005) was bibliographically verified but its full text was not retrieved. The decomposition equations and closure checks are self-contained. Current MDPI author instructions, scope and research-data/artificial-intelligence policies were read; these checks do not constitute a journal acceptance decision or human-author attestation.',
       '\nNo confidential thesis survey responses or unverified capability scores were reused. Public archive publication and formal submission have not been performed. Author details, contributions, funding, conflicts, prior-thesis relationship and human-author review remain to be completed by the authors.'
    ]
    (out/'SUPPLEMENTARY_INFORMATION.md').write_text('\n\n'.join(s),encoding='utf-8')
    print('Supplementary tables generated from actual accounting and transition outputs.')


if __name__=='__main__':
    main()
