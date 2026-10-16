# SciPy Sobol randomized quasi–Monte Carlo 方法核验

## 官方证据与访问状态

- URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.Sobol.html
- 实际访问：2026-10-16 04:36:37 UTC（北京时间 12:36:37），HTTP 200。
- 页面自身的 `docsearch:version` 与版本切换元数据均为 **SciPy 1.18.0**。这只标识所访问文档，不能用来代替实际分析环境所安装的 SciPy 版本。
- 保存：`scipy_qmc_sobol.html`（原始 HTML）；`scipy_qmc_sobol.txt`（解析文本）；`scipy_qmc_access_log.json`（URL、访问时间、HTTP 状态、字节数、SHA-256）。

## 精确短摘录与解释

| 要点 | 官方短摘录 | 正确解释 |
|---|---|---|
| 序列与点数 | “Sobol’ sequences are low-discrepancy, quasi-random numbers.” | Sobol 是低差异积分/设计点序列，不是独立同分布的普通伪随机观测样本。 |
| `random_base2` | “guarantees the balance properties of the sequence.” | `random_base2(m)` 用于生成 n = 2^m 个点。应从新引擎生成完整的 2^m 点设计，保留全部点，避免把任意长度采样描述为同样具有平衡保证。 |
| `scramble` | “If True, use LMS+shift scrambling.” | 默认 `scramble=True`；实现为 left linear matrix scramble 加 digital random shift。固定并记录随机种子/生成器状态能复现同一随机化设计。 |
| 失去平衡的情形 | “a sample size that is not a power of 2, or skips the first point, or thins the sequence” | 不能随意删除第一个点、抽稀或取非 2 的幂次的样本数后仍宣称保留官方 Sobol 平衡属性。扩大设计时应采用更大的 2^M；不是在原样本后任意补点。 |
| 独立随机化重复 | “the number R of independent replicates does not have to be a power of 2.” | 每个重复设计内保持 n = 2^m；可用多个独立 scramble 的重复比较结果，考察数值误差与收敛。重复次数 R 不要求是 2 的幂。 |
| `bits` | “Control the maximum number of points ... 2**bits. Maximal value is 64.” | `bits` 控制生成器周期上限；默认 `None` 对应 30，即最多 2^30 个点。显式最大值为 64。耗尽 2^B 点后本应重复，因此实现抛出错误。 |
| 返回精度 | “return type, which is always np.float64” | `bits` 不等于输出数据类型或任意精度。返回是 float64；IEEE 754 双精度通常有 53 位二进制有效精度。增大 `bits` 不能解释成提高结果的浮点数值精度。 |
| 事后优化 | “does not guarantee that all properties of the sample will be conserved.” | 若目标是保留标准 Sobol 设计性质，使用 `optimization=None`；不能做事后优化后无条件声称所有原有属性仍成立。 |

以上摘录对应本地文本第 59–103、116–137 行。摘录中的省略号只省略无关连接文字；完整原句以原 HTML/解析文本为准。

## 论文表述边界

建议称 **randomized quasi–Monte Carlo (RQMC) scenario sampling using scrambled Sobol sequences**。由 n = 2^m 个设计点经参数映射得到的情景集合，可以衡量在给定参数范围、变换与依赖设定下，哪些组合达到目标。若参数只定义为探索范围，满足某条件的点比例应称 **scenario share** / **fraction of evaluated scenarios**，不能写成观察到的事件频率、预测事件发生概率或经经验校准的风险概率。

即使采用了均匀、三角等参数分布，此比例也仅对应所选分布下的模型条件结果；分布不由实证识别时，不得将其解释为实际世界发生概率。Sobol 的 scramble 不会自动给输入假设赋予经验概率意义。独立 scramble 重复之间的差异反映数值积分/采样误差，也不包含结构性模型误差、数据偏差或输入分布不确定性。

建议 Methods 文案（按实际执行修改）：

“Parameter scenarios were generated using randomized quasi–Monte Carlo sampling with scrambled Sobol sequences implemented in SciPy [actual installed version]. Each design contained n = 2^m points generated with `random_base2(m)`, with `scramble=True`, `optimization=None`, and a recorded random-generator seed. Scenario coordinates were mapped to the prespecified parameter ranges [and transformations]. Reported attainment shares describe the fraction of evaluated scenarios satisfying the criterion under this sampling design; they are not empirically calibrated probabilities.”

应在补充材料记录实际 m、维度 d、bits、种子/生成器、重复次数、边界、参数映射、相关性假设、SciPy/NumPy版本。只有真的执行独立 scramble 重复或收敛检验时，才能声称进行了相应误差检查。该采样器自身也不构成 Sobol sensitivity-index analysis；若未计算相应敏感度估计量，不应把场景采样写成 Sobol 全局敏感性分析。
