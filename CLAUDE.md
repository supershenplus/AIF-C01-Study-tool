# AIF-C01 Study Tool — CLAUDE.md

## Project

**Name:** AIF-C01 Study Tool  
**Description:** CLI flashcard app for AWS Certified AI Practitioner exam (AIF-C01). Spaced repetition, domain tracking, progress persistence.  
**Phase:** MVP  
**Repo:** C:\Users\eva0011\Pycharmprojects\aws-ai-study

## Stack

- **Language:** Python 3.8+
- **TUI:** Rich
- **Algorithm:** SM-2 (spaced repetition)
- **Tests:** pytest
- **Storage:** JSON (local, offline-only)

## Layout

```
aws_ai_study/     # core package — TUI, quiz engine, SM-2, models, progress
data/             # runtime data (progress.json — gitignored)
tests/            # pytest test suite
venv/             # local virtualenv (gitignored)
run.bat           # Windows launcher
setup.bat         # Windows setup script
```

## Run

```bash
python -m aws_ai_study          # launch TUI
python -m aws_ai_study --stats  # quick stats
python -m aws_ai_study --reset  # reset progress
pytest                          # run tests
```

## Hard Rules

- **Offline-only.** No network calls, no external APIs, no telemetry.
- **Tests colocated in `tests/`.** pytest only. No mocking of core SM-2 logic — test with real data.
- **No new dependencies** without explicit approval. `rich` is the only allowed third-party lib.
- **Progress file is `data/progress.json`.** Never commit it (gitignored). Never wipe without `--reset` flag + confirmation prompt.

<!-- SHARED-STANDARDS:START -->
## Shared Standards

### Code style
- No comments unless WHY is non-obvious (hidden constraint, subtle invariant, workaround).
- No docstrings longer than one line.
- No unused imports, variables, or dead code.
- Prefer editing existing files over creating new ones.

### Safety
- No destructive operations without confirmation prompt.
- No overwriting user progress silently.

### Git
- Commit messages: imperative, lowercase, no period. Max 72 chars.
- Never commit `data/progress.json`, `.env`, or `venv/`.

### Repos sharing these standards
- C:\Users\eva0011\Pycharmprojects\aws-ai-study
<!-- SHARED-STANDARDS:END -->
