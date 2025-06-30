# ✅ **Review – Python Assessment (Intern Level)**

### ❌ **Task 1: Grid Path Counter**

**Issue:**
The code is manually summing cells and not actually counting valid paths from (0,0) to (2,2) avoiding `0` (obstacles).

**Expectation:**
Count all possible paths using **recursion** or **dynamic programming** by moving only right or down and avoiding `0` cells.



### ❌ **Task 2: Stock Feed Analyzer**

**Issues:**

* Input is taken as `input()`, but not converted to integers.
* `if t <= 1:` is invalid (`t` is a string).
* Incorrect logic for finding max and min (`prices[i+1] > prices[i]` is invalid in `for i in prices:` loop).

**Expectation:**
Collect valid integers, calculate average, min, and max safely.



### ❌ **Task 3: CSV Reader Fix**

**Issue:**

* `numbers = row.split(',')` returns strings, not numbers.
* `sum(numbers)` fails without converting strings to integers.

**Expectation:**
Convert to `int`, then sum each row.



### ❌ **Task 4: Positive Number Decorator**

**Issue:**
The decorator is completely missing. Only a normal function is written.

**Expectation:**
A proper `@check_positive` decorator that raises `ValueError` for negative inputs.



# ✅ Correct Implementations



### ✅ **Task 1: Grid Path Counter (Valid Paths Avoiding Obstacles)**

```python
def count_paths(grid, i=0, j=0, memo=None):
    if memo is None:
        memo = {}

    rows, cols = len(grid), len(grid[0])
    if i >= rows or j >= cols or grid[i][j] == 0:
        return 0
    if i == rows - 1 and j == cols - 1:
        return 1

    if (i, j) in memo:
        return memo[(i, j)]

    right = count_paths(grid, i, j + 1, memo)
    down = count_paths(grid, i + 1, j, memo)
    memo[(i, j)] = right + down
    return memo[(i, j)]

grid = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print("Total valid paths:", count_paths(grid))  # Output: 3
```



### ✅ **Task 2: Stock Price Analyzer**

```python
def analyze_prices():
    print("Enter prices (type 'done' to finish):")
    prices = []
    while True:
        val = input("Price: ")
        if val.lower() == "done":
            break
        try:
            price = float(val)
            prices.append(price)
        except ValueError:
            print("Invalid number, try again.")

    if not prices:
        print("No prices entered.")
        return

    average = sum(prices) / len(prices)
    print("\nAnalysis:")
    print("Min:", min(prices))
    print("Max:", max(prices))
    print("Average:", round(average, 2))

# Example run
# analyze_prices()
```



### ✅ **Task 3: CSV Reader Fix**

```python
def process_csv(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            numbers = line.strip().split(',')
            numbers = [int(n) for n in numbers]
            print(sum(numbers))

# Sample CSV (data.csv):
# 2,3,4
# 1,1,1
# 5,5,5
# Output:
# 9
# 3
# 15
```



### ✅ **Task 4: Positive Number Validator Using Decorator**

```python
def check_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive")
        return func(x)
    return wrapper

@check_positive
def square(x):
    return x * x

# Example usage:
try:
    print(square(5))    # ✅ Output: 25
    print(square(-3))   # ❌ Raises ValueError
except ValueError as e:
    print("Error:", e)
```



# 📌 Summary

| Task              | Original Code                   | Result | Corrected                        |
| ----------------- | ------------------------------- | ------ | -------------------------------- |
| Grid Path Counter | ❌ Wrong logic, no path checking | ❌      | ✅ Recursion with memoization     |
| Stock Analyzer    | ❌ Input handling & logic errors | ❌      | ✅ Clean parsing & calculations   |
| CSV Reader        | ❌ Didn't convert to integers    | ❌      | ✅ Correct CSV parsing            |
| Decorator         | ❌ No decorator used             | ❌      | ✅ Full decorator with validation |


