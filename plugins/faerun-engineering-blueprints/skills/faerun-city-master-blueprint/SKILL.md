---
name: faerun-city-master-blueprint
description: Create a 2D city engineering master plan showing roads, walls, gates, bridges, districts, public spaces, river and docks with preserved geometry.
metadata:
  author: Faerûn Cartographers
  version: "1.0.0"
---

# Faerûn City Master Blueprint (BP-01)

Read `../../references/common-standard.md`; load the approved geometry master. Use the Mirabar city master plan as a **style reference**, not independent geometry data.

## Draw
- City outline, outer/inner walls, towers and gates; city districts and land-use tints; major roads and walkways; bridges and docks; both riverbanks; parks and gardens; squares and the correct major civic sites.
- **Show public greenspace clearly** using muted green and translucent boundaries. Protect blocks and parcels from opaque fills or oversized labels.
- Show major structures only as flat top-down footprints/outline when known. No isometric walls, roofs or perspective.
- Preserve the street and river geometry across the five sheets.

## Engineering checks
- Verify every street reaches its approved gate or connector and bridges meet land at both ends.
- Verify each pier is attached to waterfront. Preserve parks and squares, not turning them into building lots.
- Compute outside wall diameter, enclosed area and full sheet coverage using actual XY; show feet and miles. Label estimates as modelled.

## Output
BP-01 City Master Plan, 19:13 left-panel/right-map layout, PNG and editable SVG if available, plus land-use overlay JSON and provenance.
