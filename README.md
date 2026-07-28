# ExoAnchor Hardware

[中文](README_zh.md)

This repository contains ExoAnchor hardware design outputs and hardware-specific instructions. Firmware, system architecture, and board capability truth live in the main [ExoAnchor repository](https://github.com/wxffxx/ExoAnchor).

## Current contents

| Path | Role |
| --- | --- |
| `ESP32P4/exoanchor-p4-v2.4a6/` | ⏳ Current custom ExoAnchor P4 V2.4a6, pending publication |
| [`ESP32P4/simple-diy/`](ESP32P4/simple-diy/) | Waveshare simple DIY designs and expansion board |
| [`ESP32P4/archive/`](ESP32P4/archive/) | Historical material no longer used by new designs |
| `assets/brand/` | Brand geometry for PCB silkscreen |
| `ArmLinux/CM4_CH552/`, `ESP32S31/` | Reserved platform directories, not delivered designs |

A directory, netlist, or production output does not imply validated or production-ready hardware. A capability requires an identified revision, firmware profile, and corresponding hardware evidence.

Chinese documentation is authoritative. English README files are synchronized
mirrors; resolve differences from `_zh.md`.

## License

Original ExoAnchor software, firmware and documentation are licensed under the
[MIT License](LICENSE). Original hardware designs use the same policy, including
permission to manufacture and sell hardware from covered design files.

Unless a file says otherwise, this license covers all original materials that
the ExoAnchor contributors have the right to license, including schematics,
PCB and CAD source projects, BOMs, netlists, mechanical models, manufacturing
materials, and project documentation. Copies or substantial portions must
retain the copyright and permission notice from `LICENSE`. Third-party products
and materials retain their own terms; the MIT License does not grant rights to
ExoAnchor trademarks or third-party material.
