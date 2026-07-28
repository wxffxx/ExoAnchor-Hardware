# Waveshare ESP32-P4-NANO DIY 装配指南

本方案用 Waveshare ESP32-P4-NANO、外置 HDMI USB 采集卡和四根 USB 2.0 线完成基础 KVM，不需要自定义 PCB 或焊接。

## 能力边界

完成后具备 HDMI 视频采集、USB 键鼠控制和有线网络访问；不具备 ATX 电源/复位控制，也不能检测 12V 或 3V3AUX。需要远程开机时，应在被控主机上配置 Wake-on-LAN，或另行增加受控电源硬件。

## 准备

- Waveshare ESP32-P4-NANO
- MS2109 类 HDMI USB 采集卡
- HDMI 线和网线
- 能引出 5V、GND、D+、D- 的 USB 2.0 线
- 用于烧录和日志的 USB-C 数据线
- 已安装 ESP-IDF 5.4.x 的 macOS、Windows 或 Linux 主机

不要使用只有电源线芯的 USB 线。当前验证路径也不建议使用 MS2109S 采集卡。

## 接线

1. 将采集卡插入 ESP32-P4-NANO 的 USB-A host 口。
2. 将被控主机 HDMI 输出接到采集卡 HDMI 输入。
3. 将 NANO 的 RJ45 接入有 DHCP 的局域网。
4. 按下表连接被控主机 USB HID：

| USB 信号 | ESP32-P4-NANO |
| --- | --- |
| D+，通常为绿色 | GPIO27 |
| D-，通常为白色 | GPIO26 |
| 5V，通常为红色 | 5V |
| GND，通常为黑色 | GND |

5. 将 HID 线的 USB-A 端插入被控主机。
6. 用 USB-C 数据线连接 NANO 与烧录主机。

上电前必须确认 5V 没有误接到 3V3，并确认双方共地。D+/D- 接反通常不会损坏开发板，但 HID 无法枚举。

## 构建与烧录

固件使用主仓库中的开发版共享工程和 `waveshare-p4-nano + esp32p4-rev1` 配置。项目没有 PlatformIO 配置，必须使用 ESP-IDF：

```bash
git clone https://github.com/wxffxx/ExoAnchor.git
cd ExoAnchor/device/ESP32P4/firmware/v0.86.6-dev
. "$HOME/esp/esp-idf-v5.4/export.sh"
idf.py \
  -B build-waveshare-p4-nano \
  -D SDKCONFIG=build-waveshare-p4-nano/sdkconfig \
  -D "SDKCONFIG_DEFAULTS=sdkconfig.defaults;configs/boards/sdkconfig.defaults.waveshare-p4-nano;configs/silicon/sdkconfig.defaults.esp32p4-rev1" \
  set-target esp32p4
idf.py -B build-waveshare-p4-nano build
./tools/flash-monitor.sh <PORT> \
  --build-dir build-waveshare-p4-nano \
  --wait-ip \
  --exit-on-ip
```

如果已经有主仓库，跳过 `git clone` 并直接进入对应目录。用系统显示的实际串口替换 `<PORT>`；CH343 设备不一定使用 `cu.usbmodem*` 名称。

无法自动进入下载模式时，按住 BOOT，短按 RESET，再松开 BOOT，然后重新烧录。

## 验收

按顺序确认：

1. 串口没有持续重启、panic 或 USB 初始化失败。
2. Ethernet 已获取 DHCP 地址。
3. 能通过设备地址打开 Web UI。
4. KVM 页面能显示 HDMI 画面。
5. 键盘与鼠标输入能作用到被控主机。

没有完成以上各项时，不要把单独的编译成功视为整机验证。

## 常见问题

### 找不到串口

- 确认 USB-C 是数据线，并确认系统已识别 CH343。
- 必要时安装对应驱动，再重新插拔。
- 手动进入下载模式后重试。

### 键盘鼠标不可用

- 检查 D+→GPIO27、D-→GPIO26。
- 检查 5V、GND 和共地。
- 在被控主机中确认是否枚举出 USB HID。

### 网络不可用

- 检查网线、交换机端口与 DHCP。
- 不要把 Wake-on-LAN 配置问题误判为开发板 ATX 能力。

烧录完成后，如果被控主机的 USB 5V 能稳定供电，USB-C 可只在升级或排查日志时接回。

## 许可证

本指南中的 ExoAnchor 原创内容采用仓库根目录的
[MIT License](../../../LICENSE)。Waveshare、MS2109 等第三方产品及资料仍遵循
各自条款。
