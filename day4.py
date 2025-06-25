#QUESTION 1
while True:
    try:
        totalmarks = float(input("Please Enter Total Marks (> 0): "))
    except ValueError:
        print("Invalid input. Please enter a number for total marks.")
        continue

    if totalmarks <= 0:
        print("Total marks must be greater than zero. Try again.")
    else:
        break

while True:
    try:
        marks = float(input(f"Please Enter Marks (0 – {totalmarks}): "))
    except ValueError:
        print("Invalid input. Please enter a number for marks.")
        continue

    if marks < 0:
        print("Marks cannot be negative. Try again.")
    elif marks > totalmarks:
        print(f"Marks cannot exceed total marks ({totalmarks}). Try again.")
    else:
        break

percentage=(marks/totalmarks) *100
print(f"Percentage: {percentage:.2f}%")
if percentage <=100 and percentage >=0:
     if percentage>=90:
               print("A*")
     elif percentage>=80:
               print("A")
     elif percentage>=70:
               print("B")
     elif percentage>=60:
               print("C")
     elif percentage>=50:
               print("D")
     else:
       print("F")
else:
      print("Invalid Percentage! Please Check the Marks Entered!")

#QUESTION 2
#THE RANGE ON WHICH TAX IS APPLIED MEANS BELOW 600000 NO TAX IS APPLIED IT CAN ONLY BE APPLIED 
#ONLY ABOVE 600,000 TO SPECIFIED INCOME
#Income Range (PKR)	    Tax Rate
#0 – 600,000	        0% (No tax)
#600,001 – 1,200,000	5%
#1,200,001 – 1,800,000	10%
#1,800,001 – 2,500,000	15%
#Above 2,500,000	    20%
while True:
    try:
        income = float(input("Enter your annual income in PKR (>= 0): "))
    except ValueError:
        print("Invalid input. Please enter a number for income.")
        continue

    if income < 0:
        print("Income cannot be negative. Try again.")
    else:
        break

def get_slab(income):
    if income <= 600000:
        return "slab0"
    elif income <= 1200000:
        return "slab1"
    elif income <= 1800000:
        return "slab2"
    elif income <= 2500000:
        return "slab3"
    else:
        return "slab4"

match get_slab(income):
      case "slab0":
            tax=0
      case "slab1":
               tax = (income - 600000) * 0.05
      case "slab2":
               tax=(600000*0.05)+(income - 1200000) * 0.10
      case "slab3":
              tax = (600000 * 0.05) + (600000 * 0.10) + (income - 1800000) * 0.15
      case "slab4":
               tax = (600000 * 0.05) + (600000 * 0.10) + (700000 * 0.15) + (income - 2500000) * 0.20

print("Your calculated tax is: PKR", round(tax, 2))


#QUESTION 3
while True:
    try:
        age = int(input("Enter your age (0–150): "))
    except ValueError:
        print("Please enter an integer for age.")
        continue

    if age < 0:
        print("Age cannot be negative. Try again.")
    elif age > 150:
        print("Age seems too high. Try again.")
    else:
        break

while True:
    try:
        salary = float(input("Enter your monthly salary (PKR): "))
    except ValueError:
        print("Please enter a valid number for salary.")
        continue

    if salary < 0:
        print("Salary cannot be negative. Try again.")
    else:
        break
while True:
    try:
        credit_score = int(input("Enter your credit score (300–850): "))
    except ValueError:
        print("Please enter an integer for credit score.")
        continue

    if credit_score < 300 or credit_score > 850:
        print("Credit score must be between 300 and 850. Try again.")
    else:
        break
if not (21 <= age <= 60):
    print("You are NOT eligible because your age is not within 21–60.")
elif salary < 30_000:
    print("You are NOT eligible because your monthly salary is below PKR 30,000.")
elif credit_score < 650:
    print("You are NOT eligible because your credit score is too low.")
elif credit_score < 750:
    print("You’re eligible for a Standard Loan.")
else:
    print("Congratulations! You’re eligible for a Premium Loan.")

#QUESTION 4
while True:
    try:
        a = int(input("Enter your age (0–100): "))
    except ValueError:
        print("Please enter a valid integer for age.")
        continue

    if a < 0 or a > 150:
        print("Age must be between 0 and 150. Try again.")
    else:
        break

while True:
     health=input("Enter your health condition (good / average / poor): ").strip().lower()
     if health not in ["good","average","poor"]:
          print("Please enter one of: good, average, poor.")
     else:
          break

while True:
     location = input("Enter your location (urban / rural): ").strip().lower()
     if location not in ["urban", "rural"]:
         print("Please enter either 'urban' or 'rural'.")
     else:
         break

base_premium = 10_000
premium = base_premium
if a < 25:
    premium += base_premium * 0.20
elif a > 60:
    premium += base_premium * 0.30
#No premium on good health its 0 
if health == "average":
    premium += base_premium * 0.15
elif health == "poor":
    premium += base_premium * 0.30

if location == "rural":
    premium -= base_premium * 0.10
print(f"\nYour calculated insurance premium is: PKR {premium:,.2f}")


#QUESTION 5
while True:
     try:
          money=float(input("Enter your total purchase (PKR): "))
     except ValueError:
           print("Invalid input. Please enter a number.")
           continue
     if money < 0:
      print("Purchase amount cannot be negative. Try again.")
     else:
        break
if money>=50000:
     discount=30
elif money>= 20000:
     discount=20
elif money>5000:
     discount=10
else:
     discount=0
per=money*(discount/100) 
final=money-per
print(f"\nOriginal Amount      : PKR {money:,.2f}")
print(f"Discount Percentage  : {discount}%")
print(f"Discount Amount      : PKR {per:,.2f}")
print(f"Final Amount to Pay  : PKR {final:,.2f}")

#QUESTION 6
while True:
    try:
        ag = int(input("Enter your age (0–150): "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if ag < 0 or ag > 150:
        print("Age must be between 0 and 150. Try again.")
    else:
        break

if ag <= 2:
    category = "Baby"
elif ag <= 12:
    category = "Child"
elif ag <= 19:
    category = "Teen"
elif ag <= 59:
    category = "Adult"
else:
    category = "Senior"

print(f"You are classified as: **{category}**.")

#QUESTION 7
import string
special_characters = string.punctuation
password= input("Enter Password")
length_ok = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_symbol = any(char in special_characters for char in password)
print("\nPassword Strength Check:")
if all([length_ok, has_digit, has_upper, has_lower, has_symbol]):
    print("Strong password.")
else:
    print("Weak password. Please ensure the following:")
    if not length_ok:
        print("- At least 8 characters long")
    if not has_digit:
        print("- At least 1 digit")
    if not has_upper:
        print("- At least 1 uppercase letter")
    if not has_lower:
        print("- At least 1 lowercase letter")
    if not has_symbol:
        print("- At least 1 special character (e.g. !, @, #, $)")

#QUESTION 8
while True:
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if weight <= 0:
        print("Weight must be greater than 0.")
    else:
        break
while True:
    try:
        height = float(input("Enter your height in meters (m): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if height <= 0:
        print("Height must be greater than 0.")
    else:
        break

bmi=weight/(height**2)
print(f"\nYour BMI is: {bmi:.2f}")
if bmi < 18.5:
    print(" You are underweight. Consider eating a balanced diet and consulting a healthcare provider.")
elif bmi < 25:
    print(" You have a normal weight. Maintain a healthy lifestyle!")
elif bmi < 30:
    print(" You are overweight. Consider exercise and healthier food choices.")
else:
    print(" You are in the obese range. It is recommended to seek medical and nutritional guidance.")




#QUESTION 9
print("Available Time Zones:")
print("1. UTC (0)")
print("2. PST (+5)")
print("3. EST (-5)")
print("4. CET (+1)")
zones = {
    "UTC": 0,
    "PST": 5,
    "EST": -5,
    "CET": 1
}
while True:
    try:
        value = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
        continue  

    if value < 0:
        print("Negative not allowed.")
    else:
        break

from_zone = input("Enter source time zone (UTC / PST / EST / CET): ").upper().strip()
to_zone = input("Enter target time zone (UTC / PST / EST / CET): ").upper().strip()

if from_zone in zones and to_zone in zones:
     offset=zones[to_zone] - zones[from_zone]
     new_time=(value+offset)%24
     print(f"\nTime in {from_zone}: {value}:00")
     print(f"Time in {to_zone}: {new_time}:00")
else:
       print("Invalid time zone entered.")


#QUESTION 10
while True:
    try:
        temp = float(input("Enter temperature in °C: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
while True:
    try:
        humidity = float(input("Enter humidity percentage (0–100): "))
        if 0 <= humidity <= 100:
            break
        else:
            print("Humidity must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        wind = float(input("Enter wind speed in km/h: "))
        if wind >= 0:
            break
        else:
            print("Wind speed cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a number.")
print("\nWeather Advisory:")

if temp > 40:
    print("- Extreme heat! Avoid going out and stay hydrated.")
elif temp < 5:
    print("- It's very cold. Wear warm clothes.")

if humidity > 80:
    print("- High humidity! You may feel sticky.")
elif humidity < 30:
    print("- Air is dry. Stay moisturized and drink water.")

if wind > 40:
    print("- Strong winds! Be careful outdoors.")
elif wind < 5:
    print("- Calm wind. Nice and still weather.")

if humidity > 70 and temp < 35:
    print("- You might want to carry an umbrella.")


#Question 11
while True:
    try:
        speed = float(input("Enter your vehicle speed (km/h): "))  
        if speed < 0:
            print("Speed cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
speed_limit = 80
print(f"\nSPEED LIMIT:-  {speed_limit} Km/h")
if speed <= speed_limit:
    print(" No violation. You are within the speed limit :)")
else:
    over_speed =  speed - speed_limit
    print(f" Over-speeding by {over_speed:.1f} km/h.")
    if over_speed <= 10:
        fine = 500
    elif over_speed <= 20:
        fine = 1500
    elif over_speed <= 40:
        fine = 3000
    else:
        fine = 5000
     
    print(f"Fine to pay: PKR {fine}")

#QUESTION 12
while True:
     try:
         score = int(input("Enter your credit score (300–850): "))
         if 300 <= score <= 850:
                break
         else:
                print("Credit score must be between 300 and 850.")
     except ValueError:
                print("Invalid input. Please enter a whole number.") 
if score >= 800:
    status = "Excellent"
elif score >= 740:
    status = "Very Good"
elif score >= 670:
    status = "Good"
elif score >= 580:
    status = "Fair"
else:
    status = "Poor"

print(f"\nYour credit score is {score}.")
print(f"Status: {status}")

#QUESTION 13
while True:
    try:
        ages = int(input("Enter your age: "))
        if 0 < ages <= 100:
            break
        else:
            print("Age must be between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
while True:
    try:
        incomes= float(input("Enter your monthly income in PKR: "))
        if incomes >= 0:
            break
        else:
            print("Income cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
while True:
    invtype = input("Enter investment type (stocks / bonds / real-estate): ").strip().lower()
    if invtype in ["stocks", "bonds", "real-estate"]:
        break
    else:
        print("Please choose from: stocks, bonds, or real-estate.")

if invtype == "stocks":
    if ages < 30 and incomes > 100000:
        risk = "High"
    elif ages < 50:
        risk = "Medium"
    else:
        risk = "High"
elif invtype == "real-estate":
    if incomes >= 50000:
        risk = "Medium"
    else:
        risk = "High"
elif invtype == "bonds":
    if ages > 50 or incomes < 30000:
        risk = "Low"
    else:
        risk = "Medium"

#QUESTION 14
print("\n********Medical Inquiries********")
print("\nPlease answer the following questions")
def get_response(question):
       while True:
           response=input(question).strip().lower()
           if response in["yes","no"]:
               return response
           else:
               print("Invalid response. Please type 'yes' or 'no'.")

fever = get_response("Do you have fever? ")
cough = get_response("Do you have cough? ")
fatigue = get_response("Are you feeling fatigued? ")
headache = get_response("Do you have a headache? ")
sore_throat = get_response("Do you have a sore throat? ")

print("\n******** Diagnosis Suggestion ********")
if fever == "yes" and cough == "yes" and fatigue == "yes":
    print("- You may have the flu. Rest and stay hydrated.")
elif sore_throat == "yes" and headache == "yes":
    print("- It could be a common cold. Consider seeing a doctor if symptoms persist.")
elif fever == "yes" and cough == "yes" and sore_throat == "yes":
    print("- Symptoms may match COVID-19. Consider getting tested.")
elif fatigue == "yes" and headache == "yes":
    print("- Could be due to stress or lack of sleep. Try to rest and hydrate.")
else:
    print("- Symptoms are unclear. Please consult a healthcare provider for proper diagnosis.")

#QUESTION 15
print("\n******** Smart Home Controller ********")
while True:
    try:
        temperatures = float(input("Enter room temperature (°C): "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        tame = int(input("Enter current hour (0–23): "))
        if 0 <= tame <= 23:
            break
        else:
            print("Hour must be between 0 and 23.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
while True:
    presence = input("Is someone in the room? (yes / no): ").strip().lower()
    if presence in["yes","no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")

print("\n******** Device Actions ********")
if temperatures > 30 and presence == "yes":
    print("- AC: Turned ON (it's hot and someone is home)")
else:
    print("- AC: Turned OFF")

if (tame >= 19 or tame <= 5) and presence == "yes":
    print("- Lights: Turned ON (it's dark and someone is home)")
else:
    print("- Lights: Turned OFF")
if temperatures > 24 and presence == "yes":
    print("- Fan: Turned ON (warm temperature)")
else:
    print("- Fan: Turned OFF")

#QUESTION 16
print("\n******** E-commerce Price Calculator ********")
while True:
    try:
        base_price = float(input("Enter product base price (PKR): "))
        if base_price < 0:
            print("Price cannot be negative.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
tax_rate = 0.10
tax_amount = base_price * tax_rate
if base_price >= 50000:
    discount_percent = 20
elif base_price >= 20000:
    discount_percent = 10
elif base_price >= 5000:
    discount_percent = 5
else:
    discount_percent = 0
discount_amount = base_price * (discount_percent / 100)
if base_price >= 30000:
    shipping_fee = 0
else:
    shipping_fee = 500
final_price = base_price + tax_amount - discount_amount + shipping_fee
print("\n******** Invoice ********")
print(f"Base Price         : PKR {base_price:,.2f}")
print(f"Tax (10%)          : PKR {tax_amount:,.2f}")
print(f"Discount ({discount_percent:>2}%)     : -PKR {discount_amount:,.2f}")
print(f"Shipping Fee       : PKR {shipping_fee:,.2f}")
print(f"-------------------------------")
print(f"Final Amount       : PKR {final_price:,.2f}")
print("\nThank you for shopping with us!")

#QUESTION 17
while True:
    try:
        grade = float(input("Enter your academic percentage (0–100): "))
        if 0 <= grade <= 100:
            break
        else:
            print("Percentage must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        test_score = float(input("Enter your entrance test score (0–100): "))
        if 0 <= test_score <= 100:
            break
        else:
            print("Test score must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    extra = input("Have you participated in extracurricular activities? (yes / no): ").strip().lower()
    if extra in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")
print("\n******** Admission Result ********")

if grade >= 85 and test_score >= 70:
    print(" You are eligible for admission (Merit Based).")
elif grade >= 70 and test_score >= 60 and extra == "yes":
    print(" You are eligible for admission (With Extracurricular Support).")
else:
    print(" Sorry, you are not eligible for admission at this time.")

#QUESTION 18
print("\n******** Employee Performance Evaluator ********")
while True:
    try:
        punctuality = float(input("Enter punctuality score (0–10): "))
        if 0 <= punctuality <= 10:
            break
        else:
            print("Punctuality must be between 0 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        tasks = float(input("Enter tasks completed percentage (0–100): "))
        if 0 <= tasks <= 100:
            break
        else:
            print("Percentage must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        feedback = float(input("Enter peer feedback score (0–5): "))
        if 0 <= feedback <= 5:
            break
        else:
            print("Feedback must be between 0 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")
print("\n******** Performance Rating ********")

if punctuality >= 9 and tasks >= 90 and feedback >= 4.5:
    rating = "Excellent"
elif punctuality >= 7 and tasks >= 75 and feedback >= 3.5:
    rating = "Good"
elif punctuality >= 5 and tasks >= 60 and feedback >= 2.5:
    rating = "Satisfactory"
else:
    rating = "Needs Improvement"

print(f"Your performance rating is: **{rating}**")

#QUESTION 19
print("\n******** Budget Category Advisor ********")
while True:
    try:
        income = float(input("Enter your monthly income (PKR): "))
        if income >= 0:
            break
        else:
            print("Income cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        expenses = float(input("Enter your monthly expenses (PKR): "))
        if expenses >= 0:
            break
        else:
            print("Expenses cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a number.")
savings = income - expenses
if savings >= income * 0.30:
    category = "High Budget (Good financial health)"
elif savings >= income * 0.10:
    category = "Medium Budget (Stable but monitor spending)"
else:
    category = "Low Budget (Caution: Expenses too high)"

if "Low Budget" in category:
    print("- Tip: Try reducing unnecessary expenses or increase income sources.")

print("\n******** Budget Summary ********")
print(f"Income   : PKR {income:,.2f}")
print(f"Expenses : PKR {expenses:,.2f}")
print(f"Savings  : PKR {savings:,.2f}")
print(f"Budget Category    : {category}")

#QUESTION 20
print("\n******** Gaming Progression System ********")
def response_get(prompt):
  while True:
    resp=input(prompt + " (yes/no)").strip().lower()
    if resp in ["yes","no"]:
        return resp
    else:
        print("Please enter 'yes' or 'no'.")

mission_complete = response_get("Have you completed all main missions?")
side_quests_done = response_get("Have you completed at least 5 side quests?")
has_required_xp = response_get("Do you have the required XP to level up?")
collected_item = response_get("Have you collected the special item?")
boss_defeated = response_get("Have you defeated the current boss?")
print("\n******** Level Up Evaluation ********")

if mission_complete == "yes" and has_required_xp == "yes" and boss_defeated == "yes":
    print(" You qualify for level up!")
    if side_quests_done == "yes" and collected_item == "yes":
        print(" Bonus unlocked for completing optional challenges!")
else:
    print(" You cannot level up yet. Complete all required tasks.")
    if mission_complete != "yes":
        print("- Main missions incomplete.")
    if has_required_xp != "yes":
        print("- Not enough XP.")
    if boss_defeated != "yes":
        print("- Boss not defeated.")


#QUESTION 21
print("\n******** Shipping Cost Optimizer ********")
while True:
    try:
        weigh = float(input("Enter package weight (kg): "))
        if weigh > 0:
            break
        else:
            print("Weight must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    locat= input("Enter destination (local / national / international): ").strip().lower()
    if locat in ["local", "national", "international"]:
        break
    else:
        print("Please enter 'local', 'national', or 'international'.")
while True:
    speeds = input("Enter delivery speed (standard / express): ").strip().lower()
    if speeds in ["standard", "express"]:
        break
    else:
        print("Please enter 'standard' or 'express'.")

if locat == "local":
    base_cost = 100
elif locat == "national":
    base_cost = 200
else:  
    base_cost = 500

if weigh <= 1:
    weight_cost = 50
elif weigh <= 5:
    weight_cost = 100
else:
    weight_cost = 200
speed_cost = 0
if speeds == "express":
    speed_cost = 150
total_cost = base_cost + weight_cost + speed_cost
print("\n******** Shipping Summary ********")
print(f"Destination        : {locat.title()}")
print(f"Delivery Speed     : {speeds.title()}")
print(f"Package Weight     : {weigh:.1f} kg")
print(f"Base Cost          : PKR {base_cost}")
print(f"Weight Surcharge   : PKR {weight_cost}")
print(f"Speed Surcharge    : PKR {speed_cost}")
print(f"-------------------------------")
print(f"Total Shipping Cost: PKR {total_cost}")

#QUESTION 22
print("\n******** Energy Consumption Analyzer ********")
while True:
    try:
        usage = float(input("Enter your daily energy usage (in kWh): "))
        if usage >= 0:
            break
        else:
            print("Energy usage cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
if usage <= 10:
    categ = "Efficient (Low usage – great job conserving energy!)"
elif usage <= 30:
    categ= "Average (Moderate usage – consider minor improvements)"
else:
    categ = "Overuse (High usage – consider reducing consumption)"
print("\n******** Energy Usage Summary ********")
print(f"Daily Usage       : {usage:.2f} kWh")
print(f"Consumption Level : {categ}")


#QUESTION 23
print("\n******** Diet Recommendation System ********")

while True:
    try:
        aged = int(input("Enter your age: "))
        if 0 < aged <= 120:
            break
        else:
            print("Please enter a valid age (1–120).")
    except ValueError:
        print("Invalid input. Please enter a whole number.") 
while True:
    try:
        bmis = float(input("Enter your Body Mass Index (BMI): "))
        if bmis > 0:
            break
        else:
            print("BMI must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    activity = input("Enter your activity level (low / moderate / high): ").strip().lower()
    if activity in ["low", "moderate", "high"]:
        break
    else:
        print("Please choose from: low, moderate, or high.")
while True:
    preference = input("Enter your dietary preference (vegetarian / non-vegetarian / vegan): ").strip().lower()
    if preference in ["vegetarian", "non-vegetarian", "vegan"]:
        break
    else:
        print("Please choose from: vegetarian, non-vegetarian, or vegan.")
print("\n******** Diet Recommendation ********")
if bmis < 18.5:
    diet_type = "High-calorie"
    advice = "Focus on nutrient-dense foods like nuts, dairy, whole grains, and legumes."
elif bmis <= 24.9:
    diet_type = "Balanced"
    advice = "Maintain your current diet with a mix of fruits, veggies, protein, and healthy fats."
else:
    diet_type = "Low-calorie"
    advice = "Emphasize fruits, vegetables, lean protein, and reduce processed carbs and fats."

if activity == "high":
    advice += " Increase protein intake to support muscle recovery."
elif activity == "low":
    advice += " Reduce portion sizes and avoid high-sugar snacks."

if preference == "vegan":
    advice += " Ensure you're getting enough B12, iron, and plant-based protein."
elif preference == "vegetarian":
    advice += " Include dairy, legumes, and leafy greens for balanced nutrition."
elif preference == "non-vegetarian":
    advice += " Choose lean meats and limit red meat for heart health."
if aged < 30:
    age_group = "Young"
elif aged <= 60:
    age_group = "Adult"
else:
    age_group = "Senior"
print(f"Diet Type         : {diet_type}")
print(f"Age Group         : {age_group}")
print(f"Dietary Advice    : {advice}")

#QUESTION 24
print("\n******** Exercise Intensity Calculator ********")
while True:
    try:
        ageded = int(input("Enter your age: "))
        if 10 <= ageded <= 100: #AGE STARTS WITH 10 AS ITS UNREALISTIC FOR A SMALL CHILD BELOW 10 TO DO EXCERCISE
            break
        else:
            print("Please enter a valid age (10–100).")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
while True:
    try:
        heart_rate = int(input("Enter your current heart rate (bpm): "))
        if 30 <= heart_rate <= 200:
            break
        else:
            print("Please enter a realistic heart rate (30–200 bpm).")
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    fitness = input("Enter your fitness level (beginner / intermediate / advanced): ").strip().lower()
    if fitness in ["beginner", "intermediate", "advanced"]:
        break
    else:
        print("Please choose: beginner, intermediate, or advanced.")
max_heart_rate = 220 - ageded
if fitness == "beginner":
    target_low = int(max_heart_rate * 0.5)
    target_high = int(max_heart_rate * 0.6)
    intensity = "Low Intensity"
elif fitness == "intermediate":
    target_low = int(max_heart_rate * 0.6)
    target_high = int(max_heart_rate * 0.75)
    intensity = "Moderate Intensity"
else:  
    target_low = int(max_heart_rate * 0.75)
    target_high = int(max_heart_rate * 0.9)
    intensity = "High Intensity"
if heart_rate < target_low:
    zoned = "Below target zone – Warm up more."
elif heart_rate > target_high:
    zoned = "Above target zone – Slow down to avoid overexertion."
else:
    zoned = "Within target zone – Keep it up!"
print("\n******** Workout Recommendation ********")
print(f"Age                  : {ageded}")
print(f"Fitness Level        : {fitness.title()}")
print(f"Max Heart Rate       : {max_heart_rate} bpm")
print(f"Recommended Intensity: {intensity}")
print(f"Target HR Zone       : {target_low}–{target_high} bpm")
print(f"Current HR Feedback  : {zoned}")

#QUESTION 25
print("\n******** Smart Scheduling Assistant ********")
def get_yes_no(prompt):
    while True:
        ans = input(prompt + " (yes/no): ").strip().lower()
        if ans in ["yes", "no"]:
            return ans
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
morning = get_yes_no("Are you free in the morning?")
afternoon = get_yes_no("Are you free in the afternoon?")
urgent = get_yes_no("Is the task urgent?")
priority = get_yes_no("Is it a high priority task?")
print("\n******** Scheduling Suggestion ********")
if (urgent == "yes" or priority == "yes") and morning == "yes":
    print(" Suggestion: Schedule the task in the **morning** (urgent/high priority).")
elif (urgent == "yes" or priority == "yes") and afternoon == "yes":
    print(" Suggestion: Schedule the task in the **afternoon** (urgent/high priority).")
elif morning == "yes":
    print(" Suggestion: Schedule in the **morning** (non-urgent task).")
elif afternoon == "yes":
    print(" Suggestion: Schedule in the **afternoon** (non-urgent task).")
else:
    print(" No available time slots. Try to reschedule something to make time.")





           
         

    





     

     

        







       
   

