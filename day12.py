#Question 1
print("\nDictionary Encryption System")

original_dict_q1 = {
    "username": "ahmedaziz",
    "password": "secret123",
    "email": "user@example.com"
}

def caesar_encrypt_q1(text_q1, shift_q1):
    result_q1 = ""
    for char_q1 in text_q1:
        if char_q1.isalpha():
            base_q1 = ord('A') if char_q1.isupper() else ord('a')
            result_q1 += chr((ord(char_q1) - base_q1 + shift_q1) % 26 + base_q1)
        elif char_q1.isdigit():
            result_q1 += chr((ord(char_q1) - ord('0') + shift_q1) % 10 + ord('0'))
        else:
            result_q1 += char_q1
    return result_q1

def xor_encrypt_q1(text_q1, key_q1):
    return ''.join(chr(ord(char_q1) ^ key_q1) for char_q1 in text_q1)

method_q1 = input("Choose encryption method (caesar/xor): ").strip().lower()

encrypted_dict_q1 = {}

if method_q1 == "caesar":
    while True:
        shift_input_q1 = input("Enter Caesar shift value (integer): ")
        if shift_input_q1.isdigit() or (shift_input_q1.startswith('-') and shift_input_q1[1:].isdigit()):
            shift_q1 = int(shift_input_q1)
            break
        else:
            print("Invalid shift. Please enter a valid integer.")
    for k_q1, v_q1 in original_dict_q1.items():
        encrypted_dict_q1[k_q1] = caesar_encrypt_q1(v_q1, shift_q1)

elif method_q1 == "xor":
    while True:
        key_input_q1 = input("Enter XOR key (0–255): ")
        if key_input_q1.isdigit():
            key_q1 = int(key_input_q1)
            if 0 <= key_q1 <= 255:
                break
        print("Invalid XOR key. Must be an integer between 0 and 255.")
    for k_q1, v_q1 in original_dict_q1.items():
        encrypted_dict_q1[k_q1] = xor_encrypt_q1(v_q1, key_q1)

else:
    print("Invalid method selected!")
    exit()

print("\nEncrypted Dictionary:")
for key_q1, val_q1 in encrypted_dict_q1.items():
    print(f"{key_q1}: {repr(val_q1)}")

#QUESTION 2
print("\n Dictionary Compression using Run-Length Encoding")
original_dict_q2 = {
    "alpha": "aaabbcdddd",
    "beta": [1, 1, 2, 2, 2, 3],
    "gamma": "xyz",
    "delta": [9, 9, 9, 9]
}
def run_length_encode_q2(data_q2):
    if not data_q2:
        return []

    result_q2 = []
    count_q2 = 1

    for i_q2 in range(1, len(data_q2)):
        if data_q2[i_q2] == data_q2[i_q2 - 1]:
            count_q2 += 1
        else:
            result_q2.append((data_q2[i_q2 - 1], count_q2))
            count_q2 = 1
    result_q2.append((data_q2[-1], count_q2))

    return result_q2
compressed_dict_q2 = {}
for key_q2, val_q2 in original_dict_q2.items():
    compressed_dict_q2[key_q2] = run_length_encode_q2(val_q2)
print("\n Compressed Dictionary:")
for key_q2, val_q2 in compressed_dict_q2.items():
    print(f"{key_q2}: {val_q2}")

#QUESTION 3
import sys
print("\nDictionary Memory Analyzer")
dict_str_q3 = {"a": "apple", "b": "banana", "c": "cherry"}
dict_int_q3 = {"x": 100, "y": 200, "z": 300}
dict_list_q3 = {"p": [1, 2], "q": [3, 4], "r": [5, 6]}
dict_tuple_q3 = {"m": (7, 8), "n": (9, 10), "o": (11, 12)}
dict_set_q3 = {"s": {1, 2}, "t": {3, 4}, "u": {5, 6}}
def get_total_size_q3(obj_q3):
    size_q3 = sys.getsizeof(obj_q3)
    if isinstance(obj_q3, dict):
        for key_q3, val_q3 in obj_q3.items():
            size_q3 += sys.getsizeof(key_q3)
            size_q3 += sys.getsizeof(val_q3)
    return size_q3
report_q3 = {
    "String Dict": get_total_size_q3(dict_str_q3),
    "Integer Dict": get_total_size_q3(dict_int_q3),
    "List Dict": get_total_size_q3(dict_list_q3),
    "Tuple Dict": get_total_size_q3(dict_tuple_q3),
    "Set Dict": get_total_size_q3(dict_set_q3)
}
print("\n Memory Usage Report (in bytes):")
for structure_q3, size_q3 in report_q3.items():
    print(f"{structure_q3}: {size_q3} bytes")

#Question 4
import timeit
print("\n Dictionary Performance Benchmarker")
sizes_q4 = [10, 100, 1000, 10000, 100000]
for size_q4 in sizes_q4:
    print(f"\n--- Testing Dictionary of Size {size_q4} ---")
    setup_q4 = f"""
test_dict_q4 = {{i: i for i in range({size_q4})}}
"""
    access_time_q4 = timeit.timeit("value = test_dict_q4[0]", setup=setup_q4, number=1000)
    insert_time_q4 = timeit.timeit("test_dict_q4[-1] = 999", setup=setup_q4, number=1000)
    delete_time_q4 = timeit.timeit("del test_dict_q4[0]", setup=setup_q4, number=1000)
    print(f"Access Time : {access_time_q4:.6f} seconds")
    print(f"Insert Time : {insert_time_q4:.6f} seconds")
    print(f"Delete Time : {delete_time_q4:.6f} seconds")

#QUESTION 5
import json
import os
from datetime import datetime
print("\n Dictionary Backup System")
my_dict_q5 = {
    "name": "Ahmed",
    "age": 22,
    "email": "ahmed@example.com"
}
filename_q5 = "backup_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
with open(filename_q5, "w") as file_q5:
    json.dump(my_dict_q5, file_q5)
print(" Dictionary saved to:", filename_q5)
with open(filename_q5, "r") as file_q5:
    loaded_dict_q5 = json.load(file_q5)
print(" Dictionary restored:", loaded_dict_q5)
with open(filename_q5, "r") as file_q5:
    loaded_dict_q5 = json.load(file_q5)
print(" Dictionary restored:", loaded_dict_q5)

#Question 6
print("\n Dictionary Migration Tool")
old_user_q6 = {
    "user_name": "ahmedaziz",
    "user_age": 22,
    "user_email": "ahmed@example.com"
}
new_user_q6 = {
    "name": old_user_q6["user_name"],
    "age": old_user_q6["user_age"],
    "contact": {
        "email": old_user_q6["user_email"]
    }
}
print("\n🔁 Migrated Dictionary (New Schema):")
print(new_user_q6)

#Question 7
print("\n Dictionary Template Engine")
template_q7 = "Hello, {name}! Your email is {email}. You are {age} years old."
data_q7 = {
    "name": "Ahmed",
    "email": "ahmed@example.com",
    "age": 22
}
result_q7 = template_q7.format(**data_q7)
print("\n📝 Final Message:")
print(result_q7)

#Question 8
import json
print("\n Dictionary Configuration Manager")
class ConfigurationManager_q8:
    def __init__(self, config_dict_q8=None):
        self.config_q8 = config_dict_q8 or {}
    def load_from_file(self, filename_q8):
        with open(filename_q8, 'r') as f_q8:
            self.config_q8 = json.load(f_q8)
    def save_to_file(self, filename_q8):
        with open(filename_q8, 'w') as f_q8:
            json.dump(self.config_q8, f_q8, indent=4)
    def validate(self, required_keys_q8):
        missing_q8 = [key_q8 for key_q8 in required_keys_q8 if key_q8 not in self.config_q8]
        if missing_q8:
            print(" Missing keys:", missing_q8)
        else:
            print(" All required keys are present.")
    def update(self, key_q8, value_q8):
        self.config_q8[key_q8] = value_q8
        print(f" Updated '{key_q8}' to '{value_q8}'")
    def show_config(self):
        print(" Current Configuration:")
        print(json.dumps(self.config_q8, indent=4))

initial_config_q8 = {
    "app_name": "MyApp",
    "version": "1.0",
    "debug": True
}
manager_q8 = ConfigurationManager_q8(initial_config_q8)
manager_q8.show_config()
manager_q8.validate(["app_name", "version", "debug", "database"])
manager_q8.update("debug", False)
manager_q8.update("database", "localhost")
manager_q8.show_config()
manager_q8.save_to_file("config_q8.json")

#Question 9
print("\n Dictionary Query Language")
data_q9 = {
    "user": {
        "profile": {
            "name": "Ahmed",
            "age": 22
        },
        "email": "ahmed@example.com"
    }
}
def query_dict_q9(d_q9, query_q9):
    keys_q9 = query_q9.split(".")
    current_q9 = d_q9
    for key_q9 in keys_q9:
        if isinstance(current_q9, dict) and key_q9 in current_q9:
            current_q9 = current_q9[key_q9]
        else:
            return " Key path not found!"
    return current_q9
query_input_q9 = input("Enter key path (e.g., user.profile.name): ").strip()
result_q9 = query_dict_q9(data_q9, query_input_q9)
print(" Result:", result_q9)

#Question 10
import matplotlib.pyplot as plt
print("\n Dictionary Visualization Tool - Bar Chart")
data_q10 = {
    "Math": 85,
    "English": 78,
    "Science": 92,
    "History": 74
}
subjects_q10 = list(data_q10.keys())
marks_q10 = list(data_q10.values())
plt.figure(figsize=(8, 4))
plt.bar(subjects_q10, marks_q10, color='skyblue')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.tight_layout()
plt.show()

#✅ Set Operations & Mathematics
#🎯 Focus: Learn and apply core set theory, operations, and performance principles through code.
#Question 1
print("\nSet Operations Calculator ")
set1_q1 = set(input("Enter elements of Set 1 (comma separated): ").split(","))
set2_q1 = set(input("Enter elements of Set 2 (comma separated): ").split(","))
print("\n Results:")
print("Union:", set1_q1 | set2_q1)
print("Intersection:", set1_q1 & set2_q1)
print("Difference (Set1 - Set2):", set1_q1 - set2_q1)
print("Difference (Set2 - Set1):", set2_q1 - set1_q1)
print("Symmetric Difference:", set1_q1 ^ set2_q1)

#Question 2
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
print("\n✅ Set Theory Visualizer 🧠 (2-Set Venn Diagram)")
set1_q2 = set(input("Enter elements of Set 1 (comma separated): ").split(","))
set2_q2 = set(input("Enter elements of Set 2 (comma separated): ").split(","))
venn2([set1_q2, set2_q2], set_labels=("Set 1", "Set 2"))
plt.title("Venn Diagram of Two Sets")
plt.show()

#Question 3
print("\n Set-Based Algorithms ")
print("\nA. Remove Duplicates")
list_q3a = input("Enter items with duplicates (comma separated): ").split(",")
unique_q3a = list(set(list_q3a))
print("Unique items:", unique_q3a)
print("\nB. Common Items Between Two Lists")
list1_q3b = input("Enter List 1 (comma separated): ").split(",")
list2_q3b = input("Enter List 2 (comma separated): ").split(",")
common_q3b = set(list1_q3b) & set(list2_q3b)
print("Common items:", list(common_q3b))
print("\nC. Items That Occur More Than Once")
list_q3c = input("Enter a list with possible repeats (comma separated): ").split(",")
seen_q3c = set()
repeats_q3c = set()
for item_q3c in list_q3c:
    if item_q3c in seen_q3c:
        repeats_q3c.add(item_q3c)
    else:
        seen_q3c.add(item_q3c)

print("Repeated items:", list(repeats_q3c))

#Question 4
import timeit
import random
print("\n Set Performance Analyzer ")
size_q4 = 1000000
target_q4 = size_q4 - 1
list_q4 = list(range(size_q4))
set_q4 = set(list_q4)
list_time_q4 = timeit.timeit(stmt=f"{target_q4} in list_q4", globals=globals(), number=100)
set_time_q4 = timeit.timeit(stmt=f"{target_q4} in set_q4", globals=globals(), number=100)
print(f"\nList membership test time: {list_time_q4:.6f} seconds")
print(f"Set membership test time : {set_time_q4:.6f} seconds")

#Question 5
print("\nSet Validation System")
allowed_types_q5 = (int, str, float)
def validate_set_q5(input_data_q5):
    if not isinstance(input_data_q5, set):
        print("Input is not a set.")
        return False
    for item_q5 in input_data_q5:
        if not isinstance(item_q5, allowed_types_q5):
            print(f"Invalid item type: {item_q5} ({type(item_q5).__name__})")
            return False
    print("Valid set with allowed data types.")
    return True
test_data_1_q5 = {1, 2, 3}
test_data_2_q5 = {"a", "b", "c"}
test_data_3_q5 = {1, "hello", 3.5}
test_data_4_q5 = [1, 2, 3]
test_data_5_q5 = {1, 2, (1, 2)}
validate_set_q5(test_data_1_q5)
validate_set_q5(test_data_2_q5)
validate_set_q5(test_data_3_q5)
validate_set_q5(test_data_4_q5)
validate_set_q5(test_data_5_q5)

#Question 6
import json
import csv
import pickle
print("\nSet Serialization Tool")
original_set_q6 = {"apple", "banana", "cherry"}
with open("set_q6.json", "w") as f_json_q6:
    json.dump(list(original_set_q6), f_json_q6)
with open("set_q6.json", "r") as f_json_q6:
    loaded_json_set_q6 = set(json.load(f_json_q6))
print("JSON Loaded Set:", loaded_json_set_q6)
with open("set_q6.csv", "w", newline="") as f_csv_q6:
    writer_q6 = csv.writer(f_csv_q6)
    for item_q6 in original_set_q6:
        writer_q6.writerow([item_q6])
loaded_csv_set_q6 = set()
with open("set_q6.csv", "r") as f_csv_q6:
    reader_q6 = csv.reader(f_csv_q6)
    for row_q6 in reader_q6:
        loaded_csv_set_q6.add(row_q6[0])
print("CSV Loaded Set:", loaded_csv_set_q6)
with open("set_q6.pkl", "wb") as f_bin_q6:
    pickle.dump(original_set_q6, f_bin_q6)

with open("set_q6.pkl", "rb") as f_bin_q6:
    loaded_bin_set_q6 = pickle.load(f_bin_q6)
print("Binary Loaded Set:", loaded_bin_set_q6)

#Question 7
print("\nSet Comparison Utility")
set_old_q7 = set(input("Enter old set (comma separated): ").split(","))
set_new_q7 = set(input("Enter new set (comma separated): ").split(","))
added_q7 = set_new_q7 - set_old_q7
removed_q7 = set_old_q7 - set_new_q7
unchanged_q7 = set_old_q7 & set_new_q7
print("Added items:", added_q7)
print("Removed items:", removed_q7)
print("Unchanged items:", unchanged_q7)

#Question 8
print("\nSet Transformation Pipeline")
input_set_q8 = set(map(int, input("Enter numbers (comma separated): ").split(",")))
squared_q8 = set(x * x for x in input_set_q8)
even_squares_q8 = set(x for x in squared_q8 if x % 2 == 0)
sum_result_q8 = sum(even_squares_q8)
print("Original Set:", input_set_q8)
print("Squared Set:", squared_q8)
print("Even Squares:", even_squares_q8)
print("Sum of Even Squares:", sum_result_q8)

#Question 9
print("\nSet-Based Data Structures")

class TagPermissionManager_q9:
    def __init__(self):
        self.tags_q9 = set()
        self.permissions_q9 = set()

    def add_tag(self, tag_q9):
        self.tags_q9.add(tag_q9)

    def remove_tag(self, tag_q9):
        self.tags_q9.discard(tag_q9)

    def add_permission(self, perm_q9):
        self.permissions_q9.add(perm_q9)

    def remove_permission(self, perm_q9):
        self.permissions_q9.discard(perm_q9)

    def has_tag(self, tag_q9):
        return tag_q9 in self.tags_q9

    def has_permission(self, perm_q9):
        return perm_q9 in self.permissions_q9

    def show_all(self):
        print("Tags:", self.tags_q9)
        print("Permissions:", self.permissions_q9)

manager_q9 = TagPermissionManager_q9()
manager_q9.add_tag("admin")
manager_q9.add_tag("editor")
manager_q9.add_permission("read")
manager_q9.add_permission("write")
manager_q9.remove_tag("editor")
manager_q9.remove_permission("delete")
print("Has tag 'admin':", manager_q9.has_tag("admin"))
print("Has permission 'write':", manager_q9.has_permission("write"))
manager_q9.show_all()

#Question 10
print("\nSet Mathematical Operations")
set1_q10 = set(map(int, input("Enter numbers for Set 1 (comma separated): ").split(",")))
set2_q10 = set(map(int, input("Enter numbers for Set 2 (comma separated): ").split(",")))
union_q10 = set1_q10 | set2_q10
intersection_q10 = set1_q10 & set2_q10
modulo_filtered_q10 = {x for x in union_q10 if x % 3 == 0}
squares_q10 = {x * x for x in union_q10}
print("Union:", union_q10)
print("Intersection:", intersection_q10)
print("Divisible by 3:", modulo_filtered_q10)
print("Squares of elements:", squares_q10)

#QUESTION 11
print("\nSet Intersection Algorithms")
set1_q11 = set(input("Enter elements of Set 1 (comma separated): ").split(","))
set2_q11 = set(input("Enter elements of Set 2 (comma separated): ").split(","))
set3_q11 = set(input("Enter elements of Set 3 (comma separated): ").split(","))
intersection_result_q11 = set1_q11 & set2_q11
intersection_result_q11 = intersection_result_q11 & set3_q11
print("Common elements in all sets:", intersection_result_q11)

#Question 12
print("\nSet Union Strategies")

set1_q12 = set(input("Enter elements of Set 1 (comma separated): ").split(","))
set2_q12 = set(input("Enter elements of Set 2 (comma separated): ").split(","))
set3_q12 = set(input("Enter elements of Set 3 (comma separated): ").split(","))
union_result_q12 = set1_q12 | set2_q12 | set3_q12
print("Merged union set (no duplicates):", union_result_q12)

#Question 13
print("\nSet Difference Calculator")
set_a_q13 = set(input("Enter elements of Set A (comma separated): ").split(","))
set_b_q13 = set(input("Enter elements of Set B (comma separated): ").split(","))
difference_q13 = set_a_q13 - set_b_q13
print("Elements in Set A but not in Set B:", difference_q13)

#Question 14
print("\nSet Symmetric Difference Utility")
set_a_q14 = set(input("Enter elements of Set A (comma separated): ").split(","))
set_b_q14 = set(input("Enter elements of Set B (comma separated): ").split(","))
symmetric_diff_q14 = set_a_q14 ^ set_b_q14
print("Elements in either Set A or B, but not both:", symmetric_diff_q14)

#Question 15
print("\nSet Subset Validator")
set_a_q15 = set(input("Enter elements of Set A (comma separated): ").split(","))
set_b_q15 = set(input("Enter elements of Set B (comma separated): ").split(","))
if set_a_q15.issubset(set_b_q15):
    print("Set A is a subset of Set B")
else:
    print("Set A is NOT a subset of Set B")

#Question 16
print("\nSet Superset Checker")
set_a_q16 = set(input("Enter elements of Set A (comma separated): ").split(","))
set_b_q16 = set(input("Enter elements of Set B (comma separated): ").split(","))
if set_a_q16.issuperset(set_b_q16):
    print("Set A is a superset of Set B")
else:
    print("Set A is NOT a superset of Set B")

#Question 17
print("\nSet Disjoint Tester")
set_a_q17 = set(input("Enter elements of Set A (comma separated): ").split(","))
set_b_q17 = set(input("Enter elements of Set B (comma separated): ").split(","))
if set_a_q17.isdisjoint(set_b_q17):
    print("Sets are disjoint (no common elements)")
else:
    print("Sets are NOT disjoint (they share some elements)")

#Question 18
print("\nSet Cardinality Calculator")
data_q18 = input("Enter items (comma separated): ").split(",")
unique_items_q18 = set(data_q18)
print("Number of unique items:", len(unique_items_q18))
print("Unique items:", unique_items_q18)

#Question 19
from itertools import combinations
print("\nSet Power Set Generator (Easy Version using itertools)")
input_items_q19 = input("Enter items (comma separated): ").split(",")
original_list_q19 = list(set(input_items_q19))
power_set_q19 = []
for r_q19 in range(len(original_list_q19) + 1):
    subsets_q19 = combinations(original_list_q19, r_q19)
    for subset_q19 in subsets_q19:
        power_set_q19.append(set(subset_q19))
print("\nPower Set (all subsets):")
for subset_q19 in power_set_q19:
    print(subset_q19)

#Question 20
print("\nSet Partition - Odd vs Even Numbers")
input_data_q20 = input("Enter numbers (comma separated): ").split(",")
num_set_q20 = set(map(int, input_data_q20))
odd_set_q20 = set()
even_set_q20 = set()
for num_q20 in num_set_q20:
    if num_q20 % 2 == 0:
        even_set_q20.add(num_q20)
    else:
        odd_set_q20.add(num_q20)
print("Odd numbers:", odd_set_q20)
print("Even numbers:", even_set_q20)










   


