---
name: fantasy-dungeon-underground-map
description: Underground floorplans, rooms, stairs and passages using source-faithful map data, without inventing geographic or route features.
---

# Fantasy Dungeon and Underground Map

## When to use
Underground floorplans, rooms, stairs and passages. Use when asked to produce, restyle, compare, or extract this type of fantasy map, especially in Faerûn.

## Inputs
- A user-designated authoritative base map or authoritative geometry/layers (required for factual maps).
- Optional official secondary maps, annotations, historical dates, relevant records, and requested projection or crop.
- Optional visual-style references; do not use illustrations as geographic truth.

## Style and production rules
Build a crisp top-down dungeon floorplan from source plans. Rooms, tunnels, levels, stairs, shafts, doors and underground water must retain exact supported geometry and their links. Use a clearly marked grid only if the source defines cell size. For multiple floors, create separate level maps and match every up/down connection by unique ID.

## Special validation rules
- Never add dead ends, secret doors, monsters, treasures or chambers absent from sources.
- Treat unknown passages as unknown, not passable.
- Distinguish up/down stairs, pits, blocked passages and doors based on source symbols.
- Do not assign a grid size, depth or room dimensions without measurement.

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
- [ ] Style fits **Fantasy Dungeon and Underground Map**.
- [ ] Exact same extent as source.
- [ ] All provided relevant features and names retained and correctly spelled.
- [ ] No invented road, path, river, bridge, settlement, border or site.
- [ ] Numeric measurements and periods supported by input or clearly marked unknown.
- [ ] Geometry and route connections compared against base reference.
- [ ] Map symbols, line types and legend are clear and consistent.
