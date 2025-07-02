#QUESTION 1
print("\n=== Dynamic List Manager ===")
list_items_q1 = []
def display_menu_q1():
    print("\nChoose an option:")
    print("1. Add item")
    print("2. View list")
    print("3. Update item")
    print("4. Delete item")
    print("5. Exit")
while True:
    display_menu_q1()
    choice_q1 = input("Enter your choice (1-5): ")
    if choice_q1 == "1":
        item_q1 = input("Enter item to add: ")
        list_items_q1.append(item_q1)
        print("'" + item_q1 + "' added.")
    elif choice_q1 == "2":
        if len(list_items_q1) == 0:
            print("List is empty.")
        else:
             print("\nCurrent List:")
             i_q1 = 0
             i=1
             while i_q1<len(list_items_q1):
                 print(str(i)+". "+ list_items_q1[i_q1])
                 i_q1 += 1
                 i+=1
    elif choice_q1 == "3" :
        if len(list_items_q1) == 0:
            print("List is empty.")
        else:
            index_input_q1 = input("Enter index to update: ")
            if index_input_q1.isdigit():
                index_q1 = int(index_input_q1)
                if index_q1 >= 0 and index_q1 < len(list_items_q1):
                    new_value_q1 = input("Enter new value: ")
                    list_items_q1[index_q1] = new_value_q1
                    print("Item updated.")
                else:
                    print("Invalid index.")
    elif choice_q1 =="4":
        if len(list_items_q1) == 0:
            print("List is empty.")
        else:
            index_input_q1 = input("Enter index to delete: ")
            if index_input_q1.isdigit():
                index_q1 = int(index_input_q1)
                if index_q1 >= 0 and index_q1 < len(list_items_q1):
                    removed_q1 = list_items_q1.pop(index_q1)
                    print("'" + removed_q1 + "' deleted.")
                else:
                    print("Invalid index.")
            else:
                print("Please enter a number.")
    elif choice_q1 =="5":
        print("Exiting Dynamic List Manager.")
        break
    else:
        print("Invalid choice. Try again.")

#QUESTION 2
print("\n=== List Comprehension Showcase ===")
squares_q2 = []
for x in range(1,11):
    squares_q2.append(x*x)
print("1. Squares:", squares_q2)

evens_q2 = []
for x in range(21):
    if x%2==0:
        evens_q2.append(x)
print("2. Even numbers:",evens_q2)

words_q2 = ["apple", "banana", "cherry"]
upper_words_q2 = []
for word in words_q2:
    upper_words_q2.append(word.upper())
print("3. Uppercase words:", upper_words_q2)

lengths_q2 = []
for word in words_q2:
    lengths_q2.append(len(word))
print("4. Word lengths:", lengths_q2)
nums_q2 = [-5, 3, -2, 7, 0, -1]
positive_q2 = []
for n in nums_q2:
    if n>0:
        positive_q2.append(n)
print("5. Positive numbers:", positive_q2)

matrix_q2 = [[1, 2], [3, 4], [5, 6]]
flat_q2 = []
for sublist in matrix_q2:
    for item in sublist:
        flat_q2.append(item)
print("6. Flattened list:", flat_q2)

chars_q2 = ['a', 'b', 'c']
ascii_q2 = []
for ch in chars_q2:
    ascii_q2.append(ord(ch))
print("7. ASCII values:", ascii_q2)

sentences_q2 = ["hello world", "python is fun"]
replaced_q2 = []
for s in sentences_q2:
    new_sentence_q2 = s.replace(" ", "_")
    replaced_q2.append(new_sentence_q2)
print("8. Underscore sentences:", replaced_q2)

words2_q2 = ["apple", "banana", "apricot", "grape"]
starts_a_q2 = []
for w in words2_q2:
    if w.startswith("a"):
        starts_a_q2.append(w)
print("9. Words starting with 'a':", starts_a_q2)


reverse_q2 = []
for w in words2_q2:
    reverse_q2.append(w[::-1])
print("10. Reversed words:", reverse_q2)

#QUESTION 3
print("\n=== Nested List Processor ===")
nested_list_q3 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
flattened_q3 = []
for row_q3 in nested_list_q3:
    for item_q3 in row_q3:
        flattened_q3.append(item_q3)
print("1. Flattened List:", flattened_q3)
print("2. Accessed Element at [1][2]:", nested_list_q3[1][2])
modify_row_q3 = 2
modify_col_q3 = 1
new_value_q3 = 999

if modify_row_q3 < len(nested_list_q3) and modify_col_q3 < len(nested_list_q3[modify_row_q3]):
    nested_list_q3[modify_row_q3][modify_col_q3] = new_value_q3
    print("3. Modified List:")
    for r_q3 in nested_list_q3:
        print(r_q3)
else:
    print("3. Invalid index for modification.")

#QUESTION 4
print("\n=== List Sorting Algorithms ===")
unsorted_q4 = [64, 34, 25, 12, 22, 11, 90]
def bubble_sort_q4(arr):
    arr2_q4 = []
    for val in arr:
        arr2_q4.append(val)
    n = len(arr2_q4)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr2_q4[j] > arr2_q4[j + 1]:
                temp = arr2_q4[j]
                arr2_q4[j] = arr2_q4[j + 1]
                arr2_q4[j + 1] = temp
    return arr2_q4

def merge_sort_q4(arr):
    if len(arr) <= 1:
        return arr
    mid_q4=len(arr) // 2
    left_half_q4 = []
    right_half_q4 = []
    count_q4 = 0
    for value in arr:
        if count_q4 < mid_q4:
            left_half_q4.append(value)
        else:
            right_half_q4.append(value)
        count_q4 += 1
    sorted_left_q4 = merge_sort_q4(left_half_q4)
    sorted_right_q4 = merge_sort_q4(right_half_q4)
    return merge_q4(sorted_left_q4, sorted_right_q4)

def merge_q4(left, right):
    result_q4 = []
    j = 0
    i = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_q4.append(left[i])
            i += 1
        else:
            result_q4.append(right[j])
            j += 1
    while i < len(left):
        result_q4.append(left[i])
        i += 1
    while j < len(right):
        result_q4.append(right[j])
        j += 1
    return result_q4

merge_sorted_q4 = merge_sort_q4(unsorted_q4)

print("Original List:", unsorted_q4)
print("2. Merge Sort :", merge_sorted_q4)

#QUESTION 5
print("\n=== List Searching Techniques ===")
search_list_q5 = [34, 12, 90, 56, 11, 73, 25]
def linear_search_q5(arr, target):
    index_q5 = 0
    while index_q5 < len(arr):
        if arr[index_q5] == target:
            return index_q5
        index_q5 += 1
    return -1

def binary_search_q5(arr, target):
    low_q5 = 0
    high_q5 = len(arr) - 1

    while low_q5 <= high_q5:
        mid_q5 = (low_q5 + high_q5) // 2
        if arr[mid_q5] == target:
            return mid_q5
        elif arr[mid_q5] < target:
            low_q5 = mid_q5 + 1
        else:
            high_q5 = mid_q5 - 1
    return -1

target_q5 = int(input("Enter number to search: "))
pos_linear_q5 = linear_search_q5(search_list_q5, target_q5)
sorted_list_q5 = []
for x in search_list_q5:
    sorted_list_q5.append(x)

n_q5 = len(sorted_list_q5)
for i_q5 in range(n_q5):
    for j_q5 in range(0, n_q5 - i_q5 - 1):
        if sorted_list_q5[j_q5] > sorted_list_q5[j_q5 + 1]:
            temp = sorted_list_q5[j_q5]
            sorted_list_q5[j_q5] = sorted_list_q5[j_q5 + 1]
            sorted_list_q5[j_q5 + 1] = temp

pos_binary_q5 = binary_search_q5(sorted_list_q5, target_q5)
print("\nOriginal List       :", search_list_q5)
print("Sorted List         :", sorted_list_q5)

if pos_linear_q5 != -1:
    print("1. Linear Search → Found at index", pos_linear_q5)
else:
    print("1. Linear Search → Not found")

if pos_binary_q5 != -1:
    print("2. Binary Search → Found at index", pos_binary_q5)
else:
    print("2. Binary Search → Not found")

#QUESTION 6
print("\n=== List Filtering System ===")
products_q6 = [
    {"name": "Laptop", "price": 1200, "category": "electronics"},
    {"name": "Book", "price": 80, "category": "education"},
    {"name": "Phone", "price": 600, "category": "electronics"},
    {"name": "Pen", "price": 5, "category": "stationery"},
    {"name": "Headphones", "price": 150, "category": "electronics"},
    {"name": "Notebook", "price": 120, "category": "education"}
]
filtered_q6=[]
for item_q6 in products_q6:
    if item_q6["price"] >100 and item_q6["category"] == "electronics":
        filtered_q6.append(item_q6)
    
print("Filtered Products (price > 100 & category == 'electronics'):")
for f_q6 in filtered_q6:
    print("Name:", f_q6["name"], "| Price:", f_q6["price"], "| Category:", f_q6["category"])

#QUESTION 7
print("\n=== List Transformation Tool ===")
numbers_q7 = [1, 2, 3, 4, 5]
def scale_number_q7(x):
    return x * 10

scaled_q7 = []
for n in numbers_q7:
    scaled_q7.append(n * 10)
print("1. Scaled Numbers (×10):", scaled_q7)
names_q7 = ["Ali", "Sara", "Bilal"]
greetings_q7 = []
for name in names_q7:
    greetings_q7.append("Hello, " + name + "!")
print("2. Formatted Greetings:", greetings_q7)
students_q7 = [
    {"name": "Zara", "grade": "A"},
    {"name": "Usman", "grade": "B"},
    {"name": "Hina", "grade": "A+"}
]

student_lines_q7 = []
for student in students_q7:
    line = "Name: " + student["name"] + " | Grade: " + student["grade"]
    student_lines_q7.append(line)

print("3. Mapped Student Info:")
for line in student_lines_q7:
    print(line)

#QUESTION 8
print("\n=== List Comparison Utility ===")
list1_q8 = [1, 2, 3, 4, 5]
list2_q8 = [4, 5, 6, 7, 8]
common_q8 = []
for item in list1_q8:
    if item in list2_q8:
        common_q8.append(item)

unique_to_list1_q8 = []
for item in list1_q8:
    if item not in list2_q8:
        unique_to_list1_q8.append(item)


unique_to_list2_q8 = []
for item in list2_q8:
    if item not in list1_q8:
        unique_to_list2_q8.append(item)

differences_q8 = unique_to_list1_q8 + unique_to_list2_q8
print("List 1:", list1_q8)
print("List 2:", list2_q8)
print("1. Common Elements:", common_q8)
print("2. Unique to List 1:", unique_to_list1_q8)
print("3. Unique to List 2:", unique_to_list2_q8)
print("4. All Differences:", differences_q8)

#Question 9
print("\n=== List Statistics Calculator ===")
numbers_q9 = [1, 2, 2, 3, 4, 5, 5, 5, 6]
sum_q9 = 0
for n in numbers_q9:
    sum_q9+=n
mean = sum_q9 / len(numbers_q9) 
sorted_q9 = sorted(numbers_q9)
n_q9 = len(sorted_q9)
if n_q9 % 2 == 1:
    median_q9=sorted_q9[n_q9 // 2]
else:
    mid1 = sorted_q9[n_q9 // 2 - 1]
    mid2 = sorted_q9[n_q9 // 2]
    median_q9 = (mid1 + mid2) / 2

freq_q9 = {}
for val in numbers_q9:
    if val in freq_q9:
        freq_q9[val] += 1
    else:
        freq_q9[val] = 1
highest_count_q9 = 0
mode_q9 = []

for key in freq_q9:
    if freq_q9[key] > highest_count_q9:
        highest_count_q9 = freq_q9[key]
        mode_q9 = [key]
    elif freq_q9[key] == highest_count_q9:
        mode_q9.append(key)

sq_diff_sum_q9 = 0
for val in numbers_q9:
    sq_diff_q9 = (val - mean) ** 2
    sq_diff_sum_q9 += sq_diff_q9
variance_q9 = sq_diff_sum_q9 / len(numbers_q9)

std_dev_q9 = variance_q9 ** 0.5
print("List:", numbers_q9)
print("1. Mean:", round(mean, 2))
print("2. Median:", median_q9)
print("3. Mode:", mode_q9)
print("4. Variance:", round(variance_q9, 2))
print("5. Standard Deviation:", round(std_dev_q9, 2))

#QUESTION 10
print("\n=== List Visualization Tool ===")
import matplotlib.pyplot as plt
items_q10 = ["Apples", "Bananas", "Oranges", "Grapes"]
quantities_q10 = [10, 15, 7, 5]
#bar chart
plt.figure(figsize=(6, 4))
plt.bar(items_q10, quantities_q10, color='skyblue')
plt.title("Bar Chart: Fruit Quantities")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.tight_layout()
plt.show()
#pie chart
plt.figure(figsize=(6, 6))
plt.pie(quantities_q10, labels=items_q10, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart: Fruit Distribution")
plt.axis("equal")
plt.tight_layout()
plt.show()

#QUESTION 11
print("\n=== Memory-Efficient List Operations ===")
large_list_q11 = list(range(1000000))
square_sum_q11 = 0
for number in large_list_q11:
    square_sum_q11 += number * number
print("Sum of squares:", square_sum_q11)

#QUESTION 12
print("\n=== List Performance Benchmarker ===")
import time
numbers_q12 = list(range(100000))
start_time_q12 = time.time()
doubled_q12 = []
for x in numbers_q12:
    doubled_q12.append(x * 2)
end_time_q12 = time.time()
print("1. Manual loop took:", round(end_time_q12 - start_time_q12, 4), "seconds")
start_time_q12 = time.time()
doubled_q12_v2 = [x * 2 for x in numbers_q12]
end_time_q12 = time.time()
print("2. List comprehension took:", round(end_time_q12 - start_time_q12, 4), "seconds")

#QUESTION 13
print("\n=== Custom List Data Structure ===")
class CustomList_q13:
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size
    def add(self, value):
        if len(self.data) < self.max_size:
            self.data.append(value)
        else:
            print("Max size reached.")
    def __str__(self):
        return str(self.data)

mylist_q13 = CustomList_q13(3)
mylist_q13.add(10)
mylist_q13.add(20)
mylist_q13.add(30)
mylist_q13.add(40)
print("Custom List:", mylist_q13)

#QUESTION 14
print("\n=== List Serialization System ===")
import json, csv, pickle
data_q14 = [1, 2, 3, 4, 5]
with open("data_q14.json", "w") as f_q14:
    json.dump(data_q14, f_q14)
with open("data_q14.csv", "w", newline='') as f_q14:
    writer_q14 = csv.writer(f_q14)
    writer_q14.writerow(data_q14)
with open("data_q14.pkl", "wb") as f_q14:
    pickle.dump(data_q14, f_q14)
print("List saved to JSON, CSV, and Binary format.")

#QUESTION 15
print("\n=== List Validation Framework ===")
data_q15 = [1, 2, '', 3, 'hello', 2, 5, '']
no_empty_q15 = []
for x in data_q15:
    if x != '':
        no_empty_q15.append(x)
no_duplicates_q15 = []
for x in no_empty_q15:
    if x not in no_duplicates_q15:
        no_duplicates_q15.append(x)
all_integers_q15 = True
for x in no_duplicates_q15:
    if not isinstance(x, int):
        all_integers_q15 = False
print("Cleaned List:", no_duplicates_q15)
print("All values are integers:", all_integers_q15)

#QUESTION 16
print("\n=== List Encryption Tool ===")
original_q16 = ["apple", "banana", "cherry"]
encrypted_q16 = []
for word in original_q16:
    encrypted_word = ""
    for char in word:
        encrypted_word += chr(ord(char) + 3)
    encrypted_q16.append(encrypted_word)
decrypted_q16 = []
for word in encrypted_q16:
    decrypted_word = ""
    for char in word:
        decrypted_word += chr(ord(char) - 3)
    decrypted_q16.append(decrypted_word)
print("Encrypted:", encrypted_q16)
print("Decrypted:", decrypted_q16)

#QUESTION 17
print("\n=== List Compression Algorithm ===")
data_q17 = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']
compressed_q17 = []
count_q17 = 1
for i in range(1, len(data_q17)):
    if data_q17[i] == data_q17[i - 1]:
        count_q17 += 1
    else:
        compressed_q17.append((data_q17[i - 1], count_q17))
        count_q17 = 1
compressed_q17.append((data_q17[-1], count_q17))
print("Original:", data_q17)
print("Compressed:", compressed_q17)

#QUESTION 18
print("\n=== List Diff Calculator ===")
old_q18 = ["a", "b", "c", "d"]
new_q18 = ["b", "c", "d", "e"]
added_q18 = []
removed_q18 = []
for item in new_q18:
    if item not in old_q18:
        added_q18.append(item)
for item in old_q18:
    if item not in new_q18:
        removed_q18.append(item)
print("Added:", added_q18)
print("Removed:", removed_q18)

#QUESTION 19
print("\n=== List Merge Strategies ===")
list1_q19 = [1, 2, 3]
list2_q19 = ['a', 'b', 'c']
zipped_q19 = []
for i in range(len(list1_q19)):
    zipped_q19.append((list1_q19[i], list2_q19[i]))
print("Zipped:", zipped_q19)
from itertools import chain
list3_q19 = [10, 20]
list4_q19 = [30, 40]
chained_q19 = list(chain(list3_q19, list4_q19))
print("Chained:", chained_q19)
data1_q19 = [{'id': 1, 'value': 'A'}, {'id': 2, 'value': 'B'}]
data2_q19 = [{'id': 2, 'value': 'C'}, {'id': 3, 'value': 'D'}]
merged_q19 = {}
for item in data1_q19 + data2_q19:
    merged_q19[item['id']] = item['value']
print("Merged by ID:", merged_q19)

#QUESTION 20
print("\n=== List Partitioning Tool ===")
data_q20 = list(range(1, 21))
chunked_q20 = []
chunk_size_q20 = 5
for i in range(0, len(data_q20), chunk_size_q20):
    chunked_q20.append(data_q20[i:i+chunk_size_q20])
even_q20 = []
odd_q20 = []
for x in data_q20:
    if x % 2 == 0:
        even_q20.append(x)
    else:
        odd_q20.append(x)
print("Chunks:", chunked_q20)
print("Evens:", even_q20)
print("Odds:", odd_q20)

#QUESTION 21
print("\n=== List Rotation Methods ===")
data_q21 = [1, 2, 3, 4, 5]
rotate_left_q21 = 2
left_rotated_q21 = data_q21[rotate_left_q21:] + data_q21[:rotate_left_q21]
rotate_right_q21 = 2
right_rotated_q21 = data_q21[-rotate_right_q21:] + data_q21[:-rotate_right_q21]
print("Original:", data_q21)
print("Left Rotated:", left_rotated_q21)
print("Right Rotated:", right_rotated_q21)

#QUESTION 22
print("\n=== List Permutation Generator ===")

def permute_q22(arr, current_q22=[]):
    if len(arr) == 0:
        print(current_q22)
        return
    for i in range(len(arr)):
        remaining_q22 = arr[:i] + arr[i+1:]
        permute_q22(remaining_q22, current_q22 + [arr[i]])

input_list_q22 = [1, 2, 3]
permute_q22(input_list_q22)

#QUESTION 23
print("\n=== List Combination Calculator ===")

from itertools import combinations

input_list_q23 = [1, 2, 3, 4]
k_q23 = 2

comb_q23 = list(combinations(input_list_q23, k_q23))

for combo_q23 in comb_q23:
    print(combo_q23)

#QUESTION 24
print("\n=== List Intersection Finder ===")
list1_q24 = [1, 2, 3, 4, 5]
list2_q24 = [3, 4, 5, 6, 7]
list3_q24 = [0, 3, 5, 9]
set1_q24 = set(list1_q24)
set2_q24 = set(list2_q24)
set3_q24 = set(list3_q24)
common_elements_q24 = list(set1_q24 & set2_q24 & set3_q24)
print("Common Elements in All Lists:", common_elements_q24)

#QUESTION 25
print("\n=== List Union Operator ===")
list1_q25 = [1, 2, 3, 4, 5]
list2_q25 = [4, 5, 6, 7, 8]
list3_q25 = [7, 8, 9, 10]
combined_q25 = list1_q25 + list2_q25 + list3_q25
union_q25 = list(set(combined_q25))
union_q25.sort()
print("List 1:", list1_q25)
print("List 2:", list2_q25)
print("List 3:", list3_q25)
print("Combined Union (No Duplicates):", union_q25)





     








   











         



    