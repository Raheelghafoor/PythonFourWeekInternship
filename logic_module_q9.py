#Question 9 - logic_module_q9.py

from db_module_q9 import addUserQ9, getUserQ9

def registerUserQ9(nameQ9):
    addUserQ9(nameQ9)
    return f"User {nameQ9} registered successfully."

def retrieveUserQ9(userIdQ9):
    userQ9 = getUserQ9(userIdQ9)
    if userQ9:
        return f"User Found: {userQ9['name']}"
    return "User not found."

