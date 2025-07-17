#Question 9 - test_integration_q9.py

import os
import sqlite3
from db_module_q9 import initDatabaseQ9
from logic_module_q9 import registerUserQ9, retrieveUserQ9

def resetDatabaseQ9():
    if os.path.exists("users_q9.db"):
        os.remove("users_q9.db")
    initDatabaseQ9()

def test_userRegistrationAndRetrievalQ9():
    resetDatabaseQ9()
    resultRegisterQ9 = registerUserQ9("Ali")
    assert "registered successfully" in resultRegisterQ9

    connQ9 = sqlite3.connect("users_q9.db")
    cursorQ9 = connQ9.cursor()
    cursorQ9.execute("SELECT id FROM users_q9 WHERE name = ?", ("Ali",))
    userIdQ9 = cursorQ9.fetchone()[0]
    connQ9.close()

    resultRetrieveQ9 = retrieveUserQ9(userIdQ9)
    assert "User Found" in resultRetrieveQ9