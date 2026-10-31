---
name: fantasy-architectural-cutaway-map
description: Create a source-faithful 3D orthographic or isometric architectural cutaway showing a fantasy settlement, castle or building above ground and its documented underground levels in one readable sectional image.
---

# Fantasy Architectural Cutaway Map

## When to use
Use for castles, cities, forts, temples, inns, mines, dungeons and underground complexes when the user wants to see exterior forms, interior rooms, subsurface chambers and terrain together. Default to a static high-oblique orthographic sectional illustration. A cutaway is not a GIS survey.

## Inputs and source priority
1. Approved geometry master, GIS cadastral plat, site plan and user corrections.
2. Floorplans, sections, elevation data and explicitly approved room layouts.
3. Written canon and location research for names, use, depth order and history.
4. Art references for color, texture and mood only.

Never move, add or remove documented roads, walls, gates, towers, buildings, waterways or room connections just to improve the image. Do not use an earlier generated scenic picture as a substitute for approved geometry. If plans are incomplete, create a **conceptual reconstruction** and clearly mark uncertain rooms, levels, passage shapes and heights.

## Construction
1. **Geometry lock:** fix a single plan extent and orientation. Trace exterior walls, building footprints, gate positions, tower centers, courtyard, surrounding terrain and relevant water as distinct feature classes. Keep a control-point register for correspondence with the source plan.
2. **Section plane:** choose a cut direction that exposes the key features without hiding critical structures. Write down the camera direction and section-plane position. Use parallel projection (no vanishing points) when orthographic is requested; avoid arbitrary changes to wall curvature or building footprint.
3. **Above ground:** represent towers, ruined masonry, keep, inner and outer wards, important ruins and terrain. Show structural damage only where supported, otherwise call it illustrative.
4. **Below ground:** stack proven levels in correct topological order. Show stairs, shafts, wells, passages, portals, caves, streams, labyrinths, and connections only where documented. Depth, distance and passage dimensions remain *not to scale* unless separately established.
5. **Exposure:** cut through foreground ground and walls, reveal chambers with distinct floor slabs and visible rock strata. Use shadow, lighting and line weight for readability, but not to suggest measured elevation.
6. **Labels:** use short callouts and leader lines. Label named locations using source wording. Separate surface features, buried rooms, and uncertain interpretive areas. Avoid covering important geometry.
7. **QA:** compare the surface plan against the approved source and check every underground connection against source evidence. Flag anything inferred or changed.

## Rendering options
- Main: full-color ink-and-watercolor architectural model; muted earth and stone above, dark rock below; clean outlines.
- Alternatives: monochrome pen-and-ink, engineering section blueprint, archaeological reconstruction.
- Views: orthographic oblique, isometric, or flat elevation section; never claim a perspective image is orthographic.
- With an official plat: load and apply the actual **Faerûn Cartographers Plat Standard v1.8 (or later)** skill, SVG template, seal and validator. The standard sheet is 19:13, 20% left panel and 80% map field, with A–Q/1–16 square grid and correct scale. Do not fake an authoritative horizontal or vertical scale. If the actual skill is unavailable, produce a standalone illustration with no claim of plat compliance.

## Dragonspear Castle sample scene
Use an official/source map for the above-ground outline: Great Gate and outer ward; inner gate and six-sided inner walls; ruined Dragonspear Keep with dragon skeleton; Hold of Battle Lions. Place under the keep the known basement and sealed portal cave to Avernus; deeper below show the Warrens, buried labyrinth and connection to the underground Nepenthe River. The provided Dragonspear research establishes relationships and names, **not measured room layouts or cave depth**. Note explicitly: "Interpretive sectional reconstruction; underground distances and chamber shapes not surveyed."

## Do not
- Invent traversable passages, bridges, entrances, room counts or elevations as settled facts.
- Move the river to make it fit the composition.
- Make every floor visible if that contradicts the section plane; prefer an exploded cutaway only when the user asks.
- Put the official red seal or a numeric scale on a standalone illustration by default.
- Present artistic extrapolation as an official D&D map.

## Output
A rendered image plus, when possible, an editable geometry/section manifest, keyed room/feature index, evidence notes and comparison against the reference plan. State whether the result is surveyed, source-registered, or interpretive.
