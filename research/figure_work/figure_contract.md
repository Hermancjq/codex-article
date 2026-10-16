# Figure contract

The plotting backend is Python/matplotlib, established by the analysis workflow.
The target manuscript is for Sustainability. Figures use a white background,
editable PDF/SVG text and PNG previews at 300 dpi. All glyphs must be at least
5 pt in the exported PDF. The physical width is 183 mm. No private source
filenames appear in plotted labels or captions.

## Figure 1

Question: how did activity, fuel intensity and the fuel quantity implied by
their product change from 2015 to 2025? The claim is descriptive: activity and
intensity need not move together, and their product determines reconstructed
fuel use. One quantitative panel shows all annual observations without
exclusions. Official activity and intensity series are distinguished from
reconstructed fuel. All three are normalized to 2015 = 100; 2020–2022 is shaded.
The 2017 reporting-programme change is marked without implying a physical
discontinuity. Main decomposition inference starts in 2017. There are no
stochastic replicates or inferential intervals. It is a trend
figure, not causal evidence or an engine-performance assessment.

## Figure 2

Question: which accounting term explains fuel changes before, during and after
the pandemic? The claim is that chain-linked activity and intensity effects
sum exactly to the net reconstructed fuel change. One quantitative panel
compares 2017–2019, 2019–2022 and 2022–2025. Activity and intensity contributions
are grouped bars, and net change is a diamond. Values are in million tonnes.
The decomposition is deterministic accounting from rounded official data, not
a causal estimate. No statistical intervals are manufactured.

## Figure 3

Question: when can a stipulated technical benefit offset stipulated activity
growth, and how does deployment delay change the required deployment rate?
This quantitative grid has complementary evidence roles. Panel a gives the
full-adoption technical-benefit frontier under alternative ordinary annual
activity growth and baseline improvement assumptions. Panel b identifies the
deployment-rate threshold as delay increases in one fixed illustrative case.
These are exact conditional calculations, not calibrated estimates,
probabilities, forecasts or official targets. The 10–30% technical-benefit
range and 12% annual deployment ceiling are exploratory assumptions only.
Ordinary growth and improvement rates are converted to continuous log rates.
The horizon is 15 years (2025–2040). Every plotted point has a source-data row.

## Rendered QA

Use one consistent restrained palette, line styles and labels. Source
validation, PDF glyph audit and rendered collision audit must be run after
each final export. Figure 3 also calls the render-time panel-alignment gate at
1.5 pt tolerance, with panel labels required. Inspect the actual PNG output for
each figure and each panel before delivery; document every warning.
