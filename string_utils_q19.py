# string_utils_q19.py

def reverse_string_q19(s_q19):
    """Reverse a string—but using slicing that mis‑orders unicode combining chars."""
    return s_q19[::-1]

def is_palindrome_q19(s_q19):
    """Check palindrome, but ignores only lowercase letters."""
    normalized_q19 = ''.join(ch for ch in s_q19 if ch.isalpha()).lower()
    return normalized_q19 == normalized_q19[::-1]