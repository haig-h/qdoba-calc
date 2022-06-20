import sqlite3
import csv
import pandas as pd

file = "testing.db"


try:

    sqliteConnection = sqlite3.connect(file)
    print("Connected to SQlite")

    cursor = sqliteConnection.cursor()
    print("test1")

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS testing5(foodname TEXT, allergens int, serving_size int, calories_p_serving int, calories_f_fat int, total_fat int, saturated_fat int,'
        'trans_fat int, cholesterol int, sodium int, potassium int, total_carbs int, dietary_fiber int, sugar int, protein int);')
    print('test2')
    sqliteConnection.commit()

    df = pd.read_csv('qdobaconverted.csv', encoding_errors='replace', on_bad_lines='skip')
    df.to_sql('testing5', sqliteConnection, if_exists='replace', index=True)
    df.columns=['food', 'allergens', 'serving size', 'calories per serving', 'calories in fat', 'total fat', 'saturated fat', 'trans fat', 'cholesterol', 'sodium', 'potassium',
                'total carbs', 'dietary fiber', 'sugar', 'protein']
    print('test3')
    sqliteConnection.commit()

except sqlite3.Error as error:
    print('Error occured - ', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQlite Connection Closed')