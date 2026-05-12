"""Rich Terminal UI for the AWS AI Practitioner Study Tool."""

import os
import sys
import time
from datetime import date

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.markdown import Markdown
from rich import box

from .models import Question, SessionStats
from .progress import (
    get_domain_stats,
    get_mastery_pct,
    load_progress,
    record_session,
    save_progress,
    merge_with_bank,
)
from .quiz import (
    count_due,
    count_due_tomorrow,
    record_answer,
    select_domain_questions,
    select_due_questions,
)

console = Console(force_terminal=True)


DOMAIN_NAMES = {
    1: "Fundamentals of AI and ML",
    2: "Fundamentals of Generative AI",
    3: "Applications of Foundation Models",
    4: "Guidelines for Responsible AI",
    5: "Security, Compliance, Governance",
}

DOMAIN_WEIGHTS = {1: 20, 2: 24, 3: 28, 4: 14, 5: 14}


class App:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.progress = load_progress()
        self.progress = merge_with_bank(self.progress, [q.id for q in questions])
        self.session_stats = SessionStats()
        self.running = True

    def run(self):
        """Main app loop."""
        while self.running:
            self.show_main_menu()

    def _clear(self):
        console.clear()

    def _get_input(self, prompt: str = "  Your choice: ") -> str:
        try:
            return input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return "q"

    def _pause(self, msg: str = "  Press Enter to continue..."):
        try:
            input(msg)
        except (EOFError, KeyboardInterrupt):
            pass

    # ── Main Menu ──────────────────────────────────────────────

    def show_main_menu(self):
        self._clear()
        due = count_due(self.progress, self.questions)
        streak = self.progress.get("streak_days", 0)

        # Header
        header = Text()
        header.append("  AWS AI Practitioner Study Tool", style="bold blue")
        header.append("  |  AIF-C01", style="dim")
        console.print(Panel(header, box=box.DOUBLE, border_style="blue"))
        console.print()

        # Streak and session info
        info = Text()
        if streak > 0:
            info.append(f"  Day {streak} streak", style="bold green")
        else:
            info.append("  No streak yet — start today!", style="yellow")
        info.append(f"     Session: {self.session_stats.questions_answered} answered")
        if self.session_stats.questions_answered > 0:
            pct = int(self.session_stats.accuracy * 100)
            info.append(f" ({pct}% correct)")
        console.print(info)
        console.print()

        # Due count
        if due > 0:
            console.print(f"  [bold yellow]Due for Review Today: {due} questions[/]")
        else:
            console.print("  [bold green]All caught up! No questions due today.[/]")
        console.print()

        # Domain mastery bars
        console.print("  [bold]Domain Mastery:[/]")
        for d in range(1, 6):
            pct = get_mastery_pct(self.progress, self.questions, d)
            bar = self._make_bar(pct)
            weight = DOMAIN_WEIGHTS[d]
            name = f"D{d} {DOMAIN_NAMES[d]}"
            console.print(f"  {name:<40s} {bar} {pct:4.0f}%  ({weight}%)")
        console.print()

        overall = self._overall_readiness()
        console.print(f"  [bold]Overall Readiness: {overall:.0f}%[/]")
        console.print()

        # Menu options
        console.print(f"  [bold cyan]\\[1][/] Daily Review ({due} due)")
        console.print("  [bold cyan]\\[2][/] Quiz by Domain")
        console.print("  [bold cyan]\\[3][/] Study Mode")
        console.print("  [bold cyan]\\[4][/] Progress Details")
        console.print("  [bold cyan]\\[q][/] Quit")
        console.print()

        choice = self._get_input()
        if choice == "1":
            self.show_quiz(select_due_questions(self.progress, self.questions))
        elif choice == "2":
            self.show_domain_select()
        elif choice == "3":
            self.show_study_mode()
        elif choice == "4":
            self.show_progress_details()
        elif choice == "q":
            self._quit()

    def _make_bar(self, pct: float, width: int = 20) -> str:
        filled = int(pct / 100 * width)
        empty = width - filled
        if pct >= 70:
            color = "green"
        elif pct >= 40:
            color = "yellow"
        else:
            color = "red"
        return f"[{color}]{'█' * filled}{'░' * empty}[/]"

    def _overall_readiness(self) -> float:
        total = 0.0
        for d in range(1, 6):
            m = get_mastery_pct(self.progress, self.questions, d)
            total += m * DOMAIN_WEIGHTS[d]
        return total / 100

    # ── Domain Select ──────────────────────────────────────────

    def show_domain_select(self):
        self._clear()
        console.print(Panel("  Quiz by Domain", style="bold blue"))
        console.print()
        for d in range(1, 6):
            domain_qs = [q for q in self.questions if q.domain == d]
            due = count_due(self.progress, domain_qs)
            console.print(f"  [bold cyan]\\[{d}][/] {DOMAIN_NAMES[d]}  ({due} due, {len(domain_qs)} total)")
        console.print()
        console.print("  [bold cyan]\\[b][/] Back to menu")
        console.print()

        choice = self._get_input()
        if choice in ("1", "2", "3", "4", "5"):
            d = int(choice)
            qs = select_domain_questions(self.progress, self.questions, d)
            if qs:
                self.show_quiz(qs)
            else:
                console.print(f"\n  [green]No questions due for Domain {d}![/]")
                self._pause()

    # ── Quiz Mode ──────────────────────────────────────────────

    def show_quiz(self, questions: list[Question]):
        if not questions:
            self._clear()
            console.print("\n  [green]No questions due! Come back later.[/]")
            self._pause()
            return

        # Confirm before starting
        self._clear()
        console.print(f"\n  [bold]{len(questions)} questions ready.[/]")
        console.print("  [dim]\\[Enter] Start    \\[b] Back to menu[/]")
        if self._get_input("  ") == "b":
            return

        for i, q in enumerate(questions):
            self._clear()
            console.print(f"  [dim]Question {i + 1} of {len(questions)}[/]"
                         f"{'':>30s}[blue]Domain {q.domain}[/]")
            console.print("  " + "─" * 55)
            console.print()
            console.print(f"  {q.text}")
            console.print()

            labels = ["A", "B", "C", "D"]
            for j, choice in enumerate(q.choices):
                console.print(f"    [bold cyan]\\[{labels[j]}][/] {choice}")
            console.print()

            start_time = time.time()
            answer = self._get_input("  Your answer (a/b/c/d): ")
            elapsed = time.time() - start_time

            if answer == "q":
                break

            answer_map = {"a": 0, "b": 1, "c": 2, "d": 3}
            if answer not in answer_map:
                console.print("  [yellow]Invalid input, skipping.[/]")
                self._pause()
                continue

            selected = answer_map[answer]
            is_correct = selected == q.correct_index

            # Record answer
            record_answer(self.progress, q.id, is_correct, elapsed)
            self.session_stats.record_answer(q.domain, is_correct)
            console.print()

            if is_correct:
                console.print("  [bold green]Correct![/]", end="")
                if self.session_stats.current_streak > 1:
                    console.print(f"  [magenta]+{self.session_stats.current_streak} streak[/]")
                else:
                    console.print()
            else:
                console.print(f"  [bold red]Incorrect.[/] The answer was "
                             f"[bold green]{labels[q.correct_index]}. {q.choices[q.correct_index]}[/]")

            console.print()
            console.print(f"  [cyan]► {q.explanation}[/]")
            console.print()

            if i < len(questions) - 1:
                console.print("  [dim]\\[Enter] Next question    \\[q] End quiz[/]")
                if self._get_input("  ") == "q":
                    break

        # Save and show summary
        self.progress = record_session(self.progress)
        save_progress(self.progress)
        self.show_session_summary()

    # ── Session Summary ────────────────────────────────────────

    def show_session_summary(self):
        self._clear()
        stats = self.session_stats
        if stats.questions_answered == 0:
            return

        console.print(Panel("  Session Complete", style="bold blue"))
        console.print()
        console.print(f"  Answered:  {stats.questions_answered} questions")
        console.print(f"  Correct:   {stats.correct_count} ({int(stats.accuracy * 100)}%)")
        console.print(f"  Best Run:  {stats.best_streak} in a row")
        console.print()

        if stats.domains_touched:
            console.print("  [bold]Domain Breakdown:[/]")
            for d, ds in sorted(stats.domains_touched.items()):
                bar = self._make_bar(ds["correct"] / max(ds["answered"], 1) * 100, 8)
                console.print(f"    D{d}  {bar}  {ds['correct']}/{ds['answered']} correct")
            console.print()

        due_tomorrow = count_due_tomorrow(self.progress, self.questions)
        console.print(f"  [dim]Next review: {due_tomorrow} questions due tomorrow[/]")
        console.print()
        self._pause()

        # Reset session stats for next quiz
        self.session_stats = SessionStats()

    # ── Study Mode ─────────────────────────────────────────────

    def show_study_mode(self):
        self._clear()
        console.print(Panel("  Study Mode — Browse by Domain", style="bold blue"))
        console.print()

        for d in range(1, 6):
            console.print(f"  [bold cyan]\\[{d}][/] {DOMAIN_NAMES[d]}")
        console.print()
        console.print("  [bold cyan]\\[b][/] Back to menu")
        console.print()

        choice = self._get_input()
        if choice in ("1", "2", "3", "4", "5"):
            self._show_domain_study(int(choice))

    def _show_domain_study(self, domain: int):
        domain_qs = [q for q in self.questions if q.domain == domain]
        # Group by subdomain
        subdomains: dict[str, list[Question]] = {}
        for q in domain_qs:
            subdomains.setdefault(q.subdomain, []).append(q)

        for sd in sorted(subdomains.keys()):
            self._clear()
            console.print(Panel(f"  Domain {domain} — Subdomain {sd}", style="bold blue"))
            console.print()

            for q in subdomains[sd]:
                console.print(f"  [bold]{q.text}[/]")
                console.print(f"  [green]Answer: {q.choices[q.correct_index]}[/]")
                console.print(f"  [cyan]{q.explanation}[/]")
                console.print()

            console.print("  [dim]\\[Enter] Next subdomain    \\[b] Back    \\[q] Menu[/]")
            choice = self._get_input("  ")
            if choice in ("b", "q"):
                return

    # ── Progress Details ───────────────────────────────────────

    def show_progress_details(self):
        self._clear()
        console.print(Panel("  Progress Details", style="bold blue"))
        console.print()

        domain_stats = get_domain_stats(self.progress, self.questions)

        for d in range(1, 6):
            stats = domain_stats.get(d, {})
            total = stats.get("total", 0)
            seen = stats.get("seen", 0)
            mastered = stats.get("mastered", 0)
            accuracy = stats.get("accuracy", 0)
            weakest = stats.get("weakest_subdomain", "N/A")

            console.print(f"  [bold blue]Domain {d}: {DOMAIN_NAMES[d]}[/]")
            console.print(f"    Questions: {total} total | {seen} seen | {mastered} mastered")
            console.print(f"    Accuracy:  {accuracy:.0%}")
            console.print(f"    Weakest:   Subdomain {weakest}")
            console.print()

        # Hardest questions
        records = self.progress.get("records", {})
        hard = []
        for qid, rec in records.items():
            if rec.get("times_seen", 0) > 0:
                hard.append((rec.get("easiness_factor", 2.5), qid))
        hard.sort()

        if hard:
            console.print("  [bold]Hardest Questions (lowest easiness):[/]")
            for ef, qid in hard[:5]:
                q = next((q for q in self.questions if q.id == qid), None)
                if q:
                    short = q.text[:55] + "..." if len(q.text) > 55 else q.text
                    console.print(f"    {qid} — \"{short}\" (EF: {ef:.2f})")
            console.print()

        streak = self.progress.get("streak_days", 0)
        total_mastered = sum(s.get("mastered", 0) for s in domain_stats.values())
        total_q = sum(s.get("total", 0) for s in domain_stats.values())
        console.print(f"  Study Streak:      {streak} days")
        console.print(f"  Questions Mastered: {total_mastered} / {total_q}")
        console.print()

        self._pause()

    # ── Quit ───────────────────────────────────────────────────

    def _quit(self):
        save_progress(self.progress)
        console.print("\n  [bold green]Progress saved. Keep studying![/]\n")
        self.running = False
