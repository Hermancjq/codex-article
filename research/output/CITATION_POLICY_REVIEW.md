# Internal citation and publication-policy check

**Reviewed file:** `MANUSCRIPT.md`, snapshot read on 16 October 2026. This is an internal source-and-policy check, not external peer review or an acceptance assessment. The manuscript was not edited. Line locators below refer to this snapshot.

**Main finding:** The scientific literature citations map to real sources and mostly support the narrowly worded claims. The 2025–2026 citations do not import international results as Chinese estimated parameters. One official-source title is factually wrong and should be corrected: reference 15 describes a different white paper from the one at its URL. The manuscript remains a research draft with explicit human-author and submission declarations pending; it should not be labelled fully submission-ready.

## 1. Corrections and targeted improvements

### Required: correct reference 15's document identity

- **Location:** reference 15; the associated source discussion is Section 2.1, line 31.
- **Current reference:** *Press Conference on China’s Civil Aviation Green Development Policy and Action White Paper*.
- **Actual official page title:** `民航局参加国新办 《中国交通的可持续发展》白皮书新闻发布会`.
- **Actual date:** 22 December 2020. The body says the State Council Information Office held a press conference about `《中国交通的可持续发展》`; CAAC Deputy Administrator Dong Zhiyi answered questions there. It is not a press conference on a civil-aviation green-development policy white paper.
- **The numerical support remains valid:** the page explicitly states `2019年，我国运输航空每吨公里油耗和碳排放分别为0.285千克和0.898千克`. Thus the 2019 transport-aviation intensity anchor in Section 2.1 is supported; only source identity/attribution needs correction.
- **Suggested accurate reference, explicitly a translation:**

  Civil Aviation Administration of China. *CAAC Participates in the State Council Information Office Press Conference on the White Paper “Sustainable Development of Transport in China”* [English translation of Chinese news-release title]; 22 December 2020 (in Chinese). https://www.caac.gov.cn/XWZX/MHYW/202012/t20201222_205702.html (accessed 16 October 2026).

- **Suggested body wording:** “An official CAAC report of the State Council Information Office press conference on the transport-sustainability white paper explicitly identifies the 2019 value …” This avoids calling it a CAAC white paper.
- **Saved evidence:** `/workspace/research/scope_audit/raw/53d7e6bd0a7262a76c6618c045b0a998f367efabcdcbd02228599b640e86225b.html`, together with `scope_evidence.json` and `SCOPE_FINDINGS.md` in that directory. The English wording above is identified as a translation, not asserted to be the official page's English title.

### Recommended: identify reference 16 as the actual news release

Reference 16 is a real CAAC page, dated 23 September 2022, headed `中国民航局发布《2022中国民航绿色发展政策与行动》`. Its present English title omits “2022” and makes the news page look like the policy document itself. The source supports the shared 2019/2021 intensity-series statement. For precision use:

> Civil Aviation Administration of China. *CAAC Releases “2022 Policies and Actions for Green Development of China’s Civil Aviation”* [English translation of Chinese news-release title]; 23 September 2022 (in Chinese). https://www.caac.gov.cn/XWZX/MHYW/202209/t20220923_215418.html (accessed 16 October 2026).

Alternatively cite the attached policy PDF as a separate document after checking its title page and publication identity. Do not imply an official English title has been found when only the Chinese webpage has been checked.

### Recommended: make reference 9's narrower role clearer

- **Location:** Section 4.1, line 165, “policy analyses question the adequacy of technology-centred growth strategies [7,9]”.
- **Assessment:** reference 7 directly critiques a technology-centred climate-neutral-growth narrative using EU/Finland policy documents. Reference 9 is an economic analysis of aviation policy instruments, international coordination and efficiency standards, including rebound/instrument interactions. It is not the same kind of narrative/content analysis and should not be read as independent evidence of the EU/Finland document finding.
- **Suggested narrow wording:** “Policy-document analysis questions technology-centred growth narratives [7], while economic analysis highlights interactions among efficiency standards, carbon pricing and demand responses [9].”
- Reference 9's use in Section 2.2 to contextualise rebound is reasonable, provided the manuscript continues to say its own decomposition does **not** estimate a causal rebound effect. No Chinese rebound elasticity should be inferred from Proost (2026).

### Recommended: state who/what completed the checks without implying human-author verification

- **Location:** Section 2.6, line 104.
- **Current wording:** “source records and bibliographic metadata were checked against official documents and publisher records.”
- **Assessment:** the next sentences explicitly state that human-author verification remains pending, which preserves the draft boundary. Nevertheless, the passive completed-check wording could be read out of context as an author certification.
- **Suggested wording:** “The research-assistance workflow retrieved and compared source records and bibliographic metadata with official documents and publisher records, and generated the calculations through executed Python scripts. Independent verification and approval by the named human authors remain pending.”
- Only retain statements of completed retrieval, execution and comparison for which the package contains records. Do not replace the pending status with “the authors independently verified all sources” until real authors actually do so.

### Recommended: bind the DAS to the actual delivered replication package

- **Location:** Data and Code Availability, line 197.
- **Assessment:** it correctly avoids claiming a public DOI, a GitHub release or public archiving. Supplementary files are an allowed route under the current policy. The present text says the materials are “supplied”; this must be true of the final delivery/submission rather than a future intention.
- **Action:** once the package is assembled, name its actual ZIP or supplementary-file identifier and its source ledgers. Example: “Data and code are available in the accompanying replication package, [actual filename], including [actual ledger filenames].” Do not add a public URL until public deposit has actually occurred.
- Do not use “No new data were created or analysed”: this study transcribes, transforms and analyses public observations and generates simulation outputs.

### Recommended: pin reference 19 to the runtime's official documentation

The manuscript transparently distinguishes documentation 1.18.0 from analysis runtime 1.17.0; this is not a false statement. A version-matched official URL was also successfully retrieved during this review:

https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.stats.qmc.Sobol.html

It confirms `random_base2`, power-of-two balance, LMS+shift scrambling and `float64` behavior for 1.17.0. Replacing the unversioned reference-19 URL with this pinned URL removes the mismatch. Saved HTML/text: `/workspace/research/literature_agent/policy/scipy_qmc_1_17_0_sobol.html` and `.txt` (HTTP 200). Do not change the runtime version merely to match current documentation.

### Access limitation to preserve: reference 17

Ang (2005) has verified Crossref and RePEc bibliographic identity, but no abstract or full text was obtained: Crossref has no abstract, RePEc explicitly has none, and ScienceDirect remained blocked. The manuscript's self-contained decomposition equations and numerical closure do not require claiming original-paper full-text appraisal. Keep this access limitation in the source-review ledger; authors should consult the original method before submission where possible. Do not add a quotation or a detailed property attributed to a supposedly read Ang full text. No fabricated method citation was found.

### Pending author/provenance information should remain pending

The author-declaration and AI-acknowledgment sections correctly mark unresolved information. Actual authors must complete names, affiliations, corresponding author, contributions, funding and conflicts, and confirm the source thesis's authorship and prior-publication/submission status. If the supplied thesis is publicly available or needs an unpublished-work acknowledgment, give it an appropriate citation or provenance acknowledgment after confirming those facts. Do not invent a thesis repository, DOI, publication status, ethics approval, “no conflicts,” “no funding,” all-author approval, originality declaration or absence of simultaneous submission.

## 2. Numbered-citation and metadata audit

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

## 3. Journal substantive-content check

The authoritative policy snapshot is `/workspace/research/literature_agent/policy/sustainability_policy_verified_2026-10-16.md`, backed by official HTML and access logs. Scope includes sustainability measurement, air pollution and climate change; the study's explicit fuel/activity/deployment question has a defensible scope connection. No claim that complexity guarantees novelty or acceptance appears.

- **Research structure:** Introduction, reproducible methods, results, discussion, conclusions, figures/tables and reference list are present. Abstract is approximately **176 whitespace-delimited words**, within the retrieved “about 200 words maximum” guidance; six keywords meet the stated 3–10 range.
- **Scientific boundaries:** observed data, deterministic accounting, conditional scenarios and a limited forecasting diagnostic are separated. No fake forecast superiority, inferred engine-capability effect, causal rebound estimate, lifecycle accounting or climate-neutrality outcome is claimed. Literature supports the modest motivation rather than replacing empirical evidence.
- **Reproducibility:** software versions, seeds, parameter ranges, conversion equations and scenario target are described. Public sources and derived inputs are distinguished. A final delivered package must actually contain the promised files, and authors must check the calculations and figures.
- **Data/code statement:** present and does not falsely claim public deposit. Concrete package identifiers remain desirable, and publication-time availability must match the actual deposit/supplement route. A DOI is not invented or required to exist at drafting time.
- **AI disclosure:** substantive assistance is disclosed in Methods and Acknowledgments, matching the policy's placement and submission-declaration direction. Actual product/version details and human responsibility certification still require real authors. Current pending-language is appropriate for a draft.
- **Authorship/funding/conflicts/provenance:** deliberately unresolved, not falsely negative. These are required submission-completion items and cannot be supplied by inference. A cover letter, originality/all-author approval and no-concurrent-submission assurances must likewise wait for author confirmation.
- **Editorial boundary:** this check does not establish “meets acceptance requirements,” novelty by editorial standards or a probability of acceptance. Scientific soundness and substantial new information remain editorial/reviewer judgments.

## 4. Evidence used and actions intentionally not taken

The review compared the manuscript with the saved Crossref/publisher records, `verified_references.json`, `claim_evidence_mapping.md`, official source/scope ledgers, and retrieved MDPI/SciPy documents. It did not change the manuscript, upload it to an external service, publish the code, contact a journal, submit the work, certify human authorship, or simulate an editor's decision. Scientific result replication and figure QA are outside this citation-policy review and should rely on the separate executed-analysis checks.
