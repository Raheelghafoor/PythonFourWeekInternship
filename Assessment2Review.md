# ✅ **Review – Python Assessment (Beginner Level)**


### ✅ **Section 1: List Operations**

---

### ❌ **Task 1: List Stats Calculator**

**Issues:**

* The function `analyze_numbers()` takes no parameters — violates requirement of accepting a list as input.
* Hardcoded list used inside function (`num = [...]`) instead of dynamic input.
* Variable name `even` could be `even_numbers` for clarity.

**Expectation:**

* Take list as parameter, return required stats cleanly and generically.

**Fix:**

```python
def analyze_numbers(numbers: list) -> dict:
    return {
        "count": len(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers),
        "even_numbers": [n for n in numbers if n % 2 == 0]
    }
```

---

### ❌ **Task 2: List Filtering**

**Issues:**

* Function `clean_function()` doesn’t take any arguments, violates prompt requirement.
* Hardcoded list inside.
* Does not remove `None` values.
* Poor naming: `rest`, `numb`, and `"Cleaned list :)"` are unprofessional.
* `if numb is None:` is useless because `numb` is always initialized.

**Expectation:**

* Use list comprehension to remove `None` and negative numbers.

**Fix:**

```python
def clean_list(data: list) -> list:
    return [x for x in data if x is not None and x >= 0]
```

---

### ✅ **Section 2: Dictionary Manipulation**

---

### ✅ **Task 3: Student Score Updater**

👍 **Good:**

* Correct implementation of update and score increment
* Used `round()` appropriately

❗ **Improvement:**

* Function signature should use type hints

**Suggestion:**

```python
def update_scores(students: dict, new_name: str, new_score: int) -> dict:
    ...
```

---

### ❌ **Task 4: Dictionary Filter by Score**

**Issues:**

* Returns a list of individual dicts instead of a single dict.
* Variable name `revisedclean` is unclear.
* Extra print statements inside function — not needed.

**Expectation:**
Return a dictionary directly with all students scoring >= 60.

**Fix:**

```python
def filter_passing(students: dict) -> dict:
    return {name: score for name, score in students.items() if score >= 60}
```

---

### ✅ **Section 3: Math and Built-in Modules**

---

### ✅ **Task 5: Geometry Calculator**

👍 **Good:**

* Correct formulas used
* Used `math.pi` appropriately

❗ **Improvement:**

* Function should follow prompt naming (`geometry_calculator`)
* Use type hints for clarity

**Suggestion:**

```python
def geometry_calculator(radius: float, length: float, width: float, side: float) -> dict:
    ...
```

---

### ✅ **Bonus Task: One-liner List Comprehension**

👍 **Good:**

* Correct logic to find squares of even numbers

❗ **Improvement:**

* One-liner not implemented — used a loop instead

**Fix:**

```python
squares = [x**2 for x in nums if x % 2 == 0]
```

---

### ❌ **Section 4: File Handling & Text Processing**

---

### ❌ **Task 6: Text File Analyzer**

**Issues:**

* Function `analyze_text_file(filepath)` is incomplete — just reads lines, no logic written.
* `count_words_lines()` is defined separately and not integrated.
* Word frequency and most common word not implemented.
* No dictionary return as specified.

**Expectation:**
Read file, count lines, average words per line, and find most common word.

**Fix:**

```python
from collections import Counter

def analyze_text_file(filepath: str) -> dict:
    with open(filepath, "r") as f:
        lines = f.readlines()

    line_count = len(lines)
    words = [word for line in lines for word in line.strip().split()]
    word_count = len(words)
    avg_words_per_line = word_count / line_count if line_count > 0 else 0
    most_common = Counter(words).most_common(1)[0][0] if words else None

    return {
        "lines": line_count,
        "average_words_per_line": avg_words_per_line,
        "most_common_word": most_common
    }
```

---

## 📌 Summary Table

| Task                       | Result | Key Issue / Fix Needed           |
| -------------------------- | ------ | -------------------------------- |
| List Stats Calculator      | ❌      | Hardcoded input, no parameter    |
| List Filtering             | ❌      | No parameter, didn’t remove None |
| Student Score Updater      | ✅      | Good implementation              |
| Dictionary Filter by Score | ❌      | Returned list, not a dictionary  |
| Geometry Calculator        | ✅      | Correct math + clean code        |
| Bonus List Comprehension   | ❌      | Used loop instead of one-liner   |
| Text File Analyzer         | ❌      | Incomplete — no logic written    |

---

## 🚨 Overall Comments (Strict Feedback)

* Many functions **do not follow the required signatures**, which is critical in assessments.
* **Avoid hardcoding values inside functions** — it kills reusability and violates prompt requirements.
* **Stick to one naming convention** – avoid names like `numb`, `rest`, `revisedclean`, etc.
* The **file task was left incomplete**, which is a major issue.
* Decorate your code with `type hints` and `docstrings` — this is expected even at the beginner level in serious internships.
* One-liners should be one-liners — not loops.



