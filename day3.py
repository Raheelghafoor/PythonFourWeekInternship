#QUESTION 1
userinput = input("Type something:  ")

if userinput.lower() == "true" or userinput.lower() == "false":
    print("Boolean")

elif userinput.isdigit():
    print("Integer")

elif "." in userinput:
    try:
        float(userinput)
        print("Float")
    except:
        print("String")
elif userinput.isalpha():
    print("String")

elif not userinput.isalnum():
    print("Special Characters")

else:
    print("Mixed Type")
#QUESTION 2
import sys

if len(sys.argv) != 4:
       print("\nPlease run the file like this:")
       print("\n python myfile.py <name> <age> <email>")
else:
       uname=sys.argv[1]
       uage=sys.argv[2]
       uemail=sys.argv[3]
       print("----- User Information -----")
       print("Name :", uname)
       print("Age  :", uage)
       print("Email:", uemail)

#QUESTION 3
import os
apikey=os.environ.get("API_KEY")
databaseurl=os.environ.get("DATABASE_URL")
print("\n\n----- Environment Variables -----")
print("API Key      :", apikey)
print("Database URL :", databaseurl)

#QUESTION 4
import getpass
initialpass=getpass.getpass("\n\nEnter the password:  ")
confirmpass=getpass.getpass("Re-Enter the password:  ")
if initialpass==confirmpass:
       print("PASSWORD CORRECT!")
else:
       print("PASSWORD INCORRECT! TRYAGAIN! ")

#QUESTION 5
txt=input("Enter text: ")
txt=txt.strip().lower()
clean=""
for ch in txt:
     if ch.isalnum() or ch==" ":
          clean+=ch

clean=" ".join(clean.split())
if clean.replace(" ", ""):
    print("Sanitized:", clean)
else:
    print("Invalid input!")

#QUESTION 6
import threading
answer=[]
def get_input():
     text=input("Enter something  ")
     answer.append(text)
t=threading.Thread(target=get_input)
t.start()
t.join(5)
if t.is_alive():
    print("Time is up!")
else:
    print("You typed:  ", answer[0])

#QUESTION 7
items=[]
while True:
     print("\n\n--- MENU ---")
     print("1. View")
     print("2. Add")
     print("3. Delete")
     print("4. Exit")
     choice=input("Choose 1, 2, 3 or 4: ")
     if choice=="1":
          print("Items:", items)
     elif choice == "2":
          item=input("What you want to add?")
          items.append(item)
     elif choice =="3":
            item = input("What do you want to delete? ")
            if item in items:
                 items.remove(item)
                 print("DELETED!")
            else:
                  print("Item not found!")
     elif choice =="4":
           print("Goodbye!")
           break
     
     else:
        print("Wrong choice. Try again.")

#QUESTION 8
raw_input = input("Enter values (comma-separated): ")
its = raw_input.split(",")
cleaned_items=[]
for it in its:
     it=it.strip().lower()
     cl=""
     for c in it:
          if c.isalnum() or c == " ":
               cl+=c
     if cl:
          cleaned_items.append(cl)

print("Cleaned items: ",cleaned_items)


#QUESTION 9
import re

data = input("Enter something (email, phone, or date): ")
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
phone_pattern = r'^\d{10}$'
date_pattern = r'^\d{4}-\d{2}-\d{2}$'
if re.match(email_pattern,data):
     print("Valid Email ")
elif re.match(phone_pattern, data):
     print("Valid phone number")
elif re.match(date_pattern, data):
     print("Valid Date")
else:
     print("It does not match any format! Invalid!")


#QUESTION 10
preferences = {}
while True:
     print("\n--- User Preference Menu ---")
     print("1. View Preferences")
     print("2. Set Preference")
     print("3. Update Preference")
     print("4. Exit")
     opt=input("Enter your choice (1-4): ")
     if opt=="1":
          if preferences:
             for k, val in preferences.items():
              print(f"{k.capitalize()}: {val}")
          else:
               print("No preferences set yet.")
     elif opt=="2":
             k = input("Enter preference name (e.g., theme, language): ").lower()
             if k in preferences:
                      print("This preference already exists. Try updating it instead.")
             else:
                  val = input(f"Enter value for {k}: ")
                  preferences[k] = val
                  print(f"Preference '{k}' set to '{val}'")

     elif opt == "3":
            k = input("Enter preference you want to update: ").lower()
            if k in preferences:
                 val=input(f"Enter new value for{k}")
                 preferences[k]=val
                 print(f"Preference '{k}' updated to '{val}'")
            else:
             print("Preference not found. Try adding it first :)")
     elif opt == "4":
          print("Goodbye!")
          break
     else:
          print("Invalid choice. Please enter 1, 2, 3, or 4.")

#QUESTION 11
history=[]
while True:
     print("\n--- Input History Menu ---")
     print("1. Add Input")
     print("2. View History")
     print("3. Reset History")
     print("4. Exit")
     option = input("Choose (1-4): ")
     if option=="1":
          ip=input("Enter Something: ")
          history.append(ip)
          print("saved")
     elif option=="2":
          if history:
               print("\n Input History: ")
               for i,things in enumerate(history,1):
                    print(f"{i}. {things}")
          else:
            print("History is empty.")
     elif option == "3":
        history.clear()
        print("History cleared!")
     elif option == "4":
        print("Goodbye!")
        break
     else:
          print("Invalid choice. Try 1, 2, 3, or 4.")


#QUESTION 12
import base64
tt = input("Enter text to encrypt: ")
encoded = base64.b64encode(tt.encode())
print("Encrypted:", encoded.decode())
decoded = base64.b64decode(encoded).decode()
print("Decrypted:", decoded)


#QUESTION 13
import time
sentence=(f"I love learning python")
print("Type this sentence exactly:")
print(sentence)
start = time.time()
putin=input("\nStart typing here: ")
end = time.time()
time_taken = end - start 
leng = len(putin) 
if time_taken>0:
     speed=leng/time_taken
     print(f"Time taken: {time_taken:.2f} seconds")
     print(f"Typing speed {speed:.2f} chars/sec")
else:
     print("You typed instantly not possible!")
if putin == sentence:
    print(" You typed the sentence correctly!")
else:
    print("There were mistakes in your typing.")

#QUESTION 14
commands = ["help", "hello", "exit", "edit", "email"]
typed = input("Type something: ")
for cmd in commands:
    if cmd.startswith(typed):
        print("Did you mean:", cmd)

#QUESTION 15
nme = input("What is your name? ")
tage = int(input("What is your age? "))
if tage < 18:
    parent = input("You are under 18. What is your parent's name? ")
    print("\nThanks,", nme)
    print("We'll also contact your parent:", parent)
else:
    Eail = input("You're 18 or older. What is your email address? ")
    print("\nThanks,", nme)
    print("We'll reach you at:", Eail)




        
     

