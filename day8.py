#QUESTION 1
print("\n=== Mini Unit Testing Framework ===")
def run_test(test_function):
    try:
        test_function()
        print("[pass]",test_function.__name__)
    except AssertionError as error_message:
        print("[FAIL]", test_function.__name__, "-", str(error_message))

def add_numbers(a,b):
    return a + b
def multiply_numbers(a, b):
    return a * b
def test_add_positive():
    assert add_numbers(3, 2) == 5, "3 + 2 should be 5"
def test_add_negative():
    assert add_numbers(-1, -1) == -2, "-1 + -1 should be -2"
def test_multiply_basic():
    assert multiply_numbers(4, 5) == 20, "4 * 5 should be 20"
def test_multiply_zero():
    assert multiply_numbers(4, 0) == 0, "4 * 0 should be 0"
run_test(test_add_positive)
run_test(test_add_negative)
run_test(test_multiply_basic)
run_test(test_multiply_zero)

#QUESTION 2
import random
print("\n=== Easy Test Case Generator ===")
def double_number(x):
    return x * 2
for i in range(5):
    number = random.randint(1,10)
    result = double_number(number)
    print("Test", i+1, "| Input:", number, "| Output:", result)

#QUESTION 3
import random
import datetime
print("\n=== Mock Data Creator ===")
first_names = ["Ali", "Ahmed", "Sara", "Zain", "Fatima"]
last_names = ["Khan", "Malik", "Sheikh", "Raza", "Butt"]
for i in range(5):
    first= random.choice(first_names)
    last= random.choice(last_names)
    email= f"{first.lower()}.{last.lower()}@example.com"
    year = random.randint(1990,2010)
    month=random.randint(1,12)
    day=random.randint(1,28)
    dob= datetime.date(year,month,day)
    print(f"User {i+1}: {first} {last} | Email: {email} | DOB: {dob}")

#QUESTION 4
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "undefined"
    return a / b
def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(3, 4) == 12
test_add()
test_multiply()

#QUESTION 5
import timeit
def sum_list(numbers):
    return sum(numbers)
print("\n=== Performance Testing Suite ===")
small_list = list(range(100))           
medium_list = list(range(10000))        
large_list = list(range(1000000))
def test_small():
    sum_list(small_list)

def test_medium():
    sum_list(medium_list)

def test_large():
    sum_list(large_list)
time_small = timeit.timeit(test_small, number=100)
time_medium = timeit.timeit(test_medium, number=100)
time_large = timeit.timeit(test_large, number=10)
print("Small list (100):       ", round(time_small, 6), "seconds")
print("Medium list (10,000):   ", round(time_medium, 6), "seconds")
print("Large list (1,000,000): ", round(time_large, 6), "seconds")

#QUESTION 6
import time
print("\n=== Stress Testing Tool ===")
def fake_api_call():
    return "OK"
start_time = time.time()
success = 0
failures = 0
for i in range(10000):
    try:
        result = fake_api_call()
        if result == "OK":
            success += 1
        else:
            failures += 1
    except:
        failures +=1

end_time = time.time()
print("Total Requests: ", success + failures)
print("Success:        ", success)
print("Failures:       ", failures)
print("Time Taken:     ", round(end_time - start_time, 4), "seconds")

#QUESTION 7
print("\n=== Regression Test: Greet Function ===")
def greet(name):
    return "Hello, " + name + "!"
expected_ali = "Hello, Ali!"
expected_sara = "Hello, Sara!"
result_ali = greet("Ali")
if result_ali == expected_ali:
    print(" Test Passed for Ali")
else:
    print(" Test Failed for Ali")
    print("Expected:", expected_ali)
    print("Got:     ", result_ali)
result_sara = greet("Sara")
if result_sara == expected_sara:
    print("✅ Test Passed for Sara")
else:
    print("❌ Test Failed for Sara")
    print("Expected:", expected_sara)
    print("Got:     ", result_sara)

#QUESTION 8
print("\n=== Integration Testing: User Registration + Email ===")
def register_user(username):
    if username:
        return f"{username} registered successfully"
    else:
        return "Registration failed"
def send_welcome_email(username):
    return f"Welcome email sent to {username}"
def register_and_notify(username):
    reg_msg = register_user(username)
    if "successfully" in reg_msg:
        email_msg = send_welcome_email(username)
        return reg_msg + " | " + email_msg
    else:
        return reg_msg + " | No email sent"
def test_register_and_notify():
    result = register_and_notify("Ahmed")
    expected = "Ahmed registered successfully | Welcome email sent to Ahmed"
    if result == expected:
        print(" Integration Test Passed")
    else:
        print(" Integration Test Failed")
        print("Expected:", expected)
        print("Got:     ", result)
test_register_and_notify()

#QUESTION 9
print("\n=== Automated Test Runner ===")
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def test_add_positive():
    assert add(2, 3) == 5
def test_add_zero():
    assert add(0, 0) == 0
def test_multiply_basic():
    assert multiply(3, 4) == 12
def test_multiply_by_zero():
    assert multiply(5, 0) == 0
def run_test(test_function):
    try:
        test_function()
        print("✅", test_function.__name__)
    except AssertionError:
        print("❌", test_function.__name__)
run_test(test_add)
run_test(test_multiply)
run_test(test_add_zero)
run_test(test_multiply_by_zero)

#QUESTION 10
print("\n=== CLI Bug Tracking System (Simplified) ===")
bug_list = []
while True:
    print("\n1. Report New Bug")
    print("2. View All Bugs")
    print("3. Mark Bug as Fixed")
    print("4. Exit")
    choice = input("Choose an option (1-4): ").strip()
    if choice not in ["1","2","3","4"]:
        print("⚠️ Invalid choice. Please enter 1-4.")
        continue
    if choice == "1":
        desc = input("Enter bug description: ").strip()
        if desc == "":
            print("⚠️ Description cannot be empty.")
        else:
            bug_list.append({"description": desc, "status": "Open"})
            print("✅ Bug added.")
    elif choice == "2":
        if len(bug_list) == 0:
            print("📭 No bugs reported.")
        else:
            print("\n📋 Bug List:")
            i = 0
            for bug in bug_list:
                print(str(i + 1) + ".", bug["description"], "-", "[" + bug["status"] + "]")
                i += 1
    elif choice == "3":
        if len(bug_list) == 0:
            print("❌ No bugs to fix.")
        else:
            i = 0
            for bug in bug_list:
                print(str(i + 1) + ".", bug["description"], "-", "[" + bug["status"] + "]")
                i += 1
            try:
                num = int(input("Enter bug number to mark as fixed: ").strip())
                if 1 <= num <= len(bug_list):
                    if bug_list[num - 1]["status"] == "Fixed":
                        print("ℹ️ This bug is already fixed.")
                    else:
                        bug_list[num - 1]["status"] = "Fixed"
                        print("✅ Bug marked as fixed.")
                else:
                    print("⚠️ Invalid bug number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")
    elif choice == "4":
        print("👋 Exiting Bug Tracker. Bye!")
        break

#QUESTION 11
import json
print("\n=== Simple Test Reporter ===")
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
def test_add():
    assert add(2, 3) == 5  

def test_multiply():
    assert multiply(2, 3) == 6  

def test_fail():
    assert multiply(2, 2) == 5
test_list = [test_add, test_multiply, test_fail]
results = []
for test in test_list:
    try:
        test()  
        print("✅", test.__name__)  
        results.append({"test": test.__name__, "status": "pass"})
    except AssertionError as e:
        print("❌", test.__name__, "-", str(e))  
        results.append({"test": test.__name__, "status": "fail", "error": str(e)})
with open("test_results.json", "w") as file:
    json.dump(results, file, indent=4)

print("📄 Results saved to test_results.json")

#QUESTION 12
import datetime

print("\n=== Quality Metrics Calculator ===")
bugs = [
    {"id": 1, "reported": "2024-06-01", "fixed": "2024-06-03"},
    {"id": 2, "reported": "2024-06-02", "fixed": "2024-06-04"},
    {"id": 3, "reported": "2024-06-05", "fixed": "2024-06-10"},
    {"id": 4, "reported": "2024-06-07", "fixed": "2024-06-08"},
]
total_bugs = len(bugs)
print(" Total Bugs Reported:", total_bugs)
total_days = 0
for bug in bugs:
    date_reported = datetime.datetime.strptime(bug["reported"], "%Y-%m-%d")
    date_fixed = datetime.datetime.strptime(bug["fixed"], "%Y-%m-%d")
    fix_time = (date_fixed - date_reported).days
    total_days += fix_time

average_fix_time = total_days / total_bugs
print("⏳ Average Bug Fix Time:", round(average_fix_time, 2), "days")
coverage_data = {
    "Week 1": 55,
    "Week 2": 65,
    "Week 3": 72
}

print("\n📈 Test Coverage Trend:")
for week, percent in coverage_data.items():
    print(week + ":", str(percent) + "%")

#QUESTION 13
print("\n=== Code Review Checklist Generator ===")
checklist = [
    "✅ Code follows naming conventions",
    "✅ No unused variables or functions",
    "✅ Code is properly indented",
    "✅ All new features are tested",
    "✅ No hardcoded values",
    "✅ Comments are clear and helpful",
    "✅ Function names are meaningful",
    "✅ Code is not duplicated",
    "✅ Proper error handling is done",
    "✅ All tests are passing"
]
print("📋 Before merging your code, make sure:")
for item in checklist:
    print("-",item)

#QUESTION 14
print("\n=== Testing Best Practices Guide Generator ===")
best_practices = [
    "# ✅ Testing Best Practices Guide\n",
    "1. **Write tests for every new feature**",
    "2. **Keep test functions short and focused**",
    "3. **Use meaningful test names** (like `test_login_success`)",
    "4. **Test both success and failure cases**",
    "5. **Use `assert` statements properly**",
    "6. **Avoid repeating the same code in multiple tests**",
    "7. **Keep test data realistic and readable**",
    "8. **Run tests automatically before every commit**",
    "9. **Use setup and teardown functions if needed**",
    "10. **Review test code like you review normal code**"
]
with open("testing_guide.md", "w") as file:
    for line in best_practices:
        file.write(line+"\n")       
print("📄 Guide saved as testing_guide.md")

#QUESTION 15
import traceback
print("\n=== Simple Debugging Toolkit ===")

def divide_numbers(x, y):
    print("📌 DEBUG: x =", x)
    print("📌 DEBUG: y =", y)
    return x / y

try:
    a = 10
    b = 0
    result = divide_numbers(a, b)
    print("Result:", result)
except Exception as e:
    print("\n❌ An error occurred:", e)
    print("\n🛠️ Full stack trace for debugging:")
    traceback.print_exc()

#✅ 10 Python Coding Tasks – Code Quality & Standards
#QUESTION 1
print("\n=== Code Style Checker ===")
import pycodestyle
style_checker = pycodestyle.StyleGuide()
file_to_check = "my_code_file.py"  

style_report = style_checker.check_files([file_to_check])

print("✅ Total lines checked:", style_report.counters.get("physical lines", 0))
print("❌ Style violations found:", style_report.total_errors)

if style_report.total_errors == 0:
    print("🎉 Code is clean and follows PEP 8!")
else:
    print("⚠️ Fix the warnings above to improve style.")

#QUESTION 2
print("\n=-= Documentation Generator =-=")
def docg_add(a, b):
    """Adds two numbers and returns the result."""
    return a + b
def docg_multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y
def docg_divide(numerator, denominator):
    if denominator == 0:
        return "undefined"
    return numerator / denominator
docg_functions = [docg_add, docg_multiply, docg_divide]
with open("generated_docs.md", "w") as docg_file:
    docg_file.write("# 📘 Auto-Generated Documentation\n\n")
    for func in docg_functions:
        docg_file.write(f"## {func.__name__}()\n")
        docg_file.write(func.__doc__ + "\n\n")

print("📄 Documentation saved to generateddocs.md")

#QUESTION 3
print("\n=== Code Formatter ===")
import autopep8
formatter_input_file = "sample_code_to_format.py"
with open(formatter_input_file, "r") as formatter_read_file:
    original_code = formatter_read_file.read()
formatted_code = autopep8.fix_code(original_code)
formatter_output_file = "formatted_code_output.py"
with open(formatter_output_file, "w") as formatter_write_file:
    formatter_write_file.write(formatted_code)

print("🎉 Code formatted and saved to", formatter_output_file)

#QUESTION 4 
print("\n=== Import Organizer ===")

import isort

import_file_path = "sample_imports_messy.py"

isort.file(import_file_path)

print("✅ Imports reorganized in", import_file_path)

#QUESTION 5
print("\n=== Dead Code Detector ===")
import ast
deadcode_file_path = "deadcode_sample.py"
with open(deadcode_file_path, "r") as deadcode_reader:
    deadcode_source = deadcode_reader.read()
deadcode_tree = ast.parse(deadcode_source)
deadcode_names = set()
deadcode_used = set()
for node in ast.walk(deadcode_tree):
    if isinstance(node, ast.FunctionDef):
        deadcode_names.add(node.name)
    elif isinstance(node, ast.Name):
        deadcode_used.add(node.id)
deadcode_unused = deadcode_names - deadcode_used
print("Unused functions:", deadcode_unused)

#QUESTION 6
print("\n=== Code Complexity Analyzer ===")
from radon.complexity import cc_visit
complexity_code = """
def easy(x):
    return x + 1
def hard(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(i)
"""
complexity_results = cc_visit(complexity_code)
for func in complexity_results:
    print(func.name, "- Complexity:", func.complexity)

#QUESTION 7
print("\n=== Security Audit Tool ===")
security_code = """
password = "12345"
def delete_all():
    eval("print('Danger')")
"""
if "password" in security_code or "eval(" in security_code:
    print("⚠️ Potential security issue found")

#QUESTION 8
print("\n=== Performance Profiler ===")
import cProfile
def perf_slow():
    total = 0
    for i in range(1000000):
        total += i
    return total
def perf_fast():
    return sum(range(1000000))
cProfile.run("perf_slow()")
cProfile.run("perf_fast()")

#QUESTION 9
print("\n=== Memory Leak Detector ===")
import tracemalloc
def mem_leak():
    big_list = [i for i in range(100000)]
    return big_list
tracemalloc.start()
mem_leak()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
for stat in top_stats[:3]:
    print(stat)

#QUESTION 10
print("\n=== Code Metrics Dashboard ===")
import os
metrics_path = "metrics_sample.py"
with open(metrics_path, "r") as metrics_reader:
    metrics_code = metrics_reader.read()
metrics_lines = metrics_code.count("\n")
metrics_functions = metrics_code.count("def ")
metrics_classes = metrics_code.count("class ")
print("Total lines:", metrics_lines)
print("Functions:", metrics_functions)
print("Classes:", metrics_classes)