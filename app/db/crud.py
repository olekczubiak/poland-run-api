'''
app.db.crud.py
'''
from .queries import GET_ALL_EVENTS, ALL_EVENTS_FROM_TODAY
from .database import query
import datetime

TODAY_DATE = datetime.date.today()


def get_events():
    return query(ALL_EVENTS_FROM_TODAY, {'now': TODAY_DATE}).fetchall()

def get_all_events():
    return query(GET_ALL_EVENTS).fetchall()