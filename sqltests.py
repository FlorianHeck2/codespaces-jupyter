import sqlite3
connection = sqlite3.connect("gamesave.db")
cursor = connection.cursor()
sql_command = """CREATE TABLE gamesaves (
    value INTEGER PRIMARY KEY,
    wave INTEGER);"""
#spieler1 = spieler(10,350,4,42,46,[0,0,0,0,1],0,0)
sql_command = """INSERT INTO position(xcord, ycord)
    Values (10, 350)"""
#sql_command = """DELETE FROM position"""
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