# Faerûn engineering blueprint standard v1.0

## Non-negotiable geometry rules
- Begin with the user's approved map and the latest accepted vector/GIS/JSON geometry master. An image alone is a visual reference, **not** verified survey coordinates.
- Digitize the two separate riverbanks, walls, gates, towers, roads, bridges, docks, parcels, parks, civic sites and terrain control into the master once. Keep names, feature IDs and vertex coordinates fixed in all styles.
- Use a local north-up 2D XY system: X increases east, Y increases north; the canonical unit is feet. Convert from meters using 3.280839895013123, never merely relabel values.
- Every sheet shares viewport, projection, grid origin, scale, clip boundary, coast/river shape and center positions. All style-only lines belong in separate overlay files.
- Do not rebuild streets, bridges, piers, greenspace, parcels, gates or walls to make a sheet look nicer. To change any underlying geometry, issue a new approved master revision and regenerate every sheet.
- Preserve bridge abutments on land, piers attached to waterfront, gates on the walls, and road centerlines that meet gates. Never draw roads through water without an actual bridge or causeway.
- For the approved Mirabar design, the River Mirar runs alongside the *southern* city edge, generally east to west. Mirabar sits north of the river. Do not return to the old layout where water surrounds the city.

## Technical layout
- Orthographic top-down 2D only, no roof views, perspective towers, or 3D walls.
- Landscape sheet aspect ratio 19:13. Left information panel 20% of width; map, enlarged to fill the right-hand 80%. Leave no wasted band inside the map frame.
- Navy blueprint background; subdued blue fine grid; cyan walls and towers; pale white road edges and property lines; medium-blue river; restrained green greenspace; soft land-use fills and gold civic sites. Add a distinctive, named overlay palette per sheet.
- Use true square grid cells. Border labels correspond to real cell centers, never arbitrary typography. A–Q / 01–14 are the approved Mirabar reference grid only; other settlements can have different grids.
- Show city/site title, sheet number, revision, responsible cartographer, reference/source, extent, scale, 2D projection, legend, notes, units, status and scale bar in the sidebar; put the north arrow at the bottom.
- Distances in feet, long lengths in miles, areas in square feet or acres (43,560 sq ft/acre). 5,280 feet = 1 mile. Contours and heights are in feet.
- For the sample Mirabar engineering reference: 17 columns × 14 rows × 500-ft square cells. Extent 8,500 × 7,000 feet (1.61 × 1.33 miles); this is a planning **estimate**, not an official measurement.
- The drawn scale bar must derive from actual projected XY coordinates and must agree with the labels. Avoid stretching an exported raster after rendering.
- Keep labels away from fine lot geometry. District colors should be transparent, not cover street/parcel boundaries.

## Source standards
- Official: verified D&D source/map; cite it and only claim what is supported.
- Derived: computed directly from source geometry (areas, lengths, coordinates, grid dimensions).
- Modelled: openly stated design estimate (lot sizes, utility layouts, terrain reconstructions, city size).
- Invented: campaign additions without an official source, such as speculative magical ley lines.
- Always document status and source per feature. Never present a chosen scale, assumed contour elevation, infrastructure route, or ley line as a canon survey.
- If input is only an image, digitize first and report alignment/trace error; do not claim 1-pixel preservation without vector geometry.

## Consistency tests
1. Confirm each layer uses the exact master ID/version/hash.
2. Check the same XY extent, grid pitch, map origin, north rotation, and map clipping rectangle for all sheets.
3. Overlay maps to compare walls, towers, gate centers, street corners, parks, banks, bridges, piers, and unique landmarks.
4. Geometry must not intersect water, walls, or public spaces where land parcels are proposed; explain permitted exceptions.
5. Test polygon closure and non-self-intersection; test network end points and gravity slope assumptions where applicable.
6. Produce both a PNG and editable SVG if the host supports them; include source/overlay data, verification notes and revision log.

## Five drawing sheets
- BP-01 City Master: roads, city districts, greenspace, public sites, walls, river, docks.
- BP-02 Cadastral Property: lots, blocks, public land, easements. No building footprints.
- BP-03 Topographical: 50-ft sample contours, spot heights, drainage, slopes. Use verified elevation data if available; otherwise mark the model as speculative.
- BP-04 Infrastructure: transport, water, sewer, storm drains, culverts, tunnels, service nodes, outfalls.
- BP-05 Arcane Ley Lines: proposed major/minor magical flows, nodes, nexuses, wards and anchors. Explicitly hypothetical unless supported by lore.
