---
name: black-ink-contour-atlas
description: Precise pen-only overhead atlas with light terrain contours. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
---

# Fine-Line Black Ink Contour Atlas

## Dependency
Read and follow `../faerun-map-geometry-master/SKILL.md` or the same master instructions included in the project. **Source geography overrides style examples.**

## Style target
Precise pen-only overhead atlas with light terrain contours.

## Visual recipe
Fine strokes, little hatching, clean white paper, outline trees and rooftops.

## Geographic constraints
Keep roof simplification within actual footprints.
Maintain all verified source features and named landmarks at their source coordinates; preserve street network, bridge crossings, water boundaries, building placements, and orientation. Do not import geography from the style reference.

## Conversion procedure
1. Identify the geographic source map and style reference separately.
2. Extract the source's stable geometry manifest and landmark index.
3. Apply this style only to strokes, colors, roof textures, shading, vegetation symbols, typography, and presentation.
4. Maintain source aspect ratio, north direction, and framing unless explicitly requested otherwise.
5. Cross-check every landmark against the source. Fix discrepancies before finalizing.
6. State when result is an approximate image conversion rather than a coordinate-verified render.

## Reusable prompt
> Convert the attached **SOURCE MAP** into **Fine-Line Black Ink Contour Atlas**. Use the separate **STYLE REFERENCE** for appearance only. Preserve the source map's north orientation, road intersections, building positions and footprints, walls, gates, bridges, watercourses, terrain features, named landmarks and numbered points of interest. Do not add or relocate geographic features. Fine strokes, little hatching, clean white paper, outline trees and rooftops. Keep roof simplification within actual footprints. Keep source aspect ratio and extent. If source geometry is uncertain, retain the visible geometry rather than inventing it. No unsupported labels.
