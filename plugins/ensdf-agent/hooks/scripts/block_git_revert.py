import json
import re
import sys


TERMINAL_TOOLS = {
    "execute/runInTerminal",
    "runInTerminal",
    "run_in_terminal",
}


def emit(payload):
    sys.stdout.write(json.dumps(payload))


def load_input():
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def is_blocked_command(command):
    normalized = re.sub(r"\s+", " ", command.strip())
    return any(
        re.search(pattern, normalized, re.IGNORECASE)
        for pattern in (
            r"\bgit\s+restore\b",
            r"\bgit\s+checkout\s+--\s",
            r"\bgit\s+checkout\s+\.",
        )
    )


def main():
    payload = load_input()
    if not payload:
        return

    if payload.get("tool_name") not in TERMINAL_TOOLS:
        return

    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command")
    if not isinstance(command, str) or not command.strip():
        return

    if not is_blocked_command(command):
        return

    reason = (
        "BLOCKED by ENSDF-Agent security hook.\n\n"
        "From ENSDF-Agent.agent.md (Error Recovery Protocol — Mandatory):\n"
        "  \"Nuclear data tasks require high-precision work, not typical\n"
        "  software development tasks. Do NOT use `git restore` or\n"
        "  `git checkout` to fix mistakes. You must identify and fix errors\n"
        "  carefully to maintain absolute rigor.\"\n\n"
        "Mandatory steps:\n"
        "  1. Identify the root cause through analysis, not reversion.\n"
        "  2. Fix errors using replace_string_in_file or multi_replace_string_in_file.\n"
        "  3. Validate with column_calibrate.py and ensdf_1line_ruler.py.\n"
        "  4. Let user review diffs in VS Code diff viewer before accepting changes.\n\n"
        "Rationale: Reversion bypasses the VS Code diff viewer, eliminating\n"
        "the mandatory human review layer that catches LLM formatting mistakes\n"
        "in nuclear data files."
    )

    emit(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
    )


if __name__ == "__main__":
    main()