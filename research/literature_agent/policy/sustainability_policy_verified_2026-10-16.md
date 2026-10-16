# Sustainability / MDPI 官方政策核验

实际访问：2026-10-16 04:31:55–04:32:00 UTC（北京时间 12:31:55–12:32:00）。本报告只陈述该次访问可读内容，不推断网页发布日期或后续变更。

## 访问及证据状态

| 来源 | 实际结果 | 已保存证据 |
|---|---|---|
| https://www.mdpi.com/journal/sustainability/about | HTTP 200 | sustainability_aims.html / .txt |
| https://www.mdpi.com/journal/sustainability/instructions | HTTP 200 | sustainability_instructions.html / .txt |
| https://www.mdpi.com/ethics | HTTP 200 | mdpi_ethics.html / .txt |
| https://www.mdpi.com/ethics#_bookmark21 | HTTP 200（同一 ethics 页面；不据此认定该 fragment 对应数据章节） | mdpi_data.html / .txt |
| https://www.mdpi.com/editorial_process | HTTP 200 | mdpi_editorial.html / .txt |

本轮没有 403。此前记录中的 403 是历史环境观察，不能再用来表示本轮政策无法核验。访问元数据见 access_log.json；原始文件 SHA-256 见 source_checksums.json。

## 经核验的要求与准确解释

### 1. 选题范围与研究价值

来源：Aims & Scope，https://www.mdpi.com/journal/sustainability/about （本地文本第 149–190 行）。

短摘录："Air pollution and climate change"；"Measuring and monitoring sustainability"；"full experimental and methodological details so that results can be reproduced and assessed"。

解释：能源、排放、需求变化、技术采用与政策情景等议题可与期刊环境和经济可持续性范围建立直接联系。可计算、可复现、与可持续发展问题直接相关，是可论证的匹配依据。官方范围并未要求方法越复杂越好，也不把模型复杂度等同于创新。

### 2. Article 的科学性、创新和文献

来源：Instructions for Authors，https://www.mdpi.com/journal/sustainability/instructions#submission （本地文本第 1139–1141 行）。

短摘录："scientifically sound experiments"；"a substantial amount of new information"；"the most recent and relevant references"。

解释：本任务适合 original research Article。必须提供真实资料和可检查结果；最新且相关的文献应由实际检索与核验支持。不能以未验证引文、编造数据、未经执行的复杂模型代替研究结果。会计分解、预测和情景仿真应各自表述，不可在没有识别设计时写成因果估计。

### 3. 用户不要求格式时仍需保留内容要素

来源：Instructions，https://www.mdpi.com/journal/sustainability/instructions#freeformatsub （本地文本第 1152–1156、1180–1183、1221–1224 行）。

短摘录："Sustainability now accepts free format submission"；"about 200 words maximum"。

解释：初投允许自由格式、文献格式一致即可；这不豁免作者信息、摘要、关键词、Introduction、Methods、Results、Conclusions、图表说明、经费、作者贡献、利益冲突等内容。研究文章类型说明另列 Discussion，宜保留。摘要约 200 词以内，单段，依次给问题、方法、主要结果和结论；关键词 3–10 个。可不在本任务花时间套版，但实证论文的内容要素需要完整。

### 4. 可复现方法、数据和代码

来源：Instructions，https://www.mdpi.com/journal/sustainability/instructions#manuscript 、#data 、#computer （本地文本第 1228、1245–1246、1294–1340 行）；Research Data Policies，https://www.mdpi.com/ethics （“MDPI Research Data Policies”章节）。

短摘录："Data Availability Statement (DAS)"（该节的强制声明要求）；"include all the parameters used"；"authors should release the code"。

解释：DAS 对本类研究是强制项；应说明支持结果的数据实际在哪里取得、哪些是公开资源，以及分析产生的数据可在哪里取得。MDPI 鼓励 FAIR 数据和可信仓库。新开发的代码应通过公开仓库（官方举例 GitHub）或补充材料释放，并说明软件版本、全部分析参数。公开统计资料的原始数据来源、下载日期、单位、口径、计算式、处理后表格、随机种子和情景参数应进入可复现材料。不得先写“已在 GitHub/Zenodo 公开”而实际尚未公开；本地交付不等于公共存档。对公共数据进行重新整理和分析的本研究不适合声称“No new data were created or analyzed”。

### 5. AI 使用披露

来源：MDPI Publication Ethics，https://www.mdpi.com/ethics （Artificial Intelligence → Manuscript preparation）；期刊 Instructions 第 1228 行。

短摘录："authors are required to declare this during the submission process"；"disclose details ... in the Materials and Methods section"；"product details in the Acknowledgments section"。

解释：仅语法、拼写、标点或格式等表层编辑可免披露。本任务涉及研究设计、检索辅助、分析代码、结果解释和实质写作，因此不属于豁免，应在投稿过程申报，在 Methods 交代用途，并在 Acknowledgments 给出实际产品/版本信息。AI 不能署名作者；人类作者对原创性、有效性、完整性负责，并需核对输出和每一条引文。工具名称、版本不可猜写。

建议披露草案（只在作者核对实际用途后采用）：

Methods: “Generative AI assistance was used for research planning, literature-search formulation, development and checking of analysis code, and manuscript drafting. All source records, analytical inputs and outputs, and cited references were checked against the underlying sources and reproducible analysis files by the authors.”

Acknowledgments: “During the preparation of this manuscript, the authors used [actual product name and version] for [verified description of use]. The authors have reviewed and edited the output and take full responsibility for the content of this publication.”

最后两句对“作者已检查/承担责任”的陈述须由真实作者在提交前亲自完成和确认；不能把本草案视为检查已经发生的证据。

### 6. 其他投稿和录用边界

来源：Instructions #coverletter；https://www.mdpi.com/editorial_process （本地文本第 100–106、124–130 行）。

短摘录："fits the journal’s scope and meets the expected standards of scientific soundness"；"At least two review reports"；"made exclusively by the assigned Academic Editor"。

解释：初筛看范围和科学可靠性；通过后仍须同行评议和学术编辑决定。Cover letter 必须解释意义和范围适配，作者批准、原创/非一稿多投等声明只能在作者确认后成立。满足可核验的投稿要求不等于达到可保证的录用标准；不应承诺录用。无需未经用户授权实际投稿、发邮件或公开发布。

## 对主稿的具体落实清单

- 把目标写成可检验的可持续性问题，并给出具有现实解释的增量发现。
- 用可追溯官方数据完成真实分析；明确描述年度、地区/行业边界、单位、口径和缺失值。
- 分离观察结果、分解结果与前瞻情景假设；报告敏感性和模型适用边界。
- 通过真实执行产出结果、图表和代码；只在实施完成时使用“we estimated / simulated”。
- 保留 DAS、软件/参数、GenAI 实质用途和产品详情披露草案；留空真实作者/基金/冲突信息供作者确认。
- 准备可公开的数据和代码包，但公共发布及投稿由用户另行执行或明确授权。
