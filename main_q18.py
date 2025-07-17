# main_q18.py

from bug_logger_q18 import log_bug_q18
from report_generator_q18 import generate_report_q18

if __name__ == "__main__":
    # Example: log two bugs
    log_bug_q18(
        title="Crash on empty input",
        reproduction_steps=[
            "Start app",
            "Leave input field blank",
            "Click Submit"
        ],
        fix_summary="Added input validation to reject empty strings",
        test_results="Manually tested: pass; automated unit tests added"
    )

    log_bug_q18(
        title="Wrong total in checkout",
        reproduction_steps=[
            "Add item A ($5) and B ($3) to cart",
            "Proceed to checkout"
        ],
        fix_summary="Fixed currency conversion float rounding error",
        test_results="Unit tests cover rounding edge cases"
    )

    # Generate the Markdown report
    generate_report_q18()