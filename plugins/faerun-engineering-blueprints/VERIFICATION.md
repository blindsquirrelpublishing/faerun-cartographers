# Engineering plugin verification

Checks run on October 31, 2026 against the updated local source.

| Check | Result |
|---|---|
| Root manifest against Agent Plugins 1.0 JSON Schema | Passed using jsonschema 4.26.0 and the published schema |
| Root, Codex and Claude identity/version | Passed; all use faerun-engineering-blueprints 1.0.0 |
| Both repository marketplace paths | Passed; both resolve to the complete engineering plugin |
| Six SKILL.md files | Passed the bundled skill metadata checker |
| Shared standard, schema, validator and example paths | Passed; all resolve within the engineering plugin |
| Example against master-schema.json | Passed |
| Example validator in source and both installed copies | Passed; four features, no errors |
| Codex CLI 0.166.0 local marketplace registration and plugin add | Passed; returned installedPath and version 1.0.0 |
| Codex plugin list -m faerun-cartographers --json | Installed and enabled |
| Codex app-server skills/list | All six names listed with plugin prefix; all enabled |
| Codex compatibility-only local package (root manifest omitted in test copy) | Plugin add passed; temporary test entry removed afterward |
| Claude Code 2.1.316 manifest validation | Passed; directory submission checks separately flag missing license and icon |
| Claude local marketplace add and plugin install | Passed |
| Claude plugin list and plugin details | Enabled; inventory lists all six skills |
| Installed file bytes compared to source in both hosts | Passed for all files present at install time |
| Original cartography plugin and Claude marketplace files | Unchanged from base commit 8899244a375cbed6776d6a386edcb0c8f1ed332c |

These are actual **local marketplace installation tests**, not just JSON checks. Codex used the portable manifest with its OpenAI extension; a separate test exercised the compatibility-only package. Claude used its existing manifest. No authenticated model session was used and no map was generated. No GitHub-source installation or desktop/mobile installation was tested. The added verification notes and final README wording do not change skill files or manifests tested above.

## Repeat the local tests

From a full repository checkout:

```sh
python3 scripts/validate_engineering_plugin.py
codex plugin marketplace add .
codex plugin add faerun-engineering-blueprints@faerun-cartographers --json
codex plugin list -m faerun-cartographers --json
claude plugin validate plugins/faerun-engineering-blueprints
claude plugin marketplace add .
claude plugin install faerun-engineering-blueprints@faerun-cartographers
claude plugin details faerun-engineering-blueprints@faerun-cartographers
```

Use the install paths returned by each host to check all six `skills/*/SKILL.md` files and run `scripts/validate_master.py examples/illustrative-master.json` from the installed plugin folder. Keep references, scripts and examples with the skill tree.
