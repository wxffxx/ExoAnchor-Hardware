# Waveshare ESP32-P4-NANO DIY

[中文](README_zh.md) · [Build guide (Chinese)](BuildGuide.md)

This is the fastest ExoAnchor ESP32-P4 KVM validation path. It uses a Waveshare ESP32-P4-NANO, an MS2109-class HDMI USB capture device, Ethernet, and four USB 2.0 HID wires without a custom PCB.

| Feature | Status |
| --- | --- |
| UVC video | Supported through the high-speed USB-A host port |
| USB HID | Supported on GPIO26(D-) / GPIO27(D+) |
| Ethernet | Supported through NANO RJ45/IP101GRI |
| Web console | Provided by the shared firmware |
| ATX power/reset | Not available |
| 12V / 3V3AUX sensing | Not available |

For remote boot, configure Wake-on-LAN on the target host or add separate power-control hardware.

## Connection summary

| Connection | Destination |
| --- | --- |
| MS2109 USB | NANO USB-A host |
| Target HDMI | MS2109 HDMI input |
| Ethernet | DHCP-enabled LAN |
| USB HID D+ / D- | GPIO27 / GPIO26 |
| USB HID 5V / GND | 5V / GND |
| USB-C | Initial flashing and serial diagnostics |

Before applying power, verify that target-host USB 5V is not connected to 3V3. MS2109S is not recommended for the currently verified path.

This implementation uses the development firmware's `waveshare-p4-nano + esp32p4-rev1` profile. See the [Chinese build guide](BuildGuide.md) for exact commands, safety checks, and acceptance steps. Firmware lives in the [main ExoAnchor repository](https://github.com/wxffxx/ExoAnchor/tree/main/device/ESP32P4/firmware).

## License

Original ExoAnchor documentation in this directory uses the repository's
[MIT License](../../../LICENSE); third-party products retain their own terms.
