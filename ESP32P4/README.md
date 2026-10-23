# ESP32-P4 Hardware

[中文](README_zh.md)

This directory separates hardware material by purpose:

| Directory | Contents | Boundary |
| --- | --- | --- |
| [`exoanchor-p4-v2.4a6/`](exoanchor-p4-v2.4a6/) | V2.4A6 standalone JLCEDA and KiCad projects | Conversion checked; manufacturing signoff pending |
| [`exoanchor-p4-v2.3b4/`](exoanchor-p4-v2.3b4/) | Four-layer V2.3B4 standalone JLCEDA and KiCad projects | Historical revision; conversion checked; manufacturing signoff pending |
| [`exoanchor-p4-v2.3b6/`](exoanchor-p4-v2.3b6/) | Six-layer V2.3B6 standalone JLCEDA and KiCad projects | Historical revision; conversion checked; manufacturing signoff pending |
| [`simple-diy/`](simple-diy/) | Reproducible simple DIY development-board designs and expansion boards | Used for reproduction, validation, and comparison; not the custom-board mainline |
| [`archive/`](archive/) | Historical material no longer used by new designs | Traceability only; never an input to fabrication, production, or firmware configuration |

The custom-board mainline is `exoanchor-p4-v2.4a6/`. The two V2.3 variants
are separate historical projects. Each project README identifies its native
JLCEDA and KiCad entry points, source archives, conversion checks, and remaining
ERC/DRC findings. Use the main repository's
[implementation matrix](https://github.com/wxffxx/ExoAnchor/blob/main/device/ESP32P4/boards/IMPLEMENTATION_PROFILES_zh.md)
for firmware profiles, chip revisions, and hardware-validation status.
