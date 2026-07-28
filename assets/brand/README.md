# ExoAnchor Hardware 品牌资源

本目录保存 **Riven Datum** 标志的硬件制造导出。标准 Logo 系统、Web/README 资源、颜色变量和确定性构建脚本位于主 ExoAnchor 仓库的 `assets/brand/` 与 `scripts/build_brand_assets.py`。

## 文件

- `exoanchor-symbol-silkscreen.svg`：可缩放单色母版。
- `exoanchor-symbol-silkscreen-10mm.svg`：物理宽度 10 mm 的 SVG。
- `exoanchor-symbol-silkscreen-10mm.dxf`：10 mm 闭合多段线 DXF。
- `exoanchor-symbol-silkscreen-20mm.svg`：物理宽度 20 mm 的 SVG。
- `exoanchor-symbol-silkscreen-20mm.dxf`：20 mm 闭合多段线 DXF。

紧凑板面优先使用 10 mm 版本，主板识别、治具或外壳标记可使用 20 mm 版本。投产前必须按所选 PCB 厂商规则核对最小丝印线宽和间距。

EDA 支持填充多边形导入时优先使用 SVG。DXF 导入器通常把几何体当作闭合轮廓；需要实心丝印时，应将导入轮廓转换为填充区域。

ExoAnchor 名称和 Logo 属于品牌资源，不因硬件仓库采用 MIT License 而自动获得商标许可。
