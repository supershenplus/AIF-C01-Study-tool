"""Tests for the SM-2 spaced repetition algorithm."""

import unittest
from datetime import date, timedelta

from aws_ai_study.sm2 import (
    calculate_quality,
    calculate_sm2,
    is_due,
    next_review_date,
    priority_score,
)


class TestCalculateSM2(unittest.TestCase):

    def test_first_correct_answer_interval_is_1(self):
        reps, ef, interval = calculate_sm2(quality=4, repetitions=0, easiness_factor=2.5, interval=0)
        self.assertEqual(reps, 1)
        self.assertEqual(interval, 1)

    def test_second_correct_answer_interval_is_6(self):
        reps, ef, interval = calculate_sm2(quality=4, repetitions=1, easiness_factor=2.5, interval=1)
        self.assertEqual(reps, 2)
        self.assertEqual(interval, 6)

    def test_third_correct_answer_uses_ef(self):
        reps, ef, interval = calculate_sm2(quality=4, repetitions=2, easiness_factor=2.5, interval=6)
        self.assertEqual(reps, 3)
        self.assertEqual(interval, round(6 * ef))

    def test_incorrect_resets_reps_and_interval(self):
        reps, ef, interval = calculate_sm2(quality=1, repetitions=5, easiness_factor=2.5, interval=30)
        self.assertEqual(reps, 0)
        self.assertEqual(interval, 1)

    def test_ef_never_below_1_3(self):
        ef = 2.5
        for _ in range(20):
            _, ef, _ = calculate_sm2(quality=0, repetitions=0, easiness_factor=ef, interval=1)
        self.assertGreaterEqual(ef, 1.3)

    def test_perfect_quality_increases_ef(self):
        _, new_ef, _ = calculate_sm2(quality=5, repetitions=2, easiness_factor=2.5, interval=6)
        self.assertGreater(new_ef, 2.5)

    def test_quality_3_is_correct(self):
        reps, _, _ = calculate_sm2(quality=3, repetitions=0, easiness_factor=2.5, interval=0)
        self.assertEqual(reps, 1)  # Treated as correct

    def test_quality_2_is_incorrect(self):
        reps, _, _ = calculate_sm2(quality=2, repetitions=3, easiness_factor=2.5, interval=10)
        self.assertEqual(reps, 0)  # Reset

    def test_interval_grows_over_time(self):
        reps, ef, interval = 0, 2.5, 0
        intervals = []
        for _ in range(6):
            reps, ef, interval = calculate_sm2(quality=4, repetitions=reps, easiness_factor=ef, interval=interval)
            intervals.append(interval)
        # Intervals should be non-decreasing after the first two
        for i in range(2, len(intervals)):
            self.assertGreaterEqual(intervals[i], intervals[i - 1])


class TestCalculateQuality(unittest.TestCase):

    def test_wrong_answer(self):
        self.assertEqual(calculate_quality(False, 5.0), 1)

    def test_wrong_answer_ignores_time(self):
        self.assertEqual(calculate_quality(False, 0.1), 1)

    def test_fast_correct(self):
        self.assertEqual(calculate_quality(True, 5.0), 5)

    def test_medium_correct(self):
        self.assertEqual(calculate_quality(True, 20.0), 4)

    def test_slow_correct(self):
        self.assertEqual(calculate_quality(True, 45.0), 3)

    def test_boundary_10s(self):
        self.assertEqual(calculate_quality(True, 10.0), 4)

    def test_boundary_30s(self):
        self.assertEqual(calculate_quality(True, 30.0), 3)


class TestIsDue(unittest.TestCase):

    def test_due_today(self):
        today = date(2026, 4, 27)
        self.assertTrue(is_due("2026-04-27", today))

    def test_overdue(self):
        today = date(2026, 4, 27)
        self.assertTrue(is_due("2026-04-25", today))

    def test_not_yet_due(self):
        today = date(2026, 4, 27)
        self.assertFalse(is_due("2026-04-28", today))


class TestPriorityScore(unittest.TestCase):

    def test_not_due_returns_zero(self):
        today = date(2026, 4, 27)
        self.assertEqual(priority_score("2026-04-28", 1, today), 0.0)

    def test_due_today_new_item(self):
        today = date(2026, 4, 27)
        score = priority_score("2026-04-27", 1, today)
        self.assertEqual(score, 0.0)

    def test_overdue_proportional(self):
        today = date(2026, 4, 27)
        # 3 days overdue with interval 6 -> 3/6 = 0.5
        score = priority_score("2026-04-24", 6, today)
        self.assertAlmostEqual(score, 0.5)

    def test_more_overdue_higher_priority(self):
        today = date(2026, 4, 27)
        score_a = priority_score("2026-04-25", 1, today)  # 2 days overdue / 1 = 2.0
        score_b = priority_score("2026-04-26", 1, today)  # 1 day overdue / 1 = 1.0
        self.assertGreater(score_a, score_b)


class TestNextReviewDate(unittest.TestCase):

    def test_next_review(self):
        today = date(2026, 4, 27)
        self.assertEqual(next_review_date(6, today), "2026-05-03")

    def test_next_review_1_day(self):
        today = date(2026, 4, 27)
        self.assertEqual(next_review_date(1, today), "2026-04-28")


if __name__ == "__main__":
    unittest.main()
