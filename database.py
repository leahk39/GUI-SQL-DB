"""
This is the main mod with the database code in it
"""
#test2

import sqlite3

CREATE_VINYLS_TABLE = "CREATE TABLE IF NOT EXISTS vinyls (id INTEGER PRIMARY KEY, name TEXT, album TEXT, rating INTEGER)"

INSERT_VINYL = "INSERT INTO vinyls (name, album, rating) VALUES (?, ?, ?)"

GET_ALL_VINYLS = "SELECT * FROM vinyls"

GET_ALL_VINYLS_BY_NAME = "SELECT * FROM vinyls WHERE name = ?;"

GET_BEST_ALBUM_FOR_VINYL = """
SELECT * FROM vinyls 
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""

DELETE_VINYL_BY_NAME = """
DELETE FROM vinyls
WHERE name = ?;"""

SHOW_VINYL_RANGE = """
SELECT * FROM vinyls
WHERE rating BETWEEN ? AND ?;"""

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        return connection.execute(CREATE_VINYLS_TABLE)

def add_vinyl(connection, name, album, rating):
    with connection:
        print(f"Adding vinyl: {name} ({album}) - {rating}/100")
        return connection.execute(INSERT_VINYL, (name, album, rating))

def get_all_vinyls(connection):
    with connection:
        return connection.execute(GET_ALL_VINYLS).fetchall()

def get_vinyls_by_name(connection, name):
    with connection:
        return connection.execute(GET_ALL_VINYLS_BY_NAME, (name,)).fetchall()

def get_best_album_for_vinyl(connection, name):
    with connection:
        return connection.execute(GET_BEST_ALBUM_FOR_VINYL, (name,)).fetchall()

def delete_vinyl_by_name(connection, name):
    with connection:
        return connection.execute(DELETE_VINYL_BY_NAME, (name,)).fetchall()

def show_vinyl_range(connection, low, high):
    with connection:
        return connection.execute(SHOW_VINYL_RANGE, (low, high,)).fetchall()