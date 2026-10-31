---
name: fantasy-3d-orthographic-view
description: Produce source-faithful 3D orthographic and high-oblique views of fantasy towns, cities, castles, forts and ruins using an approved plan or geometry master.
---

# Fantasy 3D Orthographic View

## Goal
Turn a verified 2D site or cadastral plan into a three-dimensional *parallel-projection* exterior view. Preserve mapped geometry, even when roofs, walls and terrain hide parts of the site. This is distinct from the Fantasy Architectural Cutaway Map skill, which reveals interiors and underground spaces.

## Inputs and authority
1. User-approved Map Geometry Master, GIS cadastral plan and land-water boundary master.
2. Source map, SVG, GIS features, elevation/contours and verified measurements.
3. Canon lore and site descriptions for names, functions, heights, architecture and era.
4. Reference paintings and photographs for style only.

Use the latest approved plan as the geometric source of truth. Do not infer geometry from earlier image-generation results. Log source conflicts and describe uncertainty. An image-only reference is not a measured survey.

## Workflow
1. **Register the source:** identify orientation, bounds, coordinate system, visible footprints, walls, towers, gates, streets, paths, bridges, water and open ground. Preserve distinct geometry layers and their topology.
2. **Set the time period:** decide whether the settlement is occupied, abandoned, ruined or rebuilt. Add only supported historical changes.
3. **Choose a true orthographic camera:** parallel projection, fixed direction, no vanishing points or size shrinkage with distance. Prefer a 30–45 degree downward view; rotate to reveal the largest number of important landmarks. Record camera direction.
4. **Lift footprints:** extrude structures *in place*; roof forms and heights must come from evidence or be labeled interpretive. Make towers, wall circuits, gate openings and roads align with their 2D footprints.
5. **Raise terrain:** use real contours where present. If no height measurements exist, show only qualitative hill/mound forms, with no numeric elevation claims. Keep waterlines, shorelines and river crossings fixed.
6. **Check occlusion:** structures may obscure others naturally. Never move, enlarge or duplicate a landmark to make it visible.
7. **Style:** default to readable fantasy ink-and-watercolor with stone, vegetation and roofs; alternatives are monochrome archaeological model, realistic reconstruction or game-map art. Decorative detail cannot alter geography.
8. **Verify:** compare plan-view footprints, gate order, road connections, walls, river course and relative positions against the source. State any uncertain architectural details and the selected viewing direction.

## Output modes
- **Standalone illustration (default):** edge-to-edge 3D orthographic site view without a fictitious measured grid or scale.
- **Faerûn Cartographers plat:** only if the user asks for the formal plate, load the actual Faerûn Cartographers Plat Standard v1.8 or later SKILL.md, spec, blank SVG, compass and official seal. Follow its 19:13 paper, 20/80 panels, fixed legend zones and validation. Do not draw an apparent 2D metric grid over a foreshortened 3D view or claim it remains square. Show the 3D illustration in the map field and use a clearly marked reference scale only if defensible.
- **Geometry paired view:** provide an accompanying 2D source-plan thumbnail or footprint index so readers can check alignment.

## Dragonspear Castle test scene
Use the approved Dragonspear Castle plan as the governing outline: Great Gate, outer ward and towers, six-sided inner walls and western gate, ruined keep, Hold of Battle Lions, courtyard and approach road. The three low hills and major ruin condition are supported by written research. Exact tower heights, hillside grades, roof damage and rubble placement are interpretive unless independently grounded. Preserve the location of the dragon skeleton across the ruined keep if requested in the site reconstruction. Do not add new bridges, buildings, gates or roads.

## Quality checks
- [ ] True orthographic/parallel projection, not perspective.
- [ ] Surface features align with the approved plan.
- [ ] Walls, towers and gates keep their original counts and positions.
- [ ] Water and terrain match the land-water and terrain masters.
- [ ] Unknown heights and architecture are described as reconstructions.
- [ ] Optional plat follows the actual plat skill, without false metric claims.

## Do not
Do not rearrange the site for a prettier shot; treat a new generated painting as factual geography; show made-up parcels; or use a numerical height/scale without source support.
