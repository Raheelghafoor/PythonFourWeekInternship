print("\nLoop Complexity Analyzer")

def count_iterations_simple(n):
    count_q1 = 0
    for i_q1 in range(n):
        count_q1 += 1
    return count_q1

def count_iterations_nested(n):
    count_q1 = 0
    for i_q1 in range(n):
        for j_q1 in range(n):
            count_q1 += 1
    return count_q1

def count_iterations_triangular(n):
    count_q1 = 0
    for i_q1 in range(n):
        for j_q1 in range(i_q1):
            count_q1 += 1
    return count_q1

def analyze_growth(func_q1, label_q1):
    print(f"\nAnalyzing: {label_q1}")
    last_q1 = 1
    for n_q1 in [10, 20, 40, 80]:
        iterations_q1 = func_q1(n_q1)
        growth_q1 = iterations_q1 / last_q1
        print(f"n={n_q1:3}, Iterations={iterations_q1:5}, Growth x{growth_q1:.2f}")
        last_q1 = iterations_q1
    if "simple" in label_q1.lower():
        print("Estimated Complexity: O(n)")
    elif "nested" in label_q1.lower():
        print("Estimated Complexity: O(n²)")
    elif "triangular" in label_q1.lower():
        print("Estimated Complexity: O(n²) but half (triangular pattern)")
analyze_growth(count_iterations_simple, "Simple Loop")
analyze_growth(count_iterations_nested, "Nested Loop")
analyze_growth(count_iterations_triangular, "Triangular Loop")

#QUESTION 2
print("\nLoop Refactoring Tool")    #good bad there to tell which function is effective and which is not
def find_number_bad_q2(lst_q2, target_q2):
    found_q2 = False
    for num_q2 in lst_q2:
        if num_q2 == target_q2:
            found_q2 = True
    return found_q2
def find_number_good_q2(lst_q2, target_q2):
    for num_q2 in lst_q2:
        if num_q2==target_q2:
            return True
    return False
def sum_even_bad_q2(lst_q2):
    total_q2 = 0
    for num_q2 in lst_q2:
        if num_q2 %2 != 0:
            pass
        else:
            total_q2+=num_q2
    return total_q2
def sum_even_good_q2(lst_q2):
    total_q2 = 0
    for num_q2 in lst_q2:
        if num_q2 %2 != 0:
            continue
        else:
            total_q2+=num_q2
    return total_q2

def check_in_list_bad_q2(lst_q2, item_q2):
    for val_q2 in lst_q2:
        if val_q2 == item_q2:
            return True
    return False
def check_in_list_good_q2(lst_q2, item_q2):
    return item_q2 in lst_q2
sample_list_q2 = [1, 3, 5, 7, 9, 11]
print("\nOriginal: find_number_bad_q2 →", find_number_bad_q2(sample_list_q2, 5))
print("Refactored: find_number_good_q2 →", find_number_good_q2(sample_list_q2, 5))
print("\nOriginal: sum_even_bad_q2 →", sum_even_bad_q2(sample_list_q2))
print("Refactored: sum_even_good_q2 →", sum_even_good_q2(sample_list_q2))
print("\nOriginal: check_in_list_bad_q2 →", check_in_list_bad_q2(sample_list_q2, 7))
print("Refactored: check_in_list_good_q2 →", check_in_list_good_q2(sample_list_q2, 7))

#Question 3
import time
print("\nLoop Testing Framework")
def sum_even_test_q3(lst_q3):
    total_q3 = 0
    for num_q3 in lst_q3:
        if num_q3 % 2 == 0:
            total_q3 += num_q3
    return total_q3
def test_loop_function_q3(func_q3, test_name_q3, test_cases_q3):
    print(f"\n🔍 Testing: {test_name_q3}")
    for label_q3, input_q3, expected_q3 in test_cases_q3:
        start_time_q3 = time.time()
        try:
            result_q3 = func_q3(input_q3)
            passed_q3 = result_q3 == expected_q3
        except Exception as e_q3:
            result_q3 = f"Error: {e_q3}"
            passed_q3 = False
        end_time_q3 = time.time()
        duration_q3 = (end_time_q3 - start_time_q3) * 1000 
        if passed_q3:
             status_q3 = "Pass"
        else:
             status_q3 = "Fail"
        print(f"{label_q3}: {status_q3} | Result={result_q3} | Time={duration_q3:.2f}ms")
test_cases_sum_even_q3 = [
    ("Empty List", [], 0),
    ("All Odds", [1, 3, 5], 0),
    ("All Evens", [2, 4, 6], 12),
    ("Mixed Small", [1, 2, 3, 4], 6),
    ("Large List", list(range(100000)), sum(i for i in range(100000) if i % 2 == 0)),
]
test_loop_function_q3(sum_even_test_q3, "Sum of Even Numbers", test_cases_sum_even_q3)

#Question 4
print("\nLoop Documentation Generator")
def loop_doc_q4(code_q4, purpose_q4, complexity_q4):
    print("\n--- Loop Code ---")
    print(code_q4.strip())
    print("\n--- Purpose ---")
    print(purpose_q4)
    print("\n--- Time Complexity ---")
    print(complexity_q4)

code1_q4 = """
for num in lst:
    total += num
"""
purpose1_q4 = "Adds all numbers in the list."
complexity1_q4 = "O(n)"
code2_q4 = """
for i in range(n):
    for j in range(n):
        count += 1
"""
purpose2_q4 = "Nested loop counting all pairs."
complexity2_q4 = "O(n²)" 
code3_q4 = """
for x in items:
    if x == target:
        return True
return False
"""
purpose3_q4 = "Checks if target is in the list."
complexity3_q4 = "O(n) worst case, O(1) best case"
loop_doc_q4(code1_q4, purpose1_q4, complexity1_q4)
loop_doc_q4(code2_q4, purpose2_q4, complexity2_q4)
loop_doc_q4(code3_q4, purpose3_q4, complexity3_q4)

#QUESTION 5
print("\nLoop Best Practices Checker")
def check_loop_best_practices_q5(code_lines_q5):
    for i, line_q5 in enumerate(code_lines_q5):
        line_q5 = line_q5.strip()
        if line_q5.startswith("for ") and "in range" in line_q5 and ":" in line_q5:
            loop_var_q5 = line_q5.split("for")[1].split("in")[0].strip()
            used_q5 = False
            for j in range(1, 4):
                if i + j < len(code_lines_q5):
                    if loop_var_q5 in code_lines_q5[i + j]:
                        used_q5 = True
            if not used_q5:
                print(f" Line {i+1}: Variable '{loop_var_q5}' in loop seems unused.")
            if "range(len(" in line_q5:
                print(f" Line {i+1}: Use 'for item in list' instead of 'range(len(list))'.")
            if "for" in line_q5 and "in []" in line_q5:
                print(f" Line {i+1}: Looping over an empty list is useless.")
sample_code_q5 = [
    "for i in range(5):",
    "    print('hello')",
    "",
    "for j in range(len(mylist)):",
    "    print(mylist[j])",
    "",
    "for x in []:",
    "    print(x)",
    "",
    "for k in range(10):",
    "    total += 1"
]
check_loop_best_practices_q5(sample_code_q5)

#Question 6
print("\nFibonacci Sequence Generator")
def fibonacci_q6(n_q6):
    if n_q6 <= 0:
        return []
    elif n_q6 == 1:
        return [0]
    elif n_q6 == 2:
        return [0, 1]

    fib_q6 = [0, 1]
    for i_q6 in range(2, n_q6):
        next_q6 = fib_q6[-1] + fib_q6[-2]
        fib_q6.append(next_q6)
    return fib_q6
print("First 5 Fibonacci numbers:", fibonacci_q6(5))
print("First 10 Fibonacci numbers:", fibonacci_q6(10))
print("First 0 Fibonacci numbers:", fibonacci_q6(0))
print("First 1 Fibonacci numbers:", fibonacci_q6(1))

#Question 7
print("\nPrime Number Generator")
def is_prime_q7(num_q7):
    if num_q7 < 2:
        return False
    for i_q7 in range(2, num_q7):
        if num_q7 % i_q7 == 0:
            return False
    return True
def generate_primes_q7(limit_q7):
    primes_q7 = []
    for number_q7 in range(2, limit_q7 + 1):
        if is_prime_q7(number_q7):
            primes_q7.append(number_q7)
    return primes_q7
limit_q7 = 30
print(f"Prime numbers up to {limit_q7}:", generate_primes_q7(limit_q7))

# QUESTION 8
print("\nBubble Sort")
def bubble_sort_q8(arr_q8):
    n_q8 = len(arr_q8)
    for i_q8 in range(n_q8):
        for j_q8 in range(0, n_q8 - i_q8 - 1):
            if arr_q8[j_q8] > arr_q8[j_q8 + 1]:
                arr_q8[j_q8], arr_q8[j_q8 + 1] = arr_q8[j_q8 + 1], arr_q8[j_q8]
    return arr_q8

print("\nInsertion Sort")
def insertion_sort_q8(arr_q8):
    for i_q8 in range(1, len(arr_q8)):
        key_q8 = arr_q8[i_q8]
        j_q8 = i_q8 - 1
        while j_q8 >= 0 and arr_q8[j_q8] > key_q8:
            arr_q8[j_q8 + 1] = arr_q8[j_q8]
            j_q8 -= 1
        arr_q8[j_q8 + 1] = key_q8
    return arr_q8

print("\nSelection Sort")
def selection_sort_q8(arr_q8):
    n_q8 = len(arr_q8)
    for i_q8 in range(n_q8):
        min_index_q8 = i_q8
        for j_q8 in range(i_q8 + 1, n_q8):
            if arr_q8[j_q8] < arr_q8[min_index_q8]:
                min_index_q8 = j_q8
        arr_q8[i_q8], arr_q8[min_index_q8] = arr_q8[min_index_q8], arr_q8[i_q8]
    return arr_q8
sample_q8 = [64, 25, 12, 22, 11]
print("\nOriginal List:", sample_q8)
print("Bubble Sort Result:", bubble_sort_q8(sample_q8.copy()))
print("Insertion Sort Result:", insertion_sort_q8(sample_q8.copy()))
print("Selection Sort Result:", selection_sort_q8(sample_q8.copy()))

#Question 9
print("\nSearch Algorithm Suite")
def linear_search_q9(arr_q9, target_q9):
    for i_q9 in range(len(arr_q9)):
        if arr_q9[i_q9] == target_q9:
            return i_q9
    return -1
def binary_search_q9(arr_q9, target_q9):
    left_q9 = 0
    right_q9 = len(arr_q9) - 1
    while left_q9 <= right_q9:
        mid_q9 = (left_q9 + right_q9) // 2
        if arr_q9[mid_q9] == target_q9:
            return mid_q9
        elif arr_q9[mid_q9] < target_q9:
            left_q9 = mid_q9 + 1
        else:
            right_q9 = mid_q9 - 1
    return -1
sample_q9 = [2, 4, 6, 8, 10, 12, 14]
print("\nLinear Search:")
print("Searching 10 → Index:", linear_search_q9(sample_q9, 10))
print("Searching 7  → Index:", linear_search_q9(sample_q9, 7))
print("\nBinary Search:")
print("Searching 10 → Index:", binary_search_q9(sample_q9, 10))
print("Searching 7  → Index:", binary_search_q9(sample_q9, 7))

#Question 10
print("\nMathematical Series Calculators")
def arithmetic_series_q10(start_q10, diff_q10, terms_q10):
    result_q10 = []
    current_q10 = start_q10
    for _ in range(terms_q10):
        result_q10.append(current_q10)
        current_q10 += diff_q10
    return result_q10
def geometric_series_q10(start_q10, ratio_q10, terms_q10):
    result_q10 = []
    current_q10 = start_q10
    for _ in range(terms_q10):
        result_q10.append(current_q10)
        current_q10 *= ratio_q10
    return result_q10
print("\nArithmetic Series (start=2, diff=3, terms=5):")
print(arithmetic_series_q10(2, 3, 5)) 
print("\nGeometric Series (start=2, ratio=3, terms=5):")
print(geometric_series_q10(2, 3, 5))

#Question 11
print("\nPattern Generation Tools")
def left_triangle_q11(rows_q11):
    print("\nLeft-Aligned Triangle:")
    for i_q11 in range(1, rows_q11 + 1):
        print("*" * i_q11)
def right_triangle_q11(rows_q11):
    print("\nRight-Aligned Triangle:")
    for i_q11 in range(1, rows_q11 + 1):
        print(" " * (rows_q11 - i_q11) + "*" * i_q11)
def pyramid_q11(rows_q11):
     print("\nCentered Pyramid:")
     for i_q11 in range(1, rows_q11 + 1):
        spaces_q11 = " " * (rows_q11 - i_q11)
        stars_q11 = "*" * (2 * i_q11 - 1)
        print(spaces_q11 + stars_q11 + spaces_q11)
def number_pyramid_q11(rows_q11):
    print("\nNumber Pyramid:")
    for i_q11 in range(1, rows_q11 + 1):
        for j_q11 in range(1, i_q11 + 1):
            print(j_q11, end=" ")
        print()
def diamond_q11(rows_q11):
    print("\nDiamond Pattern:")
    for i_q11 in range(1, rows_q11 + 1):
        print(" " * (rows_q11 - i_q11) + "*" * (2 * i_q11 - 1))
    for i_q11 in range(rows_q11 - 1, 0, -1):
        print(" " * (rows_q11 - i_q11) + "*" * (2 * i_q11 - 1))
# QUESTION 12
print("\nData Validation Loop")
while True:
    user_input_q12 = input("Enter a positive integer: ")
    if user_input_q12.isdigit():
        number_q12 = int(user_input_q12)
        if number_q12 > 0:
            print(" Valid input received:", number_q12)
            break
        else:
            print(" Please enter a number greater than 0.")
    else:
        print(" That’s not a valid integer. Try again.")

#Question 13
print("\nFile Processing Loop")
input_file_q13 = "input_q13.txt"
output_file_q13 = "output_q13.txt"
with open(input_file_q13, "w") as file_q13:
    file_q13.write("  Hello World!  \n")
    file_q13.write("Python is great.\n")
    file_q13.write("   This line has extra spaces.   \n")
with open(input_file_q13, "r") as infile_q13, open(output_file_q13, "w") as outfile_q13:
    for line_q13 in infile_q13:
        cleaned_q13 = line_q13.strip() 
        outfile_q13.write(cleaned_q13 + "\n")
print("Lines cleaned and written to", output_file_q13)

#Question 14
import random
import time
print("\nNetwork Request Simulation with Retry")
def simulate_api_call_q14(id_q14):
    return random.random() < 0.7
max_retries_q14 = 3
total_calls_q14 = 5
for request_id_q14 in range(1, total_calls_q14 + 1):
    print(f"\n🔄 Sending request #{request_id_q14}...")
    success_q14 = False
    for attempt_q14 in range(1, max_retries_q14 + 1):
        time.sleep(0.5)  
        if simulate_api_call_q14(request_id_q14):
            print(f" Request #{request_id_q14} succeeded on attempt {attempt_q14}")
            success_q14 = True
            break
        else:
            print(f" Request #{request_id_q14} failed on attempt {attempt_q14}")
    if not success_q14:
        print(f" Request #{request_id_q14} failed after {max_retries_q14} attempts.")


#Question 15
print("\nSimple Game Loop: Text Adventure")
player_health_q15 = 100
player_energy_q15 = 50
game_running_q15 = True
print(" Welcome to the Game!")
print("Type: 'move', 'rest', 'status', or 'quit'\n")
while game_running_q15:
    user_action_q15 = input(" What do you want to do? ").lower()
    if user_action_q15 == "move":
        if player_energy_q15 >= 10:
            print("You moved forward.")
            player_energy_q15 -= 10
        else:
            print("You're too tired to move. Try resting.")
    elif user_action_q15 == "rest":
        print(" Resting... You regain 20 energy.")
        player_energy_q15 += 20
        if player_energy_q15 > 100:
            player_energy_q15 = 100
    elif user_action_q15 == "status":
        print(f" Health: {player_health_q15}")
        print(f" Energy: {player_energy_q15}")
    elif user_action_q15 == "quit":
        print(" Thanks for playing!")
        game_running_q15 = False
    else:
        print(" Invalid command. Try again.")
#✅ Advanced Iteration Techniques
#🎯 Focus: Custom iterators, generators, and advanced iteration with itertools 📌 Total Programs: 20
#Question 1
print("\nCustom Iterator Class with Forward and Reverse Support")
class CustomRangeIteratorQ1:
    def __init__(self, start_q1, end_q1):
        self.start_q1 = start_q1
        self.end_q1 = end_q1
        self.current_q1 = start_q1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_q1 >= self.end_q1:
            raise StopIteration
        value_q1 = self.current_q1
        self.current_q1 += 1
        return value_q1
    def __reversed__(self):
        for i_q1 in range(self.end_q1 - 1, self.start_q1 - 1, -1):
            yield i_q1
print("Forward:")
for num_q1 in CustomRangeIteratorQ1(1, 6):
    print(num_q1, end=" ")
print("\nReverse:")
for num_q1 in reversed(CustomRangeIteratorQ1(1, 6)):
    print(num_q1, end=" ")

#Question 2
print("\nGenerator Pipeline System")
def read_data_q2():
    for line_q2 in ["10", "25", "hello", "42", "-5", "99", "end", "0"]:
        yield line_q2
def filter_numbers_q2(source_q2):
    for item_q2 in source_q2:
        if item_q2.lstrip("-").isdigit():
            yield int(item_q2)
def transform_data_q2(source_q2):
    for number_q2 in source_q2:
        yield number_q2 ** 2
def output_data_q2(source_q2):
    for result_q2 in source_q2:
        print(" Processed:", result_q2)
data_q2 = read_data_q2()
filtered_q2 = filter_numbers_q2(data_q2)
transformed_q2 = transform_data_q2(filtered_q2)
output_data_q2(transformed_q2)

#Question 3
print("\nYield-based Coroutine: Running Average Calculator")
def running_average_coroutine_q3():
    total_q3 = 0
    count_q3 = 0
    average_q3 = None
    while True:
        new_value_q3 = yield average_q3
        total_q3 += new_value_q3
        count_q3 += 1
        average_q3 = total_q3 / count_q3
avg_gen_q3 = running_average_coroutine_q3()
next(avg_gen_q3)
print("After 10:", avg_gen_q3.send(10))
print("After 20:", avg_gen_q3.send(20))
print("After 30:", avg_gen_q3.send(30))
print("After 50:", avg_gen_q3.send(50))

#Question 4
print("\nCombinations & Permutations using itertools")
import itertools
items_q4 = ['A', 'B', 'C']
print("\n Combinations of 2:")
for combo_q4 in itertools.combinations(items_q4, 2):
    print(combo_q4)
print("\n Permutations of 2:")
for perm_q4 in itertools.permutations(items_q4, 2):
    print(perm_q4)
print("\n Full Permutations:")
for full_q4 in itertools.permutations(items_q4):
    print(full_q4)

#Question 5
print("\nLazy Evaluation System: Large Dataset Processing")
def generate_large_data_q5(limit_q5):
    for i_q5 in range(limit_q5):
        yield i_q5
def filter_even_q5(source_q5):
    for number_q5 in source_q5:
        if number_q5 % 2 == 0:
            yield number_q5
def transform_square_q5(source_q5):
    for even_q5 in source_q5:
        yield even_q5 ** 2
def process_partial_q5(source_q5, max_items_q5=10):
    for i_q5, value_q5 in enumerate(source_q5):
        print("Processed:", value_q5)
        if i_q5 + 1 == max_items_q5:
            break

#Question 6
print("\nMemory-Efficient File Processor")
def read_file_lazy_q6(filename_q6):
    with open(filename_q6, 'r') as file_q6:
        for line_q6 in file_q6:
            yield line_q6
def filter_lines_q6(lines_q6):
    for line_q6 in lines_q6:
        if line_q6.strip():  
            yield line_q6
def transform_lines_q6(lines_q6):
    for line_q6 in lines_q6:
        yield line_q6.strip().upper()
def write_lines_q6(lines_q6, output_filename_q6):
    with open(output_filename_q6, 'w') as out_file_q6:
        for line_q6 in lines_q6:
            out_file_q6.write(line_q6 + "\n")
input_file_q6 = "input_data_q6.txt"
output_file_q6 = "cleaned_output_q6.txt"
with open(input_file_q6, 'w') as f_q6:
    f_q6.write("Hello\n\nworld\n Python  \n  \nGenerators\n")
raw_lines_q6 = read_file_lazy_q6(input_file_q6)
filtered_q6 = filter_lines_q6(raw_lines_q6)
transformed_q6 = transform_lines_q6(filtered_q6)
write_lines_q6(transformed_q6, output_file_q6)
print(f" Processed file saved as {output_file_q6}")

#Question 7
print("\nStream Processing Pipeline")
import random
import time
def event_stream_q7(limit_q7=10):
    for _ in range(limit_q7):
     event_q7 = {
            "type": random.choice(["click", "scroll", "hover", "error"]),
            "value": random.randint(1, 100)
        }
     yield event_q7
     time.sleep(0.1)
def filter_events_q7(events_q7):
    for event_q7 in events_q7:
        if event_q7["type"] in ["click", "scroll"]:
            yield event_q7
def transform_events_q7(events_q7):
    for event_q7 in events_q7:
        event_q7["value"] *= 10
        yield event_q7
def log_events_q7(events_q7):
    for event_q7 in events_q7:
        print(f"Processed Event → Type: {event_q7['type']}, Value: {event_q7['value']}")
raw_events_q7 = event_stream_q7(15)
filtered_q7 = filter_events_q7(raw_events_q7)
transformed_q7 = transform_events_q7(filtered_q7)
log_events_q7(transformed_q7)

#Question 8
print("\nInfinite Sequence Generators")
def infinite_arithmetic_q8(start_q8=0, step_q8=1, limit_q8=None):
    current_q8 = start_q8
    count_q8 = 0
    while True:
        if limit_q8 is not None and count_q8 >= limit_q8:
            break
        yield current_q8
        current_q8 += step_q8
        count_q8 += 1

def infinite_fibonacci_q8(limit_q8=None):
    a_q8, b_q8 = 0, 1
    count_q8 = 0
    while True:
        if limit_q8 is not None and count_q8 >= limit_q8:
            break
        yield a_q8
        a_q8, b_q8 = b_q8, a_q8 + b_q8
        count_q8 += 1
print("\nArithmetic Sequence (start=2, step=3, limit=10):")
for num_q8 in infinite_arithmetic_q8(2, 3, 10):
    print(num_q8, end=" ")
print("\n\nFibonacci Sequence (limit=10):")
for fib_q8 in infinite_fibonacci_q8(10):
    print(fib_q8, end=" ")

#Question 9
print("\nBuffered Iteration System")
class BufferedIterator_q9:
    def __init__(self, data_q9, buffer_size_q9):
        self.data_q9 = data_q9 
        self.buffer_size_q9 = buffer_size_q9
        self.index_q9 = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index_q9 >= len(self.data_q9):
            raise StopIteration
        start_q9 = self.index_q9
        end_q9 = self.index_q9 + self.buffer_size_q9
        batch_q9 = self.data_q9[start_q9:end_q9]
        self.index_q9 = end_q9
        return batch_q9
sample_data_q9 = [10, 20, 30, 40, 50, 60, 70, 80]
buffered_q9 = BufferedIterator_q9(sample_data_q9, 3)
print("Buffered Batches:")
for batch_q9 in buffered_q9:
    print(batch_q9)

#Question 10
print("\nParallel Iteration Framework")
names_q10 = ["Ali", "Sara", "Zain", "Fatima"]
scores_q10 = [85, 92, 78, 90]
grades_q10 = ["B", "A", "C", "A"]
print("Report Card:")
for index_q10, (name_q10, score_q10, grade_q10) in enumerate(zip(names_q10, scores_q10, grades_q10)):
    print(f"{index_q10 + 1}. {name_q10} → Score: {score_q10}, Grade: {grade_q10}")

#Question 11
print("\nIterator Caching System")
class CachedIterator_q11:
    def __init__(self, source_iter_q11):
        self.source_q11 = iter(source_iter_q11)
        self.cache_q11 = []
        self.index_q11 = 0 
    def __iter__(self):
        self.index_q11 = 0
        return self
    def __next__(self):
        if self.index_q11 < len(self.cache_q11):
            result_q11 = self.cache_q11[self.index_q11]
        else:
            result_q11 = next(self.source_q11)
            self.cache_q11.append(result_q11)
        self.index_q11 += 1
        return result_q11
original_iter_q11 = (x * 2 for x in range(5))
cached_q11 = CachedIterator_q11(original_iter_q11)
print("First loop (fills cache):")
for val_q11 in cached_q11:
    print(val_q11)
print("\nSecond loop (uses cache):")
for val_q11 in cached_q11:
    print(val_q11)

#Question 12
print("\nIterator Serialization")

import pickle

class SerializableIterator_q12:
    def __init__(self, data_q12):
        self.data_q12 = data_q12
        self.index_q12 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_q12 >= len(self.data_q12):
            raise StopIteration
        value_q12 = self.data_q12[self.index_q12]
        self.index_q12 += 1
        return value_q12

    def save_state(self, filename_q12):
        with open(filename_q12, "wb") as f_q12:
            pickle.dump(self, f_q12)

    @staticmethod
    def load_state(filename_q12):
        with open(filename_q12, "rb") as f_q12:
            return pickle.load(f_q12)
data_list_q12 = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
iterator_q12 = SerializableIterator_q12(data_list_q12)
print("First run:")
print(next(iterator_q12))  
print(next(iterator_q12))  
iterator_q12.save_state("iterator_state_q12.pkl")
print("\nResuming from saved state:")
resumed_q12 = SerializableIterator_q12.load_state("iterator_state_q12.pkl")
for item_q12 in resumed_q12:
    print(item_q12)

#Question 13
print("\nIterator Validation System")

import types
from collections.abc import Iterator, Iterable

def validate_object_q13(obj_q13):
    print(f"\nChecking object: {repr(obj_q13)}")

    if isinstance(obj_q13, types.GeneratorType):
        print(" Type: Generator")
    elif isinstance(obj_q13, Iterator):
        print(" Type: Iterator")
    elif isinstance(obj_q13, Iterable):
        print(" Type: Iterable")
    else:
        print(" Not Iterable or Iterator or Generator")
list_obj_q13 = [1, 2, 3]
iter_obj_q13 = iter(list_obj_q13)
gen_obj_q13 = (x for x in range(5))
num_q13 = 42
validate_object_q13(list_obj_q13) 
validate_object_q13(iter_obj_q13)  
validate_object_q13(gen_obj_q13)  
validate_object_q13(num_q13)  

#Question 14
print("\nIterator Transformation")
def transform_iterator_q14(iterable_q14, transform_func_q14):
    for item_q14 in iterable_q14:
        yield transform_func_q14(item_q14)
def square_q14(x_q14):
    return x_q14 * x_q14
def to_upper_q14(text_q14):
    return text_q14.upper()
nums_q14 = [1, 2, 3, 4, 5]
squared_q14 = transform_iterator_q14(nums_q14, square_q14)
print("Squared Numbers:")
for val_q14 in squared_q14:
    print(val_q14)
words_q14 = ["hello", "world", "python"]
uppercased_q14 = transform_iterator_q14(words_q14, to_upper_q14)
print("\nUppercased Words:")
for val_q14 in uppercased_q14:
    print(val_q14)

#Question 15
print("\nIterator Filtering System")
def filter_iterator_q15(iterable_q15, condition_func_q15):
    for item_q15 in iterable_q15:
        if condition_func_q15(item_q15):
            yield item_q15
def is_even_q15(x_q15):
    return x_q15 % 2 == 0
data_q15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_q15 = filter_iterator_q15(data_q15, is_even_q15)
print("Even Numbers:")
for val_q15 in filtered_q15:
    print(val_q15)

#Question 16
print("\nIterator Mapping Functions")
def square_q16(x_q16):
    return x_q16 * x_q16
data_q16 = [1, 2, 3, 4, 5]
mapped_map_q16 = map(square_q16, data_q16)
print("Using map():")
for val_q16 in mapped_map_q16:
    print(val_q16)
def map_generator_q16(iterable_q16, func_q16):
    for item_q16 in iterable_q16:
        yield func_q16(item_q16)
mapped_gen_q16 = map_generator_q16(data_q16, square_q16)
print("\nUsing generator:")
for val_q16 in mapped_gen_q16:
    print(val_q16)

#Question 17
print("\nIterator Reduction Operations")
from functools import reduce
data_q17 = [1, 2, 3, 4, 5]
sum_result_q17 = reduce(lambda x, y: x + y, data_q17)
print("Sum:", sum_result_q17)
product_result_q17 = reduce(lambda x, y: x * y, data_q17)
print("Product:", product_result_q17)
max_result_q17 = reduce(lambda x, y: x if x > y else y, data_q17)
print("Max:", max_result_q17)

#Question 18
print("\nIterator Zip Operations")
names_q18 = ["Ali", "Sara", "Omar", "Zoya"]
scores_q18 = [85, 92, 78, 88]
combined_q18 = zip(names_q18, scores_q18)
print("Name → Score")
for name_q18, score_q18 in combined_q18:
    print(f"{name_q18} → {score_q18}")

#Question 19
print("\nIterator Chain Operations")
import itertools
list1_q19 = [1, 2, 3]
list2_q19 = ['a', 'b', 'c']
list3_q19 = [100, 200]
chained_q19 = itertools.chain(list1_q19, list2_q19, list3_q19)
print("Chained Output:")
for item_q19 in chained_q19:
    print(item_q19)

#Question 20
print("\nIterator Tee Operations")
import itertools
data_q20 = iter([10, 20, 30, 40, 50])
iter1_q20, iter2_q20 = itertools.tee(data_q20)
print("First Iterator:")
for val_q20 in iter1_q20:
    print(" →", val_q20)
print("\nSecond Iterator:")
for val_q20 in iter2_q20:
    print(" →", val_q20)






