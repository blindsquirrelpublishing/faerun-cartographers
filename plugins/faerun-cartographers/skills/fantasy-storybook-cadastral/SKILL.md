---
name: fantasy-storybook-cadastral
description: Create a hand-painted storybook cadastral map with surveyed parcels, numbered ownership areas, woodland, buildings and a parcel schedule. Use when asked for a whimsical parchment land registry map.
---

# Fantasy Storybook Cadastral

## Workflow
1. Identify supplied source map and geometry master. If none, create explicitly fictional geography.
2. Lock extent, orientation, land/water boundaries, routes, parcels and landmarks before styling.
3. Apply this visual style without changing the locked topology.
4. Validate landmarks, crossings, grid geometry, text legibility and parcel IDs.
5. Output a map and concise notes identifying any invented or unmeasured features.

## Style and validation
Use top-down 2D geometry. Render soft watercolor forest and meadow textures, hand-inked parcel edges, buildings, footpaths and waterways. Give every parcel a unique stable ID, matching the schedule. Never make up acreage, lengths or ownership: label as illustrative or unknown if no survey. If source geometry exists, trace and lock it first; do not move roads, riverbanks, structures or parcel corners. For an original fictional map, declare that geography is invented. Include legend, north arrow, grid and scale only when supported; a decorative scale must be marked not to scale. Keep labels out of important map detail. For shared Faerûn projects, defer to the geometry master and plat standard unless the user explicitly requests a different page format.

## Conversion rules
When converting a prior map, retain the same footprint, orientation, landmark positions and topology. Treat the previous map as a visual reference, not a measured survey. Do not infer exact area from an illustration. Check square grid cells and consistent grid labels. Preserve a reusable location-to-coordinate table when available.
