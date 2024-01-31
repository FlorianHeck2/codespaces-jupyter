import sqlite3
connection = sqlite3.connect("gamesave.db")
cursor = connection.cursor()
sql_command = """CREATE TABLE gamesaves (
    value INTEGER PRIMARY KEY,
    wave INTEGER);"""

sql_command = """INSERT INTO gamesaves(value, wave)
    Values (4, 10)"""

cursor.execute(sql_command)
connection.commit()
connection.close()

# sql_command = """INSERT INTO employee (value, fname, lname, gender, birth_date)
#     VALUES (4, "William", "Shakespeare", "m", "1961-10-25");"""
# cursor.execute(sql_command)

# sql_command = """INSERT INTO employee (value, fname, lname, gender, birth_date)
#     VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
# cursor.execute(sql_command)

# connection.commit()

# connection.close()