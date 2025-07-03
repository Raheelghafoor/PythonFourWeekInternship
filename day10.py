#✅ Tuple Operations & Immutability Day 10 Part 1 🎯 Focus: Master tuple operations, immutability, and practical use cases in Python programming.
#Question 1
tup1=(1,2,3,4,5)
print("Indexing: ",tup1[2])
print("Slicing: ",tup1[1:4])
print("Concatenation: ",tup1 + (6,7))
print("Repetition: ",tup1 * 2)
print("Is 3 in tup1? ",3 in tup1)

#QUESTION 2
from collections import namedtuple
Student = namedtuple( "Student",["name", "age", "grade"])
s1 = Student("Ali", 18, "A")
print("Student Name:", s1.name)
print("Student Age:", s1.age)
print("Student Grade:", s1.grade)

#QUESTION 3
a,b,c=(10,20,30)
print("Simple Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)

x, (y, z) = (1, (2, 3))
print("\nNested Unpacking:")
print("x =", x)
print("y =", y)
print("z =", z)

p,*q,r=(5,6,7,8,9)
print("\nAsterisk (*) Unpacking:")
print("p =", p)
print("q =", q)
print("r =", r)

#QUESTION 4
locations={
    (0,0): "Home",
    (1,2): "Park",
    (2,3): "Library",
    (4,1): "School",
}
print("Location at (0, 0):",locations[(0,0)])
print("Location at (1, 2):",locations[(1,2)])
print("Location at (4, 1):",locations[(4,1)])

#QUESTION 5
import timeit
tuple_creation_time = timeit.timeit("(1, 2, 3, 4, 5)", number=100000)
list_creation_time = timeit.timeit("[1, 2, 3, 4, 5]", number=100000)
tuple_loop_time = timeit.timeit("for i in (1, 2, 3, 4, 5): pass", number=100000)
list_loop_time = timeit.timeit("for i in [1, 2, 3, 4, 5]: pass", number=100000)

#QUESTION 6
import math
def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
def calculate_midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
point1=(2,3)
point2=(6,7)
distance = calculate_distance(point1, point2)
midpoint = calculate_midpoint(point1, point2)
print("Point 1:", point1)
print("Point 2:", point2)
print("Distance between points:", distance)
print("Midpoint:", midpoint)

#QUESTION 7
records = [
    (1, "Ali", 20),
    (2, "Sara", 22),
    (3, "Ahmed", 19),
    (4, "Zara", 21)
]
def search_record(record_list, id_to_find):
     for rec in record_list:
         if rec[0] == id_to_find:
             return rec
     return None

def update_age(record_list, id_to_update, new_age):
    updated = []
    for rec in record_list:
        if rec[0] == id_to_update:
            updated.append((rec[0], rec[1], new_age))
        else:
            updated.append(rec)
    return updated
result = search_record(records, 2)
print("Search Result:", result)
records = update_age(records, 3, 25)
print("\nUpdated Records:")
for r in records:
    print(r)

#QUESTION 8
config = ("localhost", 5432, "admin", "readonly")
print("Host:", config[0])
print("Port:", config[1])
print("User:", config[2])
print("Mode:", config[3])
try:
    config[1] = 3306
except TypeError as e:
    print("\nError: Tuples are immutable! Cannot modify configuration.")
    print("Python says:", e)

#QUESTION 9
tup1 = (1, 2, 3)
tup2 = (1, 2, 3)      
tup3 = (3, 2, 1)
tup4 = ("Ali", 25, "A")  
tup5 = (1, (2, 3))
print("Hash of tup1:", hash(tup1))
print("Hash of tup2 (same as tup1):", hash(tup2))
print("Hash of tup3 (different order):", hash(tup3))
print("Hash of tup4 (mixed types):", hash(tup4))
print("Hash of tup5 (nested tuple):", hash(tup5))

#QUESTION 10
def compare_tuples(t1, t2):
    differences = []
    min_len = min(len(t1), len(t2))
    for i in range(min_len):
        if t1[i] != t2[i]:
            differences.append((i, t1[i], t2[i]))
    if len(t1) > len(t2):
        for i in range(min_len, len(t1)):
            differences.append((i, t1[i], None))
    elif len(t2) > len(t1):
        for i in range(min_len, len(t2)):
            differences.append((i, None, t2[i]))
    
    return differences

tuple1 = (1, 2, 3, 4)
tuple2 = (1, 5, 3, 8, 9)

diffs = compare_tuples(tuple1, tuple2)

print("Differences:")
for index, val1, val2 in diffs:
    print(f"Index {index}: {val1} ≠ {val2}")

#QUESTION 11
import json
import pickle
data_tuple = ("Ali", 25, "A+")
json_data = json.dumps(data_tuple)
print("JSON Serialized:", json_data)
tuple_from_json = tuple(json.loads(json_data))
print("JSON Deserialized:", tuple_from_json)
pickle_data = pickle.dumps(data_tuple)
print("Pickle Serialized (binary):", pickle_data)
tuple_from_pickle = pickle.loads(pickle_data)
print("Pickle Deserialized:", tuple_from_pickle)

#QUESTION 12
def validate_tuple(t):
    if not isinstance(t, tuple):
        return "Not a tuple"
    if len(t) != 3:
        return "Tuple must have exactly 3 elements"
    for i, value in enumerate(t):
        if not isinstance(value, int):
            return f"Element at index {i} is not an integer"
    return "Tuple is valid"
print(validate_tuple((1, 2, 3)))
print(validate_tuple([1, 2, 3]))
print(validate_tuple((1, "a", 3)))
print(validate_tuple((1, 2)))
print(validate_tuple((1, 2, 3, 4)))

#QUESTION 13
def to_list(t):
    return list(t)

def to_set(t):
    return set(t)

def to_string(t):
    return str(t)

def to_dict(t):
    return dict(t)
tup1 = (1, 2, 3)
print("List:", to_list(tup1))
print("Set:", to_set(tup1))
print("String:", to_string(tup1))

tup2 = (("a", 1), ("b", 2))
print("Dictionary:", to_dict(tup2))

#QUESTION 14
import sys
tuple_data = (1, 2, 3, 4, 5)
list_data = [1, 2, 3, 4, 5]
set_data = {1, 2, 3, 4, 5}
dict_data = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print("Tuple size:", sys.getsizeof(tuple_data), "bytes")
print("List size:", sys.getsizeof(list_data), "bytes")
print("Set size:", sys.getsizeof(set_data), "bytes")
print("Dict size:", sys.getsizeof(dict_data), "bytes")


#QUESTION 15
def push(stack, item):
    return stack + (item,)

def pop(stack):
    if not stack:
        return stack, None
    return stack[:-1], stack[-1]

my_stack = ()
my_stack = push(my_stack, 1)
my_stack = push(my_stack, 2)
my_stack = push(my_stack, 3)
print("Stack:", my_stack)
my_stack, removed = pop(my_stack)
print("Popped item:", removed)
print("Stack after pop:", my_stack)

#✅ Title: Advanced Sequence Operations Day 10 part 2
#QUESTION 1
def advanced_slice(lst):
    return lst[-2:0:-3]

data = [10, 20, 30, 40, 50, 60, 70, 80]
result = advanced_slice(data)
print("Result:", result)

#QUESTION 2

class CustomList:
    def __init__(self, elements_q2):
        self.data_q2 = elements_q2

    def __getitem__(self, index_q2):
        return self.data_q2[index_q2]

    def __len__(self):
        return len(self.data_q2)

    def __iter__(self):
        for item_q2 in self.data_q2:
            yield item_q2

my_list_q2 = CustomList([10, 20, 30, 40])

print("Item at index 2:", my_list_q2[2])
print("Length:", len(my_list_q2))

print("Items:")
for val_q2 in my_list_q2:
    print(val_q2)

#QUESTION 3
class SmartIndexerQ3:
    def __init__(self, items_q3):
        self.data_q3 = items_q3

    def get_q3(self, key_q3):
        if key_q3 == "first":
            return self.data_q3[0]
        elif key_q3 == "last":
            return self.data_q3[-1]
        elif key_q3 == "random":
            import random
            return random.choice(self.data_q3)
        else:
            return "Invalid key"
values_q3 = [10, 20, 30, 40, 50]
indexer_q3 = SmartIndexerQ3(values_q3)

print("First:", indexer_q3.get_q3("first"))
print("Last:", indexer_q3.get_q3("last"))
print("Random:", indexer_q3.get_q3("random"))
print("Invalid:", indexer_q3.get_q3("middle"))

#QUESTION 4
def fancy_iterator_q4(data_q4):
    left_q4 = 0
    right_q4 = len(data_q4) - 1
    while left_q4 <= right_q4:
        if left_q4 == right_q4:
            yield data_q4[left_q4]
        else:
            yield data_q4[left_q4]
            yield data_q4[right_q4]
        left_q4 += 1
        right_q4 -= 1

values_q4 = [10, 20, 30, 40, 50, 60]
for item_q4 in fancy_iterator_q4(values_q4):
    print(item_q4)

#QUESTION 5
import sys
import array
import numpy as np

large_list_q5 = [float(i) for i in range(10000)]

array_q5 = array.array('f', large_list_q5)
numpy_array_q5 = np.array(large_list_q5, dtype='float32')

print("List size:", sys.getsizeof(large_list_q5), "bytes")
print("Array size:", sys.getsizeof(array_q5), "bytes")
print("NumPy size:", numpy_array_q5.nbytes, "bytes")

#QUESTION 6
def fibonacci_generator_q6(n_q6):
    a_q6, b_q6 = 0, 1
    count_q6 = 0
    while count_q6 < n_q6:
        yield a_q6
        a_q6, b_q6 = b_q6, a_q6 + b_q6
        count_q6 += 1

for num_q6 in fibonacci_generator_q6(10):
    print(num_q6)

#QUESTION 7
sequence_cache_q7 = {}

def cache_decorator_q7(func_q7):
    def wrapper_q7(seq_q7):
        key_q7 = hash(tuple(seq_q7))
        if key_q7 in sequence_cache_q7:
            return sequence_cache_q7[key_q7]
        result_q7 = func_q7(seq_q7)
        sequence_cache_q7[key_q7] = result_q7
        return result_q7
    return wrapper_q7

@cache_decorator_q7
def process_sequence_q7(seq_q7):
    return sum(x**2 for x in seq_q7)

input_seq_q7 = [1, 2, 3]
print("First call:", process_sequence_q7(input_seq_q7))
print("Second call (cached):", process_sequence_q7(input_seq_q7))

#QUESTION 8

def validate_sequence_q8(data_q8, min_val_q8, max_val_q8):
    if not isinstance(data_q8, list):
        return "Error: Not a list"

    if any(x_q8 is None for x_q8 in data_q8):
        return "Error: Contains None values"

    if not all(isinstance(x_q8, int) for x_q8 in data_q8):
        return "Error: Contains non-integer values"

    if len(data_q8) != len(set(data_q8)):
        return "Error: Contains duplicate values"

    if not all(min_val_q8 <= x_q8 <= max_val_q8 for x_q8 in data_q8):
        return f"Error: Values must be between {min_val_q8} and {max_val_q8}"

    return "Sequence is valid"

#QUESTION 9

from functools import reduce

data_q9 = [1, 2, 3, 4, 5, 6]

squared_q9 = map(lambda x_q9: x_q9 ** 2, data_q9)
evens_q9 = filter(lambda x_q9: x_q9 % 2 == 0, squared_q9)
sum_q9 = reduce(lambda acc_q9, x_q9: acc_q9 + x_q9, evens_q9, 0)

print("Sum of squares of evens:", sum_q9)

#QUESTION 10
def run_length_encode_q10(seq_q10):
    encoded_q10 = []
    if not seq_q10:
        return encoded_q10
    prev_q10 = seq_q10[0]
    count_q10 = 1
    for item_q10 in seq_q10[1:]:
        if item_q10 == prev_q10:
            count_q10 += 1
        else:
            encoded_q10.append((prev_q10, count_q10))
            prev_q10 = item_q10
            count_q10 = 1
    encoded_q10.append((prev_q10, count_q10))
    return encoded_q10

data_q10 = [1, 1, 2, 2, 2, 3]
print("Original:", data_q10)
print("Encoded:", run_length_encode_q10(data_q10))

#QUESTION 11
def is_subsequence_q11(seq_q11, pattern_q11):
    n_q11 = len(seq_q11)
    m_q11 = len(pattern_q11)
    if m_q11 == 0:
        return True
    for i_q11 in range(n_q11 - m_q11 + 1):
        if seq_q11[i_q11:i_q11+m_q11] == pattern_q11:
            return True
    return False

data_q11 = [1, 2, 3, 4, 5]
pattern_q11 = [3, 4]
print(is_subsequence_q11(data_q11, pattern_q11))   
print(is_subsequence_q11(data_q11, [2, 5])) 

#Question 12
def sequence_difference_q12(a_q12, b_q12):
    b_set_q12 = set(b_q12)
    return [x for x in a_q12 if x not in b_set_q12]
A_q12 = [1, 2, 3, 4, 5, 2]
B_q12 = [2, 5]
print(sequence_difference_q12(A_q12, B_q12))   

A2_q12 = ["a", "b", "c", "a"]
B2_q12 = ["a", "c"]
print(sequence_difference_q12(A2_q12, B2_q12))

#Question 13
def merge_sorted_q13(a_q13, b_q13):
    i_q13, j_q13 = 0, 0
    merged_q13 = []
    while i_q13 < len(a_q13) and j_q13 < len(b_q13):
        if a_q13[i_q13] <= b_q13[j_q13]:
            merged_q13.append(a_q13[i_q13])
            i_q13 += 1
        else:
            merged_q13.append(b_q13[j_q13])
            j_q13 += 1
    while i_q13 < len(a_q13):
        merged_q13.append(a_q13[i_q13])
        i_q13 += 1
    while j_q13 < len(b_q13):
        merged_q13.append(b_q13[j_q13])
        j_q13 += 1
    return merged_q13

#QUESTION 14
def chunk_list_q14(data_q14, n_q14):
    chunks_q14 = []
    for i_q14 in range(0, len(data_q14), n_q14):
        chunks_q14.append(data_q14[i_q14:i_q14 + n_q14])
    return chunks_q14
my_list_q14 = [1, 2, 3, 4, 5, 6, 7]
print(chunk_list_q14(my_list_q14, 3))

#QUESTION 15
def reverse_slice_q15(data_q15):
    return data_q15[::-1]
def reverse_loop_q15(data_q15):
    result_q15 = []
    for item_q15 in data_q15:
        result_q15.insert(0, item_q15)
    return result_q15
def reverse_recursive_q15(data_q15):
    if not data_q15:
        return []
    return [data_q15[-1]] + reverse_recursive_q15(data_q15[:-1])
orig_q15 = [1, 2, 3, 4, 5]
print("Original:", orig_q15)
print("Reversed (slice):", reverse_slice_q15(orig_q15))
print("Reversed (loop):", reverse_loop_q15(orig_q15))
print("Reversed (recursion):", reverse_recursive_q15(orig_q15))
    







