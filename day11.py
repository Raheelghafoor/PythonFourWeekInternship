#✅ Title: Advanced Sequence Operations
#🎯 Focus: Dive deep into slicing, indexing, and custom sequence behavior by solving advanced problems that go beyond basic list manipulation
#QUESTION 1
def rotate_right_d11q1(lst_d11q1, k_d11q1):
    k_d11q1 = k_d11q1 % len(lst_d11q1)
    return lst_d11q1[-k_d11q1:] + lst_d11q1[:-k_d11q1]
nums_d11q1 = [1, 2, 3, 4, 5]
shift_d11q1 = 2
output_d11q1 = rotate_right_d11q1(nums_d11q1, shift_d11q1)
print(output_d11q1)
#QUESTION 2
def filter_sequence_d11q2(data_d11q2):
    seen_d11q2 = set()
    result_d11q2 = []
    for item_d11q2 in data_d11q2:
        if item_d11q2 is None:
            continue
        if item_d11q2 < 0:
            continue
        if item_d11q2 in seen_d11q2:
            continue
        seen_d11q2.add(item_d11q2)
        result_d11q2.append(item_d11q2)
    return result_d11q2
input_d11q2 = [1, None, -2, 3, 1, 4, None, -1, 3]
output_d11q2 = filter_sequence_d11q2(input_d11q2)
print(output_d11q2)

#QUESTION 3
def transform_sequence_d11q3(seq_d11q3):
    result_d11q3 = []
    for num_d11q3 in seq_d11q3:
        if num_d11q3 % 2 == 0:
            result_d11q3.append(num_d11q3 * 2)
        else:
            result_d11q3.append(num_d11q3 * 3)
    return result_d11q3
input_d11q3 = [1, 2, 3, 4, 5]
output_d11q3 = transform_sequence_d11q3(input_d11q3)
print(output_d11q3)

#QUESTION 4
def multiply_sequence_d11q4(seq_d11q4):
    product_d11q4 = 1
    for number_d11q4 in seq_d11q4:
        product_d11q4 = product_d11q4 * number_d11q4
    return product_d11q4

input_d11q4 = [1, 2, 3, 4]
output_d11q4 = multiply_sequence_d11q4(input_d11q4)
print(output_d11q4)

#QUESTION 5
def zip_to_dict_d11q5(names_d11q5, scores_d11q5):
    result_d11q5 = {} 
    for i_d11q5 in range(len(names_d11q5)):
        name_d11q5 = names_d11q5[i_d11q5]
        score_d11q5 = scores_d11q5[i_d11q5] 
        result_d11q5[name_d11q5] = score_d11q5
    return result_d11q5
names_d11q5 = ["Ali", "Sara"]
scores_d11q5 = [85, 90]
output_d11q5 = zip_to_dict_d11q5(names_d11q5, scores_d11q5)
print(output_d11q5)


#✅ Title: Dictionary Operations Deep Dive
#🎯 Focus: Explore every major functionality Python dictionaries offer — from creation and manipulation to validation, transformation, and storage.
#QUESTION 1
def even_square_dict_d11_dict1(numbers_d11_dict1):
    result_d11_dict1 = {}
    for num_d11_dict1 in numbers_d11_dict1:
        if num_d11_dict1 % 2 == 0:
            result_d11_dict1[num_d11_dict1] = num_d11_dict1 ** 2
        return result_d11_dict1
input_d11_dict1 = [1, 2, 3, 4, 5, 6]
output_d11_dict1 = even_square_dict_d11_dict1(input_d11_dict1)
print(output_d11_dict1)

#QUESTION 2
def add_or_update_student_d11_dict2(data_d11_dict2, class_name_d11_dict2, roll_no_d11_dict2, name_d11_dict2, score_d11_dict2):
    if class_name_d11_dict2 not in data_d11_dict2:
        data_d11_dict2[class_name_d11_dict2] = {}
    
    data_d11_dict2[class_name_d11_dict2][roll_no_d11_dict2] = {
        "name": name_d11_dict2,
        "score": score_d11_dict2
    }
students_d11_dict2 = {}
add_or_update_student_d11_dict2(students_d11_dict2, "Class10", "Roll01", "Ali", 85)
add_or_update_student_d11_dict2(students_d11_dict2, "Class10", "Roll02", "Sara", 90)
add_or_update_student_d11_dict2(students_d11_dict2, "Class9", "Roll05", "Ahmed", 78)
print(students_d11_dict2)

#QUESTION 3
def merge_dicts_d11_dict3(dict1_d11_dict3, dict2_d11_dict3):
    merged_d11_dict3 = dict1_d11_dict3.copy()
    for key_d11_dict3, value_d11_dict3 in dict2_d11_dict3.items():
        if key_d11_dict3 in merged_d11_dict3:
            old_value_d11_dict3 = merged_d11_dict3[key_d11_dict3]
            if isinstance(old_value_d11_dict3, list):
                merged_d11_dict3[key_d11_dict3].append(value_d11_dict3)
            else:
                merged_d11_dict3[key_d11_dict3] = [old_value_d11_dict3, value_d11_dict3]
        else:
            merged_d11_dict3[key_d11_dict3] = value_d11_dict3
    return merged_d11_dict3
dict1_d11_dict3 = {'a': 1, 'b': 2}
dict2_d11_dict3 = {'b': 3, 'c': 4}
output_d11_dict3 = merge_dicts_d11_dict3(dict1_d11_dict3, dict2_d11_dict3)
print(output_d11_dict3)

#QUESTION 4
def validate_profile_d11_dict4(profile_d11_dict4, required_keys_d11_dict4):
    for key_d11_dict4 in required_keys_d11_dict4:
        if key_d11_dict4 not in profile_d11_dict4:
            return False
    return True
required_d11_dict4 = ["name", "email", "age"]
user1_d11_dict4 = {"name": "Ali", "email": "ali@example.com", "age": 22}
print(validate_profile_d11_dict4(user1_d11_dict4, required_d11_dict4))
user2_d11_dict4 = {"name": "Sara", "age": 20}
print(validate_profile_d11_dict4(user2_d11_dict4, required_d11_dict4))

#QUESTION 5
def apply_discount_d11_dict5(products_d11_dict5):
    result_d11_dict5 = {}
    for item_d11_dict5, price_d11_dict5 in products_d11_dict5.items():
        discounted_price_d11_dict5 = price_d11_dict5 * 0.9
        result_d11_dict5[item_d11_dict5] = round(discounted_price_d11_dict5, 2)
    return result_d11_dict5
products_d11_dict5 = {
    "Laptop": 1000,
    "Mouse": 50,
    "Keyboard": 150
}
output_d11_dict5 = apply_discount_d11_dict5(products_d11_dict5)
print(output_d11_dict5)

#QUESTION 6
def filter_passed_students_d11_dict6(marks_d11_dict6):
    result_d11_dict6 = {}
    for student_d11_dict6, score_d11_dict6 in marks_d11_dict6.items():
        if score_d11_dict6 > 60:
            result_d11_dict6[student_d11_dict6] = score_d11_dict6
    return result_d11_dict6
students_d11_dict6 = {
    "Ali": 75,
    "Sara": 59,
    "Ahmed": 91,
    "Usman": 60
}
output_d11_dict6 = filter_passed_students_d11_dict6(students_d11_dict6)
print(output_d11_dict6)

#QUESTION 7
def sort_dict_by_score_d11_dict7(marks_d11_dict7):
    sorted_list_d11_dict7 = sorted(
        marks_d11_dict7.items(),
        key=lambda item_d11_dict7: item_d11_dict7[1],
        reverse=True
    )
    return sorted_list_d11_dict7
students_d11_dict7 = {
    "Ali": 75,
    "Sara": 59,
    "Ahmed": 91
}
output_d11_dict7 = sort_dict_by_score_d11_dict7(students_d11_dict7)
print(output_d11_dict7)

#QUESTION 8
import json
user_data_d11_dict8 = {
    "name": "Ali",
    "email": "ali@example.com",
    "age": 22,
    "score": 91
}
file_path_d11_dict8 = "user_profile_d11.json"
with open(file_path_d11_dict8, "w") as file_d11_dict8:
    json.dump(user_data_d11_dict8, file_d11_dict8)
with open(file_path_d11_dict8, "r") as file_d11_dict8:
    loaded_data_d11_dict8 = json.load(file_d11_dict8)
print(loaded_data_d11_dict8)

#QUESTION 9
def dict_cache_decorator_d11_dict9(func_d11_dict9):
    cache_d11_dict9 = {}
    def wrapper_d11_dict9(input_dict_d11_dict9):
        dict_key_d11_dict9 = frozenset(input_dict_d11_dict9.items())
        if dict_key_d11_dict9 in cache_d11_dict9:
            return cache_d11_dict9[dict_key_d11_dict9]

        result_d11_dict9 = func_d11_dict9(input_dict_d11_dict9)
        cache_d11_dict9[dict_key_d11_dict9] = result_d11_dict9
        return result_d11_dict9
    return wrapper_d11_dict9

def sum_values_d11_dict9(data_d11_dict9):
    return sum(data_d11_dict9.values())
user_a_d11_dict9 = {"a": 1, "b": 2}
user_b_d11_dict9 = {"a": 1, "b": 2}
user_c_d11_dict9 = {"x": 5, "y": 10}
print(sum_values_d11_dict9(user_a_d11_dict9))  
print(sum_values_d11_dict9(user_b_d11_dict9))  
print(sum_values_d11_dict9(user_c_d11_dict9))

#QUESTION 10
def find_diff_d11_dict10(dict1_d11_dict10, dict2_d11_dict10):
    result_d11_dict10 = {}
    for key_d11_dict10 in dict1_d11_dict10:
        if key_d11_dict10 in dict2_d11_dict10:
            if dict1_d11_dict10[key_d11_dict10] != dict2_d11_dict10[key_d11_dict10]:
                result_d11_dict10[key_d11_dict10] = (
                    dict1_d11_dict10[key_d11_dict10],
                    dict2_d11_dict10[key_d11_dict10]
                )
    return result_d11_dict10
old_profile_d11_dict10 = {
    "name": "Ali",
    "age": 22,
    "email": "ali@example.com"
}
new_profile_d11_dict10 = {
    "name": "Ali",
    "age": 23,
    "email": "ali123@example.com"
}
output_d11_dict10 = find_diff_d11_dict10(old_profile_d11_dict10, new_profile_d11_dict10)
print(output_d11_dict10)

#QUESTION 11
def navigate_path_d11_dict11(data_d11_dict11, path_d11_dict11):
    current_d11_dict11 = data_d11_dict11
    for key_d11_dict11 in path_d11_dict11:
        if isinstance(current_d11_dict11, dict) and key_d11_dict11 in current_d11_dict11:
            current_d11_dict11 = current_d11_dict11[key_d11_dict11]
        else:
            return None
    return current_d11_dict11

nested_dict_d11_dict11 = {
    "user": {
        "profile": {
            "email": "ali@example.com",
            "age": 22
        }
    }
}
path1_d11_dict11 = ["user", "profile", "email"]   
path2_d11_dict11 = ["user", "settings", "theme"] 
print(navigate_path_d11_dict11(nested_dict_d11_dict11, path1_d11_dict11))  
print(navigate_path_d11_dict11(nested_dict_d11_dict11, path2_d11_dict11))

#QUESTION 12
def flatten_dict_d11_dict12(nested_d11_dict12, parent_key_d11_dict12="", sep_d11_dict12="."):
    flat_dict_d11_dict12 = {}
    for key_d11_dict12, value_d11_dict12 in nested_d11_dict12.items():
        new_key_d11_dict12 = parent_key_d11_dict12 + sep_d11_dict12 + key_d11_dict12 if parent_key_d11_dict12 else key_d11_dict12

        if isinstance(value_d11_dict12, dict):
            deeper_d11_dict12 = flatten_dict_d11_dict12(value_d11_dict12, new_key_d11_dict12, sep_d11_dict12)
            flat_dict_d11_dict12.update(deeper_d11_dict12)
        else:
            flat_dict_d11_dict12[new_key_d11_dict12] = value_d11_dict12

    return flat_dict_d11_dict12
nested_input_d11_dict12 = {
    "user": {
        "profile": {
            "email": "ali@example.com",
            "age": 22
        },
        "active": True
    }
}
output_d11_dict12 = flatten_dict_d11_dict12(nested_input_d11_dict12)
print(output_d11_dict12)

#QUESTION 13
def invert_dict_d11_dict13(original_d11_dict13):
    inverted_d11_dict13 = {}

    for key_d11_dict13, value_d11_dict13 in original_d11_dict13.items():
        if value_d11_dict13 not in inverted_d11_dict13:
            inverted_d11_dict13[value_d11_dict13] = [key_d11_dict13]
        else:
            inverted_d11_dict13[value_d11_dict13].append(key_d11_dict13)

    return inverted_d11_dict13

grades_d11_dict13 = {
    "Ali": "A",
    "Sara": "B",
    "Ahmed": "A",
    "Usman": "C",
    "Fatima": "B"
}
output_d11_dict13 = invert_dict_d11_dict13(grades_d11_dict13)
print(output_d11_dict13)

#QUESTION 14
def calculate_stats_d11_dict14(marks_d11_dict14):
    scores_d11_dict14 = list(marks_d11_dict14.values())
    if not scores_d11_dict14:
        return None
    avg_d11_dict14 = sum(scores_d11_dict14) / len(scores_d11_dict14)
    min_d11_dict14 = min(scores_d11_dict14)
    max_d11_dict14 = max(scores_d11_dict14)
    return avg_d11_dict14, min_d11_dict14, max_d11_dict14
student_marks_d11_dict14 = {
    "Ali": 85,
    "Sara": 90,
    "Ahmed": 78,
    "Usman": 92
}
avg_d11_dict14, min_d11_dict14, max_d11_dict14 = calculate_stats_d11_dict14(student_marks_d11_dict14)
print("Average:", round(avg_d11_dict14, 2))
print("Minimum:", min_d11_dict14)
print("Maximum:", max_d11_dict14)

#QUESTION 15
def validate_dict_d11_dict15(data_d11_dict15):
    seen_values_d11_dict15 = set()
    for key_d11_dict15, value_d11_dict15 in data_d11_dict15.items():
        if not isinstance(key_d11_dict15, str):
            return False
        if value_d11_dict15 is None:
            return False
        if value_d11_dict15 in seen_values_d11_dict15:
            return False
        seen_values_d11_dict15.add(value_d11_dict15)
    return True
valid_dict_d11_dict15 = {
    "name": "Ali",
    "email": "ali@example.com",
    "age": 22
}
invalid_dict_d11_dict15 = {
    "name": "Ali",
    123: "ali@example.com",        
    "age": None                    
}
print("Valid dict:", validate_dict_d11_dict15(valid_dict_d11_dict15))     
print("Invalid dict:", validate_dict_d11_dict15(invalid_dict_d11_dict15))










        




    