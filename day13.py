#Question 1
boxes_q1=[None]*10
def put_q1(key_q1, value_q1):
    key_length_q1 = len(key_q1) % 10 
    box_number=key_length_q1%10
    boxes_q1[box_number] = value_q1
def get_q1(key_q1):
    key_length_q1 = len(key_q1)
    box_number=key_length_q1%10
    return boxes_q1[box_number]
put_q1("name", "Ahmed")     
put_q1("age", 21)           
put_q1("city", "Lahore")
print("Name hai:", get_q1("name"))   
print("Age hai:", get_q1("age"))     
print("City hai:", get_q1("city")) 
print("\n--- Boxes ki Halat ---")
for i in range(10):
    print(f"Box {i}: {boxes_q1[i]}")

#Question 2
import time
import random
import string
print("\n--- Hash Function Analyzer ---")
def generate_keys_q2(total_q2):
    keys_q2 = []
    for i in range(total_q2):
         length_q2 = random.randint(3, 10)
         random_letters_q2 = random.choices(string.ascii_lowercase, k=length_q2)
         key_q2 = ''.join(random_letters_q2)
         keys_q2.append(key_q2)
    return keys_q2
def hash_fn1_q2(key_q2):
    return len(key_q2) % 10
def hash_fn2_q2(key_q2):
    total_q2 = 0
    for i in range(len(key_q2)):
        total_q2 += ord(key_q2[i])
    return total_q2 % 10
def hash_fn3_q2(key_q2):
    return hash(key_q2) % 10
def analyze_hash_q2(func_q2, keys_q2, title_q2):
    print(f"\nTesting: {title_q2}")
    start_q2 = time.time()
    buckets_q2 = [0] * 10
    for i in range(len(keys_q2)):
        key_q2 = keys_q2[i]
        bucket_index_q2 = func_q2(key_q2)
        buckets_q2[bucket_index_q2] += 1
    end_q2 = time.time()
    print("Bucket Distribution:")
    for i in range(10):
        print(f"Bucket {i}: {buckets_q2[i]} keys")
    print("Time Taken:", round((end_q2 - start_q2) * 1000, 3), "ms")
key_list_q2 = generate_keys_q2(1000)
analyze_hash_q2(hash_fn1_q2, key_list_q2, "Hash Function 1: Length of Key")
analyze_hash_q2(hash_fn2_q2, key_list_q2, "Hash Function 2: ASCII Sum")
analyze_hash_q2(hash_fn3_q2, key_list_q2, "Hash Function 3: Python Built-in Hash")
    
#Question 3
print("\n--- Question 3: Collision Resolution ---")
print("\n🔗 Chaining Method")
chaining_q3 = [[] for i in range(10)]
def put_chain_q3(key, value):
    box = len(key) % 10
    chaining_q3[box].append((key, value))
def get_chain_q3(key):
    box = len(key) % 10
    for k, v in chaining_q3[box]:
        if k == key:
            return v
    return None
put_chain_q3("name", "Ahmed")
put_chain_q3("city", "Lahore")
put_chain_q3("game", "Cricket")
print("Name:", get_chain_q3("name"))
print("City:", get_chain_q3("city"))
print("Game:", get_chain_q3("game"))
print("Boxes:", chaining_q3)
print("\n➕ Linear Probing Method")
linear_q3 = [None] * 10
def put_linear_q3(key, value):
    box = len(key) % 10
    while linear_q3[box] is not None:
        box = (box + 1) % 10
    linear_q3[box] = (key, value)
def get_linear_q3(key):
    box = len(key) % 10
    start = box
    while linear_q3[box] is not None:
        if linear_q3[box][0] == key:
            return linear_q3[box][1]
        box = (box + 1) % 10
        if box == start:
            break
    return None
put_linear_q3("name", "Ahmed")
put_linear_q3("city", "Lahore")
put_linear_q3("game", "Cricket")
print("Name:", get_linear_q3("name"))
print("City:", get_linear_q3("city"))
print("Game:", get_linear_q3("game"))
print("Boxes:", linear_q3)
print("\n⬛ Quadratic Probing Method")
quadratic_q3 = [None] * 10
def put_quad_q3(key, value):
    base = len(key) % 10
    for i in range(10):
        box = (base + i*i) % 10
        if quadratic_q3[box] is None:
            quadratic_q3[box] = (key, value)
            return
def get_quad_q3(key):
    base = len(key) % 10
    for i in range(10):
        box = (base + i*i) % 10
        if quadratic_q3[box] is None:
            return None
        if quadratic_q3[box][0] == key:
            return quadratic_q3[box][1]
    return None
put_quad_q3("name", "Ahmed")
put_quad_q3("city", "Lahore")
put_quad_q3("game", "Cricket")
print("Name:", get_quad_q3("name"))
print("City:", get_quad_q3("city"))
print("Game:", get_quad_q3("game"))
print("Boxes:", quadratic_q3)

#Question 4
import time
import random
import string
print("\n--- Question 4: Performance Tester ---")
def generate_keys_q4(n):
    keys_q4 = []
    for _ in range(n):
        length_q4 = random.randint(5, 10)
        key_q4 = ''.join(random.choices(string.ascii_lowercase, k=length_q4))
        keys_q4.append(key_q4)
    return keys_q4
custom_q4 = [None] * 100
def put_custom_q4(key, value):
    index = len(key) % 100
    while custom_q4[index] is not None and custom_q4[index][0] != key:
        index = (index + 1) % 100
    custom_q4[index] = (key, value)
def get_custom_q4(key):
    index = len(key) % 100
    start = index
    while custom_q4[index] is not None:
        if custom_q4[index][0] == key:
            return custom_q4[index][1]
        index = (index + 1) % 100
        if index == start:
            break
    return None
keys_q4 = generate_keys_q4(1000)
start_custom = time.time()
for i in range(1000):
    put_custom_q4(keys_q4[i], i)
for i in range(1000):
    get_custom_q4(keys_q4[i])
end_custom = time.time()
dict_q4 = {}
start_dict = time.time()
for i in range(1000):
    dict_q4[keys_q4[i]] = i
for i in range(1000):
    temp = dict_q4[keys_q4[i]]
end_dict = time.time()
print("Custom Table Time:", round((end_custom - start_custom) * 1000, 2), "ms")
print("Python dict Time:", round((end_dict - start_dict) * 1000, 2), "ms")

#Question 5
print("\n--- Question 5: HashSet ---")
set_q5 = [None] * 50
def add_q5(item):
    index = len(item) % 50
    while set_q5[index] is not None and set_q5[index] != item:
        index = (index + 1) % 50
    set_q5[index] = item
def contains_q5(item):
    index = len(item) % 50
    start = index
    while set_q5[index] is not None:
        if set_q5[index] == item:
            return True
        index = (index + 1) % 50
        if index == start:
            break
    return False
add_q5("apple")
add_q5("banana")
add_q5("cherry")
print("banana in set?", contains_q5("banana"))
print("grape in set?", contains_q5("grape"))
print("Set:", set_q5)

#Question 6
print("\n--- Question 6: Hash Table with Resizing ---")
table_q6 = [None] * 4
size_q6 = 0
def resize_q6():
    global table_q6
    old_q6 = table_q6
    table_q6 = [None] * (2 * len(old_q6))
    for item_q6 in old_q6:
        if item_q6 is not None:
            put_q6(item_q6[0], item_q6[1])
def put_q6(key_q6, value_q6):
    global size_q6
    if size_q6 >= len(table_q6) // 2:
        resize_q6()
    index_q6 = len(key_q6) % len(table_q6)
    while table_q6[index_q6] is not None and table_q6[index_q6][0] != key_q6:
        index_q6 = (index_q6 + 1) % len(table_q6)
    table_q6[index_q6] = (key_q6, value_q6)
    size_q6 += 1
put_q6("a", 1)
put_q6("b", 2)
put_q6("c", 3)
put_q6("d", 4)
put_q6("e", 5)

print("Table Size:", len(table_q6))
print("Contents:", table_q6)

#Question 7
import json

print("\n--- Question 7: Save/Load Hash Table ---")

hash_table_q7 = [("name", "Ahmed"), ("city", "Lahore")]

with open("hash_table_q7.json", "w") as file_q7:
    json.dump(hash_table_q7, file_q7)

with open("hash_table_q7.json", "r") as file_q7:
    loaded_q7 = json.load(file_q7)

print("Loaded Table:", loaded_q7)

#Question 8
import json, time, threading

hash_table_q8 = {}

def put_q8(key, value):
    hash_table_q8[key] = value

def backup_q8():
    with open("backup_q8.json", "w") as file:
        json.dump(hash_table_q8, file)

def restore_q8():
    global hash_table_q8
    with open("backup_q8.json", "r") as file:
        hash_table_q8 = json.load(file)

def auto_backup_q8():
    backup_q8()
    threading.Timer(10, auto_backup_q8).start()

put_q8("name", "Ahmed")
put_q8("city", "Lahore")
auto_backup_q8()
time.sleep(12)
restore_q8()
print("Restored:", hash_table_q8)

#Question 9
import sys
stats_table_q9 = [None] * 10
collision_count_q9 = 0
size_q9 = 0
def put_q9(key, value):
    global collision_count_q9, size_q9
    index = len(key) % 10
    while stats_table_q9[index] is not None and stats_table_q9[index][0] != key:
        index = (index + 1) % 10
        collision_count_q9 += 1
    if stats_table_q9[index] is None:
        size_q9 += 1
    stats_table_q9[index] = (key, value)
def load_factor_q9():
    return size_q9 / len(stats_table_q9)
def memory_usage_q9():
    return sys.getsizeof(stats_table_q9)
put_q9("a", 1)
put_q9("b", 2)
put_q9("c", 3)
put_q9("d", 4)
put_q9("e", 5)
print("Load Factor:", load_factor_q9())
print("Collisions:", collision_count_q9)
print("Memory Used:", memory_usage_q9(), "bytes")

#QUESTION 10
viz_table_q10 = [None] * 10

def put_q10(key, value):
    index = len(key) % 10
    while viz_table_q10[index] is not None and viz_table_q10[index][0] != key:
        index = (index + 1) % 10
    viz_table_q10[index] = (key, value)

def show_viz_q10():
    for i in range(10):
        print(f"Box {i}:", viz_table_q10[i])

put_q10("name", "Ahmed")
put_q10("city", "Lahore")
put_q10("game", "Cricket")
show_viz_q10()

#Question 11
cache_q11 = {}
table_q11 = {}
def put_q11(key, value):
    table_q11[key] = value
    if key in cache_q11:
        del cache_q11[key]
def get_q11(key):
    if key in cache_q11:
        return cache_q11[key]
    value = table_q11.get(key)
    if value is not None:
        cache_q11[key] = value
    return value
put_q11("x", 100)
put_q11("y", 200)
print(get_q11("x"))
print(get_q11("x"))
print("Cache:", cache_q11)


#Question 12
index_table_q12 = {}

def put_q12(key, value):
    index_table_q12[key] = value

def range_query_q12(start_key, end_key):
    result = {}
    for key in sorted(index_table_q12.keys()):
        if start_key <= key <= end_key:
            result[key] = index_table_q12[key]
    return result

put_q12("apple", 10)
put_q12("banana", 20)
put_q12("cherry", 30)
put_q12("date", 40)
put_q12("fig", 50)
print("Range apple to date:", range_query_q12("apple", "date"))

#Question 13
import json
import os

cache_q13 = {}
file_path_q13 = "data_q13.json"
def put_q13(key, value):
    cache_q13[key] = value
    if os.path.exists(file_path_q13):
        with open(file_path_q13, "r") as f:
            data_q13 = json.load(f)
    else:
        data_q13 = {}
    data_q13[key] = value
    with open(file_path_q13, "w") as f:
        json.dump(data_q13, f)
def get_q13(key):
    if key in cache_q13:
        return cache_q13[key]
    if os.path.exists(file_path_q13):
        with open(file_path_q13, "r") as f:
            data_q13 = json.load(f)
            if key in data_q13:
                cache_q13[key] = data_q13[key]
                return data_q13[key]
    return None
put_q13("username", "ahmedaziz")
put_q13("email", "ahmed@example.com")
print(get_q13("username"))
print(get_q13("email"))
print("Cache Layer:", cache_q13)

#Question 14
shards_q14 = {
    "A-F": {},
    "G-L": {},
    "M-R": {},
    "S-Z": {}
}

def put_q14(key, value):
    first_char = key[0].upper()
    if "A" <= first_char <= "F":
        shards_q14["A-F"][key] = value
    elif "G" <= first_char <= "L":
        shards_q14["G-L"][key] = value
    elif "M" <= first_char <= "R":
        shards_q14["M-R"][key] = value
    elif "S" <= first_char <= "Z":
        shards_q14["S-Z"][key] = value

def get_q14(key):
    first_char = key[0].upper()
    if "A" <= first_char <= "F":
        return shards_q14["A-F"].get(key)
    elif "G" <= first_char <= "L":
        return shards_q14["G-L"].get(key)
    elif "M" <= first_char <= "R":
        return shards_q14["M-R"].get(key)
    elif "S" <= first_char <= "Z":
        return shards_q14["S-Z"].get(key)
    return None

put_q14("apple", 10)
put_q14("grape", 20)
put_q14("mango", 30)
put_q14("zebra", 40)

print("Get apple:", get_q14("apple"))
print("Get grape:", get_q14("grape"))
print("Get mango:", get_q14("mango"))
print("Get zebra:", get_q14("zebra"))
print("Shards:", shards_q14)

#Question 15
data_q15 = [
    ("name", "Ahmed"),
    ("age", "21"),
    ("city", "Lahore"),
    ("name", "Ahmed"),          
    ("email", None),             
    ("phone", "12345"),
    ("address", "Lahore"),
    ("", "missing_key"),         
    ("gender", "")               
]
def check_consistency_q15(data):
    seen_keys = set()
    duplicates = []
    missing_keys = []
    corrupted = []
    for key, value in data:
        if not key:
            missing_keys.append((key, value))
        elif key in seen_keys:
            duplicates.append((key, value))
        else:
            seen_keys.add(key)
        if value is None or value == "":
            corrupted.append((key, value))
    return duplicates, missing_keys, corrupted
d_q15, m_q15, c_q15 = check_consistency_q15(data_q15)
print("Duplicates:", d_q15)
print("Missing Keys:", m_q15)
print("Corrupted Entries:", c_q15)

#✅ Loop Patterns & Optimization
#🎯 Focus: Loop structures, custom iteration, and performance enhancements

#Question 1
import time
large_list_q1 = list(range(1000000))
start_for_q1 = time.time()
total_for_q1 = 0
for i in large_list_q1:
    total_for_q1 += i
end_for_q1 = time.time()
start_while_q1 = time.time()
total_while_q1 = 0
i_q1 = 0
while i_q1 < len(large_list_q1):
    total_while_q1 += large_list_q1[i_q1]
    i_q1 += 1
end_while_q1 = time.time()
start_comp_q1 = time.time()
total_comp_q1 = sum([i for i in large_list_q1])
end_comp_q1 = time.time()
print("For-loop time:", round((end_for_q1 - start_for_q1) * 1000, 2), "ms")
print("While-loop time:", round((end_while_q1 - start_while_q1) * 1000, 2), "ms")
print("List comprehension time:", round((end_comp_q1 - start_comp_q1) * 1000, 2), "ms")

#Question 2
import time
start_naive_q2 = time.time()
equal_pairs_naive_q2 = []
for i in range(1000):
    for j in range(1000):
        if i == j:
            equal_pairs_naive_q2.append((i, j))
end_naive_q2 = time.time()
start_opt_q2 = time.time()
equal_pairs_opt_q2 = [(i, i) for i in range(1000)]
end_opt_q2 = time.time()
print("Naive Loop Pairs:", len(equal_pairs_naive_q2))
print("Naive Time:", round((end_naive_q2 - start_naive_q2) * 1000, 2), "ms")
print("Optimized Loop Pairs:", len(equal_pairs_opt_q2))
print("Optimized Time:", round((end_opt_q2 - start_opt_q2) * 1000, 2), "ms")

#Question 3
import time
start_normal_q3 = time.time()
total_normal_q3 = 0
for i in range(0, 1000000):
    total_normal_q3 += i
end_normal_q3 = time.time()
start_unroll_q3 = time.time()
total_unroll_q3 = 0
i_q3 = 0
while i_q3 < 1000000:
    total_unroll_q3 += i_q3
    total_unroll_q3 += i_q3 + 1
    total_unroll_q3 += i_q3 + 2
    total_unroll_q3 += i_q3 + 3
    i_q3 += 4
end_unroll_q3 = time.time()
print("Normal loop sum:", total_normal_q3)
print("Normal time:", round((end_normal_q3 - start_normal_q3) * 1000, 2), "ms")
print("Unrolled loop sum:", total_unroll_q3)
print("Unrolled time:", round((end_unroll_q3 - start_unroll_q3) * 1000, 2), "ms")

#Question 4
class CustomRangeQ4:
    def __init__(self, start_q4, end_q4):
        self.current_q4 = start_q4
        self.end_q4 = end_q4

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_q4 >= self.end_q4:
            raise StopIteration
        value_q4 = self.current_q4
        self.current_q4 += 1
        return value_q4

print("Custom Iterator Output:")
for number_q4 in CustomRangeQ4(5, 10):
    print(number_q4)

#Question 5
def even_numbers_q5(limit_q5):
    for i in range(0, limit_q5 + 1, 2):
        yield i
def square_numbers_q5(limit_q5):
    for i in range(limit_q5 + 1):
        yield i * i
def fibonacci_q5(count_q5):
    a_q5, b_q5 = 0, 1
    for _ in range(count_q5):
        yield a_q5
        a_q5, b_q5 = b_q5, a_q5 + b_q5
print("Even Numbers:")
for num_q5 in even_numbers_q5(10):
    print(num_q5)

print("\nSquare Numbers:")
for num_q5 in square_numbers_q5(5):
    print(num_q5)

print("\nFibonacci Numbers:")
for num_q5 in fibonacci_q5(7):
    print(num_q5)

#Question 6
matrix_q6 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11,12],
    [13,14,15,16]
]
print("Spiral Order:")
def spiral_q6(matrix):
    top_q6 = 0
    bottom_q6 = len(matrix) - 1
    left_q6 = 0
    right_q6 = len(matrix[0]) - 1
    while top_q6 <= bottom_q6 and left_q6 <= right_q6:
        for i in range(left_q6, right_q6 + 1):
            print(matrix[top_q6][i], end=' ')
        top_q6 += 1
        for i in range(top_q6, bottom_q6 + 1):
            print(matrix[i][right_q6], end=' ')
        right_q6 -= 1
        if top_q6 <= bottom_q6:
            for i in range(right_q6, left_q6 - 1, -1):
                print(matrix[bottom_q6][i], end=' ')
            bottom_q6 -= 1
        if left_q6 <= right_q6:
            for i in range(bottom_q6, top_q6 - 1, -1):
                print(matrix[i][left_q6], end=' ')
            left_q6 += 1
spiral_q6(matrix_q6)
print("\n\nReverse Diagonal Order:")
n_q6 = len(matrix_q6)
for d in range(2 * n_q6 - 1):
    for i in range(n_q6):
        j = d - i
        if 0 <= j < n_q6:
            print(matrix_q6[i][j], end=' ')

#Question 7
print("Break example: ")
numbers_q7 = [5, 8, 13, 22, 35, 42]
target_q7 = 22
for num_q7 in numbers_q7:
    if num_q7==target_q7:
        print("Found:", num_q7)
        break
    else:
        print("Target not found")
print("\nContinue Example (Skip even numbers):")
for i_q7 in range(1, 11):
    if i_q7 % 2 == 0:
        continue
    print(i_q7)
print("\nElse Example (Search for name):")
names_q7 = ["Ali", "Zara", "Ahmed", "Nida"]
search_q7 = "Tariq"
for name_q7 in names_q7:
    if name_q7 == search_q7:
        print("Name found:", name_q7)
        break
else:
    print("Name not found in list")

#Question 8
import time
print(" Counter-Based Infinite Loop Handler:")
counter_q8 = 0
limit_q8 = 10
while True:
    print("Loop running... count =", counter_q8)
    counter_q8 += 1

    if counter_q8 >= limit_q8:
        print(" Limit reached, stopping loop!")
        break
print("\n⏱ Time-Based Infinite Loop Handler:")
start_time_q8 = time.time()
time_limit_q8 = 3 
iteration_q8 = 0
while True:
    current_time_q8 = time.time()
    if current_time_q8 - start_time_q8 > time_limit_q8:
        print("⏰ Time limit reached, stopping loop!")
        break
    print("Loop running... iteration =", iteration_q8)
    iteration_q8 += 1

#Question 9
def process_chunk_q9(chunk_q9):
    print("This chunk has", len(chunk_q9), "items.")
    for item_q9 in chunk_q9:
        print("Item:", item_q9)
    print("Done with this chunk.\n")
def chunked_loop_q9(large_list_q9, size_q9):
    total_q9 = len(large_list_q9)
    start_q9 = 0

    while start_q9 < total_q9:
        end_q9 = start_q9 + size_q9
        chunk_q9 = large_list_q9[start_q9:end_q9]
        process_chunk_q9(chunk_q9)
        start_q9 += size_q9
big_list_q9 = []
for i_q9 in range(1, 31):
    big_list_q9.append(i_q9)
chunk_size_q9 = 10
chunked_loop_q9(big_list_q9, chunk_size_q9)

#Question 11
import numpy as np
import time
data_list_q11 = list(range(1, 1000001))
data_np_q11 = np.arange(1, 1000001)
start_loop_q11 = time.time()
result_loop_q11 = []
for value_q11 in data_list_q11:
    result_loop_q11.append(value_q11 * 2)
end_loop_q11 = time.time()
start_vector_q11 = time.time()
result_vector_q11 = data_np_q11 * 2
end_vector_q11 = time.time()
print("Using Loop Time:", round((end_loop_q11 - start_loop_q11) * 1000, 2), "ms")
print("Using NumPy Vectorization Time:", round((end_vector_q11 - start_vector_q11) * 1000, 2), "ms")
print("\nLoop Output First 5:", result_loop_q11[:5])
print("Vectorized Output First 5:", result_vector_q11[:5])

#Question 12
cache_q12 = {}
def slow_multiply_q12(n_q12):
    if n_q12 in cache_q12:
        return cache_q12[n_q12]
    print("Calculating for", n_q12)
    result_q12 = n_q12 * 5
    cache_q12[n_q12] = result_q12
    return result_q12
for i_q12 in [2, 4, 2, 4, 6]:
    answer_q12 = slow_multiply_q12(i_q12)
    print(f"{i_q12} * 5 = {answer_q12}")

#Question 13
import json
import os

cache_q13 = {}
file_path_q13 = "data_q13.json"

def put_q13(key, value):
    cache_q13[key] = value
    if os.path.exists(file_path_q13):
        with open(file_path_q13, "r") as f:
            data_q13 = json.load(f)
    else:
        data_q13 = {}
    data_q13[key] = value
    with open(file_path_q13, "w") as f:
        json.dump(data_q13, f)

def get_q13(key):
    if key in cache_q13:
        return cache_q13[key]
    if os.path.exists(file_path_q13):
        with open(file_path_q13, "r") as f:
            data_q13 = json.load(f)
            if key in data_q13:
                cache_q13[key] = data_q13[key]
                return data_q13[key]
    return None

put_q13("username", "ahmedaziz")
put_q13("email", "ahmed@example.com")
print(get_q13("username"))
print(get_q13("email"))
print("Cache Layer:", cache_q13)

#Question 14
def log_loop_q14(func_q14):
    def wrapper_q14(*args, **kwargs):
        print(f"Running: {func_q14.__name__}")
        result_q14 = func_q14(*args, **kwargs)
        print(f"Finished: {func_q14.__name__}")
        return result_q14
    return wrapper_q14
def count_down_q14(n_q14):
    for i_q14 in range(n_q14, 0, -1):
        print(f"i = {i_q14}")
count_down_q14(5)

#Question15
def is_fibonacci_q15(seq_q15):
    if len(seq_q15) < 3:
        return False
    for i_q15 in range(2, len(seq_q15)):
        if seq_q15[i_q15] != seq_q15[i_q15 - 1] + seq_q15[i_q15 - 2]:
            return False
    return True
def is_palindrome_q15(seq_q15):
    return seq_q15 == seq_q15[::-1]
fib_list_q15 = [0, 1, 1, 2, 3, 5, 8]
pal_list_q15 = [1, 2, 3, 2, 1]
rand_list_q15 = [2, 4, 6, 8]
print("Is Fibonacci:", is_fibonacci_q15(fib_list_q15))    
print("Is Palindrome:", is_palindrome_q15(pal_list_q15))   
print("Random List is Fibonacci:", is_fibonacci_q15(rand_list_q15))  
print("Random List is Palindrome:", is_palindrome_q15(rand_list_q15))
    
