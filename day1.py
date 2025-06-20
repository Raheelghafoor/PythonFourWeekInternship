print("Hello world")     #Question 1   # a. simple print

message="Hello ahmed!"   #b. print with variable
print(message)  

name="Wor"             #c. print f string
print(f"Hello, {name}!")  

print("Hello,{}!".format("Ahmed"))  #d. print format

greet= "Hello"               #e. Concatenation
target="W"
print(greet + ", " + target + "!")

print("""I love 
cricket""") #f. Multistring

def say_hello():      #g. FUNCTIONS
    print("how are you")

    say_hello()

word=["Tom","Cruise"]       #h. list(array)
print(word[0]+", "+word[1])

colour=input("Enter your favourite colour: ") #i. Input from user
food=input("Enter your favourite food: ")
print(colour+", "+food+ " :)")

with open("hello.txt","r") as file:
    message = file.read()                     #j. File reading
    print(message)







#Question 2 Personal Information Manager

fullname=input("Enter your full name: ")
age=input("Enter the age: ")
address = input("Enter the address: ")
email = input("Enter your email: ")

print("\n---------Personal Information------------------")
print(f"Name  :{fullname}")
print(f"Age: {age}")
print (f"address: {address}")
print(f"email: {email}")
print("-------------------------------------------------")


#QUESTION 3 Data Type Explorer and Converter

value = input("Enter Something: ")
print("You entered ", value)
print("Original data type: ",type(value))

try:
    int_value = int(value)
    print("As integer:", int_value)
except:
    print("Can't convert to integer.")

try:
    float_value=float(value)
    print("As a float",float_value)
except:
    print("Can't convert to float.")

str_value = str(value)
print("As string:", str_value)




#QUESTION 4 Variable Scope Demonstrator

message="I am a global variable"
def outer_function():
    message="I am a global variable"

    def inner_function():
        message="I am local to inner function"
        print("Inside inner function:",message)
      
    inner_function()

print("Insider outer_function: ",message)
outer_function()
print("Back in global scope:", message)




#QUESTION 5 Memory Address Tracker

num = 10
text = "Hello"
items = [1, 2, 3]

print("""
      
      Initialize memory addresses: """)
print("num", id(num))
print("text",id(text))
print("items",id(items))

num = 20
text = "World"
items.append(4)
print("\nAfter modifying values:")
print("num:", id(num))    
print("text:", id(text))  
print("items:", id(items)) 




# QUESTION 6: Type Checking Utility

user_input = input("\n\nEnter something: ")

if user_input.lower() == "true":
    value = True
elif user_input.lower() == "false":
    value = False
else:
    try:
        value = int(user_input)
    except:
        try:
            value = float(user_input)
        except:
            value = user_input

print("\nType Checking Result:")
if isinstance(value, bool):
    print("You entered a Boolean value:", value)
elif isinstance(value, int):
    print("You entered an Integer number:", value)
elif isinstance(value, float):
    print("You entered a Float number:", value)
elif isinstance(value, str):
    print("You entered a String:", value)


# QUESTION 7: Dynamic Typing Examples

var = 10
print("\nAssigned int:")
print("Value:", var)
print("Type:", type(var))

var = "Hello"
print("\nAssigned string:")
print("Value:", var)
print("Type:", type(var))

var = [1, 2, 3]
print("\nAssigned list:")
print("Value:", var)
print("Type:", type(var))

var = 3.14
print("\nAssigned float:")
print("Value:", var)
print("Type:", type(var))

#QUESTION 8 Variable Naming Validator

import keyword  

var_name = input("Enter a variable name: ")

if var_name.isidentifier():
    print(" It is a valid Python identifier.")
else:
    print("It is invalid Python identifier.")


if keyword.iskeyword(var_name):
    print(" a Python keyword (cannot be used as a variable name).")
else:
    print("not a Python keyword.")


# QUESTION 9: Constants Simulator
PI=3.14
G=9.81
MAX_USERS=100
print("PI:", PI)
print("GRAVITY OF EARTH:", G)
print("MAX_USERS:", MAX_USERS)

#QUESTION 10: Unicode and Encoding Handler

text = input("Enter a string: ")

encoded_text = text.encode('utf-8')
print("\nEncoded in UTF-8 (bytes):", encoded_text)

decoded_text = encoded_text.decode('utf-8')
print("Decoded back to string:", decoded_text)

print("\nUnicode code points:")
for char in text:
    print(f"'{char}' → U+{ord(char):04X}")


#QUESTION 11: Number System Conversion
decimal = int(input("Please enter a decimal"))
print("\nNumber System Conversions:")
print("Binary      :", bin(decimal))      
print("Octal       :", oct(decimal))      
print("Hexadecimal :", hex(decimal)) 

#QUESTION 12: BOOLEAN EXPRESSION TABLE DLD 
a_input = input("Enter first boolean value (True/False): ")
b_input = input("Enter second boolean value (True/False): ")

a = a_input.strip().lower() == "true"
b = b_input.strip().lower() == "true"

print("\nTruth Table Results:")
print(f"A       : {a}")
print(f"B       : {b}")
print(f"A AND B : {a and b}")
print(f"A OR B  : {a or b}")
print(f"NOT A   : {not a}")
print(f"NOT B   : {not b}") 
print(f"A XOR B : {a ^ b}")

#QUESTION 13: None Value Handler
def getvalidname(name):
    if name.strip() =="": 
        return None 
    else: return name


user_input = input("Enter your name: ")
result = getvalidname(user_input)
if result is None:
    print("You didn't enter a valid name.")
else:
    print("Welcome,", result + "!")


#QUESTION 14: Garbage Collection Observer

import gc  


gc.enable()

print("Garbage collection is enabled.")


print("\nTracked objects BEFORE creating custom objects:", len(gc.get_objects()))


class MyObject:
    def __init__(self, name):
        self.name = name

obj1 = MyObject("Object 1")
obj2 = MyObject("Object 2")


obj1.other = obj2
obj2.other = obj1


objects = [obj1, obj2]

print("Created objects.")


print("\nTracked objects AFTER creation:", len(gc.get_objects()))


del obj1
del obj2
del objects

print("Deleted references to objects.")
collected = gc.collect()

print("\n  Garbage collection forced.")
print("Number of unreachable objects collected:", collected)


print("Tracked objects AFTER garbage collection:", len(gc.get_objects()))

#QUESTION 15:  Performance Timing Utility
import time
import random

numbers = random.sample(range(1, 1000), 100)

def built_in_sort(data):
    return sorted(data)
 
def bubble_sort(data):
    data = data.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

#BUILT in sort time
start = time.time()
built_in_result = built_in_sort(numbers)
end = time.time()
print("Built-in sort time:", end - start, "seconds")

#bubble sort time
start = time.time()
bubble_result = bubble_sort(numbers)
end = time.time()
print(" Bubble sort time   :", end - start, "seconds")




















