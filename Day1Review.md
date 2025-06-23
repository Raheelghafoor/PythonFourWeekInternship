### Review of Your Code Implementation for 15 Python Beginner Tasks

# Let's review each question block-by-block, identify issues, and provide improvements.

# ---
# ✅ Question 1: Hello World Variations
# ❌ Mistake: The function say_hello() is called *inside itself*, leading to RecursionError
# ❗ Fix:
def say_hello():
    print("How are you")

say_hello()  # Move the call outside the function

# ✅ Suggestion:
# You could use a loop or list to generate variations dynamically for better code organization.

# ---
# ✅ Question 2: Personal Information Manager
# 👍 Well-structured. No major issues.
# 💡 Suggestion: Add input validation (e.g., check if age is a digit).

# ---
# ✅ Question 3: Data Type Explorer and Converter
# ❌ Mistake: Exceptions are too generic
# ❗ Fix:
try:
    int_value = int(value)
    print("As integer:", int_value)
except ValueError:
    print("Can't convert to integer.")

# ✅ Suggestion:
# Use isinstance() or a helper function to make it reusable.

# ---
# ✅ Question 4: Variable Scope Demonstrator
# ❌ Mistake: outer_function defines message, but does not print it
# ❗ Fix:
def outer_function():
    message = "I am local to outer function"

    def inner_function():
        message = "I am local to inner function"
        print("Inside inner function:", message)

    inner_function()
    print("Inside outer function:", message)

outer_function()

# ✅ Suggestion: Add global keyword example to demonstrate global scope clearly

# ---
# ✅ Question 5: Memory Address Tracker
# 👍 Works fine
# 💡 Suggestion: Add `id()` print before and after each variable change to show clearer memory address change.

# ---
# ✅ Question 6: Type Checking Utility
# ❌ Minor: input type is always string, so type checks on `user_input` aren't useful until conversion
# ❗ Fix:
# Convert and then check type as done below, which is correct. Nothing to change here except possibly clearer messages.

# ---
# ✅ Question 7: Dynamic Typing Examples
# 👍 Good demonstration. No issues.

# ---
# ✅ Question 8: Variable Naming Validator
# ❗ Fix print message grammar:
# Change: `a Python keyword (cannot be used as a variable name).`
# To: `It is a Python keyword and cannot be used as a variable name.`

# ---
# ✅ Question 9: Constants Simulator
# 👍 Conventional usage is fine.
# 💡 Suggestion: You could demonstrate immutability using a class to simulate enforced constants.

# ---
# ✅ Question 10: Unicode and Encoding Handler
# ❗ Suggestion:
# Add a `try` block when decoding, in case of errors from malformed input.

# ---
# ✅ Question 11: Number System Conversion
# ❗ Add input validation:
try:
    decimal = int(input("Please enter a decimal: "))
    print("Binary:", bin(decimal))
    print("Octal:", oct(decimal))
    print("Hexadecimal:", hex(decimal))
except ValueError:
    print("Please enter a valid integer.")

# ---
# ✅ Question 12: Boolean Logic Demonstrator
# 👍 Logic and use of XOR with `^` is clever
# ❗ Suggestion: Explain XOR in comments for clarity

# ---
# ✅ Question 13: None Value Handler
# 👍 Correct implementation. Good use of `None`

# ---
# ✅ Question 14: Garbage Collection Observer
# ❗ Fix: `gc.get_objects()` returns all tracked objects, can be large. Filter if needed.
# 💡 Suggestion: Use `gc.get_stats()` for summarized tracking info

# ---
# ✅ Question 15: Performance Timing Utility
# ❌ Mistake: `time.time()` isn’t accurate for very small differences
# ❗ Fix:
import timeit
print("Built-in sort time:", timeit.timeit(lambda: built_in_sort(numbers), number=10))
print("Bubble sort time:", timeit.timeit(lambda: bubble_sort(numbers), number=10))

# ---
# ✅ Overall Suggestions
# 1. Add error handling where input is involved
# 2. Add comments to explain logic blocks
# 3. Avoid recursion mistakes like in Question 1
# 4. Use `timeit` instead of `time` for performance timing
# 5. Use specific exceptions instead of generic `except:`

# Let me know if you want a version of this fully rewritten and cleaned up in one script.
