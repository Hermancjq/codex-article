# Method and software source verification

Retrieved 16 October 2026 (Asia/Shanghai). These are additional methods sources, separate from the 13 aviation-content references.

## Ang (2005): bibliography verified, full text and abstract not read

**Reference:** Ang, B. W. (2005). The LMDI approach to decomposition analysis: a practical guide. *Energy Policy*, **33**(7), 867–871. https://doi.org/10.1016/j.enpol.2003.10.010

- Crossref DOI record retrieved successfully and saved as `raw/ang2005_crossref.json`; title, author, publication year, volume, issue and pages match the candidate supplied by the parent.
- Publisher page `https://www.sciencedirect.com/science/article/pii/S0301421503003136` returned proxy 403. Its `/abs/` equivalent also returned 403.
- RePEc bibliographic page `https://ideas.repec.org/a/eee/enepol/v33y2005i7p867-871.html` was successfully read and independently confirms these bibliographic details. It explicitly reports: “No abstract is available for this item.” Original page and text are saved as `raw/ang2005_repec.html` and `.txt`.
- **Access boundary:** this is a verified bibliographic method reference, not an original-paper content appraisal. Do not attribute detailed properties, robustness claims or a quotation to a full text that was not read. The manuscript's stated decomposition equations and zero-residual numerical checks should be self-contained and independently verified. The author may consult the full original paper before submission.

## Virtanen et al. (2020): official abstract and open full text available

**Reference:** Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J., et al.; SciPy 1.0 Contributors (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nature Methods*, **17**(3), 261–272. https://doi.org/10.1038/s41592-019-0686-2

- Crossref record and official Nature Methods article successfully retrieved; full author metadata are retained in `raw/scipy2020_crossref.json`.
- Official source: https://www.nature.com/articles/s41592-019-0686-2
- Original page and extracted text: `raw/scipy2020_publisher.html` and `.txt`.
- The official abstract identifies SciPy as an open-source Python scientific-computing library and describes an overview of its capabilities and development practices. This supports the software citation.
- **Boundary:** this 2020 paper does not discuss `stats.qmc` or Sobol sampling in its visible text. It should not be used as evidence for current Sobol API defaults or balance properties; use current official API documentation for those details and report the version actually run.

## Current Sobol API

See `policy/scipy_qmc_verified_2026-10-16.md` (verification complete) and its saved official documentation. Use the actual analyzed SciPy version and actual constructor arguments, sample count, scrambling flag and random generator/seed in the manuscript and code. A quasi-Monte Carlo share across chosen parameter bounds is not an observed probability or a data-estimated probability distribution.

The official documentation retrieved is labeled SciPy 1.18.0. It states that `random_base2(m)` generates 2^m points with balance properties; skipping the first point, thinning, or using arbitrary non-power-of-two sample counts loses these properties. `scramble=True` applies LMS followed by digital random shift. `bits` defaults to 30 when `None` and is limited to 64; it controls sequence length 2^B, while output dtype is `numpy.float64`. Sobol sequence sampling does not itself constitute Sobol sensitivity analysis.
