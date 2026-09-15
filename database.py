"""
This is the main mod with the database code in it
"""
#test2

import sqlite3

CREATE_DRINKS_TABLE = "CREATE TABLE IF NOT EXISTS drinks (id INTEGER PRIMARY KEY, name TEXT, flavor TEXT, rating INTEGER)"

INSERT_DRINK = "INSERT INTO drinks (name, flavor, rating) VALUES (?, ?, ?)"

GET_ALL_DRINKS = "SELECT * FROM drinks"

GET_ALL_DRINKS_BY_NAME = "SELECT * FROM drinks WHERE name = ?;"

GET_BEST_FLAVOR_FOR_DRINK = """
SELECT * FROM drinks 
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""

DELETE_DRINK_BY_NAME = """
DELETE FROM drinks
WHERE name = ?;"""

SHOW_BEAN_RANGE = """
SELECT * FROM drinks
WHERE rating BETWEEN ? AND ?;"""

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_DRINKS_TABLE)

def add_drink(connection, name, flavor, rating):
    with connection:
        connection.execute(INSERT_DRINK, (name, flavor, rating))

def get_all_drinks(connection):
    with connection:
        return connection.execute(GET_ALL_DRINKS).fetchall()

def get_drinks_by_name(connection, name):
    with connection:
        return connection.execute(GET_ALL_DRINKS_BY_NAME, (name,)).fetchall()

def get_best_flavor_for_drink(connection, name):
    with connection:
        return connection.execute(GET_BEST_FLAVOR_FOR_DRINK, (name,)).fetchall()

def delete_drink_by_name(connection, name):
    with connection:
        return connection.execute(DELETE_DRINK_BY_NAME, (name,)).fetchall()

def show_drink_range(connection, low, high):
    with connection:
        return connection.execute(SHOW_BEAN_RANGE, (low, high,)).fetchall()