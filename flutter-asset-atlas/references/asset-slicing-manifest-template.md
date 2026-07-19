# Asset Slicing Manifest Template

Use this to record exported or sliced production assets before Pencil restoration or Flutter implementation.

## Export Batch

- Page or module:
- Source mockup:
- Global design freeze:
- Page design freeze:
- Source design file:
- Export date:
- Export owner:
- Confirmed pre-slicing table version:
- User confirmation time:
- Production mode: single asset / atlas contact sheet / source export / mockup extraction
- Background mode: transparent / retained / safe flat background / masked cutout
- Background transparentization: none / native transparent export / source-layer export / mask extraction / flat-background removal / manual alpha mask / regenerated
- Transparent post-processing: none / alpha cleanup / matte removal / edge decontamination / manual mask

## Sliced Assets

| Asset ID | Output file | Format | Logical size | Pixel size | DPR | Background mode | Transparentization | Transparency | Post-processing | Edge padding | Compression | Flutter path |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Pubspec Entries

```yaml
flutter:
  assets:
    - assets/images/
```

## Platform Notes

- Android density:
- iOS scale:
- Web renderer:
- Performance risk:

## Gate

- Output files exist at the recorded paths.
- Every output maps to a currently confirmed pre-slicing table row; no unconfirmed asset was generated or exported.
- File formats match transparency and scaling needs.
- Background transparentization is recorded when the source asset was not natively transparent.
- Transparent assets have clean alpha edges without background halos.
- Retained-background assets match the page design-freeze background.
- Post-processed transparent assets are checked on checkerboard, light, dark, and target page backgrounds.
- Single-image output is used unless atlas/contact sheet slicing has an explicit reason.
- Raster outputs use only `DPR=2`, with pixel width and height exactly twice the recorded logical size; no separate `1x` or `3x` variants are required.
- Large assets have compression or replacement notes.
- `pubspec.yaml` entries are recorded for implementation.
