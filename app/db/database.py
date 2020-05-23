import aiosqlite

SQL_DATABASE_ADDRESS="events.db"

async def query(query: str, params=None):
    with await aiosqlite.connect(SQL_DATABASE_ADDRESS) as connection:
        try:
            cursor = await connection.cursor()
            cursor.row_factory = await aiosqlite.Row()
            if params:
                return cursor.execute(query, params)
            return cursor.execute(query)
        except Exception:
            raise Exception

# tests

# import aiosqlite
# @app.on_event("startup")
# async def startup():
# 	app.db_connection = await aiosqlite.connect('events.db')


# @app.on_event("shutdown")
# async def shutdown():
# 	await app.db_connection.close()

# @app.get("/test")
# async def test():
#     app.db_connection.row_factory = aiosqlite.Row
#     cursor = await app.db_connection.execute('''
#                                                 SELECT *
#                                                 FROM events''')
#     stats = await cursor.fetchall()
#     return stats
	

#############