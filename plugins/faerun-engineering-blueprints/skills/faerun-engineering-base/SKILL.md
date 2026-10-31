---
name: faerun-engineering-base
description: Create and check a shared 2D map geometry master for Faerûn blueprint maps with fixed imperial scale, grid and coordinates. Invoke before any engineering blueprint or when layers drift apart.
metadata:
  author: Faerûn Cartographers
  version: "1.0.0"
---

# Faerûn Engineering Geometry Master

This is the required first skill for every engineering sheet. Read `../../references/common-standard.md` and inspect the approved reference map. Generate or load one immutable `geometry-master.json`.

## Workflow
1. Confirm the approved source map, source era, and newest revision. Distinguish official lore from visual reconstruction and planning assumptions.
2. Establish 2D north-up feet coordinates and a truly square grid. Use one transform from model feet to printed pixels and keep it for all five sheets.
3. Trace one canonical copy of **both riverbanks**, city boundary, walls, towers, gates, roads, squares, parks, districts, parcels, docks, bridges and important landmarks. Raster geometry must be explicitly called traced or approximate.
4. Give each feature a stable ID, status and source. Put master features in a vector/JSON data structure. No local re-creation of master geometry is permitted in sheets.
5. Save the master and a SHA-256 hash; every overlay stores the same parent master version. Write a revision log before moving features.
6. Measure city extent, walls, lots, streets and scale from the XY data. Check 500 ft per cell equals 8,500 × 7,000 ft for a 17×14 reference grid, about 1.61×1.33 miles.
7. Re-render all five sheets after any geometry revision. Validate matching coordinates, and do not use a different river, altered roads or shifted garden in one sheet.

## Special Mirabar notes
The approved Mirabar reference has the River Mirar on the **south** edge, flowing generally east to west; preserve both banks and dock geometry. The reference dimensions and density are design estimates, not official D&D survey data.

## Output
`geometry-master.json`, `geometry-master.sha256`, `source-notes.md`, `revision-log.md`, and a base alignment proof. Use the sample validator in `scripts/validate_master.py` and the schema in `references/master-schema.json` as starting tools.
