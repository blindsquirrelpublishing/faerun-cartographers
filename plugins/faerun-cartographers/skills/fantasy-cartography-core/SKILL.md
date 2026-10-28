---
name: fantasy-cartography-core
description: Coordinate source maps and enforce positional fidelity.
---

# fantasy-cartography-core

## Shared rules
All styles must preserve source-map geometry: building footprint positions and orientations, streets, rivers, walls, gates, and landmarks. Register references to one north-up coordinate system and stable scale. Do not invent roads or move buildings. Flag disagreements and unknown data. Exact GIS fidelity requires traced vector geometry; generative images alone cannot guarantee it. Elevations must come from measured sources or be explicitly marked conceptual.

## Workflow
Trace buildings, streets, water, walls, parcels, landmarks into shared named layers with source IDs. Record scale, north, known control points and uncertainties. Compare resulting maps to original coordinates.
