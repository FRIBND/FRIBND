**AI-Assisted Nuclear Data Technical Innovation at FRIB**

**`FRIBND` AI Agent:**
The first AI Agent designed for Evaluated Nuclear Structure Data File (ENSDF) 80-column formatting has been developed and refined through daily evaluation tasks at the Facility for Rare Isotope Beams (FRIB) Nuclear Data Group.

Built on the open-source platforms Microsoft Visual Studio Code and GitHub Copilot, FRIBND integrates rapidly evolving Large Language Models (LLMs) into the routine workflows of ENSDF evaluators. FRIBND AI Agent was first introduced at the 2025 Low Energy Community Meeting and 2025 U.S. Nuclear Data Program Meeting and is available and customizable to support the broader nuclear data community.

#### FRIBND AI Agent Architecture

**Context Engineering**
*   **Custom Instructions:** Rules, Standards, Conventions, Guidelines, Guardrails.
*   **Custom Agents:** Persona, Role, Behavior, Tools.
*   **Subagents:** Handoffs, Guided Sequential Workflows.
*   **Reusable Prompts:** Commands, Specific Tasks, Standardized Workflows.
*   **Agent Skills:** Portable and Interoperable Capabilities across Agents, Scripts, Templates, Examples, Reference Docs, Dynamic Loading Resources.

**Semantic Structuring**
(Role Assignment & Tag Wrapping) organizes the context across four primary types: System Messages, User Messages, Assistant Messages, and Tool Messages. This framework ensures clear communication between the user, the AI, and the tools.

*   **System Message:**
    *   Base Identity
    *   Microsoft Safety Policies
    *   Agent Base Instructions
    *   Copilot Memories (Facts Learned from Interactions)
    *   Custom Instructions
    *   Agent Skills
    *   Custom Agents

*   **User Message:**
    *   Environment Info and Workspace Info
    *   Conversation Summary (Overview, Technical Foundation, Codebase Status, Problem Resolution, Progress Tracking, Active Work State, Recent Operations, Continuation Plan)
    *   Reminder Instructions
    *   User Requests
    *   Editor Context (Paths, Selections, Cursor, Terminal)
    *   Chat Variables (Attachments)
    *   Reusable Prompts

*   **Assistant Message:**
    *   Text Response (Talking)
    *   Tool Calls (Acting)

*   **Tool Message:**
    *   Results of Tool Calls (e.g., Data in 80-Column ENSDF Files)

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
