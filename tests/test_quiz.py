"""Tests for quiz session logic."""

import unittest
from datetime import date

from aws_ai_study.models import Question
from aws_ai_study.quiz import (
    count_due,
    record_answer,
    select_domain_questions,
    select_due_questions,
)


def _make_question(qid: str, domain: int = 1) -> Question:
    return Question(
        id=qid, domain=domain, subdomain=f"{domain}.1", difficulty="foundational",
        text="Test?", choices=["A", "B", "C", "D"], correct_index=0,
        explanation="Test explanation."
    )


class TestSelectDueQuestions(unittest.TestCase):

    def test_unseen_questions_returned(self):
        qs = [_make_question("d1_001"), _make_question("d1_002")]
        progress = {"records": {}}
        result = select_due_questions(progress, qs, limit=10, today=date(2026, 4, 27))
        self.assertEqual(len(result), 2)

    def test_due_questions_before_unseen(self):
        qs = [_make_question("d1_001"), _make_question("d1_002")]
        progress = {"records": {
            "d1_001": {
                "question_id": "d1_001", "times_seen": 3, "next_review": "2026-04-25",
                "interval": 1, "repetitions": 1, "easiness_factor": 2.5,
            },
        }}
        result = select_due_questions(progress, qs, limit=10, today=date(2026, 4, 27))
        # d1_001 is overdue so should come first
        self.assertEqual(result[0].id, "d1_001")

    def test_respects_limit(self):
        qs = [_make_question(f"d1_{i:03d}") for i in range(30)]
        progress = {"records": {}}
        result = select_due_questions(progress, qs, limit=5, today=date(2026, 4, 27))
        self.assertEqual(len(result), 5)

    def test_not_due_excluded(self):
        qs = [_make_question("d1_001")]
        progress = {"records": {
            "d1_001": {
                "question_id": "d1_001", "times_seen": 3, "next_review": "2026-05-01",
                "interval": 6, "repetitions": 2, "easiness_factor": 2.5,
            },
        }}
        result = select_due_questions(progress, qs, limit=10, today=date(2026, 4, 27))
        self.assertEqual(len(result), 0)


class TestSelectDomainQuestions(unittest.TestCase):

    def test_filters_by_domain(self):
        qs = [_make_question("d1_001", 1), _make_question("d2_001", 2)]
        progress = {"records": {}}
        result = select_domain_questions(progress, qs, domain=1, limit=10, today=date(2026, 4, 27))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].domain, 1)


class TestRecordAnswer(unittest.TestCase):

    def test_correct_answer_updates_record(self):
        progress = {"records": {
            "d1_001": {
                "question_id": "d1_001", "easiness_factor": 2.5, "interval": 1,
                "repetitions": 0, "next_review": "2026-04-27", "last_quality": None,
                "times_seen": 0, "times_correct": 0,
            }
        }}
        rec = record_answer(progress, "d1_001", True, 15.0, today=date(2026, 4, 27))
        self.assertEqual(rec.times_seen, 1)
        self.assertEqual(rec.times_correct, 1)
        self.assertEqual(rec.repetitions, 1)

    def test_wrong_answer_resets_reps(self):
        progress = {"records": {
            "d1_001": {
                "question_id": "d1_001", "easiness_factor": 2.5, "interval": 6,
                "repetitions": 3, "next_review": "2026-04-27", "last_quality": 4,
                "times_seen": 5, "times_correct": 4,
            }
        }}
        rec = record_answer(progress, "d1_001", False, 10.0, today=date(2026, 4, 27))
        self.assertEqual(rec.repetitions, 0)
        self.assertEqual(rec.interval, 1)
        self.assertEqual(rec.times_seen, 6)
        self.assertEqual(rec.times_correct, 4)

    def test_new_question_creates_record(self):
        progress = {"records": {}}
        rec = record_answer(progress, "d1_new", True, 5.0, today=date(2026, 4, 27))
        self.assertEqual(rec.question_id, "d1_new")
        self.assertEqual(rec.times_seen, 1)


class TestCountDue(unittest.TestCase):

    def test_counts_unseen_as_due(self):
        qs = [_make_question("d1_001"), _make_question("d1_002")]
        progress = {"records": {}}
        self.assertEqual(count_due(progress, qs, today=date(2026, 4, 27)), 2)

    def test_counts_overdue(self):
        qs = [_make_question("d1_001")]
        progress = {"records": {
            "d1_001": {"question_id": "d1_001", "times_seen": 1, "next_review": "2026-04-25"},
        }}
        self.assertEqual(count_due(progress, qs, today=date(2026, 4, 27)), 1)


if __name__ == "__main__":
    unittest.main()
