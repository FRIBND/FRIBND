# FRIBND Agent Plugin

FRIBND is a GitHub Copilot agent plugin for Evaluated Nuclear Structure Data File (ENSDF) work.

It packages:
- the `FRIBND` custom agent
- ENSDF-specific skills under `skills/`
- validation and safeguard hook scripts under `scripts/`

## Layout

```text
plugin/
  plugin.json
  hooks.json
  copilot-instructions.md
  agents/
  skills/
  scripts/
  temp/
```

## Local Validation

For this workspace, `.vscode/settings.json` registers:
- the local marketplace at `marketplace/`
- the local plugin root at `plugin/`

## Publish

To publish this plugin as its own source-installable repository, move the contents of this directory to the root of a dedicated Git repository.