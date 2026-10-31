---
name: faerun-cadastral-property-blueprint
description: Make 2D property parcel plans with closed lot boundaries, blocks and public land instead of individual building footprints.
metadata:
  author: Faerûn Cartographers
  version: "1.0.0"
---

# Faerûn Cadastral Property Blueprint (BP-02)

Read `../../references/common-standard.md`. Use the exact same geometry master as BP-01.

## Draw
- Plot **closed polygons** for each parcel with unique stable lot IDs; distinguish fine lot edges from heavier block limits and street rights-of-way.
- Public land, gardens and parks use muted green; civic/religious land and squares get gentle tints; industrial/dock property can use separate quiet colors.
- Keep road borders, walls, gates, bridges, dock edge and both riverbanks identical to master.
- **Do not draw buildings, roofs, isometric features or decorative icons.** Parcels represent property rights, not buildings.

## Lot logic
1. Lots need a road frontage or documented access path; preserve public easements and rights-of-way.
2. No lot extends across public streets, walls, docks, waterways, public squares or protected green areas.
3. Check polygon closure, intersections, duplicated boundaries, gaps, self-crossing lines and narrow slivers.
4. If ownership is not documented, parcel ownership is **modelled** and IDs are illustrative.
5. Compute parcel count, total parcel land, median lot area, public acreage and density using square feet and acres.

## Output
BP-02 Cadastral Property Plan with PNG/SVG, parcels.geojson (or vector JSON) and a parcel register with IDs, area, status and source.
