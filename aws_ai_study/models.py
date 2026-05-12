"""Data models for the AWS AI Practitioner Study Tool."""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional


@dataclass
class Question:
    id: str
    domain: int
    subdomain: str
    difficulty: str  # "foundational", "intermediate", "advanced"
    text: str
    choices: list[str]
    correct_index: int
    explanation: str

    @classmethod
    def from_dict(cls, d: dict) -> "Question":
        return cls(
            id=d["id"],
            domain=d["domain"],
            subdomain=d["subdomain"],
            difficulty=d.get("difficulty", "foundational"),
            text=d["text"],
            choices=d["choices"],
            correct_index=d["correct_index"],
            explanation=d["explanation"],
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "domain": self.domain,
            "subdomain": self.subdomain,
            "difficulty": self.difficulty,
            "text": self.text,
            "choices": self.choices,
            "correct_index": self.correct_index,
            "explanation": self.explanation,
        }


@dataclass
class ProgressRecord:
    question_id: str
    easiness_factor: float = 2.5
    interval: int = 1
    repetitions: int = 0
    next_review: str = ""  # ISO date string YYYY-MM-DD
    last_quality: Optional[int] = None
    times_seen: int = 0
    times_correct: int = 0

    def __post_init__(self):
        if not self.next_review:
            self.next_review = date.today().isoformat()

    @classmethod
    def from_dict(cls, d: dict) -> "ProgressRecord":
        return cls(
            question_id=d["question_id"],
            easiness_factor=d.get("easiness_factor", 2.5),
            interval=d.get("interval", 1),
            repetitions=d.get("repetitions", 0),
            next_review=d.get("next_review", date.today().isoformat()),
            last_quality=d.get("last_quality"),
            times_seen=d.get("times_seen", 0),
            times_correct=d.get("times_correct", 0),
        )

    def to_dict(self) -> dict:
        return {
            "question_id": self.question_id,
            "easiness_factor": self.easiness_factor,
            "interval": self.interval,
            "repetitions": self.repetitions,
            "next_review": self.next_review,
            "last_quality": self.last_quality,
            "times_seen": self.times_seen,
            "times_correct": self.times_correct,
        }


@dataclass
class DomainInfo:
    number: int
    name: str
    weight: int  # exam percentage
    subdomains: list[str]


@dataclass
class SessionStats:
    questions_answered: int = 0
    correct_count: int = 0
    best_streak: int = 0
    current_streak: int = 0
    domains_touched: dict[int, dict] = field(default_factory=dict)
    session_start: Optional[str] = None

    def __post_init__(self):
        if not self.session_start:
            self.session_start = datetime.now().isoformat()

    def record_answer(self, domain: int, correct: bool):
        self.questions_answered += 1
        if correct:
            self.correct_count += 1
            self.current_streak += 1
            self.best_streak = max(self.best_streak, self.current_streak)
        else:
            self.current_streak = 0

        if domain not in self.domains_touched:
            self.domains_touched[domain] = {"answered": 0, "correct": 0}
        self.domains_touched[domain]["answered"] += 1
        if correct:
            self.domains_touched[domain]["correct"] += 1

    @property
    def accuracy(self) -> float:
        if self.questions_answered == 0:
            return 0.0
        return self.correct_count / self.questions_answered
