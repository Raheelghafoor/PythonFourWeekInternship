# run_debug_q19.py

import traceback
from app_q19 import main_q19

def run_all_q19():
    try:
        main_q19()
    except Exception as e_q19:
        print("Caught exception:")
        traceback.print_exc()

if __name__ == "__main__":
    run_all_q19()