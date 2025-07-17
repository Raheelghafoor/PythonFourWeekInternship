# Advanced Debugging Workflow

## 📌 Purpose  
Define a repeatable, end‑to‑end debugging workflow that integrates breakpoints, automated testing, structured logging, profiling, and final verification to ensure production‑ready code quality.

---

## 🗺️ Workflow Overview

1. **Reproduce & Isolate**  
2. **Breakpoint Instrumentation**  
3. **Automated Tests**  
4. **Structured Logging**  
5. **Profiling & Performance Analysis**  
6. **Fix & Iterate**  
7. **Resolution Verification**  
8. **Document & Share**

---

## 1. Reproduce & Isolate  
- **Gather context**: exact steps, data, environment.  
- **Write a minimal reproduction**: isolate the failing code path in a small script or test.  

---

## 2. Breakpoint Instrumentation  
- **CLI debugger**: insert `import pdb; pdb.set_trace()` or use `breakpoint()` in Python 3.7+.  
- **IDE breakpoints**: set conditional or unconditional breakpoints in VS Code/PyCharm.  
- **Conditional logic**: only pause when variable meets failure criteria.  

```python
# example_module.py
def compute(x):
    if x < 0:
        import pdb; pdb.set_trace()      # pause when negative input
    return x * 2
    