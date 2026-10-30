# Faerûn Cartographers

42 map skills by Murray Fife, bundled as one plugin so shared map rules and style files stay together.

## Use

Attach a source map and name the style you want. The skills cover towns, terrain, parcels, ink, watercolor, tactical maps, and hex maps. Image work needs a host with image tools. Exact map checks may need local Python and traced geometry. This package supplies instructions and supporting files, not an image server.

## Install after publication

Add the GitHub repository as a plugin marketplace in a supported client. For Codex CLI:

```sh
codex plugin marketplace add https://github.com/blindsquirrelpublishing/faerun-cartographers.git
```

Then select Faerûn Cartographers from that marketplace.

## Atlas-First workflow

Start settlement projects with **faerun-atlas-first-workflow**. Create and refine the illustrated town atlas, approve its layout, then build matching map types from that same base. Reuse an approved atlas when one already exists.

[Workflow skill](plugins/faerun-cartographers/skills/faerun-atlas-first-workflow/SKILL.md) · [Full workflow](plugins/faerun-cartographers/skills/faerun-atlas-first-workflow/references/atlas-first-workflow.md)

## Included skills

- **faerun-atlas-first-workflow**: Refine and approve the illustrated town atlas before creating shared geometry, matching map types and scenic views.

- **black-ink-contour-atlas**: Precise pen-only overhead atlas with light terrain contours. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **black-ink-simple-reference**: Unadorned top-down pen drawing like hand-drafted building plan. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **bold-roof-ink**: Expressive tabletop cartography with black roof outlines and dark shadows. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **colored-property-topography**: Cadastral and terrain overlays together. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **comic-flat-color**: Bold illustrated top-down map with flat saturated color. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **dense-walled-watercolor**: Detailed packed city with walls, colored roofs and numbered sites. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **detailed-ink-overhead**: Highly detailed pen-and-ink rooftops, gardens and riverbanks. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **elevated-lookout-view**: Low-to-high oblique view from a named tower, hill or manor. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **faerun-cartographers-plat-standard**: Apply deterministic Faerûn Cartographers Plat Standard v1.8 framing to all fantasy cartography plates, with locked 19:13 sheet geometry, fixed 20% sidebar and 15/15/60/10 zones, sans-serif typography, A–Q / 1–16 square-cell reference grid, official circular stamp, fixed compass and verified scale bar.
- **faerun-map-geometry-master**: Required source-of-truth workflow for converting any supplied settlement map into alternate fantasy cartographic styles while preserving geographic landmarks and geometry.
- **fantasy-cartography-core**: Coordinate source maps and enforce positional fidelity.
- **fantasy-city-district-map**: Neighborhood and ward borders on an accurate street plan using source-faithful map data, without inventing geographic or route features.
- **fantasy-dungeon-underground-map**: Underground floorplans, rooms, stairs and passages using source-faithful map data, without inventing geographic or route features.
- **fantasy-gis-cadastral**: Flat 2D parcel and land-use map.
- **fantasy-ground-level-view**: Ground-eye town illustration from registered geometry.
- **fantasy-hex-world-map**: Create or restyle fantasy world and regional maps as classic tabletop hex maps, with earth-tone terrain cells, repeated ink terrain symbols, black landmark icons, serif place names, and a boxed title. Use for world maps, regional maps, campaign hex maps, and requests to match the supplied hex terrain reference while keeping source geography in place.
- **fantasy-historical-map**: Older borders, roads, settlements and names with dates using source-faithful map data, without inventing geographic or route features.
- **fantasy-hypsometric-elevation-map**: Elevation colors, relief and sea depth using source-faithful map data, without inventing geographic or route features.
- **fantasy-illustrated-town-atlas**: Colorful hand-painted fantasy town atlas.
- **fantasy-isometric-settlement-map**: Fixed-angle 3D-looking town illustration anchored to plan using source-faithful map data, without inventing geographic or route features.
- **fantasy-land-cover-map**: Forest, grassland, cropland, marsh, scrub, rock and water using source-faithful map data, without inventing geographic or route features.
- **fantasy-land-water-boundary-master**: Produce and validate authoritative land/water topology masks for Faerûn Cartographers, safeguarding shorelines, islands, and river connections between cadastral, topographic, political, land-cover, and illustrated map plates.
- **fantasy-physical-geography-map**: Mountains, hills, plains, forests, wetlands and water using source-faithful map data, without inventing geographic or route features.
- **fantasy-political-map**: Political jurisdictions, borders, cities and capitals using source-faithful map data, without inventing geographic or route features.
- **fantasy-topographic-survey**: Terrain contour and elevation map.
- **fantasy-trade-transportation-map**: Existing travel corridors, cargo flows and distance evidence using source-faithful map data, without inventing geographic or route features.
- **fantasy-watercolor-landscape**: Oblique watercolor scene from accurate terrain and plan.
- **gis-cadastral**: Orthographic survey-like plan with precise footprints, parcels, roads, land-use colors, grid, legend. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **ground-level-city-view**: Eye-level view from a stated observer location and facing direction. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **historic-ink-parchment**: Old-school monochrome parchment with sparse town linework. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **minimalist-footprints**: Architectural schematic with simple rectangles and polygons. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **numbered-gazetteer**: Classic D&D numbered town map with a location key. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **pictorial-watercolor-gazetteer**: Soft watercolor and ink, pale circular location numbers and legend. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **simple-walled-ink-sketch**: Sparse hand-drawn black ink plan like a classic module inset. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **tactical-clean-grid**: Minimal clean top-down tabletop grid map. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **tactical-detailed-grid**: High-detail orthographic overhead RPG tactical map with faint square grid. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **topographic-colored**: Hypsometric color bands and indexed elevation contours. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **topographic-contours-only**: Pure terrain contour linework without settlement features. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **topographic-ghosted**: Topography dominates while source roads and footprints appear faintly. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **watercolor-closeup**: Rich warm watercolor close-up of a selected town neighborhood. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.
- **watercolor-town-atlas**: Illustrated fantasy settlement atlas, colorful and detailed. Convert any supplied geographic map to this style while preserving all mapped landmarks and geometry.


## Install in Claude Code

Add the marketplace, then install the plugin:

```text
/plugin marketplace add blindsquirrelpublishing/faerun-cartographers
/plugin install faerun-cartographers@faerun-cartographers
```

If the marketplace was already added, refresh it first with `/plugin marketplace update faerun-cartographers`.

The plugin includes all 42 skills. Image output depends on the image tools available in your Claude setup.

## Example gallery

The original 41 map skills include fictional Alderford style samples. The Atlas-First workflow includes written steps and checks. These are visual examples, not checked survey maps or approved standard plats.

### black-ink-contour-atlas

[Skill](plugins/faerun-cartographers/skills/black-ink-contour-atlas/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/black-ink-contour-atlas/assets/example.jpg)

![Sample: black-ink-contour-atlas](plugins/faerun-cartographers/skills/black-ink-contour-atlas/assets/example.jpg)

### black-ink-simple-reference

[Skill](plugins/faerun-cartographers/skills/black-ink-simple-reference/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/black-ink-simple-reference/assets/example.jpg)

![Sample: black-ink-simple-reference](plugins/faerun-cartographers/skills/black-ink-simple-reference/assets/example.jpg)

### bold-roof-ink

[Skill](plugins/faerun-cartographers/skills/bold-roof-ink/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/bold-roof-ink/assets/example.jpg)

![Sample: bold-roof-ink](plugins/faerun-cartographers/skills/bold-roof-ink/assets/example.jpg)

### colored-property-topography

[Skill](plugins/faerun-cartographers/skills/colored-property-topography/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/colored-property-topography/assets/example.jpg)

![Sample: colored-property-topography](plugins/faerun-cartographers/skills/colored-property-topography/assets/example.jpg)

### comic-flat-color

[Skill](plugins/faerun-cartographers/skills/comic-flat-color/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/comic-flat-color/assets/example.jpg)

![Sample: comic-flat-color](plugins/faerun-cartographers/skills/comic-flat-color/assets/example.jpg)

### dense-walled-watercolor

[Skill](plugins/faerun-cartographers/skills/dense-walled-watercolor/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/dense-walled-watercolor/assets/example.jpg)

![Sample: dense-walled-watercolor](plugins/faerun-cartographers/skills/dense-walled-watercolor/assets/example.jpg)

### detailed-ink-overhead

[Skill](plugins/faerun-cartographers/skills/detailed-ink-overhead/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/detailed-ink-overhead/assets/example.jpg)

![Sample: detailed-ink-overhead](plugins/faerun-cartographers/skills/detailed-ink-overhead/assets/example.jpg)

### elevated-lookout-view

[Skill](plugins/faerun-cartographers/skills/elevated-lookout-view/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/elevated-lookout-view/assets/example.jpg)

![Sample: elevated-lookout-view](plugins/faerun-cartographers/skills/elevated-lookout-view/assets/example.jpg)

### faerun-cartographers-plat-standard

[Skill](plugins/faerun-cartographers/skills/faerun-cartographers-plat-standard/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/faerun-cartographers-plat-standard/assets/example.jpg)

![Sample: faerun-cartographers-plat-standard](plugins/faerun-cartographers/skills/faerun-cartographers-plat-standard/assets/example.jpg)

### faerun-map-geometry-master

[Skill](plugins/faerun-cartographers/skills/faerun-map-geometry-master/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/faerun-map-geometry-master/assets/example.jpg)

![Sample: faerun-map-geometry-master](plugins/faerun-cartographers/skills/faerun-map-geometry-master/assets/example.jpg)

### fantasy-cartography-core

[Skill](plugins/faerun-cartographers/skills/fantasy-cartography-core/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-cartography-core/assets/example.jpg)

![Sample: fantasy-cartography-core](plugins/faerun-cartographers/skills/fantasy-cartography-core/assets/example.jpg)

### fantasy-city-district-map

[Skill](plugins/faerun-cartographers/skills/fantasy-city-district-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-city-district-map/assets/example.jpg)

![Sample: fantasy-city-district-map](plugins/faerun-cartographers/skills/fantasy-city-district-map/assets/example.jpg)

### fantasy-dungeon-underground-map

[Skill](plugins/faerun-cartographers/skills/fantasy-dungeon-underground-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-dungeon-underground-map/assets/example.jpg)

![Sample: fantasy-dungeon-underground-map](plugins/faerun-cartographers/skills/fantasy-dungeon-underground-map/assets/example.jpg)

### fantasy-gis-cadastral

[Skill](plugins/faerun-cartographers/skills/fantasy-gis-cadastral/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-gis-cadastral/assets/example.jpg)

![Sample: fantasy-gis-cadastral](plugins/faerun-cartographers/skills/fantasy-gis-cadastral/assets/example.jpg)

### fantasy-ground-level-view

[Skill](plugins/faerun-cartographers/skills/fantasy-ground-level-view/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-ground-level-view/assets/example.jpg)

![Sample: fantasy-ground-level-view](plugins/faerun-cartographers/skills/fantasy-ground-level-view/assets/example.jpg)

### fantasy-hex-world-map

[Skill](plugins/faerun-cartographers/skills/fantasy-hex-world-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-hex-world-map/assets/example.jpg)

![Sample: fantasy-hex-world-map](plugins/faerun-cartographers/skills/fantasy-hex-world-map/assets/example.jpg)

### fantasy-historical-map

[Skill](plugins/faerun-cartographers/skills/fantasy-historical-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-historical-map/assets/example.jpg)

![Sample: fantasy-historical-map](plugins/faerun-cartographers/skills/fantasy-historical-map/assets/example.jpg)

### fantasy-hypsometric-elevation-map

[Skill](plugins/faerun-cartographers/skills/fantasy-hypsometric-elevation-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-hypsometric-elevation-map/assets/example.jpg)

![Sample: fantasy-hypsometric-elevation-map](plugins/faerun-cartographers/skills/fantasy-hypsometric-elevation-map/assets/example.jpg)

### fantasy-illustrated-town-atlas

[Skill](plugins/faerun-cartographers/skills/fantasy-illustrated-town-atlas/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-illustrated-town-atlas/assets/example.jpg)

![Sample: fantasy-illustrated-town-atlas](plugins/faerun-cartographers/skills/fantasy-illustrated-town-atlas/assets/example.jpg)

### fantasy-isometric-settlement-map

[Skill](plugins/faerun-cartographers/skills/fantasy-isometric-settlement-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-isometric-settlement-map/assets/example.jpg)

![Sample: fantasy-isometric-settlement-map](plugins/faerun-cartographers/skills/fantasy-isometric-settlement-map/assets/example.jpg)

### fantasy-land-cover-map

[Skill](plugins/faerun-cartographers/skills/fantasy-land-cover-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-land-cover-map/assets/example.jpg)

![Sample: fantasy-land-cover-map](plugins/faerun-cartographers/skills/fantasy-land-cover-map/assets/example.jpg)

### fantasy-land-water-boundary-master

[Skill](plugins/faerun-cartographers/skills/fantasy-land-water-boundary-master/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-land-water-boundary-master/assets/example.jpg)

![Sample: fantasy-land-water-boundary-master](plugins/faerun-cartographers/skills/fantasy-land-water-boundary-master/assets/example.jpg)

### fantasy-physical-geography-map

[Skill](plugins/faerun-cartographers/skills/fantasy-physical-geography-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-physical-geography-map/assets/example.jpg)

![Sample: fantasy-physical-geography-map](plugins/faerun-cartographers/skills/fantasy-physical-geography-map/assets/example.jpg)

### fantasy-political-map

[Skill](plugins/faerun-cartographers/skills/fantasy-political-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-political-map/assets/example.jpg)

![Sample: fantasy-political-map](plugins/faerun-cartographers/skills/fantasy-political-map/assets/example.jpg)

### fantasy-topographic-survey

[Skill](plugins/faerun-cartographers/skills/fantasy-topographic-survey/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-topographic-survey/assets/example.jpg)

![Sample: fantasy-topographic-survey](plugins/faerun-cartographers/skills/fantasy-topographic-survey/assets/example.jpg)

### fantasy-trade-transportation-map

[Skill](plugins/faerun-cartographers/skills/fantasy-trade-transportation-map/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-trade-transportation-map/assets/example.jpg)

![Sample: fantasy-trade-transportation-map](plugins/faerun-cartographers/skills/fantasy-trade-transportation-map/assets/example.jpg)

### fantasy-watercolor-landscape

[Skill](plugins/faerun-cartographers/skills/fantasy-watercolor-landscape/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/fantasy-watercolor-landscape/assets/example.jpg)

![Sample: fantasy-watercolor-landscape](plugins/faerun-cartographers/skills/fantasy-watercolor-landscape/assets/example.jpg)

### gis-cadastral

[Skill](plugins/faerun-cartographers/skills/gis-cadastral/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/gis-cadastral/assets/example.jpg)

![Sample: gis-cadastral](plugins/faerun-cartographers/skills/gis-cadastral/assets/example.jpg)

### ground-level-city-view

[Skill](plugins/faerun-cartographers/skills/ground-level-city-view/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/ground-level-city-view/assets/example.jpg)

![Sample: ground-level-city-view](plugins/faerun-cartographers/skills/ground-level-city-view/assets/example.jpg)

### historic-ink-parchment

[Skill](plugins/faerun-cartographers/skills/historic-ink-parchment/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/historic-ink-parchment/assets/example.jpg)

![Sample: historic-ink-parchment](plugins/faerun-cartographers/skills/historic-ink-parchment/assets/example.jpg)

### minimalist-footprints

[Skill](plugins/faerun-cartographers/skills/minimalist-footprints/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/minimalist-footprints/assets/example.jpg)

![Sample: minimalist-footprints](plugins/faerun-cartographers/skills/minimalist-footprints/assets/example.jpg)

### numbered-gazetteer

[Skill](plugins/faerun-cartographers/skills/numbered-gazetteer/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/numbered-gazetteer/assets/example.jpg)

![Sample: numbered-gazetteer](plugins/faerun-cartographers/skills/numbered-gazetteer/assets/example.jpg)

### pictorial-watercolor-gazetteer

[Skill](plugins/faerun-cartographers/skills/pictorial-watercolor-gazetteer/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/pictorial-watercolor-gazetteer/assets/example.jpg)

![Sample: pictorial-watercolor-gazetteer](plugins/faerun-cartographers/skills/pictorial-watercolor-gazetteer/assets/example.jpg)

### simple-walled-ink-sketch

[Skill](plugins/faerun-cartographers/skills/simple-walled-ink-sketch/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/simple-walled-ink-sketch/assets/example.jpg)

![Sample: simple-walled-ink-sketch](plugins/faerun-cartographers/skills/simple-walled-ink-sketch/assets/example.jpg)

### tactical-clean-grid

[Skill](plugins/faerun-cartographers/skills/tactical-clean-grid/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/tactical-clean-grid/assets/example.jpg)

![Sample: tactical-clean-grid](plugins/faerun-cartographers/skills/tactical-clean-grid/assets/example.jpg)

### tactical-detailed-grid

[Skill](plugins/faerun-cartographers/skills/tactical-detailed-grid/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/tactical-detailed-grid/assets/example.jpg)

![Sample: tactical-detailed-grid](plugins/faerun-cartographers/skills/tactical-detailed-grid/assets/example.jpg)

### topographic-colored

[Skill](plugins/faerun-cartographers/skills/topographic-colored/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/topographic-colored/assets/example.jpg)

![Sample: topographic-colored](plugins/faerun-cartographers/skills/topographic-colored/assets/example.jpg)

### topographic-contours-only

[Skill](plugins/faerun-cartographers/skills/topographic-contours-only/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/topographic-contours-only/assets/example.jpg)

![Sample: topographic-contours-only](plugins/faerun-cartographers/skills/topographic-contours-only/assets/example.jpg)

### topographic-ghosted

[Skill](plugins/faerun-cartographers/skills/topographic-ghosted/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/topographic-ghosted/assets/example.jpg)

![Sample: topographic-ghosted](plugins/faerun-cartographers/skills/topographic-ghosted/assets/example.jpg)

### watercolor-closeup

[Skill](plugins/faerun-cartographers/skills/watercolor-closeup/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/watercolor-closeup/assets/example.jpg)

![Sample: watercolor-closeup](plugins/faerun-cartographers/skills/watercolor-closeup/assets/example.jpg)

### watercolor-town-atlas

[Skill](plugins/faerun-cartographers/skills/watercolor-town-atlas/SKILL.md) · [Full image](plugins/faerun-cartographers/skills/watercolor-town-atlas/assets/example.jpg)

![Sample: watercolor-town-atlas](plugins/faerun-cartographers/skills/watercolor-town-atlas/assets/example.jpg)

