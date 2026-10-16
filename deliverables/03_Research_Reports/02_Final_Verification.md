# Final verification and review dispositions

This is an internal consistency and provenance record for the delivered research draft. It is not external peer review, human-author approval, a journal acceptance assessment or an exhaustive proof of manuscript correctness. The method checker also contributed to the model implementation; shared platform/context and source records are retained rather than described as independent external review.

## Executed evidence

- Eleven official paired annual observations (2015–2025), with original-report SHA-256 digests, exact quotations and PDF page locators. All eleven source files were rehashed successfully. Selected NBS yearbook turnover values agree after conversion/rounding; their underlying statistics originate with CAAC.
- Main comparison restricted to 2017–2025 following the documented processing change. Reconstructed fuel is not an independent official measurement, a territorial inventory or a domestic-engine effect.
- All eleven annual fuel-unit conversions and all seven reported chain-period closures checked against the machine-readable results. Seven principal manuscript numerical bindings were mechanically compared with the results; additional scenario, posterior and source values were checked in the recorded technical reviews.
- Seven synthetic accounting assertions and eleven mathematical/model test cases passed. These checks do not create empirical observations.
- Offline reproduction completed from the frozen official extract and explicit scenario configuration. A newly extracted copy of the delivery archive was then rerun in a separate directory: accounting JSON, transition JSON, post-2017 diagnostic JSON, analytical-frontier JSON and supplementary tables matched the source outputs byte for byte. Limited Bayesian diagnostics, two resolutions of Sobol conditional scenarios and exact corner bounds were actually run. Forecasting remains diagnostic; scenario shares remain assumption-domain shares.
- Three figure sources and final PDFs passed the retained source, text-size and collision checks; the two-panel figure passed the 1.5 pt alignment gate. Every figure was visually inspected. Full figure notes and measured QA reports accompany the exports.
- Twenty reference entries were checked for numbered mapping and source identity. Literature reading coverage is recorded. Ang (2005) was bibliographically verified; no full-text reading is claimed. A follow-up OpenAlex/Semantic Scholar metadata query also did not identify accessible full text.
- The abstract contains 185 words under the recorded tokenisation check. Word delivery contains three embedded figures, three tables and five editable display-equation objects.
- The original supplied document’s hash is unchanged. No unpublished manuscript was sent to an external model, no journal was contacted, and no repository or article was publicly released.

## Review findings addressed

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

## Remaining author-owned steps

Names, affiliations, corresponding-author details, contributions, funding, conflicts, prior-thesis relationship, final human review and exact assistance-product/version disclosure require the real authors' confirmation. The code/data package has been delivered locally, not publicly archived. These remaining steps preclude calling the draft administratively ready for immediate submission. Editorial novelty and acceptance remain matters for the journal and its reviewers.

The acronym scanner is advisory and only partially covers the abstract/body. Its LMDI expansion-parsing limitation was manually reviewed: the full method name is present in Section 2.2. This does not constitute an automated clean-document certificate.
