---
name: numbered-gazetteer
description: Classic D&D numbered town map with a location key. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
---

# Numbered Old-School Gazetteer

## Dependency
Read and follow `../faerun-map-geometry-master/SKILL.md` or the same master instructions included in the project. **Source geography overrides style examples.**

## Style target
Classic D&D numbered town map with a location key.

## Visual recipe
Black ink, numbered circles, distinct neighborhoods, compact keyed legend.

## Geographic constraints
Only label features confirmed by the source; never invent legend entries.
Maintain all verified source features and named landmarks at their source coordinates; preserve street network, bridge crossings, water boundaries, building placements, and orientation. Do not import geography from the style reference.

## Conversion procedure
1. Identify the geographic source map and style reference separately.
2. Extract the source's stable geometry manifest and landmark index.
3. Apply this style only to strokes, colors, roof textures, shading, vegetation symbols, typography, and presentation.
4. Maintain source aspect ratio, north direction, and framing unless explicitly requested otherwise.
5. Cross-check every landmark against the source. Fix discrepancies before finalizing.
6. State when result is an approximate image conversion rather than a coordinate-verified render.

## Reusable prompt
> Convert the attached **SOURCE MAP** into **Numbered Old-School Gazetteer**. Use the separate **STYLE REFERENCE** for appearance only. Preserve the source map's north orientation, road intersections, building positions and footprints, walls, gates, bridges, watercourses, terrain features, named landmarks and numbered points of interest. Do not add or relocate geographic features. Black ink, numbered circles, distinct neighborhoods, compact keyed legend. Only label features confirmed by the source; never invent legend entries. Keep source aspect ratio and extent. If source geometry is uncertain, retain the visible geometry rather than inventing it. No unsupported labels.

## Example

[View sample image](assets/example.jpg)

![Fictional numbered-gazetteer sample](assets/example.jpg)

Use this image as a style example only. It shows the fictional town of Alderford. Geometry, grid, scale, heights, labels, and plat layout have not been fully checked; follow the written rules when making maps.
