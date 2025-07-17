# Question 1

def addNumbersQ1(aQ1, bQ1):
    resultQ1 = aQ1 + bQ1
    return resultQ1
def divideNumbersQ1(aQ1, bQ1):
    import pdb; pdb.set_trace()  
    resultQ1 = aQ1 / bQ1
    return resultQ1

def multiplyNumbersQ1(aQ1, bQ1):
    import ipdb; ipdb.set_trace() 
    resultQ1 = aQ1 * bQ1
    return resultQ1

if __name__ == '__main__':
    number1Q1 = 10
    number2Q1 = 5

print("Addition:", addNumbersQ1(number1Q1, number2Q1))
print("Division:", divideNumbersQ1(number1Q1, number2Q1))  
print("Multiplication:", multiplyNumbersQ1(number1Q1, number2Q1))

#Question 2
import logging
def setupLogger():
    logger = logging.getLogger("MyLogger")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(format)
        logger.addHandler(console)

        file = logging.FileHandler("my_log_file.log")
        file.setLevel(logging.DEBUG)
        file.setFormatter(format)
        logger.addHandler(file)

    return logger
logger = setupLogger()
logger.debug("Yeh debug message hai")
logger.info("Sab kuch sahi chal raha hai")
logger.warning("Kuch warning hai bhai")
logger.error("Yeh error hai")
logger.critical("System crash hone wala hai!")

# Question 3

import cProfile
import pstats
import io
def profileFunctionQ3(funcQ3, *argsQ3, **kwargsQ3):
    profilerQ3 = cProfile.Profile()
    profilerQ3.enable()

    resultQ3 = funcQ3(*argsQ3, **kwargsQ3)

    profilerQ3.disable()
    outputQ3 = io.StringIO()
    statsQ3 = pstats.Stats(profilerQ3, stream=outputQ3).sort_stats('cumtime')
    statsQ3.print_stats()
    print(outputQ3.getvalue())

    return resultQ3
def exampleSlowFunctionQ3():
    totalQ3 = 0
    for iQ3 in range(1, 10000):
        for jQ3 in range(1, 50):
            totalQ3 += (iQ3 * jQ3) % 7
    return totalQ3

if __name__ == '__main__':
    print("Result:", profileFunctionQ3(exampleSlowFunctionQ3))

# Question 4

import tracemalloc
import time

def growmemoryq4():
    leakeddataq4=[]
    for iq4 in range(10000):
        leakeddataq4.append("leak" * 1000)
        time.sleep(0.0001)

def monitormemoryq4(funcq4):
    tracemalloc.start()
    startSnapshotQ4 = tracemalloc.take_snapshot()
    funcq4()

    endSnapshotQ4 = tracemalloc.take_snapshot()
    statsQ4 = endSnapshotQ4.compare_to(startSnapshotQ4, 'lineno')

    print("[ Top Memory Increases ]")
    for statQ4 in statsQ4[:5]:
        print(statQ4)

    tracemalloc.stop()
    if __name__ == '__main__':
         monitormemoryq4(growmemoryq4)

# Question 5

import psutil
import os
import time
import threading

def backgroundTaskQ5():
    resultQ5 = 0
    for iQ5 in range(10000000):
        resultQ5 += (iQ5 % 5) * (iQ5 % 7)
    return resultQ5

def monitorDashboardQ5(durationQ5=5):
    processQ5 = psutil.Process(os.getpid())
    startQ5 = time.perf_counter()

    for iQ5 in range(durationQ5):
        cpuQ5 = psutil.cpu_percent(interval=1)
        memQ5 = processQ5.memory_info().rss / (1024 * 1024)
        uptimeQ5 = time.perf_counter() - startQ5
        print(f"[{iQ5+1}] CPU: {cpuQ5}% | Memory: {memQ5:.2f} MB | Uptime: {uptimeQ5:.2f} sec")

def runPerformanceMonitorQ5():
    taskQ5 = threading.Thread(target=backgroundTaskQ5)
    taskQ5.start()
    monitorDashboardQ5(durationQ5=5)
    taskQ5.join()

if __name__ == '__main__':
    runPerformanceMonitorQ5()


#Question 6
def addQ6(aQ6, bQ6):
    return aQ6 + bQ6

def subtractQ6(aQ6, bQ6):
    return aQ6 - bQ6

def multiplyQ6(aQ6, bQ6):
    return aQ6 * bQ6

def divideQ6(aQ6, bQ6):
    if bQ6 == 0:
        return None
    return aQ6 / bQ6

# Question 7 

def addQ7(aQ7, bQ7):
    return aQ7 + bQ7

def subtractQ7(aQ7, bQ7):
    return aQ7 - bQ7

def multiplyQ7(aQ7, bQ7):
    return aQ7 * bQ7

def divideQ7(aQ7, bQ7):
    if bQ7 == 0:
        raise ValueError("Cannot divide by zero")
    return aQ7 / bQ7

#Question 8

from api_module_q8 import fetchUserDataQ8
from unittest.mock import patch

def test_fetchUserDataQ8_success():
    fakeUserQ8 = {"id": 101, "name": "Ahmed"}

    with patch("api_module_q8.requests.get") as mockGetQ8:
        mockGetQ8.return_value.status_code = 200
        mockGetQ8.return_value.json.return_value = fakeUserQ8

        resultQ8 = fetchUserDataQ8(101)
        assert resultQ8 == fakeUserQ8

def test_fetchUserDataQ8_failure():
    with patch("api_module_q8.requests.get") as mockGetQ8:
        mockGetQ8.return_value.status_code = 404

        resultQ8 = fetchUserDataQ8(999)
        assert resultQ8 == {"error": "User not found"}

#Question 9
# Uses the following 3 files:
# 1. db_module_q9.py
# 2. logic_module_q9.py
# 3. test_integration_q9.py

#Question 10
# Uses the following 2 files:
# 1. app_q10.py           ← Flask app with /hello route
# 2. locustfile_q10.py    ← Locust load testing script

#Question 11
# Uses the following 2 files:
# 1. app_q11.py          ← Flask app with vulnerable input endpoint
# 2. fuzzer_q11.py       ← Input fuzzing script

#Question 12
# Files Used:
# 1. call_visualizer_q12.py   ← Builds the call graph with graphviz
# 2. demo_target_q12.py       ← Target Python file to trace
# 3. run_trace_q12.py         ← Runner script to generate PNG graph

#Question 13

import traceback
import platform
import sys
import os
import json
import datetime

def simulateBugQ13(inputQ13):
    if inputQ13 == "crash":
        raise ValueError("Simulated crash triggered.")
    return f"Processed input: {inputQ13}"

def captureContextQ13(inputQ13):
    contextQ13 = {
        "timestamp": str(datetime.datetime.now()),
        "input": inputQ13,
        "os": platform.system(),
        "platform": platform.platform(),
        "python_version": sys.version,
        "cwd": os.getcwd(),
        "env_vars": {k: v for k, v in list(os.environ.items())[:5]}  # limit for brevity
    }
    return contextQ13

def logErrorQ13(contextQ13, errorQ13):
    logDataQ13 = {
        "context": contextQ13,
        "traceback": traceback.format_exc()
    }
    with open("error_log_q13.json", "w") as logFileQ13:
        json.dump(logDataQ13, logFileQ13, indent=4)
    print("Error logged to error_log_q13.json")

if __name__ == "__main__":
    try:
        userInputQ13 = input("Enter command (type 'crash' to simulate bug): ")
        contextQ13 = captureContextQ13(userInputQ13)
        print(simulateBugQ13(userInputQ13))
    except Exception as errQ13:
        logErrorQ13(contextQ13, errQ13)


#Question 14
#Used 1 file:
#debugging_best_practices_q14.md

#Question 15
#used 2 files:
#quality_check.sh
#greetQ15.py

#Question 16
#used 2 files:
#app_q16.py
#utils_q16.py

#Question 17
# Files Used:
# 1. demo_module_q17.py    ← Your target functions
# 2. ast_parser_q17.py     ← Uses `ast` to inspect function signatures & structure
# 3. run_analysis_q17.py   ← Imports & runs both AST analysis and dynamic calls

# Question 18 (Error Reproduction Script Generator) uses the following files:
#   1. bug_logger_q18.py        ← collects and stores bug entries
#   2. report_generator_q18.py  ← reads bug entries and renders the Markdown report
#   3. main_q18.py              ← example usage: logs bugs & generates the report

# Question 19 – Debugging Simulation Training System uses these files:
#   1. app_q19.py           ← orchestrator (calls all buggy modules)
#   2. math_utils_q19.py    ← factorial & prime utils with bugs
#   3. string_utils_q19.py  ← string helpers with intentional bugs
#   4. data_loader_q19.py   ← JSON loader with typo and missing error‑handling
#   5. run_debug_q19.py     ← harness that runs everything and prints tracebacks

from run_debug_q19 import run_all_q19

if __name__ == "__main__":
    run_all_q19()



# ────────────────────────────────────────────────────────────────────────────
# Question 20: Advanced Debugging Workflow Implementation
# Design and document a full debugging workflow that includes
# breakpoint setup, automated tests, logging, profiling,
# and final resolution verification.
# ────────────────────────────────────────────────────────────────────────────

"""
# Question 20: Advanced Debugging Workflow Implementation

## 📌 Goal  
Demonstrate expertise in holistic, production-ready debugging.

---

## 🔧 Full Debugging Workflow

1. **Reproduce & Isolate the Bug**  
   - Gather error logs, inputs, environment info.  
   - Create minimal reproducible test case.

2. **Setup Breakpoints**  
   - Use `breakpoint()` or `pdb` to inspect flow.  
   - In IDEs like VS Code, set conditional breakpoints.

3. **Automated Tests (pytest/unittest)**  
   - Write a test that reproduces the bug.  
   - Run suite to ensure failure is captured.

4. **Logging Strategy**  
   - Use `logging` module with different levels (`DEBUG`, `INFO`, etc.).  
   - Include contextual metadata in logs.

5. **Profiling and Resource Monitoring**  
   - Use `cProfile`, `line_profiler`, or `time.perf_counter()` for performance.  
   - Use `tracemalloc` or `objgraph` for memory leaks.

6. **Bug Fix and Rerun Tests**  
   - Fix incrementally.  
   - Confirm fix with green test and no regressions.

7. **Final Verification**  
   - Run smoke tests, regression tests.  
   - Peer review with diffs and logs.  
   - Deploy to staging for final signoff.

8. **Documentation**  
   - Document repro, root cause, fix, and test proof.  
   - Store in issue tracker or internal wiki.

---

> ✅ This complete debugging workflow boosts confidence in production code and improves long-term maintainability.
"""








