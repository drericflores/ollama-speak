import re
import tomllib
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class PackagingMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (PROJECT_ROOT / "pyproject.toml").open("rb") as stream:
            cls.pyproject = tomllib.load(stream)

    def test_project_identity_and_entry_point(self):
        project = self.pyproject["project"]
        self.assertEqual("ollama-speak", project["name"])
        self.assertEqual("README.md", project["readme"])
        self.assertEqual(
            "ollama_speak:run",
            project["scripts"]["ollama-speak"],
        )

    def test_metadata_version_matches_module(self):
        source = (PROJECT_ROOT / "ollama_speak.py").read_text(encoding="utf-8")
        match = re.search(
            r'^__version__\s*=\s*["\']([^"\']+)["\']',
            source,
            flags=re.MULTILINE,
        )
        self.assertIsNotNone(match)
        self.assertEqual(self.pyproject["project"]["version"], match.group(1))

    def test_declared_project_files_exist(self):
        for relative_path in (
            "LICENSE",
            "README.md",
            "INSTALL.md",
            "MANIFEST.in",
            "ollama_speak.py",
        ):
            with self.subTest(path=relative_path):
                self.assertTrue((PROJECT_ROOT / relative_path).is_file())

    def test_runtime_has_no_third_party_python_dependencies(self):
        self.assertEqual([], self.pyproject["project"].get("dependencies"))


if __name__ == "__main__":
    unittest.main()
