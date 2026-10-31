# Faerûn 3D Orthographic Views

Skill: `fantasy-3d-orthographic-view`.

Create 3D parallel-projection fantasy exterior views based on an approved cadastral map or map geometry master. Buildings and terrain gain height without moving walls, gates, streets, structures, rivers or landmarks. Unmeasured architecture is labeled interpretive. Complements `faerun-architectural-cutaways`, which shows interiors and underground levels.

## Claude Code
```text
/plugin marketplace add blindsquirrelpublishing/faerun-cartographers
/plugin marketplace update faerun-cartographers
/plugin install faerun-orthographic-views@faerun-cartographers
```

## Codex
```sh
codex plugin marketplace add https://github.com/blindsquirrelpublishing/faerun-cartographers.git
codex plugin marketplace upgrade faerun-cartographers
codex plugin add faerun-orthographic-views@faerun-cartographers
```

Open the skill picker and select `fantasy-3d-orthographic-view`. The actual v1.8 plat template is required only when a plat is requested. No host installation test is claimed.
