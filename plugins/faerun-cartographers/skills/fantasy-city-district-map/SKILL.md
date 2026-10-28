---
name: fantasy-city-district-map
description: Neighborhood and ward borders on an accurate street plan using source-faithful map data, without inventing geographic or route features.
---

# Fantasy City District Map

## When to use
Neighborhood and ward borders on an accurate street plan. Use when asked to produce, restyle, compare, or extract this type of fantasy map, especially in Faerûn.

## Inputs
- A user-designated authoritative base map or authoritative geometry/layers (required for factual maps).
- Optional official secondary maps, annotations, historical dates, relevant records, and requested projection or crop.
- Optional visual-style references; do not use illustrations as geographic truth.

## Style and production rules
Using the cadastral town plan, fill each known ward or neighborhood with light distinct color while keeping streets, buildings, walls, gates, markets and waterways visible. Use region-internal labels or careful leader lines. Include a compact legend of exact district names and functions where sourced.

## Special validation rules
- District polygons must match source boundaries; do not place borders along convenient streets without evidence.
- Keep street connectivity, bridges, plots and city wall/gates unchanged.
- If district bounds are not provided, request them or mark any proposed divisions as conceptual.
- Do not infer a political or wealth boundary from building style.

## Source integrity contract (required for every output)
1. Identify and rank the supplied authoritative sources before drawing. Latest user-designated official/source map controls the crop, feature positions and route geometry. Secondary maps may clarify names and dates, not silently replace geometry.
2. Keep the **exact region, area, or floor extent** shown by the user; do not fill outside the map. Treat blank/unknown as unknown, not as permission to invent.
3. Trace rivers, tributaries, coastlines, roads, paths, trails, tracks, crossings and junctions **only where source material supports them**. Preserve endpoints, turns, classifications and non-connections. Never invent a connecting line.
4. Reuse source-supported settlements, landforms, walls, gates, bridges, ruins and other sites in their proper positions. A named bridge or road junction is not automatically a town.
5. Separate mapped facts from inferred/schematic items. If a date, height, border, route, ownership or terrain class cannot be verified, show it as unknown or omit it. Do not fabricate scales, units, intervals or coordinates.
6. If multiple reference maps conflict, stop and flag important conflicts rather than averaging their shapes. Make a feature inventory and comparison checklist before rendering.
7. After drawing, visually compare the final map with source(s): same extent, topology, features, labels and spelling. Fix extra/missing/moved elements. Treat earlier AI-made maps only as **style references**, never geographic evidence.

## Shared map data / skill compatibility
May take a GIS map, georeferenced drawing, linework, vector layers, annotated raster, or plain reference image from the user's Fantasy GIS Cadastral Map, Fantasy Map to GIS Converter, Fantasy Topographic Survey, Illustrated Town Atlas, Regional Area Map or scenic skills. Keep a clean reusable set of source-controlled layers (water, relief, vegetation, routes, settlements, labels) where available. Do not assume missing layers exist.

## Handoff / delivery
Provide the finished requested visual or structured map file when feasible, plus a short list of **sources used**, **estimated/unknown details**, and **checks performed**. Do not label a decorative drawing GIS-accurate or measured without valid underlying data.


## Output quality checklist
- [ ] Style fits **Fantasy City District Map**.
- [ ] Exact same extent as source.
- [ ] All provided relevant features and names retained and correctly spelled.
- [ ] No invented road, path, river, bridge, settlement, border or site.
- [ ] Numeric measurements and periods supported by input or clearly marked unknown.
- [ ] Geometry and route connections compared against base reference.
- [ ] Map symbols, line types and legend are clear and consistent.

## Example

[View sample image](assets/example.jpg)

![Fictional fantasy-city-district-map sample](assets/example.jpg)

Use this image as a style example only. It shows the fictional town of Alderford. Geometry, grid, scale, heights, labels, and plat layout have not been fully checked; follow the written rules when making maps.
