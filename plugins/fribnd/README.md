# FRIBND Agent Plugin

AI/ML Technical Innovation at FRIB Nuclear Data Group

FRIBND AI Agent:

The first AI Agent designed for Evaluated Nuclear Structure Data File (ENSDF) workflows has been developed and refined through daily evaluation tasks at the Nuclear Data Group at the Facility for Rare Isotope Beams (FRIB).

Built on the open-source platforms Microsoft Visual Studio Code and GitHub Copilot, the FRIBND AI agent integrates rapidly evolving Large Language Models (LLMs) into the routine 80-column editing and formatting workflows currently used by ENSDF evaluators. The FRIBND AI Agent was first introduced at the 2025 Low Energy Community Meeting and 2025 U.S. Nuclear Data Program Meeting.

FRIBND is available as an open-source repository at https://github.com/FRIBND/FRIBND

To support the broader nuclear data community, a customizable version of FRIBND with 25 agent skills has been released in the Microsoft Visual Studio Code Agent Plugin Marketplace.

Note on instructions: the plugin bundles `copilot-instructions.md` as reference material, but VS Code agent plugins do not publish workspace-level instructions as an automatically applied plugin primitive. FRIBND exposes the same baseline behavior through the `FRIBND` agent and the `ensdf-core-rules` skill.

## Installation

### VS Code Agent Plugins

1. Open the Extensions view.
2. Search for `@agentPlugins`.
3. Add the `FRIBND/FRIBND` marketplace if it is not already configured.
4. Install the `fribnd` plugin.

This plugin is distributed through the `FRIBND/FRIBND` marketplace repository.

## What's Included

### Agent

- `FRIBND`: ENSDF-focused editing and validation agent for 80-column nuclear data workflows.

### Skills

- 25 ENSDF domain skills covering general ENSDF rules, data entry, QA, gamma-property checks, reconciliation, comments, reaction equations, multipolarity, and related evaluator workflows.

### Hooks

- `PreToolUse`: blocks dangerous git revert-style operations.
- `PostToolUse`: runs ENSDF validation guidance after tool activity.

## Repository Layout

- `agents/`: custom agents bundled with the plugin.
- `skills/`: installable ENSDF skills.
- `copilot-instructions.md`: bundled reference instructions shipped with the plugin payload.
- `scripts/`: bundled helper scripts referenced by the agent and skills.
- `hooks.json`: plugin hook configuration.

## Source

This plugin is published from the FRIBND repository:

https://github.com/FRIBND/FRIBND

Contact: nucleardata@frib.msu.edu

## License

MIT