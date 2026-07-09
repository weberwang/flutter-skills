# Asset Slicing Manifest Template

Use this to record exported or sliced production assets before Pencil restoration or Flutter implementation.

## Export Batch

- Page or module:
- Source mockup:
- Source design file:
- Export date:
- Export owner:

## Sliced Assets

| Asset ID | Output file | Format | Logical size | Pixel size | DPR | Transparency | Compression | Flutter path |
|---|---|---|---|---|---|---|---|---|

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
- File formats match transparency and scaling needs.
- Large assets have compression or replacement notes.
- `pubspec.yaml` entries are recorded for implementation.
