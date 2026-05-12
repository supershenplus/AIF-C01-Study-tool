"""Persistence layer for user progress data."""

import json
import os
from datetime import date, datetime
from pathlib import Path

from .models import ProgressRecord


DATA_DIR = Path(__file__).parent.parent / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"


def _default_progress_data() -> dict:
    return {
        "version": 1,
        "created": datetime.now().isoformat(),
        "last_session": None,
        "streak_days": 0,
        "last_study_date": None,
        "records": {},
    }


def load_progress(path: Path | None = None) -> dict:
    """Load progress from disk. Returns default structure if file missing or corrupt."""
    path = path or PROGRESS_FILE
    if not path.exists():
        return _default_progress_data()

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Ensure required keys exist
        defaults = _default_progress_data()
        for key in defaults:
            if key not in data:
                data[key] = defaults[key]
        return data
    except (json.JSONDecodeError, OSError):
        return _default_progress_data()


def save_progress(data: dict, path: Path | None = None) -> None:
    """Save progress to disk atomically."""
    path = path or PROGRESS_FILE
    path.parent.mkdir(parents=True, exist_ok=True)

    tmp_path = path.with_suffix(".tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    os.replace(str(tmp_path), str(path))


def merge_with_bank(progress_data: dict, question_ids: list[str]) -> dict:
    """Ensure progress has records for all questions, remove stale ones."""
    records = progress_data.get("records", {})
    today = date.today().isoformat()

    # Add new questions
    for qid in question_ids:
        if qid not in records:
            records[qid] = ProgressRecord(question_id=qid, next_review=today).to_dict()

    # Remove questions no longer in the bank
    stale = [qid for qid in records if qid not in question_ids]
    for qid in stale:
        del records[qid]

    progress_data["records"] = records
    return progress_data


def update_streak(progress_data: dict) -> dict:
    """Update study streak based on last study date."""
    today = date.today().isoformat()
    last = progress_data.get("last_study_date")

    if last is None:
        progress_data["streak_days"] = 0
    elif last == today:
        pass  # Already studied today, no change
    elif last == (date.today().replace(day=date.today().day)).isoformat():
        pass  # Same day
    else:
        last_date = date.fromisoformat(last)
        diff = (date.today() - last_date).days
        if diff == 1:
            progress_data["streak_days"] = progress_data.get("streak_days", 0) + 1
        elif diff > 1:
            progress_data["streak_days"] = 0
        # diff == 0 already handled

    return progress_data


def record_session(progress_data: dict) -> dict:
    """Mark that a study session happened today."""
    today = date.today().isoformat()
    progress_data = update_streak(progress_data)
    progress_data["last_study_date"] = today
    progress_data["last_session"] = datetime.now().isoformat()
    return progress_data


def get_domain_stats(progress_data: dict, questions: list) -> dict[int, dict]:
    """Calculate per-domain statistics.

    Returns dict mapping domain number to stats dict with keys:
        total, seen, mastered, correct, answered, accuracy, weakest_subdomain
    """
    records = progress_data.get("records", {})
    domain_stats: dict[int, dict] = {}

    for q in questions:
        d = q.domain
        if d not in domain_stats:
            domain_stats[d] = {
                "total": 0,
                "seen": 0,
                "mastered": 0,
                "correct": 0,
                "answered": 0,
                "subdomain_stats": {},
            }

        stats = domain_stats[d]
        stats["total"] += 1

        rec_data = records.get(q.id, {})
        seen = rec_data.get("times_seen", 0)
        correct = rec_data.get("times_correct", 0)
        reps = rec_data.get("repetitions", 0)

        if seen > 0:
            stats["seen"] += 1
            stats["correct"] += correct
            stats["answered"] += seen
        if reps >= 3:
            stats["mastered"] += 1

        # Track subdomain performance
        sd = q.subdomain
        if sd not in stats["subdomain_stats"]:
            stats["subdomain_stats"][sd] = {"total": 0, "correct": 0, "seen": 0}
        stats["subdomain_stats"][sd]["total"] += 1
        stats["subdomain_stats"][sd]["correct"] += correct
        stats["subdomain_stats"][sd]["seen"] += seen

    # Calculate accuracy and weakest subdomain
    for d, stats in domain_stats.items():
        stats["accuracy"] = stats["correct"] / max(stats["answered"], 1)
        worst_sd = None
        worst_acc = 1.1
        for sd, sd_stats in stats["subdomain_stats"].items():
            if sd_stats["seen"] > 0:
                acc = sd_stats["correct"] / sd_stats["seen"]
            else:
                acc = 0.0
            if acc < worst_acc:
                worst_acc = acc
                worst_sd = sd
        stats["weakest_subdomain"] = worst_sd

    return domain_stats


def get_mastery_pct(progress_data: dict, questions: list, domain: int | None = None) -> float:
    """Calculate mastery percentage for a domain or overall."""
    records = progress_data.get("records", {})
    total = 0
    score = 0.0

    for q in questions:
        if domain is not None and q.domain != domain:
            continue
        total += 1
        rec_data = records.get(q.id, {})
        seen = rec_data.get("times_seen", 0)
        correct = rec_data.get("times_correct", 0)
        if seen > 0:
            score += correct / seen

    return (score / max(total, 1)) * 100


def reset_progress(path: Path | None = None) -> None:
    """Delete progress file to start fresh."""
    path = path or PROGRESS_FILE
    if path.exists():
        path.unlink()
