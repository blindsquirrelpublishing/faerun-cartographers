# Faerûn Dungeon Cartography

Three linked skills for converting a source dungeon map into a 2D schematic, playable battle map and isometric cutaway. The [Dungeon Geometry Master](references/dungeon-geometry-master.md) is the shared source of truth.

## Workflow
1. Trace the original source, identify rooms and passage graph, and mark uncertain scale and levels.
2. Review and approve the geometry master.
3. Create the 2D schematic and verify connections.
4. Create playable room maps with explicit grid assumptions.
5. Create an isometric cutaway from the SAME geometry master.
6. Compare room ids, passage edges, water and level transitions before publication.

## Install in Claude Code
```text
/plugin marketplace add blindsquirrelpublishing/faerun-cartographers
/plugin marketplace update faerun-cartographers
/plugin install faerun-dungeon-cartography@faerun-cartographers
```

These are instructions for image-capable tools, not a 3D mesh generator. An old adventure sketch with no verified scale must remain not-to-scale until measurements are supplied or an adaptation is approved.
