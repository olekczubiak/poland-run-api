'''
app.db.database.py
'''
SQL_DATABASE_ADDRESS="events.db"
import sqlite3


def query(query: str, params=None):
    with sqlite3.connect(SQL_DATABASE_ADDRESS) as connection:
        try:
            cursor = connection.cursor()
            cursor.row_factory = sqlite3.Row
            if params:
                return cursor.execute(query, params)
            return cursor.execute(query)
        except Exception:
            raise Exception


''''
async - only for tests
'''
# import aiosqlite
# async def query(query: str, params=None):
#     with await aiosqlite.connect(SQL_DATABASE_ADDRESS) as connection:
#         try:
#             cursor = await connection.cursor()
#             cursor.row_factory = await aiosqlite.Row()
#             if params:
#                 return cursor.execute(query, params)
#             return cursor.execute(query)
#         except Exception:
#             raise Exception
