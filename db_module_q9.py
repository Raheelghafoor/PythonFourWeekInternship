#Question 9 - db_module_q9.py

import sqlite3

def initDatabaseQ9():
    connQ9 = sqlite3.connect("users_q9.db")
    cursorQ9 = connQ9.cursor()
    cursorQ9.execute("CREATE TABLE IF NOT EXISTS users_q9 (id INTEGER PRIMARY KEY, name TEXT)")
    connQ9.commit()
    connQ9.close()

def addUserQ9(nameQ9):
    connQ9 = sqlite3.connect("users_q9.db")
    cursorQ9 = connQ9.cursor()
    cursorQ9.execute("INSERT INTO users_q9 (name) VALUES (?)", (nameQ9,))
    connQ9.commit()
    connQ9.close()

def getUserQ9(userIdQ9):
    connQ9 = sqlite3.connect("users_q9.db")
    cursorQ9 = connQ9.cursor()
    cursorQ9.execute("SELECT id, name FROM users_q9 WHERE id = ?", (userIdQ9,))
    resultQ9 = cursorQ9.fetchone()
    connQ9.close()
    if resultQ9:
        return {"id": resultQ9[0], "name": resultQ9[1]}
    return None

