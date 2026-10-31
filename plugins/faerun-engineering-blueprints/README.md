# Engineering Map Skills v1.0

This plugin adds **six engineering blueprint skills** to the existing Faerûn Cartographers marketplace, without changing its original plugin.

| Sheet | Skill | Main drawing |
|---|---|---|
| Base | `faerun-engineering-base` | Shared, measured geometry master and grid checks |
| BP-01 | `faerun-city-master-blueprint` | Walled town plan and greenspace |
| BP-02 | `faerun-cadastral-property-blueprint` | Property parcels, blocks, public land |
| BP-03 | `faerun-topographical-engineering-blueprint` | Terrain, contours and drainage |
| BP-04 | `faerun-civil-infrastructure-blueprint` | Civil roads, pipes, drains, utilities |
| BP-05 | `faerun-arcane-leyline-blueprint` | Proposed ley routes, nexus nodes and wards |

All drawings use the approved source geometry, a common 2D north-up coordinate grid, **feet and miles**, square cells, 19:13 sheet, 20% information panel on the left and map filling the right 80%.

Start with `faerun-engineering-base` and approve the traced vector geometry before producing or re-producing the five maps. **Do not infer exact survey geometry or official lore from a generated image.** The default Mirabar scale is a modelled 500 ft per cell, across 17×14 cells.

The five approved Mirabar screenshots serve as style references in the original ZIP from the project. This GitHub release includes complete instructions, a source schema, sample master and a validator; the image files are not embedded in this repository edition.

Test the example geometry:
```bash
python3 scripts/validate_master.py examples/illustrative-master.json
```
