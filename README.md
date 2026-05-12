# AIF-C01 Study Tool

Terminal-based flashcard app for the AWS Certified AI Practitioner exam (AIF-C01). Uses spaced repetition (SM-2 algorithm) to surface weak areas and track readiness across all five exam domains.

## About

Study smarter for AIF-C01 by drilling questions domain-by-domain or letting the scheduler surface cards that are due for review. Progress persists between sessions so you can pick up where you left off.

**Exam domains covered:**

| Domain | Topic | Weight |
|--------|-------|--------|
| D1 | Fundamentals of AI and ML | 20% |
| D2 | Fundamentals of Generative AI | 24% |
| D3 | Applications of Foundation Models | 28% |
| D4 | Guidelines for Responsible AI | 14% |
| D5 | Security, Compliance, Governance | 14% |

## Requirements

- Python 3.8+
- `rich >= 13.0`

## Setup

```bat
setup.bat
```

Or manually:

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Launch interactive TUI
python -m aws_ai_study

# Quick stats
python -m aws_ai_study --stats

# Reset all progress
python -m aws_ai_study --reset
```

On Windows you can also double-click `run.bat`.
