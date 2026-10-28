from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from publish import project_unchanged, stage_publication


class PublicationTests(unittest.TestCase):
    def commit(self, root):
        subprocess.run(["git", "add", "--all"], cwd=root, check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "-c", "user.name=Gerby test", "-c", "user.email=test@example.invalid", "commit", "--no-gpg-sign", "-m", "Test revision"], cwd=root, check=True, stdout=subprocess.DEVNULL)
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()

    def test_publication_commit_does_not_invalidate_its_own_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init"], cwd=root, check=True, stdout=subprocess.DEVNULL)
            (root / "scripts").mkdir()
            (root / "docs").mkdir()
            (root / "documentation").mkdir()
            (root / "scripts/build.py").write_text("source v1")
            (root / "documentation/deployment.md").write_text("Authored documentation")
            (root / "docs/index.html").write_text("Old edition")
            built_revision = self.commit(root)
            (root / "docs/index.html").write_text("New edition")
            self.commit(root)
            self.assertTrue(project_unchanged(built_revision, root))
            (root / "documentation/deployment.md").write_text("Updated publication rules")
            self.commit(root)
            self.assertFalse(project_unchanged(built_revision, root))

    def test_changed_build_code_requires_a_rebuild(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init"], cwd=root, check=True, stdout=subprocess.DEVNULL)
            (root / "build.py").write_text("v1")
            built_revision = self.commit(root)
            (root / "build.py").write_text("v2")
            self.commit(root)
            self.assertFalse(project_unchanged(built_revision, root))
            self.assertFalse(project_unchanged("--all", root))
            self.assertFalse(project_unchanged("a" * 40, root))

    def test_only_the_generated_folder_is_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site, destination = root / "_site", root / "docs"
            site.mkdir()
            destination.mkdir()
            (destination / "obsolete.html").write_text("Old content")
            authored = root / "documentation"
            authored.mkdir()
            (authored / "deployment.md").write_text("Keep the publication instructions")
            with self.assertRaises(ValueError):
                stage_publication(site, destination)
            self.assertTrue((destination / "obsolete.html").is_file())
            (site / ".nojekyll").touch()
            (site / "collection.json").write_text('{"entries": []}')
            (site / "upstream.json").write_text('{"sources": [{"commit": "exact-source"}]}')
            (site / "index.html").write_text("New edition")
            stage_publication(site, destination)
            self.assertFalse((destination / "obsolete.html").exists())
            self.assertEqual((destination / "index.html").read_text(), "New edition")
            self.assertEqual((authored / "deployment.md").read_text(), "Keep the publication instructions")

    def test_empty_edition_removes_old_content_without_source_revisions(self):
        import json
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site, destination = root / '_site', root / 'docs'
            site.mkdir()
            destination.mkdir()
            (destination / 'old-mathematics.html').write_text('Old theorem')
            (site / '.nojekyll').touch()
            (site / 'index.html').write_text('GMT Stack')
            (site / 'collection.json').write_text(json.dumps({'chapters': [], 'topics': [], 'entries': []}))
            (site / 'upstream.json').write_text(json.dumps({'sources': []}))
            stage_publication(site, destination)
            self.assertFalse((destination / 'old-mathematics.html').exists())
            self.assertEqual((destination / 'index.html').read_text(), 'GMT Stack')

    def test_nonempty_edition_still_requires_source_revisions(self):
        import json
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory) / '_site'
            site.mkdir()
            (site / '.nojekyll').touch()
            (site / 'upstream.json').write_text(json.dumps({'sources': []}))
            for field in ('chapters', 'topics', 'entries'):
                collection = {'chapters': [], 'topics': [], 'entries': []}
                collection[field] = [{'title': 'Untracked content'}]
                (site / 'collection.json').write_text(json.dumps(collection))
                with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'empty collection'):
                    stage_publication(site, Path(directory) / 'docs')


if __name__ == "__main__":
    unittest.main()
