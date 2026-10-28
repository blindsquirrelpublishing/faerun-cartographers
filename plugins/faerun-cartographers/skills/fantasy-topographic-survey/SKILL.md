---
name: fantasy-topographic-survey
description: Terrain contour and elevation map.
---

# fantasy-topographic-survey

## Shared rules
All styles must preserve source-map geometry: building footprint positions and orientations, streets, rivers, walls, gates, and landmarks. Register references to one north-up coordinate system and stable scale. Do not invent roads or move buildings. Flag disagreements and unknown data. Exact GIS fidelity requires traced vector geometry; generative images alone cannot guarantee it. Elevations must come from measured sources or be explicitly marked conceptual.

## Workflow
Render 10-foot contours only when height data supports that interval. Include index contours, elevation labels, legend, scale and vertical datum. Preserve rivers and landform geometry. Without elevations, mark output hypothetical.
