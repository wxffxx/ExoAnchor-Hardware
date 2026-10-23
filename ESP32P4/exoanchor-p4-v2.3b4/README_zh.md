# ExoAnchor P4 V2.3B4 独立工程

[English](README.md)

整理日期：2026-10-22。本工程从现有本地归档中提取 `ESP32P4_Prototype_V2.3b4layers_260724封存（已验证）`，提供独立的嘉立创 EDA 与 KiCad 工程。包含原理图、PCB 和依赖库；没有同步当前云端工程。

源工程的原理图名称沿用了 `SCH_ESP32P4_Prototype_V2.3b6_1`，但所绑定的板、PCB 丝印和四个铜层均属于 **V2.3b4**。保留该历史名称；不能仅凭原理图名称判定版本。源板名称中的“已验证”是历史标注，本次没有重做实物验证。

## 打开工程

| 格式 | 入口 | 说明 |
| --- | --- | --- |
| 嘉立创原生导入包 | [ExoAnchor_P4_V2.3B4.epro2](JLCEDA/ExoAnchor_P4_V2.3B4.epro2) | 在嘉立创 EDA 专业版中导入；已在全离线 V4.1.60 成功导入并打开 PCB |
| 嘉立创文件夹工程 | [ExoAnchor_P4_V2.3B4.eprj3](JLCEDA/ExoAnchor_P4_V2.3B4/ExoAnchor_P4_V2.3B4.eprj3) | 原生软件生成；须保留同目录的 `pcb/`、`sch/` 等文件 |
| KiCad 工程 | [ExoAnchor_P4_V2.3B4.kicad_pro](KiCad/ExoAnchor_P4_V2.3B4.kicad_pro) | 保留完整 `KiCad/` 目录 |
| KiCad 原理图 | [ExoAnchor_P4_V2.3B4.kicad_sch](KiCad/ExoAnchor_P4_V2.3B4.kicad_sch) | 导航根页加八张设计图页 |
| KiCad PCB | [ExoAnchor_P4_V2.3B4.kicad_pcb](KiCad/ExoAnchor_P4_V2.3B4.kicad_pcb) | 4 个铜层，保留布线、过孔和铜区 |

导入与检查使用 **KiCad Nightly 10.99.0-1556-g74ef325b2f**；没有验证稳定版 KiCad 9/10 的兼容性。工程内包含符号库、38 个本地封装及 `${KIPRJMOD}` 相对路径库表；仅复制 `KiCad/` 到另一临时目录后，重新导出的网表仍完全一致。

源 3D 模型引用被保留，但未附带 STEP/WRL 几何文件，不保证完整离线 3D 显示。

## 提取与转换核对

| 项目 | 结果 |
| --- | --- |
| 设计范围 | 1 块板、8 张有效设计图页；KiCad 另有导航根页 |
| 图页 | P1、USB_UART/Other IO、ETH、P4、HDMI_Captrue_MS2109、Power、PCIe、TF |
| 实体器件 | 源 PCB、KiCad PCB 和 KiCad 原理图均为 185 个，位号集合一致 |
| 器件焊盘 | 753 个，编号集合与网络名称逐一匹配 |
| 网络连接 | 149 / 149 个非空源网络的端点集合匹配；软件中的显示名称可能不同 |
| 器件位置 | 扣除导入坐标平移后，没有超过 1 微米的位置差异 |
| PCB 对象 | 4 个铜层、1902 段直线走线、25 段弧形走线、401 个过孔 |
| 自由焊盘 | 另外使用 5 个 KiCad 封装容器承载，因此 PCB 中共 190 个封装对象 |
| 原生完整性 | 220 个设计、库及支持文档与源包字节一致；配置仅调整默认打开的 PCB |

相关记录：[转换核对](validation/parity.json)、[原生源校验](validation/native-source-verification.json)、[原生软件打开检查](validation/native-open.json)、[目录迁移检查](validation/portability.json)。

KiCad 转换做了以下修复，嘉立创原生设计文档保持源数据：

- 提取依赖封装，将误导入为微型通孔的 SMD 焊盘恢复为 SMD，并恢复原理图与 PCB 的 185 个器件关联。
- 将源工程跨页网络标签转为 KiCad 全局标签，恢复短路符号的导线语义，补齐电源符号唯一位号和本地库默认关联。
- 依据原生 V3 原理图与 PCB 焊盘网络，恢复 PCIe 的 16 组独立导线；修正 V2 兼容导出将 GND、3V3AUX、WAKE# 错误合并的问题。`U12.B10` 为 3V3AUX，`U12.B11` 为 WAKE#。
- 从原生路径重建正反面 R 形铜图案，圆弧按最大 2° 步长采样；原有图框、文字和布局保留，包括源布局中的图框重叠。

四层版的 V2 兼容导出还漏掉一段 0.00166624 mm 的 `P4_VDDO1_FLASH` 顶层走线，已根据原生 V3 记录补回。 两版各有四段零长度原生线记录未转入 KiCad。参见 [直线走线核对](validation/native-track-comparison.json)。跨格式几何不宣称逐字节相同。

## 检查边界

这是工程提取与转换交付，尚未完成制造签核：

- KiCad DRC：**1504 项**（1312 个错误、192 个警告），报告中未连接项为 0，未报告 `shorting_items` 或 `invalid_padstack`。间距、线宽、孔径、环宽、热焊盘、板边、丝印等问题仍需审阅。
- KiCad ERC：**777 项**，涉及引脚类型冲突、未驱动引脚、库符号差异、悬空端点等。没有关闭规则或豁免检查来清空报告。
- 检查使用 KiCad 默认／导入规则；尚未完整映射原嘉立创规则与制造叠层参数。剩余问题需区分源设计、规则差异和转换差异。
- 本次未执行嘉立创原生 ERC/DRC、下单、制造、装配、上电或接口实测。

详见 [规则摘要](validation/rules-summary.json)、[DRC](validation/pcb-drc.json)、[ERC](validation/sch-erc.json)。

## 目录与来源

| 目录／文件 | 内容 |
| --- | --- |
| `JLCEDA/` | 原生 `.epro2` 与可编辑 `.eprj3` 文件夹工程 |
| `KiCad/` | 工程、原理图、PCB、本地符号和封装库 |
| `preview/` | PCB 正反面 SVG/PNG、原理图 SVG 和概览；用于浏览 |
| `reference/` | 保留已知 PCIe 问题的 V2 兼容导出原件 |
| `validation/` | 来源、哈希、转换修复、连接核对及规则报告 |
| `scripts/` | 可独立运行的器件、焊盘、网络和位置核对脚本 |
| `SHA256SUMS.txt` | 交付文件校验值 |

原生来源为 `hardware-reserve/lceda-2026-10-01/source/ProPrj_ExoAnchor-ESP32P4_2026-09-30.epro2`。KiCad 初始导入使用 `ProPrj_ExoAnchor-ESP32P4_2026-10-19.epro`，再依原生证据修复。完整源哈希与提取范围分别见 `validation/extraction-v3.json`、`validation/extraction.json`。这些路径仅记录来源；打开工程不依赖原工作区。

**`reference/V2_compatibility_export_as_received.epro` 仅供审计，不能作为当前工程入口。** 嘉立创请使用上表中的原生 `.epro2` 或 `.eprj3`。`LICENSE` 复制自硬件仓库的 MIT 许可证；保留第三方元件库标识与属性。

## 复查

在本目录使用兼容的 `kicad-cli` 导出新网表，再运行核对脚本：

```sh
kicad-cli sch export netlist --format kicadxml -o validation/kicad-netlist.xml KiCad/ExoAnchor_P4_V2.3B4.kicad_sch
python3 scripts/verify_conversion.py
```

脚本相对于自身目录定位工程，不匹配时以非零状态退出；不替代 ERC/DRC、制造审查或实物验证。
