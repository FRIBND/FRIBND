# FRIBND AI Agent Plugin

Part of the AI/ML Technical Innovation Project at the FRIB Nuclear Data Group.

## Overview

The first AI Agent designed for Evaluated Nuclear Structure Data File (ENSDF) workflows.
Developed and refined through daily evaluation tasks at the Nuclear Data Group at the Facility for Rare Isotope Beams (FRIB).

Built on the open-source platforms Microsoft Visual Studio Code and GitHub Copilot, the FRIBND AI Agent integrates rapidly evolving Large Language Models (LLMs) into the routine 80-column editing and formatting workflows used by ENSDF evaluators.

## Development Timeline

- 2026-03-25: FRIBND Version 0.0.1, with 2 Agent Hooks and 24 Agent Skills, was released as an Agent Plugin via the Microsoft VS Code Plugin Marketplace.

- 2026-03-04: FRIBND became available as an open-source repository at https://github.com/FRIBND/FRIBND.

- 2026-02-23: Agent Skills were introduced as modular, portable capabilities that can be dynamically loaded into the FRIBND AI Agent to perform specific tasks within ENSDF workflows.

- 2025-11-14: The FRIBND Custom Agent Chat Mode was upgraded to the FRIBND Custom AI Agent.

- 2025-10-30: The FRIBND AI Agent was introduced at the 2025 U.S. Nuclear Data Program Meeting.

- 2025-08-14: The FRIBND AI Agent was first introduced at the 2025 Low Energy Community Meeting.

- 2025-08-06: The initial version of the FRIBND Custom Agent Chat Mode was posted within https://github.com/sunlijie-msu/ENSDF.

## Installation

1. Configure plugin marketplaces by clicking "Add Item" and entering `FRIBND/FRIBND` in the `setting(chat.plugins.marketplaces)` setting.
2. Open the Extensions view (`kb(workbench.view.extensions)`) and enter `@agentPlugins FRIBND` in the search field.
   - Alternatively, select the **More Actions** (three dots) icon in the Extensions sidebar and choose **Views** > **Agent Plugins**.
3. Click **Install** to install the FRIBND Plugin in your user profile.

## Caveats

As of 2026-03-26:
- VS Code does not support installing Agent Plugins in a specific workspace.
- VS Code Agent Plugins do not support workspace-level `copilot-instructions.md` shipped with the plugin.
- VS Code Agent Plugins do not support Agent-scoped hooks.
- Agent Skills performance and reliability vary based on the underlying LLM capabilities and the complexity of the task.

## What's Shipped

### Agent

- `FRIBND`: AI Agent for Evaluated Nuclear Structure Data File (ENSDF) 80-column fixed format, exact column positioning, data formatting, and editing with absolute precision and numerical rigor.

### Skills

- 25 ENSDF domain skills covering general ENSDF rules, data entry, QA, gamma-property checks, reconciliation, comments, reaction equations, multipolarity, and related evaluator workflows.

### Hooks

- `PreToolUse`: blocks dangerous git revert-style operations.
- `PostToolUse`: runs ENSDF validation guidance after tool activity.

## Repository Layout

- `agents/`: Custom agents bundled with the plugin.
- `skills/`: Installable ENSDF skills.
- `scripts/`: Bundled helper scripts referenced by the agent and skills.
- `hooks.json`: Plugin hook configuration.

Contact: nucleardata@frib.msu.edu

## License

MIT