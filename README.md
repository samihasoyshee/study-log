# StudyLog

A simple Python study tracker that logs study sessions — subject, hours studied, productivity rating, and notes — to a CSV file, so you can build a record of your study habits over time.

## Features
- Add a study session with subject, hours studied, productivity rating (1–10), and notes
- Automatically timestamps each session with the current date
- Saves all sessions to `study_sessions.csv`, so your history persists between runs
- Built across 3 modular files (`main.py`, `session_manager.py`, `file_handler.py`) instead of a single script

## How to run
1. Clone the repo: `git clone https://github.com/samihasoyshee/study-log.git`
2. Navigate into the folder: `cd study-log`
3. Run: `python main.py`
4. Choose option `1` to add a study session, or `2` to exit

## What I learned
Splitting a program into separate files by responsibility (input handling vs. file I/O vs. the main menu), and working with Python's built-in `csv`, `datetime`, and `os` modules to persist data between runs.

## Author
Samiha Salam Oyshee