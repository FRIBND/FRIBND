# FRIBND Plugin

ENSDF-focused GitHub Copilot agent plugin for nuclear structure data evaluation workflows at FRIB.

## Installation

### VS Code Agent Plugins

1. Open the Extensions view.
2. Search for `@agentPlugins`.
3. Add the `FRIBND/FRIBND` marketplace if it is not already configured.
4. Install the `fribnd` plugin.

### Install From Source

Use `Chat: Install Plugin From Source` and enter:

```text
https://github.com/FRIBND/FRIBND
```

## What's Included

### Agent

- `FRIBND`: ENSDF-focused editing and validation agent for 80-column nuclear data workflows.

### Skills

- 24 ENSDF domain skills covering data entry, QA, gamma-property checks, reconciliation, comments, reaction equations, multipolarity, and related evaluator workflows.

### Hooks

- `PreToolUse`: blocks dangerous git revert-style operations.
- `PostToolUse`: runs ENSDF validation guidance after tool activity.

## Repository Layout

- `agents/`: custom agents bundled with the plugin.
- `skills/`: installable ENSDF skills.
- `scripts/`: bundled helper scripts referenced by the agent and skills.
- `hooks.json`: plugin hook configuration.

## Source

This plugin is published from the FRIBND repository:

https://github.com/FRIBND/FRIBND

## License

MIT