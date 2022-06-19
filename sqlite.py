import sqlite3


file = "testing.db"

try:
    sqliteConnection = sqlite3.connect(file)
    print("Connected to SQlite")
except sqlite3.Error as error:
    print('Failed to connect to sqlite', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('sqlite connection closed')
