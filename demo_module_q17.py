# demo_module_q17.py

def add_q17(a_q17, b_q17):
    """Returns the sum of two numbers."""
    return a_q17 + b_q17

def greet_q17(name_q17):
    """Prints a greeting."""
    print(f"Hello, {name_q17}!")

def factorial_q17(n_q17):
    """Computes n! recursively."""
    if n_q17 <= 1:
        return 1
    return n_q17 * factorial_q17(n_q17 - 1)