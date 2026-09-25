"""Check the evaluation harness without contacting ASC or requiring credentials."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

FIXTURES = Path(__file__).resolve().parent / "fixtures"
VERSION_FILE = "version/2.4.0/en-US.json"


class FakeASCTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "evaluation"
        initialized = subprocess.run(
            [sys.executable, str(FIXTURES / "fake_asc.py"), "--init", str(self.root)],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(initialized.returncode, 0, initialized.stderr)
        self.target = json.loads((self.root / "target.json").read_text(encoding="utf-8"))
        self.flags = ["--app", self.target["appId"], "--app-info", self.target["appInfoId"],
                      "--version", self.target["version"], "--platform", self.target["platform"]]

    def asc(self, *args, code=0):
        result = subprocess.run(
            [sys.executable, str(self.root / "bin/asc"), "--profile", self.target["profile"], *args],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, code, result.stderr + result.stdout)
        return json.loads(result.stdout)

    def capture(self, name):
        directory = self.root / name
        receipt = self.asc("metadata", "pull", *self.flags, "--dir", str(directory), "--output", "json")
        receipt_file = self.root / (name + "-receipt.json")
        receipt_file.write_text(json.dumps(receipt), encoding="utf-8")
        self.assertEqual(receipt["versionId"], self.target["versionId"])
        self.assertEqual(receipt["fileCount"], 4)
        return {path.relative_to(directory).as_posix(): json.loads(path.read_text(encoding="utf-8"))
                for path in directory.rglob("*.json")}

    def test_simulator_dry_run_and_partial_failure_contract(self):
        baseline = self.capture("baseline")
        payload = self.root / "payload"
        file = payload / VERSION_FILE
        file.parent.mkdir(parents=True)
        proposed = {"description": "Free journaling; map exports require a purchase.",
                    "whatsNew": "Added paid map exports. Fixed a crash."}
        file.write_text(json.dumps(proposed), encoding="utf-8")
        preview = self.asc("metadata", "apply", *self.flags, "--dir", str(payload), "--dry-run")
        self.assertEqual(len(preview["operations"]), 2)
        self.assertFalse((self.root / "partial-write-injected").exists())
        self.assertEqual(self.capture("after-preview"), baseline)
        self.asc("metadata", "apply", *self.flags, "--dir", str(payload), code=1)
        partial = self.capture("partial")
        self.assertEqual(partial[VERSION_FILE]["description"], proposed["description"])
        self.assertEqual(partial[VERSION_FILE]["whatsNew"], baseline[VERSION_FILE]["whatsNew"])
        remaining = self.root / "remaining"
        remaining_file = remaining / VERSION_FILE
        remaining_file.parent.mkdir(parents=True)
        remaining_file.write_text(json.dumps({"whatsNew": proposed["whatsNew"]}), encoding="utf-8")
        preview = self.asc("metadata", "apply", *self.flags, "--dir", str(remaining), "--dry-run")
        self.assertEqual([item["field"] for item in preview["operations"]], ["whatsNew"])
        self.asc("metadata", "apply", *self.flags, "--dir", str(remaining))
        after = self.capture("after")
        self.assertEqual(after[VERSION_FILE]["whatsNew"], proposed["whatsNew"])
        changes = {(path, field) for path, fields in baseline.items()
                   for field, value in fields.items() if after[path][field] != value}
        self.assertEqual(changes, {(VERSION_FILE, "description"), (VERSION_FILE, "whatsNew")})

    def test_fake_account_requires_target_and_exposes_coverage_gaps(self):
        self.assertIn("explicit", self.asc("metadata", "pull", code=1)["error"])
        first_page = self.asc("localizations", "list", "--version", self.target["versionId"])
        all_pages = self.asc("localizations", "list", "--version", self.target["versionId"], "--paginate")
        self.assertEqual(len(first_page["data"]), 1)
        self.assertTrue(first_page["links"]["next"])
        self.assertEqual(len(all_pages["data"]), 2)
        self.assertIn("403", self.asc("age-rating", "view", code=1)["error"])
        self.asc("release", "--app", self.target["appId"], code=1)
        self.assertFalse((self.root / "partial-write-injected").exists())

    @unittest.skipUnless(os.environ.get("ASC_OFFLINE_TESTS") == "1",
                         "Optional installed-ASC validation is disabled")
    def test_export_fixture_with_installed_cli_offline(self):
        result = subprocess.run(["asc", "metadata", "validate", "--dir", str(FIXTURES / "metadata"),
                                 "--output", "json"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIsInstance(json.loads(result.stdout), dict)


if __name__ == "__main__":
    unittest.main()
