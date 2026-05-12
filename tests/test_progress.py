"""Tests for the persistence layer."""

import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from aws_ai_study.models import ProgressRecord
from aws_ai_study.progress import (
    load_progress,
    merge_with_bank,
    save_progress,
)


class TestLoadProgress(unittest.TestCase):

    def test_missing_file_returns_default(self):
        path = Path(tempfile.mkdtemp()) / "nonexistent.json"
        data = load_progress(path)
        self.assertEqual(data["version"], 1)
        self.assertEqual(data["records"], {})

    def test_corrupt_file_returns_default(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("not valid json {{{")
            path = Path(f.name)
        data = load_progress(path)
        self.assertEqual(data["version"], 1)
        path.unlink()

    def test_valid_file_loads(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"version": 1, "records": {"d1_001": {"question_id": "d1_001"}},
                       "created": "2026-04-27", "last_session": None,
                       "streak_days": 3, "last_study_date": "2026-04-26"}, f)
            path = Path(f.name)
        data = load_progress(path)
        self.assertEqual(data["streak_days"], 3)
        self.assertIn("d1_001", data["records"])
        path.unlink()


class TestSaveProgress(unittest.TestCase):

    def test_save_and_load_roundtrip(self):
        tmpdir = Path(tempfile.mkdtemp())
        path = tmpdir / "data" / "progress.json"
        data = {"version": 1, "records": {"d1_001": {"question_id": "d1_001"}},
                "created": "2026-04-27", "last_session": None,
                "streak_days": 0, "last_study_date": None}
        save_progress(data, path)
        loaded = load_progress(path)
        self.assertEqual(loaded["records"]["d1_001"]["question_id"], "d1_001")

    def test_creates_parent_directory(self):
        tmpdir = Path(tempfile.mkdtemp())
        path = tmpdir / "nested" / "dir" / "progress.json"
        save_progress({"version": 1, "records": {}}, path)
        self.assertTrue(path.exists())


class TestMergeWithBank(unittest.TestCase):

    def test_adds_new_questions(self):
        data = {"records": {}}
        data = merge_with_bank(data, ["d1_001", "d1_002"])
        self.assertIn("d1_001", data["records"])
        self.assertIn("d1_002", data["records"])

    def test_preserves_existing_records(self):
        data = {"records": {"d1_001": {"question_id": "d1_001", "times_seen": 5}}}
        data = merge_with_bank(data, ["d1_001", "d1_002"])
        self.assertEqual(data["records"]["d1_001"]["times_seen"], 5)

    def test_removes_stale_questions(self):
        data = {"records": {"d1_001": {"question_id": "d1_001"}, "old_q": {"question_id": "old_q"}}}
        data = merge_with_bank(data, ["d1_001"])
        self.assertNotIn("old_q", data["records"])


if __name__ == "__main__":
    unittest.main()
