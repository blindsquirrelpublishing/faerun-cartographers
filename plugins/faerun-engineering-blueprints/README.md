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

## Install in Codex

Use a Codex version with plugin marketplace support. Add this repository once, then install the engineering plugin:

```sh
codex plugin marketplace add https://github.com/blindsquirrelpublishing/faerun-cartographers.git
codex plugin add faerun-engineering-blueprints@faerun-cartographers
codex plugin list --json
```

If the marketplace is already added, refresh it before the install:

```sh
codex plugin marketplace upgrade faerun-cartographers
```

In a Codex client with a Plugins page, select the **Faerûn Cartographers** marketplace, then install and enable **Faerûn Engineering Blueprints**. The original cartography plugin is a separate install and is not required for these six skills. If a command is missing, check `codex plugin --help` and use a client with plugin support.

## Install in Claude Code

```text
/plugin marketplace add blindsquirrelpublishing/faerun-cartographers
/plugin install faerun-engineering-blueprints@faerun-cartographers
```

If already added, refresh with `/plugin marketplace update faerun-cartographers` before installing. Use `/plugin` to confirm the engineering plugin is installed and enabled.

## Find and use the six skills

Both hosts load the same six `skills/<name>/SKILL.md` files listed above. In a new Codex chat, open the skill picker with `$` and select the full skill name, such as `$faerun-engineering-blueprints:faerun-engineering-base`. Codex lists these skills with the `faerun-engineering-blueprints:` prefix. In Claude Code, type `/faerun-engineering-blueprints:` and select a skill, such as `/faerun-engineering-blueprints:faerun-engineering-base`.

For a read-only first check, ask the host to list all six engineering skill names and read `references/common-standard.md`, `references/master-schema.json`, and `scripts/validate_master.py` from the installed engineering plugin. Then ask it to run the validator on the bundled example. Check all six names against the table above. Record the host version, installed plugin version and results before calling an install tested.

Relative paths in each skill start at its own folder. `../../references/common-standard.md` points to the shared plugin standard. The base skill also links to the schema, validator and example with `../../` paths. Keep the **whole plugin folder** together; copying only `SKILL.md` files omits the shared files. Local Python 3 is needed for the validator; map output needs suitable drawing or image tools in the host.

## Package formats

- Root `plugin.json`: Agent Plugins 1.0 metadata with `extensions.com.openai.interface`; portable hosts load skills from `skills/`.
- `.codex-plugin/plugin.json`: Codex compatibility metadata with `skills: "./skills/"`, relative to the plugin root. Its identity, version and display fields match the root manifest.
- `.claude-plugin/plugin.json`: existing Claude metadata, using the same `skills/` directory.
- Repository `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`: both point to this complete plugin folder.

The engineering version remains **1.0.0** in all three manifests. This adds host metadata and setup notes to that release.

Format and command references: [OpenAI package guide](https://developers.openai.com/plugins/build/plugins) and [Codex command reference](https://learn.chatgpt.com/docs/developer-commands).

## Checks

From the repository root, run the package checks:

```sh
python3 scripts/validate_engineering_plugin.py
```

From this plugin folder, test the example geometry:

```bash
python3 scripts/validate_master.py examples/illustrative-master.json
```

The package checker tests JSON metadata, host catalog paths, all six skill names and local supporting file paths. It also runs the example validator. It does not install a plugin or prove that a host has loaded its skills. See [verification status](VERIFICATION.md) for the checks actually run.
