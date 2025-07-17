# bug_logger_q18.py

import json
import datetime
import os

DATA_FILE = "bugs_q18.json"

def _load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def _save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def log_bug_q18(title, reproduction_steps, fix_summary, test_results):
    """
    Adds a new bug entry with:
    - title: short bug title
    - reproduction_steps: list of steps
    - fix_summary: description of the fix
    - test_results: pass/fail or details
    """
    data = _load_data()
    entry = {
        "id": len(data) + 1,
        "timestamp": datetime.datetime.now().isoformat(),
        "title": title,
        "reproduction_steps": reproduction_steps,
        "fix_summary": fix_summary,
        "test_results": test_results
    }
    data.append(entry)
    _save_data(data)
    return entry