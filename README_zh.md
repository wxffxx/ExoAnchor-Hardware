# ExoAnchor Hardware

[English](README.md)

本仓库保存 ExoAnchor 的硬件设计输出与硬件专用说明；固件、系统架构和板型能力事实位于主 [ExoAnchor 仓库](https://github.com/wxffxx/ExoAnchor)。

## 当前内容

| 路径 | 定位 |
| --- | --- |
| `ESP32P4/exoanchor-p4-v2.4a6/` | ⏳ 当前自研 ExoAnchor P4 V2.4a6，待发布 |
| [`ESP32P4/simple-diy/`](ESP32P4/simple-diy/) | Waveshare 简易 DIY 方案与扩展板 |
| [`ESP32P4/archive/`](ESP32P4/archive/) | 不再参与新设计的历史资料 |
| `assets/brand/` | PCB 丝印用品牌图形 |
| `ArmLinux/CM4_CH552/`、`ESP32S31/` | 预留平台目录，不代表已有可交付设计 |

目录、网表或生产输出文件的存在不代表硬件已经验证或可量产。具体能力必须同时有明确修订版、固件 profile 和对应真机证据。

中文文档是事实源；英文 README 只作同步镜像，发生差异时以 `_zh.md` 为准。

## 许可证

ExoAnchor 原创软件、固件和文档采用 [MIT License](LICENSE)。原创硬件设计也采用
MIT，包括依据授权范围内设计文件制造和销售硬件的许可。

除非具体文件另有声明，本许可适用于 ExoAnchor 贡献者有权授权的全部原创资料，
包括原理图、PCB 与 CAD 源工程、BOM、网表、结构模型、生产资料和项目文档。
复制或实质性使用时须保留 `LICENSE` 中的版权与许可声明。第三方产品和资料仍遵循
各自条款；MIT License 不授予 ExoAnchor 商标或第三方权利。
