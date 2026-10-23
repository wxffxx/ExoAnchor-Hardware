# ESP32-P4 硬件

[English](README.md)

本目录按板型和硬件资料用途组织：

| 目录 | 内容 | 使用边界 |
| --- | --- | --- |
| [`exoanchor-p4-v2.4a6/`](exoanchor-p4-v2.4a6/) | V2.4A6 的 JLCEDA 与 KiCad 独立工程 | 转换已核对；制造签核待完成 |
| [`exoanchor-p4-v2.3b4/`](exoanchor-p4-v2.3b4/) | 四层 V2.3B4 的 JLCEDA 与 KiCad 独立工程 | 历史版本；转换已核对；制造签核待完成 |
| [`exoanchor-p4-v2.3b6/`](exoanchor-p4-v2.3b6/) | 六层 V2.3B6 的 JLCEDA 与 KiCad 独立工程 | 历史版本；转换已核对；制造签核待完成 |
| [`simple-diy/`](simple-diy/) | 可复刻的简易 DIY 开发板方案与扩展板 | 用于复刻、验证和对照，不代表自研主线 |
| [`archive/`](archive/) | 不再参与新设计的历史资料 | 只用于追溯，不能作为打样、生产或固件配置输入 |

自研板主线为 `exoanchor-p4-v2.4a6/`，两种 V2.3 板型分别保留为独立历史工程。
各工程 README 提供嘉立创、KiCad 入口、来源、转换检查与剩余 ERC/DRC 问题。
板型对应的固件
profile、芯片版本和真机验证状态以主仓库的
[板型实现矩阵](https://github.com/wxffxx/ExoAnchor/blob/main/device/ESP32P4/boards/IMPLEMENTATION_PROFILES_zh.md)
为准。
