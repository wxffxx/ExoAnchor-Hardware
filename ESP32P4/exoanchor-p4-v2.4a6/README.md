# ExoAnchor P4 V2.4A6 standalone project

[中文](README_zh.md)

Prepared on 2026-10-22. The board is named `ESP32P4_Prototype_V2.4a6`; its PCB silkscreen reads `Prototype V2.4A6`.

This directory contains that board and its dependencies. The JLCEDA project was extracted from existing local archives. The KiCad conversion includes targeted repairs and connectivity comparisons. No current cloud-project synchronization was performed. Chinese documentation is authoritative.

## Open the projects

| Format | Entry point | Instructions |
| --- | --- | --- |
| Native JLCEDA import archive | [ExoAnchor_P4_V2.4A6.epro2](JLCEDA/ExoAnchor_P4_V2.4A6.epro2) | Import as a local project in JLCEDA Pro; successfully imported and the PCB opened in offline V4.1.60 |
| Native JLCEDA folder project | [ExoAnchor_P4_V2.4A6.eprj3](JLCEDA/ExoAnchor_P4_V2.4A6/ExoAnchor_P4_V2.4A6.eprj3) | Keep the containing directory, including `pcb/` and `sch/`, together |
| KiCad project | [ExoAnchor_P4_V2.4A6.kicad_pro](KiCad/ExoAnchor_P4_V2.4A6.kicad_pro) | Use KiCad Nightly 10.99 and keep the entire `KiCad/` directory |
| KiCad schematic | [ExoAnchor_P4_V2.4A6.kicad_sch](KiCad/ExoAnchor_P4_V2.4A6.kicad_sch) | Navigation root with eight design sheets |
| KiCad PCB | [ExoAnchor_P4_V2.4A6.kicad_pcb](KiCad/ExoAnchor_P4_V2.4A6.kicad_pcb) | Six copper layers, tracks, vias, and copper zones |

Import and verification used `10.99.0-1556-g74ef325b2f`. These are development-version files; compatibility with stable KiCad 9/10 was not verified. Local symbols, 38 footprint files, and library tables are included. The tables use `${KIPRJMOD}` relative paths. A copy relocated to an unrelated temporary directory exported the same net endpoint sets.

Source 3D model references are retained, but STEP/WRL geometry is not bundled. A complete 3D view is not guaranteed.

## Contents and checks

| Item | Result |
| --- | --- |
| Design | One board, eight design sheets, and one additional KiCad navigation root |
| Sheets | P1, ETH, P4, HDMI_Captrue_MS2109, USB_UART/Other IO, Power, PCIe, TF |
| Components | 190 in the source PCB, KiCad PCB, and KiCad schematic; identical reference sets |
| Component pads | 772 checked; pad-number sets and net names match |
| Connectivity | All 154 nonempty source net endpoint sets match; display names may differ between applications |
| Placement | No component position difference above 1 micrometre after compensating for the import translation |
| PCB | Six copper layers, 1,894 straight tracks, 25 arc tracks, and 406 vias |
| Free pads | Five additional KiCad footprint containers hold native free pads, giving 195 footprint objects in total |
| Native extraction | 193 design, library, and support documents retain their source bytes; one configuration document changes the default board; 190 unused thumbnails were removed |

See the [parity report](validation/parity.json), [native document verification](validation/native-source-verification.json), [native application check](validation/native-open.json), and [relocation check](validation/portability.json).

## Conversion repairs

The following changes apply to the KiCad conversion. Native JLCEDA design documents retain their source data.

- Extracted dependent footprints, corrected SMD pads imported as tiny through-hole pads, and restored schematic-to-PCB component links.
- Mapped cross-sheet source net labels to KiCad global labels and restored the wire semantics of source short-circuit symbols.
- Restored 14 independent native V3 PCIe wire groups using the native schematic, unchanged PCB pad nets, and July netlist as evidence. This repairs incorrect GND/3V3AUX/WAKE# merging in the V2 compatibility export. `U12.B10` is 3V3AUX and `U12.B11` is WAKE#.
- Reconstructed continuous front/back R-shaped copper artwork from source paths, sampling arcs at a maximum step of 2 degrees.
- Relinked local symbol/footprint defaults, assigned unique power-symbol references, and translated schematic pages onto the grid without changing connectivity. Source frames, text, and layout are retained.

V3 and V2 PCB component references, pad nets, and component placements match. The V2 export omitted four zero-length lines and two approximately 0.0002794 mm line segments. Cross-format geometry is therefore not claimed to be byte-identical. Detailed records are in `validation/`.

## Outstanding signoff

This delivery completes project extraction and conversion checks. It does not establish manufacturing readiness.

- KiCad DRC: 1,457 items, comprising 1,327 errors and 130 warnings. There are zero reported unconnected items and no reported shorting or invalid-padstack items. Clearance, track width, via dimensions/annular rings, thermals, board edges, silkscreen, and other findings remain to be reviewed.
- KiCad ERC: 767 items, including pin-type conflicts, cached/library symbol differences, undriven pins, and dangling wire endpoints. Rules were not disabled and findings were not waived to clear these reports.
- Checks use KiCad default/imported rules. Original JLCEDA rules and manufacturing stackup parameters have not been exhaustively mapped. Each remaining finding still needs attribution to the source design, rule differences, or residual conversion differences.
- Native JLCEDA ERC/DRC, fabrication, assembly, power-on, and functional interface testing were not performed during this extraction.

See the [rules summary](validation/rules-summary.json), [PCB DRC](validation/pcb-drc.json), and [schematic ERC](validation/sch-erc.json).

## Provenance and directory layout

| Directory | Contents |
| --- | --- |
| `JLCEDA/` | Native `.epro2` archive and editable `.eprj3` folder project |
| `KiCad/` | Project, schematics, PCB, local symbols, and footprints |
| `preview/` | Top/bottom PCB SVG/PNG, schematic SVG pages, and overview; browsing aids, not manufacturing files |
| `reference/` | Historical 2026-07-29 BOM, schematic PDF, netlist, Altium/PADS exports, and untouched V2 conversion source |
| `validation/` | Extraction provenance, hashes, connectivity checks, rule reports, and conversion records |
| `scripts/` | Connectivity and component placement verification scripts |

The native source was `hardware-reserve/lceda-2026-10-01/source/ProPrj_ExoAnchor-ESP32P4_2026-09-30.epro2`. Initial KiCad import used `ProPrj_ExoAnchor-ESP32P4_2026-10-19.epro`, followed by repairs against native evidence. Complete source hashes are in `validation/extraction-v3.json` and `validation/extraction.json`. These paths record provenance; opening this project does not require the original workspace.

`reference/V2_compatibility_export_as_received.epro` retains a known PCIe compatibility-export issue for audit purposes. **Do not use it as the current design entry point.** Use the `.epro2` or `.eprj3` listed above for JLCEDA.

Historical references were extracted from the hardware repository's local `codex/p4-v2.4a6-archive-20261022` branch, commit `96cf71e`, under `ESP32P4/exoanchor-p4-v2.4a6/`. They are historical records, not confirmed current manufacturing deliverables. `LICENSE` is copied from the hardware repository's MIT license. Original third-party component-library identifiers and properties are retained.

## Repeat the checks

From this directory, export a fresh netlist with a compatible `kicad-cli`, then run the comparison:

```sh
kicad-cli sch export netlist --format kicadxml -o validation/kicad-netlist.xml KiCad/ExoAnchor_P4_V2.4A6.kicad_sch
python3 scripts/verify_conversion.py
```

The script resolves paths relative to this project and exits nonzero if parity fails. It checks component references, pad nets, net endpoint sets, and component placements. It does not replace ERC/DRC, manufacturing review, or physical validation. `SHA256SUMS.txt` records the delivered file hashes.
