import queries
from .database import query

async def get_all_events():
    return query(queries.GET_ALL_EVENTS).fetchall()