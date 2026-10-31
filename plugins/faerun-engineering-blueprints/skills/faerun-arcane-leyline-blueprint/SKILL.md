---
name: faerun-arcane-leyline-blueprint
description: Create a speculative or lore-backed 2D magical ley line plan with currents, nexuses, ward rings and anchors without altering the city plan.
metadata:
  author: Faerûn Cartographers
  version: "1.0.0"
---

# Faerûn Arcane Ley Line Blueprint (BP-05)

Read `../../references/common-standard.md`; load the fixed master geometry from the other plans.

## Lore status
**Never present a new Mirabar ley line, nexus or arcane ward network as official D&D lore without a verifiable source.** Use a visible note: *Hypothetical arcane survey / campaign-designed overlay*. Preserve any actual campaign source offered by the user separately from official lore.

## Overlay
- Major courses: electric-violet or bright-blue paths. Minor routes: dotted violet. Nodes/nexuses: fine gold circular symbols. Ward circles: faint cyan. Gate anchors: gold squares. Flow: thin arrows.
- Soft glows must never hide lot boundaries, wall rings, parks, road alignment, bridges or riverbanks. Magical lines are overlays, not city-planning changes.
- Arcane elements have unique node IDs, XY feet coordinates, type, strength/capacity if defined, classification and source/status; network edges link existing nodes or stated external crossings.
- Gate wards must anchor to existing approved gates. A proposed central nexus at the High Seat or a garden is a **design choice**, not presumed canon.
- Use separate line patterns for buried, surface or uncertain magic; do not invent reliable energy units.

## Checks
1. Verify existing river, wall, road, garden, dock and parcel geometry remained identical.
2. Each line has an origin/destination node, plausible termination and documented flow.
3. Show unstable zones, wards and surges only if the scenario supports them.
4. Label this BP-05 rather than BP-01 and include the hypothesis/source statement prominently.

## Output
BP-05 Arcane Ley Line Plan, PNG/SVG and `ley-network.json` with node list, links, source and confidence.
