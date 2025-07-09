#🔹 Section 1: List Operations (30 mins)
#QUESTION 1
def analyze_numbers():
    num = [5, 20, 16, 28, 19, 22]
    count = len(num)
    maxvalue = max(num)
    avg = sum(num) / count
    even = []
    for n in num:
        if n % 2 == 0:
            even.append(n)
    return {
        "count": count,
        "max": maxvalue,
        "average": avg,
        "even numbers": even
    }

result = analyze_numbers()
print(result)

#QUESTION 2
def clean_function():
    numb=[10, 25, 6, 8, -13, -20]
    clean=[]
    if numb is None:
        print("Numb has no value")
       
    else:
        for i in numb:
            if i>0:
                clean.append(i)
    return{
        "Cleaned list :)" : clean
    }

rest=clean_function()
print(rest)

#🔹 Section 2: Dictionary Manipulation (25 mins)
#QUESTION 3
def update_scores(students, newst, newscore):
    students[newst] = newscore
    for name in students:
        students[name] = round(students[name] * 1.10, 2)
    return students

scores = {
    "Ali": 50,
    "BabarAzam": 95
    }

updated = update_scores(scores, "Ahmed", 75)
print(updated)

#QUESTION 4
def filter_passing(student):
    revisedclean=[]
    print("\n")
    for name in student:
        if student[name] >=60:
            revisedclean.append({name:student[name]})
    
    return revisedclean
scored = {
    "Ali": 50,
    "BabarAzam": 95,
    "M.Rizwan " :45
    }
ret=filter_passing(scored)
print(ret)
#🔹 Section 3: Math and Built-in Modules (30 mins)
#Question 5
import math

def calc_shapes(r, l, w, s):
    area = math.pi * r ** 2
    perimeter = 2 * (l + w)
    volume = s ** 3

    result = {
        "Circle area": area,
        "Rectangle perimeter": perimeter,
        "Cube volume": volume
    }
    
    return result
output = calc_shapes(3, 4, 5, 2)
print(output)

#Bonus(Optional-10 mins)
nums=[8,10,2,5,7,4,11,13,15]
square=[]
for ni in nums:
    if ni%2==0:
        square.append(ni*ni)

print("The square of nums = ", square)

#Question 6
def analyze_text_file(filepath):
    with open(filepath, "r") as f:
        data = f.readlines()

def count_words_lines(text):
    word_count=len(text.split())
    line_count=len(text.splitlines())
    return word_count,line_count
