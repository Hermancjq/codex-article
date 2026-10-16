# Replication materials

The accompanying English manuscript analyses official Chinese commercial-air-transport activity and fuel intensity, then evaluates explicitly assumed deployment scenarios. It does not estimate domestic engine capabilities or causal policy effects.

## Contents and provenance

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

## Offline reproduction

Use Python 3.12.14 with the exact package versions in `requirements_research.txt`. A fresh virtual environment can be created outside any existing project and populated with `python -m pip install -r requirements_research.txt`. Installation requires access to the normal package registry; reproducing the analysis with installed dependencies requires no network.

From the extracted package root:

```bash
python reproduce.py
```

The command checks frozen input hashes, runs seven accounting arithmetic checks and eleven model/boundary checks, reproduces the accounting and conditional scenarios, writes the limited forecast diagnostics and rebuilds supplementary tables and figures. Logs preserve command outputs and failure status. The model checks use explicitly synthetic examples, not empirical observations.

The reproduction command also runs `figure_work/audit_figures.py` on the regenerated exports. Equivalent QA commands are recorded in `output/figures/QA_notes.md`. Source/geometry audits do not verify empirical authenticity or manuscript conclusions. Manuscript DOCX conversion used Pandoc; the supplied Word files already contain the three figures and editable equations.

## Statistical and interpretive boundary

Q is operator-based turnover of mainland China-registered carriers, including international services; it is not airport throughput or a territorial inventory. I is interpreted as transport-aviation intensity based on official same-value anchors and statistical continuity, not year-by-year enterprise matching. F = 0.1 Q I in Mt is reconstructed from rounded official inputs, not independently observed total fuel. The main data begin in 2017; earlier observations remain visible but are not treated as harmonised across the processing change.

The Bayesian benchmark has only two eligible tests in the extended series and none in the principal post-2017 period. It does not calibrate the scenario domain or establish model superiority. QMC design shares are not probabilities. Additional efficiency is relative to an improving baseline; adoption is fuel-use-weighted, not the fraction of aircraft replaced. No lifecycle, contrail, health, domestic-engine causal or comprehensive climate-neutrality result is claimed.

## Public release and author review

This is a local delivery package, not a GitHub release, Zenodo deposit or journal submission. The human authors must verify their authorship, declarations, evidence and interpretation and provide an archival location or attach the package as supplementary material before submission. The official policy audit is a source-based checklist, not an acceptance guarantee.
