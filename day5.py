#✅ 15 Python Coding Tasks – Advanced Logic Implementation
#QUESTION 1
print("=== Welcome to the Multi-Step Form ===")
while True:
    name = input("Step 1 - Enter your name: ").strip()
    if len(name) >= 2 and name.isalpha():
        print(" Name accepted.")
        break
    else:
        print(" Invalid name. Please enter a valid name (only letters, at least 2 characters).")
while True:
    age_input = input("Step 2 - Enter your age: ").strip()
    if age_input.isdigit():
        age = int(age_input)
        if 10 <= age <= 100:
            print(" Age accepted.")
            break
        else:
            print(" Age must be between 10 and 100.")
    else:
        print(" Please enter a valid number.")
while True:
    email = input("Step 3 - Enter your email: ").strip()
    if "@" in email and "." in email:
        print(" Email accepted.")
        break
    else:
        print(" Invalid email format. Try again.")
print("\n=== Review Your Information ===")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"Email: {email}")       
while True:
    confirm = input("Is this information correct? (yes/no): ").lower()
    if confirm == "yes":
        print(" Form submitted successfully!")
        break
    elif confirm == "no":
        print(" Form not submitted. Restart the form to correct data.")
        break
    else:
        print(" Please type 'yes' or 'no'.")

#QUESTION 2
print("\n=== Game Character Manager ===")
state = "idle"
health = 100

def show_status():
    print(f"\n Current State: {state.upper()} | Health: {health}")

while True:
    show_status()
    print("\nChoose an action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Die")
    print("4. Revive (only if dead)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()
    if not choice.isdigit():
        print(" Please enter a number between 1 and 5.")
        continue
    choice = int(choice)

    if choice == 1:
        if state == "dead":
            print(" You are dead. You can't attack.")
        else:
            print(" Attacking!")
            state = "attack"
            health -= 10
            if health <= 0:
                print(" You died in battle!")
                state = "dead"
                health = 0
            else:
                state = "idle"

    elif choice == 2:
        if state == "dead":
            print(" You are dead. You can't heal.")
        else:
            print(" Healing...")
            state = "heal"
            health += 15
            if health > 100:
                health = 100
            state = "idle"

    elif choice == 3:
        print(" You chose to die.")
        state = "dead"
        health = 0

    elif choice == 4:
        if state == "dead":
            print(" Reviving...")
            state = "idle"
            health = 50
        else:
            print(" You are not dead.")

    elif choice == 5:
        print(" Exiting Game Character Manager.")
        break

    else:
        print(" Invalid choice. Please enter 1 to 5.")

#QUESTION 3
print("===  Smart Recommendation Engine ===")
while True:
    type_input = input("What do you want (movies/books/games)? ").strip().lower()
    if type_input in ["movies", "books", "games"]:
        break
    else:
        print(" Please choose from: movies, books, or games.")
if type_input == "movies":
    while True:
        genre_input = input("Enter movie genre (action/comedy): ").strip().lower()
        if genre_input == "action":
            print(" Try: 'John Wick', 'Mad Max'")
            break
        elif genre_input == "comedy":
            print(" Try: 'The Hangover', 'Superbad'")
            break
        else:
            print(" Please choose 'action' or 'comedy'.")
elif type_input == "books":
    while True:
        genre_input = input("Enter book genre (fantasy/mystery): ").strip().lower()
        if genre_input == "fantasy":
            print(" Try: 'Harry Potter', 'The Hobbit'")
            break
        elif genre_input == "mystery":
            print(" Try: 'Sherlock Holmes', 'Gone Girl'")
            break
        else:
            print(" Please choose 'fantasy' or 'mystery'.")

elif type_input == "games":
    while True:
        genre_input = input("Enter game genre (sports/adventure): ").strip().lower()
        if genre_input == "sports":
            print(" Try: 'FIFA', 'NBA 2K'")
            break
        elif genre_input == "adventure":
            print(" Try: 'Zelda', 'Uncharted'")
            break
        else:
            print(" Please choose 'sports' or 'adventure'.")

#QUESTION 4
print("\n=== Dynamic Pricing System ===")

original_price = 100

while True:
    demand_level = input("Enter demand (low/medium/high): ").strip().lower()
    if demand_level in ["low", "medium", "high"]:
        break
    else:
        print("Please enter 'low', 'medium', or 'high'.")

while True:
    time_input = input("Enter time (morning/afternoon/night): ").strip().lower()
    if time_input in ["morning", "afternoon", "night"]:
        break
    else:
        print("Please enter 'morning', 'afternoon', or 'night'.")

while True:
    location_input = input("Enter location type (urban/rural): ").strip().lower()
    if location_input in ["urban", "rural"]:
        break
    else:
        print("Please enter 'urban' or 'rural'.")

price = original_price

if demand_level == "high":
    price += 30
elif demand_level == "medium":
    price += 15

if time_input == "night":
    price += 10
elif time_input == "morning":
    price -= 5

if location_input == "urban":
    price += 20
elif location_input == "rural":
    price -= 10

print("\nFinal price based on conditions: $", price)

#QUESTION 5
print("\n********Medical Inquiries********")
print("\nPlease answer the following questions")
def get_response(question):
       while True:
           response=input(question).strip().lower()
           if response in["yes","no"]:
               return response
           else:
               print("Invalid response. Please type 'yes' or 'no'.")

fever = get_response("Do you have fever? ")
cough = get_response("Do you have cough? ")
fatigue = get_response("Are you feeling fatigued? ")
headache = get_response("Do you have a headache? ")
sore_throat = get_response("Do you have a sore throat? ")

print("\n******** Diagnosis Suggestion ********")
if fever == "yes" and cough == "yes" and fatigue == "yes":
    print("- You may have the flu. Rest and stay hydrated.")
elif sore_throat == "yes" and headache == "yes":
    print("- It could be a common cold. Consider seeing a doctor if symptoms persist.")
elif fever == "yes" and cough == "yes" and sore_throat == "yes":
    print("- Symptoms may match COVID-19. Consider getting tested.")
elif fatigue == "yes" and headache == "yes":
    print("- Could be due to stress or lack of sleep. Try to rest and hydrate.")
else:
    print("- Symptoms are unclear. Please consult a healthcare provider for proper diagnosis.")

#QUESTION 6
print("\n=== Portfolio Advisor ===")
while True:
    age_input = input("Enter your age: ").strip()
    if age_input.isdigit():
        user_age = int(age_input)
        if user_age > 0:
            break
    print("Please enter a valid positive number for age.")
while True:
    income_level = input("Enter your income level (low/middle/high): ").strip().lower()
    if income_level in ["low", "middle", "high"]:
        break
    print("Please enter 'low', 'middle', or 'high'.")
while True:
    risk_level = input("What is your risk tolerance (low/medium/high): ").strip().lower()
    if risk_level in ["low", "medium", "high"]:
        break
    print("Please enter 'low', 'medium', or 'high'.")
print("\n=== Recommended Strategy ===")

if risk_level == "high" and user_age < 35 and income_level == "high":
    print("Aggressive Growth: Consider stocks, mutual funds, and crypto.")
elif risk_level == "medium" and user_age < 50 and income_level in ["middle", "high"]:
    print("Balanced Portfolio: Mix of stocks and bonds.")
elif risk_level == "low" or user_age >= 60 or income_level == "low":
    print("Conservative Plan: Focus on bonds, savings, and fixed income.")
else:
    print("Moderate Strategy: Consider a balanced approach with steady growth options.")

#QUESTION 7
print("\n=== Smart Thermostat System ===")
while True:
    time_period = input("Enter time of day (morning/afternoon/night): ").strip().lower()
    if time_period in ["morning", "afternoon", "night"]:
        break
    print("Please enter 'morning', 'afternoon', or 'night'.")

while True:
    occupancy_status = input("Is someone at home? (yes/no): ").strip().lower()
    if occupancy_status in ["yes", "no"]:
        break
    print("Please type 'yes' or 'no'.")

while True:
    weather_condition = input("Enter current weather (hot/cold/mild): ").strip().lower()
    if weather_condition in ["hot", "cold", "mild"]:
        break
    print("Please enter 'hot', 'cold', or 'mild'.")

print("\n=== Temperature Recommendation ===")

if occupancy_status == "no":
    print("Set thermostat to energy-saving mode (temperature: 24°C).")
elif weather_condition == "cold":
    if time_period == "morning":
        print("Increase temperature to 22°C for comfort.")
    else:
        print("Keep temperature at 21°C.")
elif weather_condition == "hot":
    if time_period == "afternoon":
        print("Cool down to 20°C.")
    else:
        print("Maintain at 22°C.")
else:  
    print("Maintain moderate temperature at 23°C.")

#QUESTION 8
print("\n=== Content Moderation System ===")
flagged_keywords = ["hate", "violence", "kill", "stupid", "idiot", "dumb"]
user_text = input("Enter your content: ").strip().lower()
flagged_found = False
for word in flagged_keywords:
    if word in user_text:
        flagged_found = True
        break
print("\n=== Moderation Result ===")
if flagged_found:
    print(" Inappropriate content detected. Please revise your message.")
else:
    print(" Content is clean. No issues found.")

#QUESTION 9
print("\n=== Risk Assessment Tool ===")
while True:
    age_input = input("Enter your age: ").strip()
    if age_input.isdigit():
        risk_age = int(age_input)
        if risk_age > 0:
            break
    print("Please enter a valid positive number for age.")
while True:
    smokes = input("Do you smoke? (yes/no): ").strip().lower()
    if smokes in ["yes", "no"]:
        break
    print("Please answer with 'yes' or 'no'.")
while True:
    has_illness = input("Do you have any chronic illness? (yes/no): ").strip().lower()
    if has_illness in ["yes", "no"]:
        break
    print("Please answer with 'yes' or 'no'.")

risk_score = 0
if risk_age >= 60:
    risk_score += 2
elif risk_age >= 40:
    risk_score += 1

if  smokes == "yes":
    risk_score += 2

if has_illness == "yes":
    risk_score += 2
print("\n=== Risk Evaluation Result ===")
if risk_score >= 5:
    print("Risk Level: HIGH — Please consult a medical professional.")
elif risk_score >= 3:
    print("Risk Level: MEDIUM — Consider regular check-ups and healthy habits.")
else:
    print("Risk Level: LOW — Keep up your good health practices.")

#QUESTION 10
print("\n=== Welcome to HelpBot ===")
print("Ask me something. Type 'exit' to end.\n")

while True:
    question = input("You: ").strip().lower()

    if question == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    elif question == "what are your hours":
        print("Bot: We are open from 9 AM to 5 PM.")

    elif question == "how to reset password":
        print("Bot: Click on 'Forgot Password' on the login page.")

    elif question == "where is my order":
        print("Bot: Check the 'My Orders' section in your account.")

    elif question == "how to contact support":
        print("Bot: Email us at support@example.com.")

    elif "?" in question:
        print("Bot: I don't know that. I’ll ask a human to help you.")

    else:
        print("Bot: Sorry, I didn't understand. Please ask something else.")

#QUESTION 11
print("\n=== Fraud Detection System ===")
while True:
    amount_input = input("Enter transaction amount: ").strip()
    if amount_input.isdigit():
        transaction_amount = int(amount_input)
        if transaction_amount > 0:
            break
    print("Please enter a valid positive number.")
while True:
    count_input = input("How many transactions in last hour? ").strip()
    if count_input.isdigit():
        transaction_count = int(count_input)
        if transaction_count > 0:
            break
    print("Please enter a valid positive number.")
reasons = []
if transaction_amount > 10000:
    reasons.append("High transaction amount")
if transaction_count > 5:
    reasons.append("Too many transactions in short time")

if reasons:
    print("\nSuspicious activity detected!")
    for r in reasons:
        print("Reason:", r)
else:
    print("\nNo fraud detected. Transaction seems normal.")

#QUESTION 12
print("\n=== Quality Control Checker ===")
while True:
    size_input = input("Enter size accuracy (0 to 10): ").strip()
    if size_input.isdigit():
        size_accuracy = int(size_input)
        if 0 <= size_accuracy <= 10:
            break
    print("Please enter a number between 0 and 10.")
while True:
    color_input = input("Enter color match score (0 to 10): ").strip()
    if color_input.isdigit():
        color_score = int(color_input)
        if 0 <= color_score <= 10:
            break
    print("Please enter a number between 0 and 10.")
while True:
    durability_input = input("Enter durability rating (0 to 10): ").strip()
    if durability_input.isdigit():
        durability_rating = int(durability_input)
        if 0 <= durability_rating <= 10:
            break
    print("Please enter a number between 0 and 10.")
average_score = (size_accuracy + color_score + durability_rating) / 3
print("\n=== Quality Check Result ===")
if average_score >= 8:
    print("Result: PASS ")
elif average_score >= 5:
    print("Result: REWORK ")
else:
    print("Result: REJECT ")

#QUESTION 13
print("\n=== Resource Allocation Optimizer ===")
while True:
    skill_input = input("Enter skill level (beginner/intermediate/expert): ").strip().lower()
    if skill_input in ["beginner", "intermediate", "expert"]:
        break
    print("Please enter 'beginner', 'intermediate', or 'expert'.")
while True:
    available = input("Are you available now? (yes/no): ").strip().lower()
    if available in ["yes", "no"]:
        break
    print("Please answer with 'yes' or 'no'.")
while True:
    task_priority = input("Enter task priority (low/medium/high): ").strip().lower()
    if task_priority in ["low", "medium", "high"]:
        break
    print("Please enter 'low', 'medium', or 'high'.")
print("\n=== Task Assignment Result ===")

if available == "no":
    print("Cannot assign task — Resource not available.")
elif skill_input == "expert" and task_priority == "high":
    print("Assign task:  High-priority task assigned to expert.")
elif skill_input in ["intermediate", "expert"] and task_priority in ["medium", "high"]:
    print("Assign task:  Medium/High task assigned.")
elif skill_input == "beginner" and task_priority == "low":
    print("Assign task:  Low-priority task assigned to beginner.")
else:
    print("Do not assign:  Task requirements do not match resource.")

#QUESTION 14
print("\n=== Emergency Response System ===")
while True:
    emergency_type = input("Enter emergency type (fire/medical/security): ").strip().lower()
    if emergency_type in ["fire", "medical", "security"]:
        break
    print("Please enter 'fire', 'medical', or 'security'.")
while True:
    severity = input("Enter severity (low/medium/high): ").strip().lower()
    if severity in ["low", "medium", "high"]:
        break
    print("Please enter 'low', 'medium', or 'high'.")
while True:
    location = input("Enter location type (urban/rural): ").strip().lower()
    if location in ["urban", "rural"]:
        break
    print("Please enter 'urban' or 'rural'.")
print("\n=== Response Suggestion ===")
if severity == "high":
    print("Action:  Dispatch emergency team immediately.")
elif severity == "medium":
    if location == "urban":
        print("Action:  Send local response unit within 10 minutes.")
    else:
        print("Action:  Alert nearest emergency center for rural assistance.")
else:
    print("Action: Log the report and monitor. No urgent dispatch needed.")
if emergency_type == "fire":
    print("Note:  Fire brigade should be informed.")
elif emergency_type == "medical":
    print("Note:  Nearest ambulance service alerted.")
elif emergency_type == "security":
    print("Note:  Local police department notified.")

#QUESTION 15
print("\n=== Smart Traffic Controller ===")
while True:
    traffic_level = input("Enter congestion level (low/medium/high): ").strip().lower()
    if traffic_level in ["low", "medium", "high"]:
        break
    print("Please enter 'low', 'medium', or 'high'.")
while True:
    special_event = input("Is there any special event nearby? (yes/no): ").strip().lower()
    if special_event in ["yes", "no"]:
        break
    print("Please type 'yes' or 'no'.")
print("\n=== Signal Timing Recommendation ===")

if traffic_level == "high" or special_event == "yes":
    print("Signal stays GREEN longer (extended duration).")
elif traffic_level == "medium":
    print("Signal stays GREEN for normal duration.")
else:
    print("Signal stays GREEN for shorter duration (low traffic).")

#✅ 20 Python Coding Tasks – Problem-Solving Patterns
#QUESTION 1
print("\n=== Pattern Recognition Suite ===")
user_input = input("Enter some text or numbers: ").strip()
if user_input.isdigit():
    print("Pattern Detected: Only Numbers")
elif user_input.isalpha():
    print("Pattern Detected: Only Letters")
elif user_input.isalnum():
    print("Pattern Detected: Letters and Numbers (Alphanumeric)")
elif "@" in user_input and "." in user_input:
    print("Pattern Detected: Might be an Email Address")
elif len(set(user_input)) == 1:
    print("Pattern Detected: Repeated Characters")
elif " " in user_input:
    print("Pattern Detected: Sentence or Phrase")
else:
    print("Pattern: Unknown or Special Characters Detected")

#QUESTION 2
main_task = input("Enter the main problem to solve: ").strip()
subtasks = []
for i in range(1, 4):
    subtask = input(f"Enter subtask {i}: ").strip()
    subtasks.append(subtask)
print("\n=== Breakdown of Your Problem ===")
print("Main Task:", main_task)
print("Subtasks:")
for index, task in enumerate(subtasks, start=1):
    print(f"  {index}. {task}")

#QUESTION 3
print("\n=== Algorithm Visualizer: Bubble Sort ===")
numbers = input("Enter some numbers (space-separated): ").strip()
num_list = []
for n in numbers.split():
    num_list.append(int(n))
for i in range(len(num_list)):
    for j in range(len(num_list)-1-i):
          if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    print(num_list)
print("\nSorted List:", num_list)

#QUESTION 4
print("\n=== Debugging Helper ===")

try:
    num1 = int(input("Enter the first number: ").strip())
    num2 = int(input("Enter the second number: ").strip())

    result = num1 / num2
    print("Result of division:", result)

except ValueError:
    print(" Error: Please enter valid numbers only.")

except ZeroDivisionError:
    print(" Error: Cannot divide by zero.")

except Exception as e:
    print(" An unexpected error occurred:", str(e))

print("Program completed.")

#QUESTION 5
print("\n=== Simple Code Complexity Checker ===")
print("Enter your code line by line. Type 'end' to stop.\n")

lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    lines.append(line.strip())
count = 0
for line in lines:
    if line.startswith("if") or line.startswith("for") or line.startswith("while"):
        count += 1
complexity = 1 + count

print("\n=== Complexity Check Result ===")
print("Estimated Complexity:", complexity)

#QUESTION 6
import time

print("\n=== Performance Profiler ===")
def sample_task():
    print("Running a sample task...")
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

start_time = time.time()
result = sample_task()
end_time = time.time()
duration = end_time - start_time
print("Task completed. Result:", result)
print(f"Execution time: {duration:.4f} seconds")

#QUESTION 7
import sys

print("\n=== Memory Usage Tracker ===")
num = 123
text = "Hello, world!"
my_list = [1, 2, 3, 4, 5]
my_dict = {"a": 1, "b": 2}
print("Memory used by integer (num):", sys.getsizeof(num), "bytes")
print("Memory used by string (text):", sys.getsizeof(text), "bytes")
print("Memory used by list (my_list):", sys.getsizeof(my_list), "bytes")
print("Memory used by dictionary (my_dict):", sys.getsizeof(my_dict), "bytes")

#QUESTION 8
print("\n=== Error Pattern Detector ===")
print("Type log lines below (type 'end' to stop):")
errors = 0
while True:
    line = input()
    if line.lower() == "end":
        break
    if "error" in line.lower() or "fail" in line.lower():
        errors += 1
print("\nTotal error lines found:", errors)
if errors > 0:
    print("Warning: Some errors were found in the logs.")
else:
    print("All good. No errors found.")

#QUESTION 9
print("\n=== Code Optimization Suggestion Tool ===")
print("Enter a block of code (type 'end' to finish):")
code_lines = []
while True:
    line=input()
    if line.strip().lower() == "end":
        break
    code_lines.append(line.strip())
print("\n=== Suggestions ===")
suggested = False
for line in code_lines:
     if "for" in line and "range(len(" in line:
        print("- Suggestion: Use 'enumerate()' instead of 'range(len(...))' for better readability.")
        suggested = True
     if "+=" in line and line.strip().startswith("sum") and "for" in line:
        print("- Suggestion: Use built-in 'sum()' function for faster performance.")
        suggested = True
     if "== True" in line or "== False" in line:
        print("- Suggestion: Use just 'if condition' or 'if not condition' instead of comparing with True/False.")
        suggested = True
if not suggested:
    print("No common inefficiencies found. Your code looks fine!")


#QUESTION 10
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 6) == -12

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_mixed():
    assert add(-2, 3) == 1

#QUESTION 11
print("\n=== Simple Documentation Generator ===")
print("Type your function lines (type 'end' to stop):\n")

lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    lines.append(line.strip())

print("\n=== Generated Documentation ===")
for line in lines:
    if line.startswith("def ") and "(" in line and "):" in line:
        # Get function name
        func_name = line.split("def ")[1].split("(")[0]

        # Get parameters
        inside = line.split("(")[1].split(")")[0]
        parameters = inside.split(",") if inside else []

        print(f"\nFunction Name: {func_name}")
        if parameters:
            print("Parameters:", ", ".join([p.strip() for p in parameters]))
        else:
            print("Parameters: None")
        print("Description: (Write what this function does)")
        print("Returns: (Describe the output)")

#QUESTION 12
print("\n=== Simple Code Review Tool ===")
print("Type your code line by line. Type 'end' to stop:\n")

code = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    code.append(line)

print("\n=== Code Review Results ===")

in_function = False
function_line_count = 0

for i in range(len(code)):
    line = code[i]

    if line.strip().startswith("def "):
        in_function = True
        function_line_count = 1
        continue

    if in_function:
        if line.strip() == "":
            in_function = False
        else:
            function_line_count += 1
            if function_line_count > 15:
                print("Warning: Function too long (more than 15 lines)")
                in_function = False

    if line.count("    ") >= 4:
        print("Warning: Deeply nested code (4+ indent levels)")

print("Review completed.")

#QUESTION 13
print("\n=== Best Practices Checker ===")
print("Enter your code line by line (type 'end' to stop):")

code_lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    code_lines.append(line.strip())

print("\n=== PEP8 & Naming Warnings ===")

for line in code_lines:
    if len(line) > 79:
        print("Line too long (over 79 characters):", line)
    
    if "=" in line and not line.strip().startswith("#"):
        parts = line.split("=")
        var_name = parts[0].strip()
        if var_name != var_name.lower():
            print("Warning: Variable name should be lowercase:", var_name)
        if len(var_name) < 2:
            print("Warning: Variable name too short:", var_name)
    
    if "  " in line:
        print("Warning: Extra spaces found in line:", line)
    
    if line.strip().startswith("print(") and "  " in line:
        print("Check spacing in print statement:", line)

print("\nCheck completed.")

#QUESTION 14
print("\n=== Security Vulnerability Scanner ===")
print("Paste your code line by line (type 'end' to finish):")

code_lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    code_lines.append(line.strip())

print("\n=== Scan Results ===")

for line in code_lines:
  
    if "password" in line.lower() or "secret" in line.lower():
        if "=" in line and ('"' in line or "'" in line):
            print("Warning: Hardcoded credential detected:", line)

   
    if "import os" in line or "import subprocess" in line:
        print("Warning: Risky import detected (os/subprocess):", line)

    if "eval(" in line or "exec(" in line:
        print("Warning: Dangerous function usage (eval/exec):", line)

print("\nScan complete. Always avoid hardcoded credentials and unsafe code.")

#QUESTION 15
print("\n=== Code Metrics Calculator ===")
print("Paste your code line by line (type 'end' to stop):")

code_lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    code_lines.append(line)
total_lines = len(code_lines)
blank_lines = 0
comment_lines = 0
function_count = 0
for line in code_lines:
    stripped = line.strip()
    if stripped == "":
        blank_lines += 1
    elif stripped.startswith("#"):
        comment_lines += 1
    elif stripped.startswith("def "):
        function_count += 1
print("\n=== Code Metrics ===")
print("Total Lines of Code (LOC):", total_lines)
print("Blank Lines:", blank_lines)
print("Comment Lines:", comment_lines)
print("Function Definitions:", function_count)


#QUESTION 16
print("\n=== Refactoring Assistant ===")
print("Paste your code line by line (type 'end' to finish):")
code_lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    code_lines.append(line)

print("\n=== Refactoring Suggestions ===")
block_start = None
block_length = 0
suggested = False 

for i, line in enumerate(code_lines):
    stripped = line.strip()
    if stripped and line.startswith("    "):  
        if block_start is None:
            block_start = i
        block_length += 1
    else:
        if block_length >= 10:
            print(f"- Suggestion: Extract lines {block_start + 1} to {i} into a separate function.")
            suggested = True   
        block_start = None
        block_length = 0

if block_length >= 10:
    print(f"- Suggestion: Extract lines {block_start + 1} to {len(code_lines)} into a function.")
    suggested = True

if not suggested:
    print("No large blocks found. Your code looks modular!")

print("Review completed.")



#QUESTION 17
print("\n=== Design Pattern Identifier ===")
print("Describe your code behavior or purpose:")
print("Type 'end' to stop entering lines.\n")

description_lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    description_lines.append(line.lower())

description = " ".join(description_lines)

print("\n=== Suggested Design Pattern ===")

if "only one" in description or "global access" in description or "one instance" in description:
    print("→ Pattern Match: Singleton Pattern")
    print("Use when you need only one instance of a class (e.g., a database connection).")

elif "creates objects" in description or "decide which class" in description or "based on condition" in description:
    print("→ Pattern Match: Factory Pattern")
    print("Use when you need to create objects without specifying the exact class.")

elif "notify" in description or "listeners" in description or "event" in description or "subscribe" in description:
    print("→ Pattern Match: Observer Pattern")
    print("Use when multiple objects should be notified of changes in another object.")

else:
    print("Could not confidently match to a known pattern. Try including words like:")
    print("- 'only one', 'notify', 'creates objects', 'subscribe', etc.")

#QUESTION 18
print("\n=== Code Smell Detector ===")
print("Paste your code line by line (type 'end' to finish):")

code_lines = []
while True:
    line = input()
    if line.strip().lower() == "end":
        break
    code_lines.append(line)

print("\n=== Detected Code Smells ===")

method_lines = 0
inside_method = False
function_count = 0
magic_number_found = False

for line in code_lines:
    stripped = line.strip()
    if stripped.startswith("def "):
        function_count += 1
        inside_method = True
        method_lines = 1
        continue

    if inside_method:
        if stripped == "":
            inside_method = False
        else:
            method_lines += 1
            if method_lines > 15:
                print("- Smell: Long method detected (more than 15 lines)")

    
    for word in stripped.split():
        if word.isdigit() and word not in ["0", "1"]:
            print(f"- Smell: Magic number used → {word}")
            magic_number_found = True
            break


if function_count > 8:
    print("- Smell: Large class detected (more than 8 functions)")

if function_count == 0 and not magic_number_found:
    print("No obvious code smells found. Good job!")

print("Analysis complete.")

#QUESTION 19
import time

print("\n=== Performance Bottleneck Finder ===")
def slow_function():
    time.sleep(1.5)
    return "Slow work done"

def fast_function():
    time.sleep(0.2)
    return "Fast work done"

def test_function(func):
    start = time.time()
    result = func()
    end = time.time()
    duration = end - start
    print(f"{func.__name__} took {duration:.3f} seconds → Result: {result}")
    return duration


slow_time = test_function(slow_function)
fast_time = test_function(fast_function)


if slow_time > fast_time * 2:
    print("\n  Bottleneck detected: 'slow_function' is significantly slower.")
else:
    print("\n No major bottleneck detected.")


#QUESTION 20
print("\n=== Quality Assurance Suite ===")
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 4) == -8

tests = [("test_add", test_add), ("test_multiply", test_multiply)]
passed = 0
failed = 0

print("\nRunning tests...\n")
for name, test in tests:
    try:
        test()
        print(f"[PASS] {name}")
        passed += 1
    except AssertionError:
        print(f"[FAIL] {name}")
        failed += 1

print("\n=== Test Summary ===")
print("Tests Passed:", passed)
print("Tests Failed:", failed)

if failed == 0:
    print("All tests passed successfully!")
else:
    print(" Some tests failed. Please review.")
