---
name: tactical-clean-grid
description: Minimal clean top-down tabletop grid map. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
---

# Clean Tabletop Battlemap

## Dependency
Read and follow `../faerun-map-geometry-master/SKILL.md` or the same master instructions included in the project. **Source geography overrides style examples.**

## Style target
Minimal clean top-down tabletop grid map.

## Visual recipe
Simple flat roof planes, quiet pastel palette, clear paths and trees.

## Geographic constraints
Do not add terrain or structures to fill whitespace.
Maintain all verified source features and named landmarks at their source coordinates; preserve street network, bridge crossings, water boundaries, building placements, and orientation. Do not import geography from the style reference.

## Conversion procedure
1. Identify the geographic source map and style reference separately.
2. Extract the source's stable geometry manifest and landmark index.
3. Apply this style only to strokes, colors, roof textures, shading, vegetation symbols, typography, and presentation.
4. Maintain source aspect ratio, north direction, and framing unless explicitly requested otherwise.
5. Cross-check every landmark against the source. Fix discrepancies before finalizing.
6. State when result is an approximate image conversion rather than a coordinate-verified render.

## Reusable prompt
> Convert the attached **SOURCE MAP** into **Clean Tabletop Battlemap**. Use the separate **STYLE REFERENCE** for appearance only. Preserve the source map's north orientation, road intersections, building positions and footprints, walls, gates, bridges, watercourses, terrain features, named landmarks and numbered points of interest. Do not add or relocate geographic features. Simple flat roof planes, quiet pastel palette, clear paths and trees. Do not add terrain or structures to fill whitespace. Keep source aspect ratio and extent. If source geometry is uncertain, retain the visible geometry rather than inventing it. No unsupported labels.

## Example

[View sample image](assets/example.jpg)

![Fictional tactical-clean-grid sample](assets/example.jpg)

Use this image as a style example only. It shows the fictional town of Alderford. Geometry, grid, scale, heights, labels, and plat layout have not been fully checked; follow the written rules when making maps.
