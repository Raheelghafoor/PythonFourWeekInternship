# report_generator_q18.py

import json

DATA_FILE = "bugs_q18.json"
OUTPUT_FILE = "debug_report_q18.md"

def generate_report_q18():
    with open(DATA_FILE, "r") as f:
        bugs = json.load(f)

    lines = ["# Debugging Report", ""]
    for bug in bugs:
        lines += [
            f"## Bug #{bug['id']}: {bug['title']}",
            f"- **Logged at:** {bug['timestamp']}",
            "",
            "**Reproduction Steps:**",
        ]
        for i, step in enumerate(bug["reproduction_steps"], 1):
            lines.append(f"  {i}. {step}")
        lines += [
            "",
            f"**Fix Summary:** {bug['fix_summary']}",
            "",
            f"**Test Results:** {bug['test_results']}",
            "",
            "---",
            ""
        ]

    with open(OUTPUT_FILE, "w") as out:
        out.write("\n".join(lines))
    print(f"Report generated: {OUTPUT_FILE}")