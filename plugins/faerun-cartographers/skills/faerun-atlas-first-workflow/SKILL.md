---
name: faerun-atlas-first-workflow
description: Make the illustrated town atlas the first visual checkpoint for fantasy settlement mapping. Use for new towns and cities, refining settlement layouts, matching map sets, or cadastral, land-water, district, terrain, ink, isometric and scenic views of a settlement. Reuse a previously approved atlas; build each output from its shared base instead of a chain of restyled images.
---

# Faerûn Atlas-First Workflow

Apply this default sequence to settlement projects: research, illustrated atlas, refine and approve, freeze version, trace shared geometry, render requested map types, check against the approved atlas.

Read [the full workflow](references/atlas-first-workflow.md) for the review checklist, output table and change rules.

## Establish the working base

1. Read supplied research and maps. Separate sourced facts, user choices and assumptions. Resolve major conflicts in banks, bridges, gates and named places before fixing the layout.
2. Check whether this settlement already has an approved illustrated atlas. Reuse the exact approved version when available. Do not restart atlas creation for every requested style.
3. If none exists, use Fantasy Illustrated Town Atlas to create the first visual draft. Load the current Faerûn Cartographers Plat Standard, its actual template, spec and assets before composing a plate. Do not approximate the frame from memory.
4. Refine river shape, crossings, walls, gates, streets, named sites, building density, open ground and full map extent. Check population fit without claiming a roof count proves capacity. Mark any added countryside as assumed.
5. Present the concrete atlas for layout approval before starting later map types. Reuse approval already given; honor explicit user instructions to proceed or waive a checkpoint. Do not treat an unresolved map error as approved merely because the user requested another style.
6. Freeze the chosen atlas version and record its filename, crop, bounds, north, scale evidence, landmark IDs and assumptions. Approval selects the working layout; it does not make assumed details official lore.

## Trace once and reuse

Use Map Geometry Master and Fantasy Land-Water Boundary Master after atlas refinement to trace the approved layout. Read their current skills. The atlas-first order controls settlement production order; their geometry and validation rules still apply.

Create shared land/water, roads, crossings, building footprints, walls, gates, docks, named sites and supported land-cover layers. Keep constructed objects and boats separate from water and land; continue water beneath bridges. Check overlays against the approved atlas. Save a lossless mask, editable geometry and a parent-version record.

Do not require a finished vector survey before making the first illustrated atlas. For later output, prefer checked geometry. If only image conversion is feasible, produce an explicitly approximate draft and do not claim that traced layers or exact alignment exist.

## Render requested outputs

Read each requested map style skill. Branch all outputs from the approved atlas and matching shared layers, not the latest generated derivative. Combined property/terrain maps may use checked component layers sharing the same parent, crop and scale.

Keep riverbanks, road connections, bridge endpoints, walls, gates, buildings and landmark positions fixed. Label unknown parcels as assumed and district borders as proposed. Use numeric heights, contour intervals or water depths only with valid supporting data. Keep hypothetical terrain separate from measured layers.

For scenic views, record camera position, direction, eye height and field of view. Preserve sightlines and allow occlusion. Never move a site to show it or add bridges to improve a scene. Treat unsupported heights and facade details as artistic estimates. Omit the plat frame from scenic views unless requested.

## Check and revise

Compare every output with its approved parent: extent, north, river connections, bridge count, gates, road junctions, named sites, building density and scale. Check plates against the actual Plat Standard, including square cells, round seal, fixed compass and scale dimensions.

Fix style errors in the affected output. For a geography change, revise and version the atlas, update shared layers and rebuild affected maps together. Never silently patch only one output's river or street.

Report the parent version and material assumptions briefly. Never call an image conversion coordinate-verified. Use the current user instruction when it explicitly selects a different edit target or scope, and record that choice.
