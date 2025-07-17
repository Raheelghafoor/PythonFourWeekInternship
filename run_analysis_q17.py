# run_analysis_q17.py

import importlib.util
import sys
from ast_parser_q17 import analyze_functions_q17

MODULE_PATH_Q17 = "demo_module_q17.py"

def dynamic_import_q17(path_q17, module_name_q17):
    spec_q17 = importlib.util.spec_from_file_location(module_name_q17, path_q17)
    module_q17 = importlib.util.module_from_spec(spec_q17)
    spec_q17.loader.exec_module(module_q17)
    return module_q17

if __name__ == "__main__":
    print("=== AST Analysis ===")
    analyze_functions_q17(MODULE_PATH_Q17)

    print("=== Dynamic Execution ===")
    demo_mod_q17 = dynamic_import_q17(MODULE_PATH_Q17, "demo_module_q17")
    result_add_q17 = demo_mod_q17.add_q17(3, 4)
    print(f"add_q17(3, 4) → {result_add_q17}")
    demo_mod_q17.greet_q17("Ahmed")
    print(f"factorial_q17(5) → {demo_mod_q17.factorial_q17(5)}")
