# Debugging Best Practices

## 📌 Purpose
Provide a solid reference for effective debugging steps, tools, and what to avoid when diagnosing bugs in Python projects.

---

## ✅ Core Principles

- **Understand the Bug**: Read the error message, logs, and symptoms carefully.
- **Reproduce Consistently**: Ensure the bug can be triggered repeatedly.
- **Isolate the Problem**: Reduce code to the minimal failing snippet.
- **Be Systematic**: Change one thing at a time and observe the effect.
- **Use the Right Tools**: Use debuggers, loggers, and profilers effectively.
- **Think Logically**: Don’t guess—verify your assumptions.
- **Fix the Root Cause**: Not just the symptom, fix the actual issue.

---

## 🧭 Recommended Debugging Steps

1. **Read Stack Trace**  
   Understand where and why the error occurred.

2. **Add Print/Logging Statements**  
   Print variable values to track logic and state. Replace with logging for long-term use.

3. **Use Python Debuggers**  
   Tools:  
   - `pdb` – built-in CLI debugger  
   - `breakpoint()` – simple entry point  
   - IDE debuggers (e.g., PyCharm, VSCode)

4. **Write Unit Tests**  
   Create small tests to verify behavior as you debug.

5. **Check Recent Code Changes**  
   Look at diffs or commits that may have introduced the bug.

6. **Validate Assumptions**  
   Add assertions and sanity checks to confirm expected behavior.

7. **Use Version Control**  
   Use `git bisect` to find which commit introduced the bug.

8. **Consult Documentation**  
   Check official docs or community forums for known issues.

---

## 🧨 Debugging Anti-Patterns (What NOT to Do)

| ❌ Anti-Pattern                 | ✅ Better Approach                              |
|-------------------------------|--------------------------------------------------|
| Random changes to code        | Make one change at a time, test, and observe     |
| Ignoring logs or stack traces | Read errors carefully—they usually explain a lot |
| Adding `try/except` blindly   | Catch specific exceptions and understand why     |
| Deleting failing code blocks  | Isolate and fix the issue, not hide it           |
| Overusing `print()` everywhere| Use structured logging for real applications     |
| Blaming environment/machine   | First verify if it happens elsewhere             |

---

## 🛠 Useful Debugging Tools

| Tool        | Use Case                       |
|-------------|--------------------------------|
| `pdb`       | Interactive command-line debug |
| `logging`   | Track behavior via logs        |
| `traceback` | Format error reports           |
| `pytest`    | Automated test discovery       |
| `coverage`  | Find untested code             |
| IDE Debugger| Breakpoints, step-in/out       |

---

## 💡 Pro Tips

- Use `assert` statements to catch logic errors early.
- Keep your functions small and pure—easier to debug.
- Prefer exceptions over silent failures.
- Reboot the environment to rule out config bugs.

---

## 📚 References

- [Python pdb Docs](https://docs.python.org/3/library/pdb.html)
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Effective Debugging – Book Summary](https://effectivedebugging.com/)

---

*Document by: Ahmed Aziz*  
*Created: 2025-07-17*