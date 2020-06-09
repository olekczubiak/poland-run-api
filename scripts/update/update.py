import os
import sqlite3

from search import append_events, name, time, distance, place, website

def open_func(*args):
    for file_name in args:
        append_events(file_name)


def html_files(number_of_files):
    for n in range(0, number_of_files):
        open_func(f'async_{n}.html')


if __name__ == "__main__":
    html_files(16)
    try:
        
        sqliteConnection = sqlite3.connect(os.path.realpath('/Users/olek/Documents/dev/RunApi/events.db'))
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        for n in range(0, len(time)):
            sqlite_insert_query = """INSERT INTO running_events
                            (Title, Time, Website, Place, Distance) 
                            VALUES 
                            (?,?,?,?,?)"""
            count = cursor.execute(sqlite_insert_query, (name[n], time[n], website[n], place[n], distance[n]))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")