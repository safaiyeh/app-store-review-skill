"""Packaging checks that catch incomplete releases and broken bundled references."""
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_release_versions_and_notes_agree(self):
        def read_json(name):
            return json.loads((ROOT / name).read_text(encoding="utf-8"))

        version = read_json("metadata.json")["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertEqual(read_json(".codex-plugin/plugin.json")["version"], version)
        self.assertEqual(read_json(".claude-plugin/plugin.json")["version"], version)
        self.assertEqual(read_json(".claude-plugin/marketplace.json")["plugins"][0]["version"], version)
        frontmatter = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
        self.assertEqual(re.search(r'^  version: "([^"]+)"$', frontmatter, re.M)[1], version)
        issue_template = (ROOT / ".github/ISSUE_TEMPLATE/skill-feedback.yml").read_text(encoding="utf-8")
        self.assertIn(f'placeholder: "{version}"', issue_template)
        self.assertTrue((ROOT / f"release-notes/v{version}.md").is_file())

    def test_bundled_markdown_links_resolve(self):
        documents = [ROOT / "README.md", ROOT / "SKILL.md"]
        for directory in ("references", "rules", "release-notes", "tests/scenarios"):
            documents.extend((ROOT / directory).glob("*.md"))
        for document in documents:
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
                parts = urlsplit(link)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                with self.subTest(document=document.relative_to(ROOT), link=link):
                    target = (document.parent / unquote(parts.path)).resolve()
                    self.assertTrue(target.is_relative_to(ROOT), "Bundled link escapes the package")
                    self.assertTrue(target.exists(), "Missing bundled resource")

    def test_plugins_bundle_the_skill_root(self):
        codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        claude = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(codex["skills"], "./")
        self.assertEqual(claude["plugins"][0]["source"], "./")
        for name in ("SKILL.md", "references/asc-setup.md", "references/metadata-audit.md",
                     "references/metadata-fixes.md"):
            self.assertTrue((ROOT / name).is_file())


if __name__ == "__main__":
    unittest.main()
