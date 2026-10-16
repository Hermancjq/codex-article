# Internal source and boundary review

This is an internal source audit conducted within the same Codex platform. It is not external peer review, journal review, human-author verification or acceptance assessment. No manuscript text was changed.

Reviewed file: `/workspace/research/output/MANUSCRIPT.md`, 228-line snapshot, SHA-256 `96eda33b596c8f97ee79e17c265c69579040fd2a4a8aff1342c97011844bd79a`. Line numbers below refer to that snapshot.

## Corrections needed

1. **Reference 15 misidentifies the white paper (line 223; cited at line 31).** The actual official page is titled `民航局参加国新办《中国交通的可持续发展》白皮书新闻发布会`, not a press conference on a civil-aviation green-development policy/action white paper. The present title conflates the December 2020 transport white paper with the September 2022 aviation publication. Replace the reference title with an accurate translation, for example: *CAAC Participates in the State Council Information Office Press Conference on the White Paper “Sustainable Development of Transport in China”*; retaining the exact Chinese title in brackets would remove translation ambiguity. The existing date, URL and transport-intensity quotation are correct. Source: `scope_audit/raw/53d7e6bd0a7262a76c6618c045b0a998f367efabcdcbd02228599b640e86225b.html`, title and main paragraph beginning `《中国交通的可持续发展》白皮书中对绿色发展用了专门章节进行描述`.

2. **Abstract wording can imply all eleven annual pairs were checked against NBS (line 5).** The documented NBS numerical checks concern turnover in 2019, 2023 and 2024, not all eleven Q/I pairs and not the fuel-intensity series. Change to: “Eleven annual observations for 2015–2025 were assembled from CAAC publications; selected turnover observations were cross-checked against NBS yearbooks.” Section 2.1, line 29, otherwise states the scope and non-independence correctly. Evidence: `scope_audit/nbs_turnover_crosscheck.csv`.

3. **Make the remaining denominator ambiguity explicit in the methods (line 31; related limitation at line 185).** The existing continuity qualification is substantially accurate. However, the cited 2024 statistical system also defines general-aviation converted-tonne-km and combined average-converted-tonne-km intensities, alongside transport-only intensity. The current text mentions only the transport formula, making the reason for the inferential qualification less visible. Add a short sentence such as: “The survey system separately defines general-aviation and combined converted-tonne-kilometre measures; our transport-only interpretation relies on the official transport-aviation anchors and continuity of the annual indicator.” This does not require abandoning the documented scope decision or treating the derived product as unusable. It prevents readers mistaking a located formula for direct proof that each annual bulletin independently restated that same denominator. Source: 2024 statistical survey system, item 126, printed pp.80–81 / physical PDF pp.84–85; `scope_audit/scope_evidence.json`.

## Small editorial source clarification

At line 19, “replace untraceable capability indices” describes the revision process and can be read as an unreferenced criticism of prior research. Prefer “use publicly documented operational statistics to examine deployment requirements”. The underlying manuscript audit established insufficient traceability in the supplied materials, not that every capability index in the field is untraceable. This wording issue does not contaminate the empirical data or recreate the original unsupported questionnaire results.

Reference 16 (line 224) could also identify the year and distinguish the release page from the document: the linked page is `中国民航局发布《2022中国民航绿色发展政策与行动》`; the underlying official PDF is archived at `scope_audit/raw/24d537035bc4c214d1b0fab89e7b5298d462d180464316e294eebdb52a41f8be.pdf`. Calling the linked item an official policy release in line 31 would be maximally precise, although the release faithfully reproduces the relevant policy-document figures.

## Empirical values independently checked: no numerical corrections needed

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

## Boundary checks passed

- **No independent fuel-total claim:** lines 31, 46, 110, 116 and 185 consistently identify F as reconstructed. They do not treat QI identity closure as independent empirical validation.
- **Operator versus territorial scope:** lines 13, 29, 181 and 193 correctly refer to mainland China-registered carriers, include international services, exclude foreign carriers and distinguish national territorial inventory coverage.
- **NBS reuses CAAC-source data:** line 29 correctly limits the check to transcription and cross-publication consistency. None of the three NBS values conflicts with the respective CAAC rounded number; no averaging of different official versions was performed.
- **2017 change is appropriately handled:** line 27 accurately reflects the 2017 bulletin's statement: `2017年度行业综合统计系统正式上线后，由于航空公司生产数据处理流程和审核规则发生变化，2017年度相关数据和增速按照最新的口径进行计算。` The original is at physical PDF p.18, note [1]. The post-2017 principal analysis and the warning against assuming full-record harmonisation are appropriate. This does not establish that all possible later revisions have independently been ruled out, and the manuscript does not claim that.
- **Original questionnaire and capability results are not inherited:** lines 19, 68, 104, 171 and 187 use the original design–testing–manufacturing perspective only as conceptual motivation. The paper does not report the original 364-person questionnaire as a newly conducted survey, reuse its coefficients as causal estimates, or invent confidential engine-development observations.
- **Scenario inputs remain assumptions:** lines 64–94 and the relevant Results/Discussion paragraphs distinguish fuel-use-weighted adoption from aircraft replacement, baseline and incremental benefit, hypothetical ranges from observations, and scenario-design shares from real-world probabilities. No official-data provenance is falsely attached to the future parameter ranges.
- **No climate-neutrality overclaim:** lines 179–181 correctly distinguish fuel mass, lifecycle greenhouse gases, contrails, health effects and territorial-inventory coverage.

This audit checks empirical input traceability, principal accounting numbers and the stated research boundary. It does not independently verify every cited scholarly paper's substantive claim, validate all scenario code or establish readiness for journal acceptance; those are separate review tasks.
