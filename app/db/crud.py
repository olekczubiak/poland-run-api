'''
app.db.crud.py
'''
from .queries import GET_ALL_EVENTS
from .database import query

def get_all_events():
    return query(GET_ALL_EVENTS).fetchall()