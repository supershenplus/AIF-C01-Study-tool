"""Entry point for the AWS AI Practitioner Study Tool."""

import argparse
import sys

from rich.console import Console

from .question_bank import get_all_questions
from .progress import load_progress, reset_progress, get_domain_stats, get_mastery_pct
from .tui import App, DOMAIN_NAMES, DOMAIN_WEIGHTS

console = Console()


def main():
    parser = argparse.ArgumentParser(description="AWS AI Practitioner Study Tool (AIF-C01)")
    parser.add_argument("--reset", action="store_true", help="Reset all progress and start fresh")
    parser.add_argument("--stats", action="store_true", help="Show quick stats and exit")
    args = parser.parse_args()

    if args.reset:
        confirm = input("  Reset all progress? This cannot be undone. (y/n): ").strip().lower()
        if confirm == "y":
            reset_progress()
            console.print("  [green]Progress reset.[/]")
        else:
            console.print("  [yellow]Cancelled.[/]")
        return

    questions = get_all_questions()

    if args.stats:
        progress = load_progress()
        console.print("\n  [bold blue]AWS AI Practitioner — Quick Stats[/]\n")
        for d in range(1, 6):
            pct = get_mastery_pct(progress, questions, d)
            console.print(f"  D{d} {DOMAIN_NAMES[d]:<40s} {pct:.0f}%")
        overall = sum(get_mastery_pct(progress, questions, d) * DOMAIN_WEIGHTS[d] for d in range(1, 6)) / 100
        console.print(f"\n  [bold]Overall Readiness: {overall:.0f}%[/]")
        console.print(f"  Streak: {progress.get('streak_days', 0)} days\n")
        return

    app = App(questions)
    app.run()


if __name__ == "__main__":
    main()
