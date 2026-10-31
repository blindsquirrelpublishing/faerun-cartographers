---
name: faerun-civil-infrastructure-blueprint
description: Create a 2D civil infrastructure blueprint showing roads, piers, sewers, water supply, drainage, service tunnels and utility nodes on fixed geography.
metadata:
  author: Faerûn Cartographers
  version: "1.0.0"
---

# Faerûn Civil Infrastructure Blueprint (BP-04)

Read `../../references/common-standard.md` and load the exact geometry master.

## Overlay
- Street/bridge/dock hierarchy plus potable water, sewer, storm drainage, culverts, cisterns, possible service tunnels, shafts, valves, pump/collection sites and outfalls.
- Use blue solid for water mains, orange dashed for sewers, green dotted for storm drains, purple dashed for service tunnels, and labeled node circles. Do not rely on color alone.
- Show all utility networks as **nodes and connected segments**, each with ID, source, destination, type, flow direction, status and uncertainty.
- Keep wall rings, parks, parcels, major roads, piers, riverbanks and gate locations in precisely the same places as BP-01.

## Checks
1. Never draw pipes and drains on top of river as if streets, or unconnected tunnels that end arbitrarily.
2. Water and sewer crossing a bridge must be explicitly supported by a plausible conduit.
3. Gravity sewers need verified gradient; if terrain is not measured label flow **proposed**, not engineered fact.
4. Do not assume modern pressurized infrastructure for medieval/fantasy settings without stating design technology.
5. Verify that discharge points reach open water or treatment facilities and are not accidentally inland.

## Output
BP-04 Infrastructure Plan, PNG/SVG and utility-network JSON with node IDs, feature provenance, continuity report and assumptions.
