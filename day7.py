#✅ 15 Python Coding Tasks – Mathematical Computing Suite
#question 1
import statistics

print("Statistical Calculator Suite")
stats_input = input("Enter numbers separated by commas: ")

try:
    stats_parts = stats_input.split(",")
    stats_numbers = []
    for item in stats_parts:
        item = item.strip()
        stats_numbers.append(float(item))

    stats_mean = statistics.mean(stats_numbers)
    stats_median = statistics.median(stats_numbers)

    try:
        stats_mode = statistics.mode(stats_numbers)
    except statistics.StatisticsError:
        stats_mode = "No single mode"

    stats_stdev = statistics.stdev(stats_numbers)
    stats_variance = statistics.variance(stats_numbers)

    print("Mean:", stats_mean)
    print("Median:", stats_median)
    print("Mode:", stats_mode)
    print("Standard Deviation:", stats_stdev)
    print("Variance:", stats_variance)

except ValueError:
    print("Error: Enter only numbers separated by commas")

#question 2
import random

print("Probability Simulator")
while True:
    print("Choose an option")
    print("1. Coin Flip")
    print("2. Dice Roll")
    print("3. Weather Prediction")

    prob_choice = input("Enter 1, 2 or 3: ").strip()

    if prob_choice in ["1", "2", "3"]:
        prob_choice = int(prob_choice)
        break
    else:
        print("Invalid input")

if prob_choice == 1:
    while True:
        flips_input = input("How many coin flips: ").strip()
        if flips_input.isdigit():
            flips_total = int(flips_input)
            if flips_total > 0:
                break
            else:
                print("Enter a number greater than 0")
        else:
            print("Enter a valid number")

    count_heads = 0
    count_tails = 0

    for i in range(flips_total):
        coin_result = random.choice(["Heads", "Tails"])
        print("Flip", i+1, ":", coin_result)
        if coin_result == "Heads":
            count_heads += 1
        else:
            count_tails += 1

    print("Heads:", count_heads)
    print("Tails:", count_tails)

elif prob_choice == 2:
    while True:
        rolls_input = input("How many dice rolls: ").strip()
        if rolls_input.isdigit():
            rolls_total = int(rolls_input)
            if rolls_total > 0:
                break
            else:
                print("Enter a number greater than 0")
        else:
            print("Enter a valid number")

    for i in range(rolls_total):
        dice_result = random.randint(1, 6)
        print("Roll", i+1, ":", dice_result)

elif prob_choice == 3:
    while True:
        days_input = input("How many days to predict: ").strip()
        if days_input.isdigit():
            days_total = int(days_input)
            if days_total > 0:
                break
            else:
                print("Enter a number greater than 0")
        else:
            print("Enter a valid number")

    for i in range(days_total):
        weather_result = random.choices(
            ["Sunny", "Rainy", "Cloudy"],
            weights=[0.5, 0.3, 0.2],
            k=1
        )[0]
        print("Day", i+1, ":", weather_result)

#question 3
print("Function Table Viewer")
func_input_3 = input("Enter a function of x (example: x**2 + 3*x): ")

x_values_3 = list(range(-10, 11))

print("x     y")
for x_val_3 in x_values_3:
    try:
        y_val_3 = eval(func_input_3, {"x": x_val_3, "__builtins__": {}})
        print(x_val_3, " ", y_val_3)
    except:
        print(x_val_3, " ", "error")

#question 4
print("Number Theory Toolkit")

def check_prime_4(num_check_4):
    if num_check_4 < 2:
        return False
    for i in range(2, int(num_check_4 ** 0.5) + 1):
        if num_check_4 % i == 0:
            return False
    return True

def find_gcd_4(num1_4, num2_4):
    while num2_4 != 0:
        num1_4, num2_4 = num2_4, num1_4 % num2_4
    return num1_4

def find_lcm_4(num1_4, num2_4):
    return abs(num1_4 * num2_4) // find_gcd_4(num1_4, num2_4)

def find_factors_4(fact_num_4):
    factor_list_4 = []
    for i in range(1, fact_num_4 + 1):
        if fact_num_4 % i == 0:
            factor_list_4.append(i)
    return factor_list_4

while True:
    print("Choose an option")
    print("1. Prime Check")
    print("2. GCD")
    print("3. LCM")
    print("4. Factor a Number")
    print("5. Exit")

    choice_input_4 = input("Enter 1 to 5: ").strip()

    if choice_input_4 == "1":
        prime_input_4 = input("Enter number to check: ").strip()
        if prime_input_4.isdigit():
            prime_val_4 = int(prime_input_4)
            if check_prime_4(prime_val_4):
                print(prime_val_4, "is prime")
            else:
                print(prime_val_4, "is not prime")
        else:
            print("Invalid number")

    elif choice_input_4 == "2":
        gcd_a_4 = input("Enter first number: ").strip()
        gcd_b_4 = input("Enter second number: ").strip()
        if gcd_a_4.isdigit() and gcd_b_4.isdigit():
            gcd_val_a = int(gcd_a_4)
            gcd_val_b = int(gcd_b_4)
            result_gcd_4 = find_gcd_4(gcd_val_a, gcd_val_b)
            print("GCD is", result_gcd_4)
        else:
            print("Invalid numbers")

    elif choice_input_4 == "3":
        lcm_a_4 = input("Enter first number: ").strip()
        lcm_b_4 = input("Enter second number: ").strip()
        if lcm_a_4.isdigit() and lcm_b_4.isdigit():
            lcm_val_a = int(lcm_a_4)
            lcm_val_b = int(lcm_b_4)
            result_lcm_4 = find_lcm_4(lcm_val_a, lcm_val_b)
            print("LCM is", result_lcm_4)
        else:
            print("Invalid numbers")

    elif choice_input_4 == "4":
        factor_input_4 = input("Enter number to factor: ").strip()
        if factor_input_4.isdigit():
            factor_val_4 = int(factor_input_4)
            if factor_val_4 > 0:
                factor_result_4 = find_factors_4(factor_val_4)
                print("Factors are", factor_result_4)
            else:
                print("Enter a number greater than 0")
        else:
            print("Invalid number")

    elif choice_input_4 == "5":
        break

    else:
        print("Invalid choice")

#QUESTION 5
print("Matrix Operations")

def get_numberq5(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Enter a valid number")

def read_matrix(rows, cols, name):
    print("Enter values for", name)
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = get_numberq5(f"{name}[{i+1}][{j+1}]: ")
            row.append(val)
        matrix.append(row)
    return matrix

def add_matrices(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def subtract_matrices(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
        result.append(row)
    return result
def multiply_matrices(a,b):
    result=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(b[0])):
            total=0
            for k in range(len(b)):
                 total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result

print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = input("Choose 1, 2 or 3: ")

if choice == "1" or choice == "2":
    r = get_numberq5("Rows: ")
    c = get_numberq5("Columns: ")
    mat1 = read_matrix(r, c, "Matrix A")
    mat2 = read_matrix(r, c, "Matrix B")
    if choice == "1":
        result = add_matrices(mat1, mat2)
        print("A + B:")
    else:
        result = subtract_matrices(mat1, mat2)
        print("A - B:")
    for row in result:
        print(row)

elif choice == "3":
    r1 = get_numberq5("Rows for A: ")
    c1 = get_numberq5("Cols for A: ")
    r2 = get_numberq5("Rows for B: ")
    c2 = get_numberq5("Cols for B: ")
    if c1 != r2:
        print("Cannot multiply: Columns of A must match rows of B")
    else:
        mat1 = read_matrix(r1, c1, "Matrix A")
        mat2 = read_matrix(r2, c2, "Matrix B")
        result = multiply_matrices(mat1, mat2)
        print("A x B:")
        for row in result:
            print(row)
else:
    print("Invalid choice")

#QUESTION 6
print("Geometric Calculator")

import math

def get_numberq6(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Enter a number greater than 0")
        except:
            print("Invalid number")

def circle_calculations():
    r = get_numberq6("Enter radius of the circle: ")
    area = math.pi * r * r
    perimeter = 2 * math.pi * r
    print("Circle Area:", round(area, 2))
    print("Circle Perimeter:", round(perimeter, 2))

def rectangle_calculations():
    length = get_numberq6("Enter length: ")
    width = get_numberq6("Enter width: ")
    area = length * width
    perimeter = 2 * (length + width)
    print("Rectangle Area:", area)
    print("Rectangle Perimeter:", perimeter)

def sphere_calculations():
    r = get_numberq6("Enter radius of the sphere: ")
    volume = (4/3) * math.pi * r ** 3
    surface_area = 4 * math.pi * r ** 2
    print("Sphere Volume:", round(volume, 2))
    print("Sphere Surface Area:", round(surface_area, 2))

print("Choose shape")
print("1. Circle")
print("2. Rectangle")
print("3. Sphere")

shape_choice = input("Enter 1, 2 or 3: ")

if shape_choice == "1":
    circle_calculations()
elif shape_choice == "2":
    rectangle_calculations()
elif shape_choice == "3":
    sphere_calculations()
else:
    print("Invalid choice")


#QUESTION 7
print("Financial Calculator")
def get_numberq7(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Enter a number zero or more")
        except:
            print("Invalid number")
def compound_interest():
    principal=get_numberq7("Enter the principle amount")
    rate=get_numberq7("Enter annual interest rate (%):")
    time = get_numberq7("Enter time in years: ")
    compoundings = get_numberq7("Enter number of times interest is compounded per year: ")
    amount = principal * (1 + (rate / (100 * compoundings))) ** (compoundings * time)
    interest = amount - principal
    print("Final Amount:", round(amount, 2))
    print("Total Interest Earned:", round(interest, 2))
def loan_emi():
    loan = get_numberq7("Enter loan amount: ")
    rate = get_numberq7("Enter annual interest rate (%): ")
    years = get_numberq7("Enter loan term in years: ")

    monthly_rate = rate / (12 * 100)
    months = years * 12

    if rate == 0:
        emi = loan / months
    else:
        emi = loan * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

    print("Monthly EMI:", round(emi, 2))
    print("Total Payment:", round(emi * months, 2))
    print("Total Interest:", round(emi * months - loan, 2))

print("Choose option")
print("1. Compound Interest")
print("2. Loan EMI")

choice = input("Enter 1 or 2: ")

if choice == "1":
    compound_interest()
elif choice == "2":
    loan_emi()
else:
    print("Invalid choice")


#QUESTION 8
print("Physics Calculator")
def get_numberq8(prompt):
    while True:
        try:
          value=float(input(prompt))
          return value
        except:
          print("Enter a valid number")
          
def calculate_speed():
    distance = get_numberq8("Enter distance in meters: ")
    time = get_numberq8("Enter time in seconds: ")
    if time == 0:
        print("Time cannot be zero")
        return
    speed = distance / time
    print("Speed is", round(speed, 2), "meters per second")
def calculate_force():
    mass = get_numberq8("Enter mass in kilograms: ")
    acceleration = get_numberq8("Enter acceleration in meters per second squared: ")
    force = mass * acceleration
    print("Force is", round(force, 2), "Newtons")
def calculate_kinetic_energy():
    mass = get_numberq8("Enter mass in kilograms: ")
    velocity = get_numberq8("Enter velocity in meters per second: ")
    ke = 0.5 * mass * velocity * velocity
    print("Kinetic Energy is", round(ke, 2), "Joules")
print("Choose calculation")
print("1. Speed = Distance / Time")
print("2. Force = Mass × Acceleration")
print("3. Kinetic Energy = 0.5 × Mass × Velocity squared")
choice = input("Enter 1, 2 or 3: ")

if choice == "1":
    calculate_speed()
elif choice == "2":
    calculate_force()
elif choice == "3":
    calculate_kinetic_energy()
else:
    print("Invalid choice")
#QUESTION 9
print("Chemistry Formula Solver")

chem_weights = {
    "H": 1.008,
    "C": 12.01,
    "O": 16.00,
    "N": 14.01,
    "Na": 22.99,
    "Cl": 35.45,
    "S": 32.07
}

formula = input("Enter chemical formula (like H2O or CO2): ")
i = 0
total = 0

while i < len(formula):
    ch = formula[i]
    i += 1
    if i < len(formula) and formula[i].islower():
        ch += formula[i]
        i += 1

    num = ""
    while i < len(formula) and formula[i].isdigit():
        num += formula[i]
        i += 1

    count = int(num) if num else 1

    if ch in chem_weights:
        total += chem_weights[ch] * count
    else:
        print("Unknown element:", ch)
        total = None
        break

if total is not None:
    print("Molecular weight is", round(total, 3), "g/mol")

#Question 10
print("Engineering Unit Converter")

def get_numberq10(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Enter a valid number")

def meters_to_feet(m):
    return m * 3.28084
def feet_to_meters(f):
    return f / 3.28084
def kg_to_pounds(kg):
    return kg * 2.20462
def pounds_to_kg(lb):
    return lb / 2.20462
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
print("Choose conversion:")
print("1. Meters to Feet")
print("2. Feet to Meters")
print("3. Kilograms to Pounds")
print("4. Pounds to Kilograms")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")
choice = input("Enter 1 to 6: ")

if choice == "1":
    val = get_numberq10("Enter meters: ")
    print("Feet:", round(meters_to_feet(val), 4))
elif choice == "2":
    val = get_numberq10("Enter feet: ")
    print("Meters:", round(feet_to_meters(val), 4))
elif choice == "3":
    val = get_numberq10("Enter kilograms: ")
    print("Pounds:", round(kg_to_pounds(val), 4))
elif choice == "4":
    val = get_numberq10("Enter pounds: ")
    print("Kilograms:", round(pounds_to_kg(val), 4))
elif choice == "5":
    val = get_numberq10("Enter Celsius: ")
    print("Fahrenheit:", round(celsius_to_fahrenheit(val), 2))
elif choice == "6":
    val = get_numberq10("Enter Fahrenheit: ")
    print("Celsius:", round(fahrenheit_to_celsius(val), 2))
else:
    print("Invalid choice")

#QUESTION 11
print("Trigonometry Calculator")

import math

def get_numberq11(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Enter a valid number")
print("Choose angle type")
print("1. Degrees")
print("2. Radians")
angle_type = input("Enter 1 or 2: ")
if angle_type == "1":
    angle_deg = get_numberq11("Enter angle in degrees: ")
    angle_rad = math.radians(angle_deg)
elif angle_type == "2":
    angle_rad = get_numberq11("Enter angle in radians: ")
else:
    print("Invalid choice")
    exit()
sine_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
try:
    tan_val = math.tan(angle_rad)
except:
    tan_val = "undefined"

print("sin =", round(sine_val, 4))
print("cos =", round(cos_val, 4))
if abs(cos_val) < 1e-10:
    print("tan = undefined")
else:
    print("tan =", round(tan_val, 4))

#QUESTION 12
print("Calculus Approximator")
def get_numberq12(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Enter a valid number")
def get_function_input():
    return input("Enter a function of x (example: x**2 + 3*x): ")
def evaluate_function(func_str, x_val):
    try:
        return eval(func_str, {"x": x_val, "__builtins__": {}})
    except:
        print("Invalid function")
        return None
def approximate_derivative(func_str, x_val, h=0.0001):
    f_x1 = evaluate_function(func_str, x_val + h)
    f_x2 = evaluate_function(func_str, x_val)
    if f_x1 is None or f_x2 is None:
        return None
    return (f_x1 - f_x2) / h
def approximate_integral(func_str, a, b, n=1000):
    width = (b - a) / n
    total = 0
    for i in range(n):
        x1 = a + i * width
        x2 = a + (i + 1) * width
        y1 = evaluate_function(func_str, x1)
        y2 = evaluate_function(func_str, x2)
        if y1 is None or y2 is None:
            return None
        total += (y1 + y2) / 2 * width
    return total
print("1. Derivative at a point")
print("2. Definite Integral")

choice = input("Choose 1 or 2: ")

if choice == "1":
    func_input = get_function_input()
    x_point = get_numberq12("Enter the x value to find derivative: ")
    result = approximate_derivative(func_input, x_point)
    if result is not None:
        print("Approximate derivative is", round(result, 4))

elif choice == "2":
    func_input = get_function_input()
    start = get_numberq12("Enter lower limit a: ")
    end = get_numberq12("Enter upper limit b: ")
    result = approximate_integral(func_input, start, end)
    if result is not None:
        print("Approximate integral is", round(result, 4))
else:
    print("Invalid choice")

#QUESTION 13
print("Linear Algebra Basics")
def get_numberq13(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Enter a valid number")

def determinant_2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def inverse_2x2(m):
    det = determinant_2x2(m)
    if det == 0:
        return None
    return [
        [ m[1][1]/det, -m[0][1]/det],
        [-m[1][0]/det,  m[0][0]/det]
    ]
def read_matrixq13(rows, cols, name):
    print("Enter values for", name)
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = get_numberq13(f"{name}[{i+1}][{j+1}]: ")
            row.append(val)
        matrix.append(row)
    return matrix
def solve_2x2_system(a, b):
    det = determinant_2x2(a)
    if det == 0:
        return None
    d1 = [[b[0], a[0][1]], [b[1], a[1][1]]]
    d2 = [[a[0][0], b[0]], [a[1][0], b[1]]]
    x = determinant_2x2(d1) / det
    y = determinant_2x2(d2) / det
    return (x, y)
print("1. Determinant (2x2)")
print("2. Inverse (2x2)")
print("3. Solve 2x2 Linear System (Ax = b)")

choice_q13 = input("Choose 1, 2 or 3: ")

if choice_q13 == "1":
    m = read_matrixq13(2, 2, "Matrix")
    d = determinant_2x2(m)
    print("Determinant is:", round(d, 4))

elif choice_q13 == "2":
    m = read_matrixq13(2, 2, "Matrix")
    inv = inverse_2x2(m)
    if inv is None:
        print("Matrix not invertible")
    else:
        print("Inverse matrix:")
        for row in inv:
            print([round(val, 4) for val in row])
elif choice_q13 == "3":
    a = read_matrixq13(2, 2, "Matrix A")
    b = []
    for i in range(2):
        b.append(get_numberq13(f"Enter b[{i+1}]: "))
    sol = solve_2x2_system(a, b)
    if sol is None:
        print("No unique solution")
    else:
        print("Solution is: x =", round(sol[0], 4), ", y =", round(sol[1], 4))

else:
    print("Invalid choice")

#QUESTION 14
print("Gradient Descent Optimizer")

def get_numberq14(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Enter a valid number")
def get_function_input():
    return input("Enter a function in x (example: x**2 - 4*x + 3): ")
def get_derivative_input():
    return input("Enter its derivative in x (example: 2*x - 4): ")
def evaluate_expression(expr, x_val):
    try:
        return eval(expr, {"x": x_val, "__builtins__": {}})
    except:
        print("Error in evaluating expression")
        return None
func_str = get_function_input()
deriv_str = get_derivative_input()
x_val = get_numberq14("Enter starting x value: ")
learning_rate = get_numberq14("Enter learning rate (like 0.1): ")
iterations = int(get_numberq14("How many steps to run: "))
print("Starting Gradient Descent...")

for i in range(iterations):
    gradient = evaluate_expression(deriv_str, x_val)
    if gradient is None:
        break
    x_val = x_val - learning_rate * gradient
    print("Step", i + 1, ": x =", round(x_val, 5), "f(x) =", round(evaluate_expression(func_str, x_val), 5))

print("Final minimum estimate at x =", round(x_val, 5))

#QUESTION 15
print("N-Queens Puzzle Solver")
def print_board(board):
    for row in board:
        line = ""
        for col in row:
            if col == 1:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()
def is_safe(board, row, col, n):
     for i in range(col):
        if board[row][i] == 1:
            return False
     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
     for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
     return True
def solve(board, col, n):
    if col >= n:
        print("One solution:")
        print_board(board)
        return True  
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, col + 1, n):
                return True
            board[row][col] = 0  
    return False
def start_n_queens():
    try:
        n = int(input("Enter N (number of queens, try 4): "))
        if n < 1:
            print("N must be at least 1")
            return
        board = [[0] * n for _ in range(n)]
        if not solve(board, 0, n):
            print("No solution found")
    except:
        print("Please enter a valid number")

start_n_queens()

#✅ 15 Python Coding Tasks – Data Processing & File Handling
#QUESTION 1 - CSV Data Processor
import csv

print("\n--- CSV Data Processor ---")
with open("sample.csv", newline='') as csv_file_q1:
    csv_reader_q1 = csv.DictReader(csv_file_q1)
    csv_rows_q1 = list(csv_reader_q1)
    print("Total rows:", len(csv_rows_q1))
    print("Column names:", csv_reader_q1.fieldnames)

    csv_missing_q1 = {col: 0 for col in csv_reader_q1.fieldnames}
    for row in csv_rows_q1:
        for col in csv_reader_q1.fieldnames:
            if row[col] == '':
                csv_missing_q1[col] += 1
    print("Missing values per column:", csv_missing_q1)

#QUESTION 2 - JSON Configuration Manager
import json

print("\n--- JSON Configuration Manager ---")
with open("config.json", "r") as json_file_q2:
    config_data_q2 = json.load(json_file_q2)

print("Original Configuration:")
print(json.dumps(config_data_q2, indent=2))

config_data_q2["debug"] = False
config_data_q2["timeout"] = 45
config_data_q2["logging"] = {
    "level": "INFO",
    "file": "app.log"
}

with open("config.json", "w") as json_file_q2_out:
    json.dump(config_data_q2, json_file_q2_out, indent=2)

print("Updated configuration saved to config.json.")

#QUESTION 3 - Text File Analyzer
print("\n--- Text File Analyzer ---")

with open("sample.txt", "r") as txt_file_q3:
    txt_lines_q3 = txt_file_q3.readlines()

txt_word_count_q3 = 0
txt_word_freq_q3 = {}
txt_total_line_len_q3 = 0

for line_q3 in txt_lines_q3:
    words_q3 = line_q3.strip().split()
    txt_word_count_q3 += len(words_q3)
    txt_total_line_len_q3 += len(line_q3)

    for word in words_q3:
        word = word.lower()
        txt_word_freq_q3[word] = txt_word_freq_q3.get(word, 0) + 1

txt_most_freq_word_q3 = max(txt_word_freq_q3, key=txt_word_freq_q3.get)
txt_avg_line_len_q3 = txt_total_line_len_q3 / len(txt_lines_q3)

print("Total Words:", txt_word_count_q3)
print("Most Frequent Word:", txt_most_freq_word_q3)
print("Average Line Length:", round(txt_avg_line_len_q3, 2))

#QUESTION 4
import json

print("\n--- Data Validation Suite ---")

user_profiles_q4 = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": -5, "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "Dana", "age": 130, "email": 123},
    {"name": 999, "age": 30, "email": "dana@example.com"}
]

required_fields_q4 = ["name", "age", "email"]
field_types_q4 = {
    "name": str,
    "age": int,
    "email": str
}
field_ranges_q4 = {
    "age": (0, 120)
}

for idx_q4, profile_q4 in enumerate(user_profiles_q4):
    print(f"\nValidating Profile #{idx_q4 + 1}: {profile_q4}")
    errors_q4 = []

    for field_q4 in required_fields_q4:
        if field_q4 not in profile_q4:
            errors_q4.append(f"Missing required field: {field_q4}")
        else:
            if not isinstance(profile_q4[field_q4], field_types_q4[field_q4]):
                errors_q4.append(f"Incorrect type for '{field_q4}' (expected {field_types_q4[field_q4].__name__})")

            if field_q4 in field_ranges_q4 and isinstance(profile_q4[field_q4], (int, float)):
                min_val_q4, max_val_q4 = field_ranges_q4[field_q4]
                if not (min_val_q4 <= profile_q4[field_q4] <= max_val_q4):
                    errors_q4.append(f"'{field_q4}' out of range ({min_val_q4}-{max_val_q4})")

    if errors_q4:
        print(" Invalid profile due to:")
        for err_q4 in errors_q4:
            print("  -", err_q4)
    else:
        print(" Valid profile.")

#QUESTION 5
import csv

print("\n--- CSV Report Generator ---")

with open("report_data.csv", newline='') as file_q5:
    reader_q5 = csv.DictReader(file_q5)
    rows_q5 = list(reader_q5)
    fieldnames_q5 = reader_q5.fieldnames

total_rows_q5 = len(rows_q5)
column_totals_q5 = {col: 0 for col in fieldnames_q5 if col != "Name"}
numeric_counts_q5 = {col: 0 for col in fieldnames_q5 if col != "Name"}

for row_q5 in rows_q5:
    for col in column_totals_q5:
        try:
            val_q5 = float(row_q5[col])
            column_totals_q5[col] += val_q5
            numeric_counts_q5[col] += 1
        except:
            pass

with open("summary_report.txt", "w") as report_file_q5:
    report_file_q5.write("===== Report Summary =====\n")
    report_file_q5.write(f"Total records: {total_rows_q5}\n\n")
    for col in column_totals_q5:
        avg_q5 = column_totals_q5[col] / numeric_counts_q5[col] if numeric_counts_q5[col] else 0
        report_file_q5.write(f"Column: {col}\n")
        report_file_q5.write(f"  Total: {round(column_totals_q5[col], 2)}\n")
        report_file_q5.write(f"  Average: {round(avg_q5, 2)}\n\n")

print("Summary written to summary_report.txt")

#QUESTION 6
import csv
import json

print("\n--- Data Comparison Tool ---")
print("1. Compare CSV files")
print("2. Compare JSON files")

choice_q6 = input("Choose 1 or 2: ")

if choice_q6 == "1":
    file1_q6 = input("Enter first CSV filename: ")
    file2_q6 = input("Enter second CSV filename: ")
    with open(file1_q6, newline='') as f1_q6, open(file2_q6, newline='') as f2_q6:
        data1_q6 = list(csv.DictReader(f1_q6))
        data2_q6 = list(csv.DictReader(f2_q6))
    min_len_q6 = min(len(data1_q6), len(data2_q6))
    print(f"\nComparing first {min_len_q6} rows:")
    for i in range(min_len_q6):
        if data1_q6[i] != data2_q6[i]:
            print(f"Difference in row {i+1}:")
            print("File 1:", data1_q6[i])
            print("File 2:", data2_q6[i])
elif choice_q6 == "2":
    file1_q6 = input("Enter first JSON filename: ")
    file2_q6 = input("Enter second JSON filename: ")
    with open(file1_q6, "r") as f1_q6, open(file2_q6, "r") as f2_q6:
        json1_q6 = json.load(f1_q6)
        json2_q6 = json.load(f2_q6)
    all_keys_q6 = set(json1_q6.keys()) | set(json2_q6.keys())
    for key_q6 in all_keys_q6:
        val1_q6 = json1_q6.get(key_q6, "N/A")
        val2_q6 = json2_q6.get(key_q6, "N/A")
        if val1_q6 != val2_q6:
            print(f"Key: {key_q6}")
            print("File 1:", val1_q6)
            print("File 2:", val2_q6)
else:
    print("Invalid choice")

#QUESTION 7

import os
import shutil

print("\n--- File Organizer ---")

folder_path_q7 = input("Enter the folder path to organize: ")

if not os.path.exists(folder_path_q7):
    print("Folder not found")
else:
    types_q7 = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".doc"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Audio": [".mp3", ".wav"],
        "Spreadsheets": [".xlsx", ".csv"]
    }

    files_q7 = os.listdir(folder_path_q7)

    for file_q7 in files_q7:
        full_path_q7 = os.path.join(folder_path_q7, file_q7)
        if os.path.isfile(full_path_q7):
            moved_q7 = False
            for folder_q7, ext_list_q7 in types_q7.items():
                if file_q7.lower().endswith(tuple(ext_list_q7)):
                    target_folder_q7 = os.path.join(folder_path_q7, folder_q7)
                    os.makedirs(target_folder_q7, exist_ok=True)
                    shutil.move(full_path_q7, os.path.join(target_folder_q7, file_q7))
                    moved_q7 = True
                    break
            if not moved_q7:
                other_folder_q7 = os.path.join(folder_path_q7, "Others")
                os.makedirs(other_folder_q7, exist_ok=True)
                shutil.move(full_path_q7, os.path.join(other_folder_q7, file_q7))

    print("Files organized successfully.")

#QUESTION 8
import os
import shutil
import datetime
print("\n--- Backup System ---")

source_folder_q8 = input("Enter source folder path: ")
backup_base_q8 = input("Enter backup destination folder path: ")
if not os.path.exists(source_folder_q8):
    print("Source folder not found")
else:
    timestamp_q8 = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_q8 = os.path.join(backup_base_q8, "backup_" + timestamp_q8)
    os.makedirs(backup_folder_q8, exist_ok=True)

    files_q8 = os.listdir(source_folder_q8)
    for file_q8 in files_q8:
        full_src_q8 = os.path.join(source_folder_q8, file_q8)
        full_dst_q8 = os.path.join(backup_folder_q8, file_q8)
        if os.path.isfile(full_src_q8):
            shutil.copy2(full_src_q8, full_dst_q8)

    print("Backup completed in:", backup_folder_q8)

#QUESTION 9
import csv
import json

print("\n--- Data Migration Tool ---")
print("1. CSV to JSON")
print("2. JSON to CSV")

choice_q9 = input("Enter 1 or 2: ")

if choice_q9 == "1":
    csv_input_q9 = input("Enter CSV file name (e.g., data.csv): ")
    json_output_q9 = input("Enter JSON output file name (e.g., data.json): ")
    with open(csv_input_q9, newline='') as file_q9_csv:
        reader_q9 = csv.DictReader(file_q9_csv)
        rows_q9 = list(reader_q9)
    with open(json_output_q9, "w") as file_q9_json:
        json.dump(rows_q9, file_q9_json, indent=2)
    print("CSV data converted to JSON and saved to", json_output_q9)

elif choice_q9 == "2":
    json_input_q9 = input("Enter JSON file name (e.g., data.json): ")
    csv_output_q9 = input("Enter CSV output file name (e.g., data.csv): ")
    with open(json_input_q9, "r") as file_q9_json:
        data_q9 = json.load(file_q9_json)
    if isinstance(data_q9, list) and len(data_q9) > 0:
        with open(csv_output_q9, "w", newline='') as file_q9_csv:
            writer_q9 = csv.DictWriter(file_q9_csv, fieldnames=data_q9[0].keys())
            writer_q9.writeheader()
            writer_q9.writerows(data_q9)
        print("JSON data converted to CSV and saved to", csv_output_q9)
    else:
        print("Invalid JSON structure")

else:
    print("Invalid choice")

#QUESTION 10
print("\n--- Configuration Manager ---")

def read_config_file(filename_q10):
    config_data_q10 = {}
    with open(filename_q10, "r") as file_q10:
        for line_q10 in file_q10:
            line_q10 = line_q10.strip()
            if line_q10 and not line_q10.startswith("#") and "=" in line_q10:
                key_q10, value_q10 = line_q10.split("=", 1)
                config_data_q10[key_q10.strip()] = value_q10.strip()
    return config_data_q10

def write_config_file(filename_q10, config_data_q10):
    with open(filename_q10, "w") as file_q10:
        for key_q10, value_q10 in config_data_q10.items():
            file_q10.write(f"{key_q10}={value_q10}\n")

file_name_q10 = input("Enter .env/.ini filename: ")
config_q10 = read_config_file(file_name_q10)

print("\nCurrent Configuration:")
for k_q10, v_q10 in config_q10.items():
    print(k_q10, "=", v_q10)

while True:
    update_choice_q10 = input("\nDo you want to update a key? (yes/no): ").lower()
    if update_choice_q10 == "no":
        break
    key_q10 = input("Enter key to update or add: ")
    value_q10 = input("Enter new value: ")
    config_q10[key_q10] = value_q10

write_config_file(file_name_q10, config_q10)
print("Updated configuration saved to", file_name_q10)

#QUESTION 11
import os
import time
import shutil
from datetime import datetime

print("\n--- Log Rotation System ---")

log_filename_q11 = "application.log"
size_limit_bytes_q11 = 1000  # 1 KB for testing, change as needed

def rotate_log_q11():
    timestamp_q11 = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name_q11 = f"{log_filename_q11}.{timestamp_q11}.bak"
    shutil.move(log_filename_q11, new_name_q11)
    print("Log rotated:", new_name_q11)

while True:
    if os.path.exists(log_filename_q11):
        size_q11 = os.path.getsize(log_filename_q11)
        if size_q11 > size_limit_bytes_q11:
            rotate_log_q11()
            open(log_filename_q11, "w").close()
    time.sleep(5)

#QUESTION 12
import zipfile
import time
import os

print("\n--- Data Archiver ---")

def get_files_to_archive_q12():
    files_q12 = []
    while True:
        file_name_q12 = input("Enter file to add (or type 'done' to finish): ")
        if file_name_q12.lower() == 'done':
            break
        elif os.path.exists(file_name_q12):
            files_q12.append(file_name_q12)
        else:
            print("File does not exist.")
    return files_q12

def create_zip_archive_q12(file_list_q12):
    timestamp_q12 = time.strftime("%Y%m%d_%H%M%S")
    zip_name_q12 = f"archive_{timestamp_q12}.zip"
    with zipfile.ZipFile(zip_name_q12, 'w') as archive_q12:
        for file_q12 in file_list_q12:
            archive_q12.write(file_q12)
    print("Archive created:", zip_name_q12)

files_to_zip_q12 = get_files_to_archive_q12()
if files_to_zip_q12:
    create_zip_archive_q12(files_to_zip_q12)
else:
    print("No files selected.")

#QUESTION 13
import hashlib

print("\n--- File Integrity Checker ---")

def get_checksum_q13(filename_q13, method_q13='md5'):
    try:
        if method_q13 == 'md5':
            hasher_q13 = hashlib.md5()
        elif method_q13 == 'sha256':
            hasher_q13 = hashlib.sha256()
        else:
            print("Unsupported method.")
            return None

        with open(filename_q13, 'rb') as file_q13:
            while True:
                chunk_q13 = file_q13.read(4096)
                if not chunk_q13:
                    break
                hasher_q13.update(chunk_q13)
        return hasher_q13.hexdigest()

    except FileNotFoundError:
        print("File not found.")
        return None

file1_q13 = input("Enter first file name: ")
file2_q13 = input("Enter second file name to compare: ")
method_choice_q13 = input("Choose method (md5 or sha256): ").lower()

checksum1_q13 = get_checksum_q13(file1_q13, method_choice_q13)
checksum2_q13 = get_checksum_q13(file2_q13, method_choice_q13)

if checksum1_q13 and checksum2_q13:
    print("Checksum of", file1_q13, ":", checksum1_q13)
    print("Checksum of", file2_q13, ":", checksum2_q13)
    if checksum1_q13 == checksum2_q13:
        print(" Files are identical.")
    else:
        print(" Files are different.")


#QUESTION 14
import csv

print("\n--- Data Anonymizer ---")

input_file_q14 = "users.csv"
output_file_q14 = "anonymized_users.csv"

with open(input_file_q14, newline='') as infile_q14:
    reader_q14 = csv.DictReader(infile_q14)
    fieldnames_q14 = reader_q14.fieldnames
    rows_q14 = []

    for row_q14 in reader_q14:
        if "name" in row_q14:
            row_q14["name"] = "REDACTED"
        if "email" in row_q14:
            row_q14["email"] = "hidden@example.com"
        rows_q14.append(row_q14)

with open(output_file_q14, 'w', newline='') as outfile_q14:
    writer_q14 = csv.DictWriter(outfile_q14, fieldnames=fieldnames_q14)
    writer_q14.writeheader()
    writer_q14.writerows(rows_q14)

print(" Anonymized data saved to:", output_file_q14)

#QUESTION 15
import os
print("\n--- Batch File Processor ---")

folder_path_q15 = "data_files"
output_folder_q15 = "processed_files"

os.makedirs(output_folder_q15, exist_ok=True)

for filename_q15 in os.listdir(folder_path_q15):
    if filename_q15.endswith(".txt") or filename_q15.endswith(".csv"):
        input_path_q15 = os.path.join(folder_path_q15, filename_q15)
        output_path_q15 = os.path.join(output_folder_q15, filename_q15)

        with open(input_path_q15, 'r', encoding='utf-8') as file_in_q15:
            lines_q15 = file_in_q15.readlines()

        lines_lower_q15 = [line.lower() for line in lines_q15]

        with open(output_path_q15, 'w', encoding='utf-8') as file_out_q15:
            file_out_q15.writelines(lines_lower_q15)

        print("Processed:", filename_q15)

print("All .txt and .csv files have been processed to lowercase.")