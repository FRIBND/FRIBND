from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PYTHON_SYNC = REPO_ROOT / "sync_plugin_from_local_agent.py"
POWERSHELL_SYNC = REPO_ROOT / "sync-plugin-from-local-agent.ps1"

MANAGED_FILES = {
    Path("agents/ENSDF-Agent.agent.md"): "source-agent\n",
    Path("copilot-instructions.md"): "source-instructions\n",
    Path("hooks/scripts/validate_ens.py"): "print('validate')\n",
    Path("prompts/example.prompt.md"): "prompt\n",
    Path("scripts/tool.py"): "print('tool')\n",
    Path("skills/example/SKILL.md"): "skill\n",
}

PRESERVED_PLUGIN_FILE = Path("hooks/scripts/block_git_revert.py")

EXCLUDED_SOURCE_FILES = {
    Path("docs/guide.md"): "docs should never sync\n",
    Path("temp/scratch.txt"): "temp should never sync\n",
    Path("scripts/__pycache__/tool.cpython-311.pyc"): "cache should never sync\n",
}

EXCLUDED_TARGET_FILES = {
    Path("docs/leftover.md"): "leftover docs\n",
    Path("temp/leftover.txt"): "leftover temp\n",
    Path("scripts/__pycache__/leftover.pyc"): "leftover cache\n",
}


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class SyncScriptFixture:
    def __init__(self) -> None:
        self._temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self._temp_dir.name)
        self.source = self.root / "source" / ".github"
        self.plugin = self.root / "plugin"

    def close(self) -> None:
        self._temp_dir.cleanup()

    def populate(self) -> None:
        for relative, content in MANAGED_FILES.items():
            write_file(self.source / relative, content)

        for relative, content in EXCLUDED_SOURCE_FILES.items():
            write_file(self.source / relative, content)

        for relative in (
            Path("agents/ENSDF-Agent.agent.md"),
            Path("copilot-instructions.md"),
            Path("hooks/scripts/validate_ens.py"),
            Path("prompts/example.prompt.md"),
            Path("scripts/tool.py"),
            Path("skills/example/SKILL.md"),
        ):
            write_file(self.plugin / relative, f"stale-{relative.as_posix()}\n")

        write_file(self.plugin / "scripts/stale_only.py", "remove me\n")
        write_file(self.plugin / PRESERVED_PLUGIN_FILE, "preserve me\n")
        write_file(self.plugin / "README.md", "plugin readme\n")
        write_file(self.plugin / "plugin.json", "{}\n")
        write_file(self.plugin / "hooks.json", "{}\n")

        for relative, content in EXCLUDED_TARGET_FILES.items():
            write_file(self.plugin / relative, content)


class SyncScriptTests(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.fixture = SyncScriptFixture()
        self.fixture.populate()

    def tearDown(self) -> None:
        self.fixture.close()

    def assert_synced_plugin_tree(self) -> None:
        for relative, content in MANAGED_FILES.items():
            self.assertTrue((self.fixture.plugin / relative).is_file(), relative.as_posix())
            self.assertEqual((self.fixture.plugin / relative).read_text(encoding="utf-8"), content)

        self.assertFalse((self.fixture.plugin / "scripts/stale_only.py").exists())
        self.assertTrue((self.fixture.plugin / PRESERVED_PLUGIN_FILE).is_file())
        self.assertEqual((self.fixture.plugin / PRESERVED_PLUGIN_FILE).read_text(encoding="utf-8"), "preserve me\n")

        for relative in EXCLUDED_SOURCE_FILES:
            self.assertFalse((self.fixture.plugin / relative).exists(), f"excluded source file synced: {relative.as_posix()}")

        for relative in EXCLUDED_TARGET_FILES:
            self.assertFalse((self.fixture.plugin / relative).exists(), f"excluded target file not cleaned: {relative.as_posix()}")

        self.assertFalse((self.fixture.plugin / "docs").exists())
        self.assertFalse((self.fixture.plugin / "temp").exists())

    def run_python_sync(self, dry_run: bool = False) -> subprocess.CompletedProcess[str]:
        command = [
            sys_executable(),
            str(PYTHON_SYNC),
            "--source-github-path",
            str(self.fixture.source),
            "--plugin-root",
            str(self.fixture.plugin),
        ]
        if dry_run:
            command.append("--dry-run")
        return subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=True)

    def run_powershell_sync(self, dry_run: bool = False) -> subprocess.CompletedProcess[str]:
        command = [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(POWERSHELL_SYNC),
            "-SourceGitHubPath",
            str(self.fixture.source),
            "-PluginRoot",
            str(self.fixture.plugin),
        ]
        if dry_run:
            command.append("-DryRun")
        return subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=True)

    def test_python_sync_dry_run_preserves_filesystem(self) -> None:
        result = self.run_python_sync(dry_run=True)
        self.assertIn("COPY   agents/ENSDF-Agent.agent.md", result.stdout)
        self.assertIn("REMOVE scripts/stale_only.py", result.stdout)
        self.assertTrue((self.fixture.plugin / "scripts/stale_only.py").exists())
        self.assertTrue((self.fixture.plugin / "docs/leftover.md").exists())

    def test_python_sync_applies_expected_changes(self) -> None:
        self.run_python_sync(dry_run=False)
        self.assert_synced_plugin_tree()

    def test_powershell_sync_applies_expected_changes(self) -> None:
        self.run_powershell_sync(dry_run=False)
        self.assert_synced_plugin_tree()


def sys_executable() -> str:
    return os.environ.get("PYTHON", os.sys.executable)


if __name__ == "__main__":
    unittest.main()