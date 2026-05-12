"""Quiz session logic: question selection, scoring, and answer recording."""

import random
from datetime import date

from .models import ProgressRecord, Question
from .sm2 import calculate_quality, calculate_sm2, is_due, next_review_date, priority_score


def select_due_questions(
    progress_data: dict,
    questions: list[Question],
    limit: int = 20,
    today: date | None = None,
) -> list[Question]:
    """Select questions due for review, ordered by priority.

    Mixes overdue items (highest priority first) with unseen items.
    """
    if today is None:
        today = date.today()

    records = progress_data.get("records", {})
    due = []
    unseen = []

    for q in questions:
        rec_data = records.get(q.id)
        if rec_data is None:
            unseen.append(q)
            continue

        if rec_data.get("times_seen", 0) == 0:
            unseen.append(q)
        elif is_due(rec_data.get("next_review", today.isoformat()), today):
            score = priority_score(
                rec_data["next_review"],
                rec_data.get("interval", 1),
                today,
            )
            due.append((score, q))

    # Sort due items by priority descending
    due.sort(key=lambda x: x[0], reverse=True)
    result = [q for _, q in due]

    # Mix in unseen items
    random.shuffle(unseen)
    result.extend(unseen)

    return result[:limit]


def select_domain_questions(
    progress_data: dict,
    questions: list[Question],
    domain: int,
    limit: int = 10,
    today: date | None = None,
) -> list[Question]:
    """Select questions for a specific domain, due first then unseen."""
    domain_questions = [q for q in questions if q.domain == domain]
    return select_due_questions(progress_data, domain_questions, limit, today)


def record_answer(
    progress_data: dict,
    question_id: str,
    is_correct: bool,
    response_time: float,
    today: date | None = None,
) -> ProgressRecord:
    """Record an answer and update SM-2 state. Returns updated record."""
    if today is None:
        today = date.today()

    records = progress_data.get("records", {})
    rec_data = records.get(question_id, ProgressRecord(question_id=question_id).to_dict())

    quality = calculate_quality(is_correct, response_time)

    new_reps, new_ef, new_interval = calculate_sm2(
        quality=quality,
        repetitions=rec_data.get("repetitions", 0),
        easiness_factor=rec_data.get("easiness_factor", 2.5),
        interval=rec_data.get("interval", 1),
    )

    rec_data["repetitions"] = new_reps
    rec_data["easiness_factor"] = round(new_ef, 4)
    rec_data["interval"] = new_interval
    rec_data["next_review"] = next_review_date(new_interval, today)
    rec_data["last_quality"] = quality
    rec_data["times_seen"] = rec_data.get("times_seen", 0) + 1
    if is_correct:
        rec_data["times_correct"] = rec_data.get("times_correct", 0) + 1
    rec_data["question_id"] = question_id

    records[question_id] = rec_data
    progress_data["records"] = records

    return ProgressRecord.from_dict(rec_data)


def count_due(progress_data: dict, questions: list[Question], today: date | None = None) -> int:
    """Count how many questions are due for review today."""
    if today is None:
        today = date.today()

    records = progress_data.get("records", {})
    count = 0
    for q in questions:
        rec_data = records.get(q.id)
        if rec_data is None or rec_data.get("times_seen", 0) == 0:
            count += 1  # Unseen counts as due
        elif is_due(rec_data.get("next_review", today.isoformat()), today):
            count += 1
    return count


def count_due_tomorrow(progress_data: dict, questions: list[Question], today: date | None = None) -> int:
    """Count questions due tomorrow."""
    if today is None:
        today = date.today()
    from datetime import timedelta
    tomorrow = today + timedelta(days=1)

    records = progress_data.get("records", {})
    count = 0
    for q in questions:
        rec_data = records.get(q.id)
        if rec_data is None:
            continue
        if rec_data.get("times_seen", 0) == 0:
            continue
        if is_due(rec_data.get("next_review", today.isoformat()), tomorrow):
            count += 1
    return count
