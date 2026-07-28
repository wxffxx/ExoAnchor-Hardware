# Waveshare ESP32-P4-NANO DIY

[English](README.md) · [装配指南](BuildGuide.md)

这是 ExoAnchor ESP32-P4 最快的 KVM 验证方案：直接使用 Waveshare ESP32-P4-NANO、MS2109 类 HDMI USB 采集卡、有线网络和四根 USB 2.0 HID 线，不需要自定义 PCB。

| 功能 | 状态 |
| --- | --- |
| UVC 视频 | 支持，使用 USB-A 高速 host 口 |
| USB HID | 支持，GPIO26(D-) / GPIO27(D+) |
| Ethernet | 支持，使用 NANO RJ45/IP101GRI |
| Web 控制台 | 由共享固件提供 |
| ATX 电源/复位 | 不支持 |
| 12V / 3V3AUX 检测 | 不支持 |

需要远程开机时，应在被控主机上配置 Wake-on-LAN，或另行增加电源控制硬件。

## 连接摘要

| 连接 | 目标 |
| --- | --- |
| MS2109 USB | NANO USB-A host |
| 被控主机 HDMI | MS2109 HDMI 输入 |
| Ethernet | 有 DHCP 的局域网 |
| USB HID D+ / D- | GPIO27 / GPIO26 |
| USB HID 5V / GND | 5V / GND |
| USB-C | 初始化烧录与串口调试 |

上电前必须确认被控主机 USB 5V 没有接到 3V3。当前验证路径不建议使用 MS2109S。

本实现使用开发固件的 `waveshare-p4-nano + esp32p4-rev1` 配置；准确命令、安全检查与验收步骤见[装配指南](BuildGuide.md)。固件入口位于[主 ExoAnchor 仓库](https://github.com/wxffxx/ExoAnchor/tree/main/device/ESP32P4/firmware)。

## 许可证

本目录中的 ExoAnchor 原创文档采用仓库根目录的
[MIT License](../../../LICENSE)；第三方产品仍遵循各自条款。
