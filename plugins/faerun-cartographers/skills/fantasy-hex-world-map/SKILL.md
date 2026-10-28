---
name: fantasy-hex-world-map
description: Create or restyle fantasy world and regional maps as classic tabletop hex maps, with earth-tone terrain cells, repeated ink terrain symbols, black landmark icons, serif place names, and a boxed title. Use for world maps, regional maps, campaign hex maps, and requests to match the supplied hex terrain reference while keeping source geography in place.
---

# Fantasy Hex World Map

## Load the reference

Open `assets/style-reference.png` before drawing. Read `references/style-guide.md` for the terrain key, layer order, prompt pattern, and review checks. Treat the image as a style sample, not as a source for a new map's place names or geography. Ignore the large article title, author credit, website text, dark lower overlay, and screen controls. Do not fill the hidden part of the sample from guesswork.

## Set the map brief

Identify the area, source map, known features, extent, north, output size, and any stated scale. Use the user's requested world or region; do not assume the sample's small area is a whole world. Match the source extent and aspect ratio by default. With a named existing setting, use supplied evidence and official sources where needed. Mark unsupported details as unknown. Do not pass new details off as official lore.

For an existing map, load `fantasy-cartography-core` and `faerun-map-geometry-master` when available. Use `fantasy-land-water-boundary-master` for maps with coasts, islands, or river mouths. Keep coasts, water connections, landforms, settlements, landmarks, roads, and borders at their source positions. Retain a common coordinate frame and source IDs across plates. Report missing source data if it blocks the map.

For a new made-up world, create geography only within the user's brief. Keep land, rivers, drainage, terrain bands, and travel links coherent. Distinguish these design choices from sourced facts. Ask only for details that block useful work; otherwise state brief assumptions and proceed.

## Build the hex layer

Use one regular flat-top hex lattice with a shared origin, cell size, and orientation. Keep the grid continuous across terrain types and sheet edges. Do not stretch individual cells to fit the map. Use thin muted brown or olive strokes; keep the lines visible but weaker than place names and landmarks.

Keep geography as a separate master layer. Use cell fills and symbols to express terrain without moving source features. Let coasts and rivers cross cells at their true positions. For a deliberately snapped game board, keep the original layer, record the cell assignment rule, and label the result as generalized. Do not silently snap exact source geography.

State the scale only when supported. For regular flat-top hexes with side length s, flat-to-flat distance is sqrt(3) times s; point-to-point width is 2 times s. State what any hex distance means. Do not assume a fixed six-mile hex. Use world-scale terrain groups on a world map and finer symbols on a regional map; avoid settlement-level detail on a whole-world sheet.

## Apply the style

Use warm ochre and tan hills, brown mountains, green forest cells, dull green marsh, and muted blue water. Use small repeated pen symbols: shaded mountain peaks, low hill strokes, round clustered trees, and reed tufts. Keep symbols centered in their cells, with a consistent size and spacing. Use near-black silhouettes for castles, caves, ruins, and other key sites. Separate site icons from terrain marks.

Use dark bold serif place labels with a restrained cream halo where needed. Give broad region names lower density and wider spacing. Use a cream boxed title with a thin double dark border and small corner details. Add a thin outer frame and light paper grain. Use a muted red line only for a border or route with a known meaning; explain it in the key. Do not add a red line just because one appears in the sample.

Use a small key for terrain and site marks that need explanation. Add north and scale only when known. Keep the map readable without a key for every repeated hill or tree.

## Choose a rendering method

For a visual concept or free illustration, use the available image-generation tool with the source map and bundled style sample as separate references. Load its image skill first. Explain each reference's role in the prompt. Do not claim exact geography from an unchecked generated image.

For exact cell geometry, source fidelity, or clean small text, build the grid, fills, labels, frame, scale, and source layers with SVG or another code-based drawing tool. Use reusable terrain symbols. If adding generated art, keep it below the locked source layers. Do not use image generation for a precise scale bar, measured boundaries, or final label placement.

For a Faerûn Cartographers plat, load the actual `faerun-cartographers-plat-standard` skill and use its template and assets. Apply this hex style inside the map window. Let the plat skill control the 19:13 sheet, sidebar, fonts, compass, seal, square reference grid, and scale. Its font rules take precedence over this style's serif labels. Keep any square reference grid visually distinct from the terrain hexes. Use the sample-style boxed title only on standalone maps, not as a second title on a plat. Never claim plat compliance without checking against the actual standard.

## Review and deliver

Check source alignment, water connections, cell shape, terrain key, label spelling, label overlap, symbol spacing, border meaning, and scale. Inspect the full rendered map and a close view. Use the checklist in the style guide. Fix failures before delivery. State any known limits that remain.

Save the finished map and any requested editable source using the current file workflow. Include a short note on source evidence, scale status, and any generalized features. Do not claim exact source fidelity or standards compliance without checking it.
