# ESP32-P4 历史硬件资料

状态：历史追溯，不是活动设计输入

最后整理日期：2026-07-29

本目录按硬件修订版或设计快照保存不再作为当前输入的历史资料，包括已淘汰的
ExoAnchor P4 修订版、当前修订版的旧导出，以及简易 DIY 方案的旧导出。每组资料
使用独立子目录，后续收到的原理图、PCB、BOM 或其他文件应归入对应版本或快照，
而不是按文件格式集中存放。当前 ExoAnchor P4 设计为
`../exoanchor-p4-v2.4a6/`，尚未公开。

## ExoAnchor P4 归档

历史网表的文件名已经规范化为
`Netlist_SCH_ESP32P4_Prototype_<版本>_<日期>.net`；重命名不改变文件内容。

| 来源标签 | 归档目录 | 当前资料 | 大小 | SHA-256 |
| --- | --- | --- | ---: | --- |
| V0 | [`exoanchor-p4-v0/`](exoanchor-p4-v0/) | [`Netlist_SCH_ESP32P4_Prototype_V0_2026-07-26.net`](exoanchor-p4-v0/Netlist_SCH_ESP32P4_Prototype_V0_2026-07-26.net) | 189,046 | `a4954adaebef238132060bf58cb97955f9e143317d1aa0b368beedefb3b9e854` |
| V1 | [`exoanchor-p4-v1/`](exoanchor-p4-v1/) | [`Netlist_SCH_ESP32P4_Prototype_V1_2026-07-26.net`](exoanchor-p4-v1/Netlist_SCH_ESP32P4_Prototype_V1_2026-07-26.net) | 216,723 | `b35b51ecb41967ef891c05e3475f929eb94a3540fa1963fd0e911e15f723ee17` |
| V2 | [`exoanchor-p4-v2/`](exoanchor-p4-v2/) | [`Netlist_SCH_ESP32P4_Prototype_V2_2026-07-26.net`](exoanchor-p4-v2/Netlist_SCH_ESP32P4_Prototype_V2_2026-07-26.net) | 189,359 | `389203b29fa8f2f25757d24086547d930a926b635bd014a009c164319b82e592` |
| V2.1 | [`exoanchor-p4-v2.1/`](exoanchor-p4-v2.1/) | [`Netlist_SCH_ESP32P4_Prototype_V2.1_2026-07-26.net`](exoanchor-p4-v2.1/Netlist_SCH_ESP32P4_Prototype_V2.1_2026-07-26.net) | 189,611 | `c35fd8c57d1308617186735d15b8d2b9188f910ac61c24b6434585435cc96f75` |
| V2.1b | [`exoanchor-p4-v2.1b/`](exoanchor-p4-v2.1b/) | [`Netlist_SCH_ESP32P4_Prototype_V2.1b_2026-07-26.net`](exoanchor-p4-v2.1b/Netlist_SCH_ESP32P4_Prototype_V2.1b_2026-07-26.net) | 183,798 | `a474080aee7a09a4d9c43ef9c99ae0bc6784c3ff5f92f2d29c895862406a51e2` |
| V2.3b6 | [`exoanchor-p4-v2.3b6/`](exoanchor-p4-v2.3b6/) | [`Netlist_SCH_ESP32P4_Prototype_V2.3b6_2026-07-26.net`](exoanchor-p4-v2.3b6/Netlist_SCH_ESP32P4_Prototype_V2.3b6_2026-07-26.net) | 196,008 | `1e95a1a1416dab73239264a79f8220cb309c9b48a8eeb20dd4082ad33f069737` |
| V2.4a6（旧导出） | [`exoanchor-p4-v2.4a6/`](exoanchor-p4-v2.4a6/) | [`BOM_ESP32P4_Prototype_V2.4a6_SCH_ESP32P4_Prototype_V2.4a6_2026-07-28.csv`](exoanchor-p4-v2.4a6/BOM_ESP32P4_Prototype_V2.4a6_SCH_ESP32P4_Prototype_V2.4a6_2026-07-28.csv) | 9,250 | `c6df4d98c0e0a2949c55c13cd5d9270e1a8a316bffe0274bf887abf804005d22` |

收到的两份 V2.3b6 文件逐字节相同，因此只保留一份。

## Waveshare NANO 扩展板旧导出

2026-06-27 设计输出已被当前
[2026-07-29 设计资料](../simple-diy/waveshare-nano-expansion/)
替代。

| 归档目录 | 资料 | 大小 | SHA-256 |
| --- | --- | ---: | --- |
| [`waveshare-nano-expansion-2026-06-27/`](waveshare-nano-expansion-2026-06-27/) | [`BOM_P4exp_Board_2026-06-27.csv`](waveshare-nano-expansion-2026-06-27/BOM_P4exp_Board_2026-06-27.csv) | 511 | `0e39be56ede3182ef628a6b4cb88f24a49e1036d0afe4dffb71aae3efe5568cc` |
| [`waveshare-nano-expansion-2026-06-27/`](waveshare-nano-expansion-2026-06-27/) | [`PADS_P4exp_Board_2026-06-27.zip`](waveshare-nano-expansion-2026-06-27/PADS_P4exp_Board_2026-06-27.zip) | 24,155 | `b0d66a50065c83a33585da69a7972fffca8b49fd4f8e59a8a3439f1cfe85c24e` |
| [`waveshare-nano-expansion-2026-06-27/`](waveshare-nano-expansion-2026-06-27/) | [`Schematic_P4exp_Board_2026-06-27.pdf`](waveshare-nano-expansion-2026-06-27/Schematic_P4exp_Board_2026-06-27.pdf) | 658,228 | `c012a6e210c3d973ca55530643d3e45720da01039bb0459f75d85621155b85af` |

## 历史变化摘要

| 标签 | 相对上一标签的主要变化 |
| --- | --- |
| V0 | 形成 Ethernet、TF、HDMI/UVC、USB HID、ATX 与电源状态基线 |
| V1 | 增加 USB 3.0、第二 Ethernet 和 PCIe 实验路径；调整 HID、调试与电源实现 |
| V2 | 移除 USB 3.0 实验电路；增加 eMMC 与第二路 USB-UART；Ethernet 收敛 |
| V2.1 | 整理单路 Ethernet 与调试串口，没有核心功能增删 |
| V2.1b | 移除 eMMC，恢复 TF 与卡检测；与 2026-07-14 的 V2.1b 逐字节相同 |
| V2.3b6 | 增加次级 SPI 存储、定位/状态和维护接口，保留双 USB-UART、TF、KVM 与 ATX 路径 |

## 使用规则

- `archive/.gitattributes` 将所有子目录中的 `.net` 标记为 binary，避免 Git
  改写封存文件。
- 同名资料必须先比对 SHA-256；新导出不能覆盖归档。
- 本归档 V2.3b6 的 SHA-256 与当前固件映射来源不同，不能替换主仓库记录的 `2026-07-25.tel`。
