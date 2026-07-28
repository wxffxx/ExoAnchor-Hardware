# Waveshare NANO 简易扩展板

[English](README.md)

该实现由 Waveshare ESP32-P4-NANO 与 2026-07-29 简易扩展板设计资料组成，
定位介于纯 DIY 直连和完整自研板之间。

| 功能 | 状态 |
| --- | --- |
| UVC 视频 | 使用 NANO 高速 USB host |
| USB HID | 使用 NANO GPIO26(D-) / GPIO27(D+) |
| Ethernet | 使用 NANO RJ45/IP101GRI |
| ATX 电源控制 | 扩展板有相关设计资料，尚未形成独立固件 profile 与真机能力结论 |
| 12V 检测 | 只有在实际装配、接线并验证后才能声明 |
| 3V3AUX 检测 | 当前扩展板不支持 |

当前固件没有 `waveshare-nano-expansion` 专用 overlay，基础构建仍使用 `waveshare-p4-nano + esp32p4-rev1`。在 GPIO、极性和真机验收完成前，不能因为扩展板预留接口就向固件声明电源能力。

## 当前设计资料

| 资料 | 文件 |
| --- | --- |
| 原理图 PDF | [`Schematic_P4exp_Board_2026-07-29.pdf`](Schematic_P4exp_Board_2026-07-29.pdf) |
| BOM | [`BOM_P4exp_Board_2026-07-29.csv`](BOM_P4exp_Board_2026-07-29.csv) |
| Protel 2.0 网表 | [`Netlist_P4exp_Board_2026-07-29.net`](Netlist_P4exp_Board_2026-07-29.net) |
| PADS 可编辑工程 | [`PADS_P4exp_Board_2026-07-29.zip`](PADS_P4exp_Board_2026-07-29.zip) |
| Altium Designer 可编辑工程 | [`Altium_P4exp_Board_2026-07-29.zip`](Altium_P4exp_Board_2026-07-29.zip) |

SHA-256：

- 原理图 PDF：`7a5c945d9531abc44d430904f8e7a60036c5b5088ae6e32079de86db953c8531`
- BOM：`aa7df051e909764933a54336b64b8547ce8f0c65c73e104cf613ff87cdf80e4a`
- 网表：`95d57b1b5f3bd710142c1b7a807a51297bca06a7cf4909529d7961b61f54cd55`
- PADS：`0f240734144123e3cbc75f2202f2d38558cafa21bf457db24a166093a935351b`
- Altium Designer：`657b0a082d1715dda86cf20e6cc7cb769afbbc3af53908a8013a795fb5dfa3a6`

这些文件是 2026-07-29 的设计输出，不等同于已验证或可量产版本。固件入口位于
[主 ExoAnchor 仓库](https://github.com/wxffxx/ExoAnchor/tree/main/device/ESP32P4/firmware)。

## 许可证

本目录中的 ExoAnchor 原创扩展板资料采用仓库根目录的
[MIT License](../../../LICENSE)，包括允许依据这些资料制造和销售硬件。
第三方产品仍遵循各自条款。
