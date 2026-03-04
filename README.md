# FRIBND AI Agent for ENSDF

## Overview
The first AI agent dedicated to Evaluated Nuclear Structure Data File (ENSDF) 80-column formatting has been developed and refined through daily evaluation tasks at the Facility for Rare Isotope Beams (FRIB) Nuclear Data Group. 

Built on the open-source platforms Microsoft Visual Studio Code and GitHub Copilot, these tools integrate rapidly evolving Large Language Models (LLMs) into the routine workflows of ENSDF evaluators. The tools were first introduced at the 2025 Low Energy Community Meeting and are available and customizable to support the broader nuclear data community.

## AI/ML Implementation & Context Management
The implementation incorporates ENSDF-specific context management for AI using three key components. These components are assembled with GitHub Copilot base instructions to ensure all AI actions comply with strict ENSDF 80-column standards.

*   **FRIBND Custom Agent:** Defines core behavior, tool invocation, and structured agentic workflows:
    *   *Workflow:* Understand $\rightarrow$ Investigate $\rightarrow$ Plan $\rightarrow$ Implement $\rightarrow$ Debug $\rightarrow$ Test $\rightarrow$ Iterate $\rightarrow$ Validate
*   **Repository Custom Instructions:** Defines ENSDF 80-column format rules, notation standards, and quality assurance measures.
*   **Specialized Agent Skills:** Provides tailored expertise for specific tasks, including automated data extraction from publications (utilizing built-in vision capabilities) and precise data entry alignment.

---

## FRIBND AI Agent Architecture

### Context Engineering
*   **Custom Instructions:** Rules, standards, conventions, guidelines, and guardrails.
*   **Custom Agents:** Persona, role, behavior, and tools.
*   **Subagents:** Handoffs and guided sequential workflows.
*   **Reusable Prompts:** Commands, specific tasks, and standardized workflows.
*   **Agent Skills:** Portable and interoperable capabilities across agents, scripts, templates, examples, reference documentation, and resources.

### Semantic Structuring
Semantic structuring (Role Assignment & Tag Wrapping) organizes context across four primary message types. This framework ensures clear communication between the user, the AI, and the tools.

*   **System Message:**
    *   Base identity
    *   Microsoft safety policies
    *   Agent base instructions
    *   Copilot memories (facts learned from interactions)
    *   Custom instructions
    *   Agent skills
    *   Custom agents
*   **User Message:**
    *   Environment and workspace information
    *   Conversation summary: Overview, technical foundation, codebase status, problem resolution, progress tracking, active work state, recent operations, and continuation plan
    *   Reminders (user requests)
    *   Editor context: Edited file paths, selections, cursor position, and terminal data
    *   Chat variables (attachments)
    *   Reusable prompts
*   **Assistant Message:**
    *   Text response (Talking)
    *   Tool call (Acting)
*   **Tool Message:**
    *   Result of tool calls (e.g., data formatted in 80-column `.ens` files)

### Structured Message Assembly Pipeline
1.  File Discovery
2.  Parsing and Loading
3.  Tool Reference Resolution
4.  Semantic Structuring (Role Assignment & Tag Wrapping: System, User, Assistant, or Tool)
5.  Content Rendering
6.  Integration into a Raw Chat Message Array

### Endpoint Conversion
*   **Payload Construction:** Builds a JSON payload based on the message array.
*   **Model Configuration:** Defines model selection, tool definitions (JSON schema), token limits, sampling parameters (temperature, top_p), streaming options, and thinking budgets.
