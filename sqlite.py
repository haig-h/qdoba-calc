import sqlite3
import pandas as pd

file = "food.db"

try:

    sqliteConnection = sqlite3.connect(file)
    print("Connected to SQlite")

    cursor = sqliteConnection.cursor()

    df = pd.read_csv('qdobaconverted.csv', names=['food', 'allergens', 'serving size(g)', 'calories per serving', 'calories in fat', 'total fat(g)', 'saturated fat(g)', 'trans fat(g)', 'cholesterol(mg)', 'sodium(mg)', 'potassium(mg)',
                'total carbs(g)', 'dietary fiber(g)', 'sugar(g)', 'protein(g)'] ,encoding_errors='replace', on_bad_lines='skip')
    df.to_sql('foods', sqliteConnection, if_exists='replace', index=True)

    sqliteConnection.commit()

except sqlite3.Error as error:
    print('Error occured - ', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQlite Connection Closed')