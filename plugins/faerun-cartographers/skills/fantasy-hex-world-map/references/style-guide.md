# Style Guide and Build Notes

## Reference traits

The bundled image is a tall crop of a regional hex map behind article text. The clear upper part supplies the best visual evidence. Use its general drawing language, not its exact named locations, title, page crop, credits, or lower dark shading. It does not establish a numeric scale, full world extent, map projection, or the meaning of the red line.

## Terrain and mark key

Use these as working colors, not measured samples. Adjust for legibility and match them across plates.

| Feature | Base color | Ink treatment |
| --- | --- | --- |
| Open ground | Straw #C3B861 | Sparse short grass strokes |
| Hills | Ochre #B39A50 | Two or three low curved ridges |
| Mountains | Brown #977443 | Steep small peaks with dark side shading |
| Forest | Green #7E9E4B | Tight groups of round tree crowns and short trunks |
| Marsh | Gray green #81977B | Repeated reed tufts and small wet-ground strokes |
| Sea and lake | Blue #548A9B | Calm flat fill; slight texture if useful |
| Grid | Brown olive #75613C | Thin lines, low contrast |
| Sites | Near black #211D17 | Simple castle, cave, ruin, tower, or town marks |
| Known border | Muted red #B74435 | Clear solid line, explained in the key |
| Title panel | Cream #EFE0BB | Double dark border and small corner details |

Use varied strokes within a small set of repeated symbols. Keep the page flat and plan-based; let terrain marks read as pictorial map signs. Avoid glossy 3D terrain, aerial photos, large buildings, deep cast shadows, glowing labels, harsh digital gradients, and heavy stains. Do not mix forest icons at several unrelated scales.

## Grid notes

For a flat-top hex centered at (cx, cy), use vertices (cx + s cos(k pi/3), cy + s sin(k pi/3)), k = 0 through 5. Use center positions x = x0 + 1.5 s q and y = y0 + sqrt(3) s (r + q/2) for integer axial coordinates q and r. Clip the lattice at the map window; do not distort it. Keep cell IDs if used stable between exports and zooms.

At world scale, state the projection or treat the layout as a fictional flat game board. A flat regular hex grid does not give equal ground distances across an entire globe under every projection. Do not assert planet-wide distance accuracy without a defined model.

Preserve master vectors for water, roads, and borders. Terrain cells may use the dominant cover, while coast and river lines stay continuous. Use mixed edge cells if needed. Do not turn ships into islands, thicken rivers into land gaps, merge nearby islands, or connect separate waters just to make tile fills simpler.

## Layer order

1. Paper base and map clipping frame.
2. Land and water master fills.
3. Terrain cell fills, clipped at shorelines.
4. Light hex grid.
5. Terrain ink symbols.
6. Rivers, roads, and borders with separate line styles.
7. Site icons and label halos, then names.
8. Title, key, north, scale, and outer frame.

## Prompt pattern

Use after loading the required source and style images. Replace brackets with known brief values. Omit unsupported fields rather than making up measurements.

> Draw [area] as a classic tabletop hex map. Use source reference 1 for geography and reference 2 only for drawing style. Preserve the source extent, coastlines, islands, river branches and mouths, named sites, roads, and borders. Use one flat-top hex lattice, thin brown olive grid lines, straw plains, ochre hills, brown mountain cells, green forest cells, dull green marsh, and muted blue water. Fill cells with small repeated pen-drawn terrain signs. Use black site silhouettes, clear dark serif place names with light cream halos, a cream double-bordered title panel, and a thin outer frame. Keep [known features] at their source positions. Include only supplied names and known routes. Use a red line only for [confirmed meaning, if any]. Leave off the article text, credits, website, screen controls, and dark overlay seen in the style sample. [Known scale and north, or scale status.] Keep all names readable and all water connections intact.

For a plat, replace standalone framing and serif instructions with the loaded plat template's frame and type rules. For a new made-up world, replace the source-preservation wording with the approved world brief; retain the style and review rules.

## Final checks

- Verify all cells share one side length and orientation.
- Compare map control points and major water features to the source.
- Confirm the grid does not shift geography or imply a false scale.
- Confirm terrain symbols match the key and remain clear at final size.
- Check site count, names, positions, and label collisions.
- Check line meanings; do not present a boundary as a river or road.
- Check the scale statement against a measured bar, if shown.
- Confirm the title and key do not hide important map features.
- Confirm none of the sample's article overlay or unrelated names appears.
- Record missing evidence, uncertain features, and any cell-based generalization.

## Example requests

- Restyle this supplied regional map with classic hex terrain signs; keep all coastlines and towns in place.
- Build a new fictional world map with three continents, using this hex-map style and no fixed hex distance.
- Make a regional hex map from the supplied official source and place it within the current Faerûn Cartographers plat.
