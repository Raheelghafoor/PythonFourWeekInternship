# math_utils_q19.py

def factorial_q19(n_q19):
    """Compute n! but has an off‑by‑one bug."""
    result_q19 = 1
    for i_q19 in range(1, n_q19):  # should be range(1, n_q19+1)
        result_q19 *= i_q19
    return result_q19

def is_prime_q19(n_q19):
    """Return True if n is prime, but forgets to handle n=2 correctly."""
    if n_q19 < 2:
        return False
    for i_q19 in range(2, int(n_q19 ** 0.5)):  # should be +1
        if n_q19 % i_q19 == 0:
            return False
    return True