import sqlite3
import pandas as pd
from datetime import datetime
# creating and connecting to a database to store newly created habits.
conn = sqlite3.connect('habits.db')
cursor = conn.cursor()

# creating the columns for the table while informing the user that the table already exists.
# autoincrement ensures a unique identifier is generated everytime the user adds a habit.
# unique prevents duplicate data from being added everytime this script is executed.
try:
    cursor.execute("""
create table if not exists habits (
id integer primary key autoincrement,
habit varchar(223),
created_at date,
unique(habit)
);
""")
    conn.commit()
    print('Table created successfully')
except:
    print('Table already exists')

# function to add values to the table
def add_habits(habit):

# creates a variable that stores the exact date and time a habit was formed or repeated.
    now = datetime.now().strftime('%Y-%m-%d-%H-%M')

# adds user data to the habit tracker table.
# the try-except block informs the user whether the data was inserted successfully or not and explains the type of error that occurred.
    try:
        cursor.execute('insert or ignore into habits (habit, created_at) values (?, ?);',
                  (habit, now)
                  )
        conn.commit()
        print(f'{habit} successfully added on {now}')
    except sqlite3.Error as e:
        print(f'database error: {e}')
        print('data already exists')

# ensures all columns of the table are returned when the script is executed.
pd.set_option('display.max_columns', None)

print(add_habits('habit_1'))
print(add_habits('habit_2'))
print(add_habits('habit_3'))
print(pd.read_sql_query('select * from habits', con = conn))

