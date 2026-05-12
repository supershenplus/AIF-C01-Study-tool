"""SM-2 Spaced Repetition Algorithm.

Pure functions implementing the SuperMemo SM-2 algorithm for scheduling
review intervals based on recall quality.
"""

from datetime import date, timedelta


def calculate_sm2(
    quality: int,
    repetitions: int,
    easiness_factor: float,
    interval: int,
) -> tuple[int, float, int]:
    """Calculate new SM-2 parameters after a review.

    Args:
        quality: Response quality 0-5 (0=blackout, 5=perfect recall)
        repetitions: Number of consecutive correct reviews
        easiness_factor: Current easiness factor (>= 1.3)
        interval: Current review interval in days

    Returns:
        Tuple of (new_repetitions, new_easiness_factor, new_interval)
    """
    # Update easiness factor
    new_ef = easiness_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    new_ef = max(1.3, new_ef)

    if quality >= 3:
        # Correct answer
        if repetitions == 0:
            new_interval = 1
        elif repetitions == 1:
            new_interval = 6
        else:
            new_interval = round(interval * new_ef)
        new_repetitions = repetitions + 1
    else:
        # Incorrect — reset
        new_repetitions = 0
        new_interval = 1

    return new_repetitions, new_ef, new_interval


def calculate_quality(is_correct: bool, response_time: float) -> int:
    """Map correctness and response time to SM-2 quality score.

    Args:
        is_correct: Whether the answer was correct
        response_time: Seconds taken to answer

    Returns:
        Quality score 0-5
    """
    if not is_correct:
        return 1

    if response_time < 10:
        return 5
    elif response_time < 30:
        return 4
    else:
        return 3


def is_due(next_review: str, today: date | None = None) -> bool:
    """Check if a question is due for review.

    Args:
        next_review: ISO date string (YYYY-MM-DD)
        today: Override date for testing
    """
    if today is None:
        today = date.today()
    review_date = date.fromisoformat(next_review)
    return review_date <= today


def priority_score(next_review: str, interval: int, today: date | None = None) -> float:
    """Calculate review priority. Higher = more urgent.

    Items proportionally most overdue get highest priority.
    Unseen items (interval=1, due today) get 0.5.

    Args:
        next_review: ISO date string (YYYY-MM-DD)
        interval: Current review interval in days
        today: Override date for testing
    """
    if today is None:
        today = date.today()
    review_date = date.fromisoformat(next_review)
    days_overdue = (today - review_date).days

    if days_overdue < 0:
        return 0.0  # Not yet due

    if interval == 0:
        interval = 1

    return days_overdue / interval


def next_review_date(interval: int, today: date | None = None) -> str:
    """Calculate the next review date.

    Args:
        interval: Days until next review
        today: Override date for testing

    Returns:
        ISO date string
    """
    if today is None:
        today = date.today()
    return (today + timedelta(days=interval)).isoformat()
