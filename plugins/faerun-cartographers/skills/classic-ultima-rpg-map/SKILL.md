---
name: classic-ultima-rpg-map
description: Create or restyle a fantasy map as a classic top-down tile-based pixel-art RPG overworld with terrain tiles, houses, paths, bridges and a map key. Use for Ultima-like maps.
---

# Classic Ultima RPG Map

## Workflow
1. Identify supplied source map and geometry master. If none, create explicitly fictional geography.
2. Lock extent, orientation, land/water boundaries, routes, parcels and landmarks before styling.
3. Apply this visual style without changing the locked topology.
4. Validate landmarks, crossings, grid geometry, text legibility and parcel IDs.
5. Output a map and concise notes identifying any invented or unmeasured features.

## Style and validation
Use orthographic top-down tiles, a limited retro palette, pixel-crisp edges, repeated forest/grass/water/mountain tiles and simple sprites for landmarks. Do not use isometric projection, smooth painterly shading or modern 3D effects. Establish a tile coordinate system and ensure square cells; A–Q labels and row numbers must align with the actual tile grid. Preserve source map topology and key locations; rasterize from a locked geometry master rather than improvising rivers or adding bridges. Draw labels in a side panel or small numbered map markers where possible. Show legend and landmark index. Any scale must be based on real or declared fictional measurements; otherwise say not to scale. For original fictional geography, state that it is invented. Do not copy any game asset sprites; make original retro-style tile art.

## Conversion rules
When converting a prior map, retain the same footprint, orientation, landmark positions and topology. Treat the previous map as a visual reference, not a measured survey. Do not infer exact area from an illustration. Check square grid cells and consistent grid labels. Preserve a reusable location-to-coordinate table when available.
