---
name: ensdf-core-rules
description: >
  Use this skill for general ENSDF editing, formatting, validation, or fixed-column
  work when no narrower ENSDF skill fully covers the task. Applies the shared
  FRIBND baseline rules for 80-column field positioning, uncertainty notation,
  ascending energy ordering, edit-validate-repeat workflow, and compliance
  checklist reporting.
argument-hint: [ENSDF file or task]
---

# ENSDF Core Rules

## Purpose

Provide a plugin-native home for the shared FRIBND ENSDF rules that are bundled
in `copilot-instructions.md`. Use this skill as the default baseline whenever an
ENSDF task is general-purpose and not already better covered by a narrower,
domain-specific skill.

## Use This Skill When

- Editing ENSDF records without a more specific skill already matching the task
- Validating 80-column field placement and left-justification rules
- Applying uncertainty notation and scientific-notation conventions
- Checking L-record and G-record ascending energy order
- Enforcing the mandatory edit-validate-repeat workflow
- Producing the required compliance checklist for ENSDF work

## Mandatory Baseline Rules

- Treat ENSDF as a strict 80-column fixed-format system with 1-based columns
- Preserve exact field boundaries and left-justify values within their fields
- Keep L-records and attached G-records in ascending energy order
- Distinguish data-record uncertainty fields from comment-line `{In}` notation
- Follow the one-edit, one-validation cycle for every ENSDF line change
- Use existing validation scripts before creating any new helper script
- Report a truthful compliance checklist and disclose any remaining limitations

## Required Validation Workflow

For ENSDF line edits, run these checks as applicable:

1. `python scripts/ensdf_1line_ruler.py --line "..."` after each edited line
2. `python scripts/column_calibrate.py "file.ens"` before and after edit batches
3. `python scripts/check_gamma_ordering.py "file.ens"` when L/G ordering matters

## Source Of Truth

The complete FRIBND reference text remains bundled in `copilot-instructions.md`
at the plugin root. This skill exists because VS Code agent plugins publish
agents, skills, hooks, slash commands, and MCP servers, but not workspace-level
`copilot-instructions.md` as an automatically applied customization primitive.