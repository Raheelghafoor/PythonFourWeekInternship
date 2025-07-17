# app_q19.py

from math_utils_q19 import factorial_q19, is_prime_q19
from string_utils_q19 import reverse_string_q19, is_palindrome_q19
from data_loader_q19 import load_config_q19

def main_q19():
    cfg = load_config_q19("config.json")      # BUG 1: missing file‑not‑found handling
    print("Config:", cfg)

    print("5! =", factorial_q19(5))           # BUG 2: factorial off‑by‑one
    print("Is 17 prime?", is_prime_q19(17))   # BUG 3: incorrectly reports some primes

    s = "RaceCar"
    print("Reversed:", reverse_string_q19(s)) # BUG 4: doesn’t preserve case
    print("Is palindrome?", is_palindrome_q19(s))

if __name__ == "__main__":
    main_q19()