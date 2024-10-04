"""SQLite3 database operations in Python."""

import numpy as np
import randomname
import sqlite3


# Initialization
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# query to check if table named 'users' exists
## SELECT
query_if_table_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"
cursor.execute(query_if_table_exists)
table_exists = cursor.fetchone()

if table_exists:
    # Adding a new user to the 'users' table if table already exists
    print("Table 'users' already exists. Adding a new user...")

    # Generate random name and age
    name = str(randomname.get_name())
    age = str(np.random.randint(18, 60))
    
    # query to insert data into the 'users' table
    params = (name, age)  # Parameters to insert into the query
    ## INSERT
    query_add_user = f"INSERT INTO users (name, age) VALUES (?, ?)"
    cursor.execute(query_add_user, params)
    connection.commit()  # Commit the transaction

else:
    # Create the 'users' table if it does not exist
    ## CREATE
    create_table_query = "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
    cursor.execute(create_table_query)
    print("Table 'users' created.")

## SELECT
# Example query to fetch data from the 'users' table
query_fetch_data = "SELECT * FROM users"
cursor.execute(query_fetch_data)
data = cursor.fetchall()

for row in data:
    print(row)

# Close the connection
connection.close()
