---
name: faerun-topographical-engineering-blueprint
description: Create a 2D engineering topographic sheet with contour lines, spot elevations, slopes and drainage over unchanged city geometry.
metadata:
  author: Faerûn Cartographers
  version: "1.0.0"
---

# Faerûn Topographical Engineering Blueprint (BP-03)

Read `../../references/common-standard.md`; do not move any approved city features.

## Draw
- Fine elevation contour polylines, index contours, labeled spot heights, slope arrows, retention walls, drainage channels, floodplains and breaklines.
- Preserve the city streets, parks, walls, riverbanks, bridges, docks and major sites as a **fixed faded base**. Contours overlay but do not replace those features.
- Use 50-foot contour spacing only as a sample design. Tune intervals to surveyed terrain. Avoid cluttering gates or parcel corners with elevation text.
- No arbitrary land contours crossing water; bank edges must not be redrawn as a closed inland river.

## Height accuracy
1. Prefer published survey controls, spot heights or a trustworthy elevation model.
2. If heights aren't measured, state **conceptual/modelled terrain**. Do not invent sea-level values without a datum.
3. Declare height datum, vertical units (feet), contour interval and whether it is a model or measured survey.
4. Test noncrossing contours, sensible downhill flow and drainage to the river. Validate that labeled spot heights fit contours.
5. Do not make civil engineering claims for unverified underground drainage or grades.

## Output
BP-03 Topographical Plan, PNG/SVG, editable contours/elevation data and explicit source/elevation-status notes.
