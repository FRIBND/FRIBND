**ENSDF-Agent:** Part of the AI/ML Technical Innovation at the FRIB Nuclear Data Group (nucleardata@frib.msu.edu).

## Overview

The first AI Agent designed for Evaluated Nuclear Structure Data File (ENSDF) workflows.
Developed and refined through daily evaluation tasks at the Nuclear Data Group at the Facility for Rare Isotope Beams (FRIB).

Built on the open-source platforms Microsoft Visual Studio Code and GitHub Copilot, ENSDF-Agent integrates the power of rapidly advancing Large Language Models (LLMs) into the routine workflows of nuclear data evaluators.

## Development Timeline

- 2026-03-25: ENSDF-Agent Version 0.0.1, with 2 Agent Hooks and 24 Agent Skills, was released as an Agent Plugin via the Microsoft VS Code Plugin Marketplace.

- 2026-03-04: ENSDF-Agent became available as an open-source repository at https://github.com/FRIBND/ENSDF-Agent.

- 2026-02-23: Agent Skills were introduced as modular, portable capabilities that can be dynamically loaded into ENSDF-Agent to perform specific tasks within ENSDF workflows.

- 2025-11-14: The ENSDF-Agent Custom Agent Chat Mode was upgraded to ENSDF-Agent.

- 2025-10-30: ENSDF-Agent was introduced at the 2025 U.S. Nuclear Data Program Meeting.

- 2025-08-14: ENSDF-Agent was first introduced at the 2025 Low Energy Community Meeting.

- 2025-08-06: The initial version of the ENSDF-Agent Custom Agent Chat Mode was posted within https://github.com/sunlijie-msu/ENSDF.

## Installation

1. Configure plugin marketplaces by clicking "Add Item" and entering `FRIBND/ENSDF-Agent` in the `setting(chat.plugins.marketplaces)` setting.
2. Open the Extensions view (`kb(workbench.view.extensions)`) and enter `@agentPlugins ENSDF-Agent` in the search field.
   - Alternatively, select the **More Actions** (three dots) icon in the Extensions sidebar and choose **Views** > **Agent Plugins**.
3. Click **Install** to install the ENSDF-Agent Plugin in your user profile.

## Caveats

As of 2026-03-26:
- VS Code does not support installing Agent Plugins in a specific workspace.
- VS Code Agent Plugins do not support workspace-level `copilot-instructions.md` shipped with the plugin.
- VS Code Agent Plugins do not support Agent-scoped hooks.
- Agent Skills performance and reliability vary based on the underlying LLM capabilities and the complexity of the task.


#### ENSDF-Agent Architecture
<img width="2752" height="1536" alt="Architecture" src="https://github.com/user-attachments/assets/63ee8a24-89d5-45df-b60e-237094add77f" />

## What's Shipped

### Agent

- `ENSDF-Agent`: AI Agent for Evaluated Nuclear Structure Data File (ENSDF) 80-column fixed format, exact column positioning, data formatting, and editing with absolute precision and numerical rigor.

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