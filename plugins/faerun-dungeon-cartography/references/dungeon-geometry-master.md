# Dungeon Geometry Master v1.0

Create and approve this master BEFORE any style output. Use one canonical coordinate system (x,y in feet; z in feet for each level), with an explicit origin and orientation. Record provenance and uncertainty. Never infer true measurements from an unscaled sketch.

## Required data
- metadata: source, source date, units, scale status, north direction, confidence.
- levels: id, floor elevation (or unknown), ceiling elevation (or unknown).
- rooms: stable id, original label, level id, closed 2D polygon (or approximate bounds flagged), entrance points, terrain, features, confidence.
- passages: stable id, connected room ids, path polyline, width if known, level changes, traversability, confidence.
- transitions: stairs, slopes, ladders, shafts, pits, portals; endpoints and elevation delta or unknown.
- water: channels, pools, falls, flow direction only when known; connected endpoints.
- landmarks: doors, traps, treasure, notes; attached to room/passage ids, not floating labels.

## Hard rules
1. Trace source room adjacency and passage connections first. A visual crossing is NOT a junction unless the source says so.
2. Never add, remove, merge, split, or reroute a room, passage, bridge, stair, or water connection without a marked proposal and approval.
3. Preserve source labels; distinguish confirmed, interpreted, and unknown features.
4. Preserve every master id across 2D, battle and isometric versions. If a 3D projection hides a room, provide a cutaway or inset; do not move it.
5. No invented feet, square grid scale, z values, or passage widths. A not-to-scale schematic must say so.
6. Do not treat decorative grid lines or a generated image as measured geometry.

## Validation before release
- Compare room-id sets, adjacency edge sets, level transitions, water topology, and source feature counts against the master.
- Check labels do not hide passages; use keyed numbers if needed.
- Check scale bar arithmetic and square grid aspect ratio; verify feet and miles where applicable.
- Produce a change report listing unknowns, inferred geometry, occluded rooms, and unresolved mismatches.
- Do not call the result geometrically verified until these checks pass.
