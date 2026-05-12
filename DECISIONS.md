# DECISIONS — AIF-C01 Study Tool

Format: `## TITLE`, then Choice / Why / Rejected.

---

## Spaced repetition algorithm: SM-2

**Choice:** SM-2  
**Why:** Well-documented, proven for flashcard apps, simple to implement in pure Python with no deps. Matches Anki's core model which users already trust.  
**Rejected:** Leitner boxes (less adaptive), FSRS (more complex, overkill for MVP).

---

## TUI library: Rich

**Choice:** Rich  
**Why:** Zero-config terminal rendering, cross-platform (including Windows), handles color/tables/panels without curses. Single dependency.  
**Rejected:** curses (Windows hostile), Textual (heavier, overkill for MVP), blessed (less maintained).

---

## Storage: local JSON (offline-only)

**Choice:** JSON file at `data/progress.json`  
**Why:** Zero infrastructure, zero network, works fully offline. Exam prep tool — no account needed.  
**Rejected:** SQLite (overkill for single-user local tool), cloud sync (violates offline-only constraint).

---

## Test framework: pytest

**Choice:** pytest  
**Why:** Standard Python testing, minimal boilerplate, works well with SM-2 unit tests.  
**Rejected:** unittest (more verbose, no benefit here).
