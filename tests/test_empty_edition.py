"""The reset must leave no inherited content or stale generated routes."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build
from collection import check_links
from publish import stage_publication


class EmptyEditionTests(unittest.TestCase):
    def test_complete_build_clears_old_routes_and_does_not_fetch_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / "site", root / "site")
            fixtures = {"books.json": {"version": 1, "books": []},
                        "collection.json": {"version": 1, "chapters": [], "topics": [], "entries": []},
                        "formalizations.json": {"version": 1, "entries": []}}
            for filename, data in fixtures.items():
                (root / filename).write_text(json.dumps(data))
            stale = root / "_site" / "tag" / "OLDTAG" / "index.html"
            stale.parent.mkdir(parents=True)
            stale.write_text("Old mathematical content")
            chunks = root / "_site" / "search-data"
            chunks.mkdir()
            (chunks / "000.json").write_text('[{"text": "Old theorem"}]')
            with patch.object(build, "ROOT", root), patch.object(build, "fetch_source") as fetch, patch.object(build.subprocess, "check_output", return_value="a" * 40):
                build.build(fetch=True)
            fetch.assert_not_called()
            site = root / "_site"
            self.assertFalse(stale.exists())
            self.assertFalse(chunks.exists())
            inventory = json.loads((site / "collection.json").read_text())
            for key in ("chapters", "topics", "entries"):
                self.assertEqual(inventory[key], [])
            self.assertEqual(json.loads((site / "search.json").read_text()), [])
            self.assertEqual(json.loads((site / "formalizations.json").read_text())["entries"], [])
            self.assertEqual(json.loads((site / "upstream.json").read_text())["sources"], [])
            self.assertFalse((site / "assets" / "mathjax").exists())
            for page in site.rglob("*.html"):
                soup = BeautifulSoup(page.read_text(), "html.parser")
                self.assertNotIn("Old mathematical content", soup.get_text())
                self.assertFalse(soup.select("[data-gerby-tag], [data-load-comments], [data-comment-term]"))
                self.assertNotIn("MingchenXia", str(soup))
                self.assertNotIn("mathjax/tex-chtml.js", str(soup))
            self.assertIn("No chapters have been added yet.", (site / "index.html").read_text())
            check_links(site)
            stage_publication(site, root / "docs")
            check_links(root / "docs")


if __name__ == "__main__":
    unittest.main()
