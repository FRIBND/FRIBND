Part of the AI/ML Technical Innovation at the FRIB Nuclear Data Group (nucleardata@frib.msu.edu).

**ENSDF-Agent:**
## Overview

The first AI Agent designed for Evaluated Nuclear Structure Data File (ENSDF) workflows.
Developed and refined through daily evaluation tasks at the Nuclear Data Group at the Facility for Rare Isotope Beams (FRIB).

Built on the open-source platforms Microsoft Visual Studio Code and GitHub Copilot, ENSDF-Agent integrates the power of rapidly advancing Large Language Models (LLMs) into the routine workflows of nuclear data evaluators.

## Development Timeline

- 2026-03-25: ENSDF-Agent Version 0.0.1, with 2 Agent Hooks and 24 Agent Skills, was released as an Agent Plugin via the Microsoft VS Code Plugin Marketplace.

- 2026-03-04: ENSDF-Agent became available as an open-source repository at https://github.com/FRIBND/ENSDF-Agent.

- 2026-02-23: Agent Skills were introduced as modular, portable capabilities that can be dynamically loaded into ENSDF-Agent to perform specific tasks within ENSDF workflows.

- 2025-11-14: The FRIBND Custom Agent Chat Mode was upgraded to ENSDF AI Agent.

- 2025-10-30: The FRIBND AI Agent was introduced at the 2025 U.S. Nuclear Data Program Meeting.

- 2025-08-14: The FRIBND AI Agent was first introduced at the 2025 Low Energy Community Meeting.

- 2025-08-06: The initial version of the FRIBND Custom Agent Chat Mode was posted within https://github.com/sunlijie-msu/ENSDF.

## Installation

1. Configure plugin marketplaces by clicking "Add Item" and entering `ENSDF-Agent/ENSDF-Agent` in the `setting(chat.plugins.marketplaces)` setting.
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



**Harness Engineering**
*   **Custom Instructions:** Rules, Standards, Conventions, Guidelines, Guardrails.
*   **Custom Agents:** Persona, Role, Behavior, Tools.
*   **Subagents:** Handoffs, Guided Sequential Workflows.
*   **Reusable Prompts:** Commands, Specific Tasks, Standardized Workflows.
*   **Agent Skills:** Portable and Interoperable Capabilities across Agents, Scripts, Templates, Examples, Reference Docs, Dynamic Loading Resources.
*   **Agent Hooks:** Deterministic Pre/Post-Action Commands.
*   **Agent Plugins:** Prepackaged Bundles of Customizations.

**Semantic Structuring**
(Role Assignment & Tag Wrapping) organizes the context across four primary types: System Messages, User Messages, Assistant Messages, and Tool Messages.
This framework ensures clear communication between the user, the AI, and the tools.

*   **System Message:**
    *   Base Identity
    *   Microsoft Safety Policies
    *   Agent Base Instructions
    *   Copilot Memories (Facts learned from interactions)
    *   Custom Instructions
    *   Agent Skills
    *   Custom Agents

*   **User Message:**
    *   Environment Info and Workspace Info
    *   Conversation Summary (Overview, Technical Foundation, Codebase Status, Problem Resolution, Progress Tracking, Active Work State, Recent Operations, Continuation Plan)
    *   Reminder Instructions
    *   User Requests
    *   Editor Context (File paths, Selections, Cursor position, Terminal)
    *   Explicit References (Attachments)
    *   Reusable Prompts

*   **Assistant Message:**
    *   Text Response (Talking)
    *   Tool Calls (Acting)

*   **Tool Message:**
    *   Results of Tool Calls (e.g., Data in ENS files)

**Structured Message Assembly Pipeline**
1.  File Discovery
2.  Parsing and Loading
3.  Tool Reference Resolution
4.  Semantic Structuring (Role Assignment & Tag Wrapping: System, User, Assistant, or Tool)
5.  Content Rendering
6.  Integration into a Raw Chat Message Array

**Endpoint Conversion**
*   **Payload Construction:** JSON Payload Built Based on the Message Array
*   **Model Configuration:** Model Selection, Tool Definitions (JSON Schema), Token Limits, Sampling Parameters (Temperature, Top_p), Streaming Options, and Thinking Budget

