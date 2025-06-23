#QUESTION 1 DAY2
num1=float(input("Enter the first number"))
num2=float(input("Enter second number"))
print("\n--- result ---")
print("Addition",num1+num2)
if num1 > num2:
           print("Subtraction ",num1-num2)
else:
      print("Subtraction: ",num2-num1)

if num2!=0:
         print("Division: ",num1/num2)
         print("Floor division: ",num1 // num2)
         print("Modulus: ",num1%num2)
else:
       print("Division: Cannot divide by zero!")
       print("Floor Division: Cannot divide by zero!")
       print("Modulus: Cannot divide by zero!")

print("Exponentiation:", num1 ** num2)

#Question 2

num1=int(input("Enter the first Integer"))
num2=int(input("Enter the second Integer"))

print("\n----Printing Binary Reperesentation---")
print("num1 =", num1,"In Binary representation: ",bin(num1))
print("num2 =",num2,"In Binary representation: ",bin(num2))

print("\n----Printing Bit-wise----")
print("And (num1 & num2):",num1 & num2,"| Binary: ",bin(num1&num2))
print("OR (num1 | num2):",num1 | num2,"| Binary: ",bin(num1|num2))
print("XOR (num1 ^ num2):",num1 ^ num2,"| Binary: ",bin(num1^num2))

print("NOT (~num1):",~num1,"| Binary: ",bin(~num1))
print("NOT (~num2): ",~num2,"| Binary:",bin(~num2))

#left wise
print("Left shift (num1<<1)",num1<<1,"|Binary: ",bin(num1 << 1))
print("Left shift (num2<<1)",num2<<1,"|Binary: ",bin(num2 << 1))
 
#Right wise
print("Right shift (num1>>1)",num1>>1,"|Binary: ",bin(num1 >> 1))
print("Right shift  (num2>>1)",num2>>1,"|Binary: ",bin(num2 >> 1))

#QUESTION 3
expression=input("Enter an arthematic expression ")
print("\n Original expression: ", expression)
result=eval(expression)
print("The evaluated result= ",result)
print("\nNote: Python follows this precedence order:")
print("1. Parentheses ()")
print("2. Exponentiation ** (right to left)")
print("3. Multiplication *, Division /, Floor Division //, Modulus %")
print("4. Addition + and Subtraction -")

#Question 4
expression = input("Enter a expression")
result = eval(expression)
print("Result: ",result)

#QUESTION 5
print("\nTruth Table for: A and B or not C")
print("-----------------------------------")
print(" A     B     C     Result")
print("-----------------------------------")

for A in [True,False]:
   for B in [True,False]:
        for C in [True,False]:
                result = A and B or not C
                print(f"{A:<6}{B:<6}{C:<6}{result}")

#Question 6
print("Enter 3 numbers:")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

nums =[a,b,c]
print("\nA\tB\t==\t!=\t<\t>")
print("---------------------------------------------")

for x in nums:
       for y in nums:
              print(x, "\t", y, "\t", x == y, "\t", x != y, "\t", x < y, "\t", x > y)

#Question 7
x=int(input("Enter a starting number"))
print("Starting value of x: ",x)

x+=5
print("After x+=5: x")

x-=2
print("After x-=2: ",x)

x*=3
print("After x*=3: ", x)

x/=2
print("Print x/=2: ",x)

x //= 2
print("After x //= 2: ", x)

x %= 4
print("After x %= 4:", x)

x **= 2
print("After x **= 2:", x)

#Question 8
print("Comparing strings:")
str1 = "hello"
str2 = "hello"
print("str1 == str2:", str1 == str2) #equality check
print("str1 is str2", str1 is str2)#memory check
print("id(str1):", id(str1))
print("id(str2):", id(str2))

print("Comparing integers:")
x = 100
y = 100
print("x == y:", x == y)              
print("x is y:", x is y)                
print("id(x):", id(x))
print("id(y):", id(y))
print()

print("Comparing lists:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2:", list1 == list2) 
print("list1 is list2:", list1 is list2)  
print("id(list1):", id(list1))
print("id(list2):", id(list2))
print()

print("Assigning same list:")
list3 = list1
print("list1 == list3:", list1 == list3)  
print("list1 is list3:", list1 is list3)  
print("id(list1):", id(list1))
print("id(list3):", id(list3))

#QUESTION 9
my_string = "hello world"
my_list = [1, 2, 3, 4, 5]
my_set = {10, 20, 30}
my_dict = {"name": "Ali", "age": 20, "city": "Lahore"}

userinp = input("Enter something to check membership: ")
print("\n--- Membership Check ---")
print("In String:", userinp in my_string)
print("Not in String:", userinp not in my_string)

try:
      user_number = int(userinp)
      print("In List:", user_number in my_list)
      print("Not in List:", user_number not in my_list)
except:
       print("In List: False (input is not a number)")
       print("Not in List: True")

try:
    user_number = int(userinp)
    print("In Set:", user_number in my_set)
    print("Not in Set:", user_number not in my_set)
except:
    print("In Set: False (input is not a number)")
    print("Not in Set: True")

print("In Dictionary (keys):", userinp in my_dict)
print("Not in Dictionary (keys):", userinp not in my_dict)

#Question 10
def check_a():
      print("Running check_A")
      return False

def check_b():
      print("Running check_B")
      return True

print("\nTesting AND (check_A and check_B):")
if check_a() and check_b():
      print("Both are True")
else:
      print("At least one is False")

print("\nTesting OR (check_B or check_A):")
if check_b() or check_a():
    print("At least one is True")
else:
    print("Both are False")

#QUESTION 11
import cmath
num1 = complex(input("Enter first complex number: "))
num2 = complex(input("Enter second complex number: "))
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2
print("\n--- Standard Form ---")
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)
print("\n--- Polar Form ---")
print("First number polar:", cmath.polar(num1))
print("Second number polar:", cmath.polar(num2))

#QUESTION 12
print("Enter numbers like 1.5e4 (which means 15000)")

num1 = float(input("Enter first number: "))  
num2 = float(input("Enter second number: ")) 
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Cannot divide by zero"

print("\n--- Normal Results ---")
print("Sum:", sum_result)
print("Difference:", sub_result)
print("Product:", mul_result)
print("Division:", div_result)

print("\n--- Scientific Results ---")
print("Sum: {:.2e} ".format(sum_result) )
print("Difference: {:.2e} ".format(diff_result))
print("Product: {:.2e}".format(prod_result))
print("Division: {:.2e}".format(div_result))
print("Product: {:.2e}".format(mul_result))  

if isinstance(div_result, float):  # only format if it's a number
    print("Division: {:.2e}".format(div_result))
    print("Type of vaiable",type(div_result))
else:
    print("Division:", div_result)
    print("Type of vaiable",type(div_result))
    
#QUESTION 13
a = 0.1
b = 0.2
c = a + b
print("Normal float result (0.1 + 0.2):", c)
print("Using round function",round(c,2))
from decimal import Decimal
x= Decimal('0.1')
y= Decimal('0.2')
print(x+y)

#QUESTION 14
import sys
a=10*100
b = 99999999999999999999999999999999999999999
sum_result = a + b
product_result = a * b
print("Big number A:", a)
print("Big number B:", b)
print("\nSum:", sum_result)
print("Product:", product_result)

print("\nsys.maxsize: ",sys.maxsize)
print("Is A > sys.maxsize?", a > sys.maxsize)

#QUESTION 15
print("=== Clock Time Calculator ===")

current_hour = int(input("Enter current hour (0-23): "))

add_hours = int(input("How many hours to add? "))

new_hour = (current_hour + add_hours) % 24

print("Time after", add_hours, "hours will be:", new_hour, ":00")

#QUESTION 16
import timeit
import math
base = 2
exponent = 100
def power_pow():
    result = pow(base, exponent)
    return result
def power_star():
    result = base ** exponent
    return result
def power_math_pow():
    result = math.pow(base, exponent)
    return result

print("Timing for each method:")

time1=timeit.timeit(power_pow,number=100000)
print("Using ** :", time1)

time2 = timeit.timeit(power_pow, number=100000)
print("Using pow():", time2)

time3 = timeit.timeit(power_math_pow, number=100000)
print("Using math.pow():", time3)

#QUESTION 17
a = 7
b = 3

print("=== Positive Numbers ===")
print("a / b =", a / b)    #
print("a // b =", a // b)  
print("a % b =", a % b)    

a = -7
b = 3

print("\n=== Negative Numerator ===")
print("a / b =", a / b)    
print("a // b =", a // b)  
print("a % b =", a % b)    

a = 7
b = -3

print("\n=== Negative Denominator ===")
print("a / b =", a / b)    
print("a // b =", a // b)  
print("a % b =", a % b)    

a = -7
b = -3

print("\n=== Both Negative ===")
print("a / b =", a / b)    
print("a // b =", a // b)  
print("a % b =", a % b)    

#Question 18
print(f"{'A':<6}{'B':<6}{'AND':<8}{'OR':<8}{'XOR':<8}{'NOT A'}")

for A in [False,True]:
   for B in [False,True]:
     andresult=A and B
     orresult=A or B
     xorresult=A^B
     notresult= not A
     print(f"{A:<6}{B:<6}{andresult:<8}{orresult:<8}{xorresult:<8}{notresult}")

#QUESTION 19
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
d_input = input("Enter value for d (True/False): ")
if d_input.lower() == "true":
    d = True
else:
    d = False

print(f"\nEvaluating: {a}+{b}>{c} and not {d}")

step1=a+b
print(f"\n Printing step1=a+b {step1}")

step2=step1>c
print(f"Step 2: {step1} > {c} → {step2}")

step3=not d
print(f"Step 3: not {d} → {step3}")

finalresult=step2 and step3
print(f"Step 4: {step2} and {step3} → {finalresult}")

print(f"\nFinal Result: {finalresult}")

#QUESTION 20
import timeit
import math
x = 123
y = 456

def arth():
     return x+y
def bitwise():
     return x&y
def powerstar():
     return x**y
def powmath():
     return math.pow(x,5)

print("ADDITION= ",timeit.timeit(arth,number=100000))
print("BITWISE= ",timeit.timeit(bitwise,number=100000))
print("Powerstar= ",timeit.timeit(powerstar,number=100000))
print("Powermath= ",timeit.timeit(powmath,number=100000))
     



      


      



              





