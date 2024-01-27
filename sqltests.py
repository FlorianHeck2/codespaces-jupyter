import sqlite3
connection = sqlite3.connect("gamesave.db")
cursor = connection.cursor()
sql_command = """
CREATE TABLE employee (
    value INTEGER PRIMARY KEY,
    fname VARCHAR(20),
    lname VARCHAR(20),
    gender CHAR(1),
    birth_date DATE);"""
#cursor.execute(sql_command)

sql_command = """INSERT INTO employee (value, fname, lname, gender, birth_date)
    VALUES (4, "William", "Shakespeare", "m", "1961-10-25");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO employee (value, fname, lname, gender, birth_date)
    VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
cursor.execute(sql_command)

connection.commit()

connection.close()