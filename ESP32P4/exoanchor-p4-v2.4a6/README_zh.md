# ExoAnchor P4 V2.4A6 独立工程

[English](README.md)

整理日期：2026-10-22。板卡标识为 `ESP32P4_Prototype_V2.4a6`，PCB 丝印为 `Prototype V2.4A6`。

本目录只包含该板及其依赖。嘉立创原生设计从现有本地归档提取；KiCad 版为完成针对性修复和网络核对的转换工程。未从云端同步更新。

## 打开工程

| 格式 | 入口 | 使用方式 |
| --- | --- | --- |
| 嘉立创专业版原生导入包 | [JLCEDA/ExoAnchor_P4_V2.4A6.epro2](JLCEDA/ExoAnchor_P4_V2.4A6.epro2) | 在嘉立创 EDA 专业版中导入本地工程；已用全离线 V4.1.60 实际导入并打开 PCB |
| 嘉立创专业版目录工程 | [JLCEDA/ExoAnchor_P4_V2.4A6/ExoAnchor_P4_V2.4A6.eprj3](JLCEDA/ExoAnchor_P4_V2.4A6/ExoAnchor_P4_V2.4A6.eprj3) | 保留整个同名目录及其中的 `pcb/`、`sch/` 后打开 |
| KiCad 工程 | [KiCad/ExoAnchor_P4_V2.4A6.kicad_pro](KiCad/ExoAnchor_P4_V2.4A6.kicad_pro) | 使用 KiCad Nightly 10.99，保留整个 `KiCad/` 目录 |
| KiCad 原理图 | [KiCad/ExoAnchor_P4_V2.4A6.kicad_sch](KiCad/ExoAnchor_P4_V2.4A6.kicad_sch) | 根页链接到 8 个子页 |
| KiCad PCB | [KiCad/ExoAnchor_P4_V2.4A6.kicad_pcb](KiCad/ExoAnchor_P4_V2.4A6.kicad_pcb) | 六层 PCB，含布线、过孔和铜区 |

KiCad 文件由本机 `10.99.0-1556-g74ef325b2f` 导入和验证，使用开发版文件格式。未验证 KiCad 9/10 稳定版兼容性。符号库、38 个封装文件及库表均随目录提供；库表采用 `${KIPRJMOD}` 相对路径。已用移到另一临时目录的副本导出网表，确认连接集合一致。

源文件的 3D 模型引用仍保留，实际 STEP/WRL 几何没有随包收集；不保证 3D 视图完整。

## 内容与检查结果

| 项目 | 结果 |
| --- | --- |
| 板卡 / 原理图 | 1 块板，8 个设计页，另有 1 个 KiCad 导航根页 |
| 页面 | P1、ETH、P4、HDMI_Captrue_MS2109、USB_UART/Other IO、Power、PCIe、TF |
| 器件 | 原始 PCB、KiCad PCB、KiCad 原理图均为 190 个，位号集合一致 |
| 器件焊盘 | 772 个逐项核对，编号集合和网络名称均一致 |
| 网络连接 | 154 组非空网络，器件引脚连接集合全部一致；允许软件间网络显示名称不同 |
| 位置 | 按导入坐标平移对齐后，未发现超过 1 μm 的器件位置偏差 |
| PCB | 6 个铜层、1,894 条直线走线、25 条弧线走线、406 个过孔 |
| 自由焊盘 | KiCad 额外采用 5 个封装容器承载原 PCB 自由焊盘，因此总封装对象为 195 个 |
| 嘉立创提取 | 193 个设计、库及支持文档保持源归档字节内容，另 1 个配置文档更新默认打开的板；移除 190 个未使用缩略图 |

[完整网络核对结果](validation/parity.json)、[原生文档校验](validation/native-source-verification.json)、[原生应用打开记录](validation/native-open.json)、[搬迁验证](validation/portability.json)。

## 转换修复

KiCad 中完成了以下转换处理，嘉立创原生设计文档保持源数据：

- 提取该板依赖的封装，修正导入器把 SMD 焊盘变成微小通孔的情况，并恢复元件与 PCB 的关联。
- 将源工程允许跨页连接的网络标签映射为 KiCad 全局标签，恢复源短接符号的导线连接语义。
- 依据 V3 原生 PCIe 页的 14 组独立导线、原 PCB 焊盘网络及 7 月历史网表，修复 V2 兼容导出造成的 GND、3V3AUX、WAKE# 错误合并。`U12.B10` 为 3V3AUX，`U12.B11` 为 WAKE#。
- 按源路径恢复正反面 R 字形铜图案的连续轮廓，用 2° 最大角步长离散圆弧。
- 整理本地符号/封装引用，为电源符号补齐唯一标号；原理图统一平移到栅格位置，不改变连接关系。保留源图框、文字与布局。

V3 与 V2 的 PCB 器件、焊盘网络、器件位置一致。V2 导出省略 4 条零长度线和 2 条长度约 0.0002794 mm 的线段；因此这里不宣称跨格式几何逐字节完全一致。详见 `validation/` 的转换记录。

## 尚未签核的项目

本交付完成的是独立工程整理与转换核对，尚未完成投板签核。

- KiCad DRC：1,457 项，其中 1,327 个 error、130 个 warning；报告中的未连接项目为 0，未报告 shorting_items 或 padstack 无效项。仍有间距、线宽、过孔尺寸/环宽、热焊盘、边缘及丝印等问题待审查。
- KiCad ERC：767 项，包含符号引脚类型冲突、库与嵌入符号差异、未驱动引脚、悬空线端等。没有通过关闭规则或豁免来消除报告。
- 检查使用 KiCad 默认/导入规则；嘉立创原始规则与层叠制造参数没有完成逐项迁移。告警是否来自原设计、规则差异或剩余转换偏差，仍需逐项确认。
- 嘉立创原生 ERC/DRC、实际打样、装配、上电及接口功能均未在此次整理中验证。

详见 [检查汇总](validation/rules-summary.json)、[PCB DRC](validation/pcb-drc.json)、[原理图 ERC](validation/sch-erc.json)。

## 来源与目录

| 目录 | 内容 |
| --- | --- |
| `JLCEDA/` | 嘉立创原生 `.epro2` 和可编辑目录工程 `.eprj3` |
| `KiCad/` | 工程、原理图、PCB、本地符号和封装 |
| `preview/` | PCB 顶/底层 SVG/PNG，原理图 SVG 和总览；用于浏览，不是制造文件 |
| `reference/` | 2026-07-29 历史 BOM、原理图 PDF、网表及 Altium/PADS 导出；另存未修改的 V2 转换来源 |
| `validation/` | 提取来源、哈希、连接核对、检查报告及转换记录 |
| `scripts/` | 网络和器件位置核对脚本 |

原生来源为 `hardware-reserve/lceda-2026-10-01/source/ProPrj_ExoAnchor-ESP32P4_2026-09-30.epro2`；KiCad 初始转换使用 `ProPrj_ExoAnchor-ESP32P4_2026-10-19.epro`，随后按原生证据修复。完整源哈希见 `validation/extraction-v3.json` 和 `validation/extraction.json`。这些路径只记录来源，打开交付工程无需依赖原工作区。

`reference/V2_compatibility_export_as_received.epro` 是保留已知 PCIe 兼容导出问题的审计原件，**不要用它作为当前设计入口**。JLC 工程请使用上面的 `.epro2` 或 `.eprj3`。

历史参考资料从硬件仓库本地分支 `codex/p4-v2.4a6-archive-20261022`、提交 `96cf71e` 下的 `ESP32P4/exoanchor-p4-v2.4a6/` 提取。它们是历史记录，未认定为当前制造资料。`LICENSE` 沿用硬件仓库的 MIT 许可；第三方器件库的原有标识和属性保留。

## 重新核对

在本目录执行，先用支持当前格式的 `kicad-cli` 重新导出网表，再执行比较：

```sh
kicad-cli sch export netlist --format kicadxml -o validation/kicad-netlist.xml KiCad/ExoAnchor_P4_V2.4A6.kicad_sch
python3 scripts/verify_conversion.py
```

脚本相对本目录工作，检查不通过会返回非零退出码。它只验证器件、焊盘网络、网络连接集合和器件位置；不替代 ERC/DRC、制造审查或实物验证。`SHA256SUMS.txt` 记录交付时文件哈希。
