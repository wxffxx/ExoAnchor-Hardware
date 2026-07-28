# Waveshare NANO Simple Expansion Board

[中文](README_zh.md)

This implementation combines a Waveshare ESP32-P4-NANO with the simple
expansion-board design materials dated 2026-07-29. It sits between direct DIY
wiring and a full custom board.

| Feature | Status |
| --- | --- |
| UVC video | Uses the NANO high-speed USB host |
| USB HID | Uses NANO GPIO26(D-) / GPIO27(D+) |
| Ethernet | Uses NANO RJ45/IP101GRI |
| ATX power control | Present in expansion-board design materials, but no independent firmware profile or hardware-validated capability exists |
| 12V sensing | May be claimed only after actual assembly, wiring, and validation |
| 3V3AUX sensing | Not available on the current expansion board |

There is no `waveshare-nano-expansion` firmware overlay. The base build still uses `waveshare-p4-nano + esp32p4-rev1`. Until GPIOs, polarity, and hardware acceptance are complete, reserved expansion interfaces must not be advertised as firmware power capabilities.

## Current design materials

| Material | File |
| --- | --- |
| Schematic PDF | [`Schematic_P4exp_Board_2026-07-29.pdf`](Schematic_P4exp_Board_2026-07-29.pdf) |
| BOM | [`BOM_P4exp_Board_2026-07-29.csv`](BOM_P4exp_Board_2026-07-29.csv) |
| Protel 2.0 netlist | [`Netlist_P4exp_Board_2026-07-29.net`](Netlist_P4exp_Board_2026-07-29.net) |
| Editable PADS project | [`PADS_P4exp_Board_2026-07-29.zip`](PADS_P4exp_Board_2026-07-29.zip) |
| Editable Altium Designer project | [`Altium_P4exp_Board_2026-07-29.zip`](Altium_P4exp_Board_2026-07-29.zip) |

SHA-256:

- Schematic PDF: `7a5c945d9531abc44d430904f8e7a60036c5b5088ae6e32079de86db953c8531`
- BOM: `aa7df051e909764933a54336b64b8547ce8f0c65c73e104cf613ff87cdf80e4a`
- Netlist: `95d57b1b5f3bd710142c1b7a807a51297bca06a7cf4909529d7961b61f54cd55`
- PADS: `0f240734144123e3cbc75f2202f2d38558cafa21bf457db24a166093a935351b`
- Altium Designer: `657b0a082d1715dda86cf20e6cc7cb769afbbc3af53908a8013a795fb5dfa3a6`

These files are design outputs dated 2026-07-29; they do not by themselves
indicate a validated or production-ready revision. Firmware lives in the
[main ExoAnchor repository](https://github.com/wxffxx/ExoAnchor/tree/main/device/ESP32P4/firmware).

## License

Original ExoAnchor expansion-board materials use the repository's
[MIT License](../../../LICENSE), including permission to manufacture and sell
hardware based on them. Third-party products retain their own terms.
