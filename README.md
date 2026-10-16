# Aviation Efficiency Research

英文研究稿：**Efficiency Gains, Growing Fuel Demand and Deployment Frontiers in China’s Commercial Aviation**。

本仓库保存论文、补充材料、报告、图表、Excel数据及可复现代码。使用2015—2025年11组官方年度数据；考虑2017年统计处理变化，主分析采用2017—2025年。当前为供真实作者审阅的研究稿，尚未投稿。

## 下载与阅读

- [全部研究输出（ZIP）](downloads/ALL_RESEARCH_OUTPUTS.zip)
- 英文全文：[Word](deliverables/01_Manuscript/MANUSCRIPT_EN.docx) · [PDF](deliverables/01_Manuscript/MANUSCRIPT_EN.pdf)
- 英文补充材料：[Word](deliverables/02_Supplementary/SUPPLEMENTARY_INFORMATION.docx) · [PDF](deliverables/02_Supplementary/SUPPLEMENTARY_INFORMATION.pdf)
- 完整成果与核验报告汇编：[Word](deliverables/03_Research_Reports/COMPLETE_RESEARCH_COMPENDIUM.docx) · [PDF](deliverables/03_Research_Reports/COMPLETE_RESEARCH_COMPENDIUM.pdf)
- [官方数据与分析结果（Excel，17个工作表）](deliverables/04_Data_and_Code/RESEARCH_DATA_AND_RESULTS.xlsx)
- [交付目录](deliverables/00_DOWNLOAD_INDEX.md) · [单幅图、源数据与图表合集](deliverables/05_Figures)

## 复现分析

展开后的完整复现材料在 [`research/`](research/)，入口说明见 [REPLICATION_README.md](research/REPLICATION_README.md)。

在Python 3.12.14及所列依赖环境中，从仓库根目录执行：

```bash
python -m pip install -r research/requirements_research.txt
python research/reproduce.py
```

复现从已核验的官方数据摘录开始，无需重新联网采集；原始官方网址、页码及文件哈希保存在数据和来源记录中。该流程已在独立解压目录重跑，主要数值输出一致。

## 研究边界

燃油量是官方运输周转量和强度指标的重构估计。前瞻部署情景使用明确的压力测试假设，情景占比不代表现实发生概率。本文没有识别国产发动机或相关政策的因果效果，也未声称实现完整气候中和。

真实作者仍须核实全文，并完成作者、单位、经费、利益冲突、原论文关系及人工智能使用披露等事项。内部来源和技术核对不等同于外部同行评审或期刊录用决定。
