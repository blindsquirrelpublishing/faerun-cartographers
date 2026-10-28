---
name: fantasy-land-water-boundary-master
description: Produce and validate authoritative land/water topology masks for Faerûn Cartographers, safeguarding shorelines, islands, and river connections between cadastral, topographic, political, land-cover, and illustrated map plates.
---

# Fantasy Land-Water Boundary Master

## When to use
Apply **first** whenever two or more fantasy cartography maps must share land and water geometry, or when the user requests shoreline, riverbank, island, wetland-water, or channel corrections. This skill defines geography; the specialized map skill determines later visual content. The Faerûn Cartographers Plat Standard defines framing and typography.

## Authority and reference priority
1. An explicit user-approved land–water boundary master is the **sole geometry authority** for downstream plates. The latest approved Yartar land–water reference is in `references/yartar-land-water-master-reference.png`, but only when the user confirms that version is authoritative.
2. When no approved master exists, use the current user's designated source plan, surveyed/georeferenced layer, or traced source geometry. Never derive water from artistic blue hues alone when bridges, boats, piers, walls, roof shadows or terrain coloring are present.
3. Older maps supply names or provenance unless explicitly designated as geographic authority. Previous AI illustrations supply style only unless directly approved as a geometry reference.
4. Do not fabricate islands, channels, bridge crossings, or shoreline detail to make a map prettier. A **city wall is not a shoreline** and a **boat is not an island**.

## Required deliverables
- **Two-class map**: land (solid warm ivory) and water (solid blue), with thin consistent boundary strokes; optional confirmed labels only. No constructed features or vegetation.
- **Binary master mask**: water=1 (white) and land=0 (black), or the inverse if clearly documented. Prefer lossless PNG aligned exactly to the map-field pixel bounds.
- **Geometry master**: SVG paths with explicit `land`, `water`, and `shoreline` layers; GeoJSON polygon/multipolygon features if geometry has been precisely digitized and topology validated. Never claim georeferencing/true geographic coordinates for pixel-space digitization.
- **Metadata**: source filename/version, extent, aspect/coordinates, water/land convention, confidence, known ambiguities, approval state, and revision history.
- A fixed **master ID and checksum** inherited by every derivative map. If land/water boundaries change, issue a new revision of the master; do not silently change only one derivative.

## Extraction and topology workflow
1. Freeze the crop and viewport: record exact image coordinates of the right-hand map field. Exclude left sidebar, title, scale bar, and coordinate labels from geographic geometry.
2. Define north orientation, map coordinates, and any valid survey scale **only when evidenced**. A drawn grid is not itself proof of scale.
3. Trace major, continuous water surfaces first; explicitly identify upstream Surbrin, the east-bank land carrying Yartar, the Dessarin confluence, the southern channels, and verified islands.
4. Confirm bank continuity: the east-bank town is part of the continental land mass north and east of Yartar. **Yartar must not become an island** from interpreting roads, walls, field lines, or waterways as water.
5. Remove *all* boats, wakes, docks, jetties, wharves, bridges, gates, building footprints, retaining walls, and decorative rocks that are not actually distinct land features. Shore boulders may inform the shoreline but do not automatically become standalone islands.
6. Trace true islands as closed, contiguous land polygons completely surrounded by actual water. Check every isolated polygon against the source. No boat-sized false islands.
7. Use polygon containment and connected-component checks: water channels cannot pass through known terrain, and the Yartar mainland must remain connected to land to its north and east. Avoid accidental thin blue slivers surrounding built walls.
8. Export master geometry once, then **render subsequent plates against this immutable geometry**. Use compositing or masks rather than redrawing shorelines by prompt.
9. Verify land-water topology by overlaying masks from each downstream map on the master: boundary discrepancy target is zero pixels when geometric masks share raster dimensions. Correct the derivative, not the approved master.

## Downstream use
- **Cadastral**: place buildings, lots, streets, piers, walls, and bridge graphics above fixed land/water boundaries. No roads alter the coast.
- **Topographic**: use land mask to clip hypsometric elevation fill and contour lines to dry land; use water mask for river bathymetry if evidenced. Leave boats, bridges, buildings, city walls, roads, parcels, docks, and all vegetation absent. Do not mistake small watercraft for islands.
- **Land cover / political / historical / illustrated**: derive land and water footprints directly from master; only overlay thematic content.
- **Overlay plates**: exact same pixel-space crop and transform; cadastral ghost layer may be transparent but must never shift the master geography.

## Faerûn Cartographers Plat Standard v1.8 compatibility
Use the most recent user-approved plat standard in preference to outdated bundled plate instructions. Current authoritative design: whole sheet 19:13; information panel 20% width; map field 80%; left panel zones 15% location/title (all horizontally centered), 15% map info, 60% variable legend, and 10% compass/seal/scale. Global Arial/sans-serif; white background; clean thin black separators. Map coordinate grid A–Q (17 columns), rows 1–16 with physically square cells. Compass size fixed; official **circular** red hand-stamped seal may rotate slightly and overlap the section above but may not stretch. The scale below the compass and stamp must numerically **and geometrically match** the Map Information statement. Do not state unsupported numeric map scales, bathymetry or contour heights as measured facts.

## Mandatory acceptance tests
- [ ] Land connected to north and east of Yartar; no spurious ring of water around the city.
- [ ] Surbrin and Dessarin confluence and water channels match source/approved master.
- [ ] Each island exists in the authoritative reference; no boats, piers or bridges converted into land.
- [ ] Exact same map-field extent, projection/schematic coordinate framing, grid, and orientation in derivative plates.
- [ ] Difference-overlay shows no moved shoreline or new/dropped island in downstream maps.
- [ ] No vegetation or artificial features appear on a terrain-only topographic plate.
- [ ] Contours and depth annotations are expressly tagged interpretive when not survey-backed.
- [ ] Official red seal retains 1:1 aspect ratio and original artwork; no newly invented stamp design.
- [ ] User approval recorded before promoting a draft to a shared geographic master.

## Failure recovery
If any validation fails, do not describe the map as exact, authoritative, or overlay-compatible. Return to the approved master geometry; isolate and fix only the thematic layer, preserve unchanged bank and island masks, and rerun the overlay check.
