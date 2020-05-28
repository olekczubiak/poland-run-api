'''
app.db.crud.py
'''
import datetime

from .queries import (GET_ALL_EVENTS, ALL_EVENTS_FROM_TODAY, 
                    FIND_EVENTS_BY_DISTANCE, ARCHIVED_EVENTS,
                    FIND_EVENTS_BY_CITY_MONTH)
from .database import query


TODAY_DATE = datetime.date.today()


def get_events(per_page, page):
    return query(ALL_EVENTS_FROM_TODAY, {'now': TODAY_DATE, 'limit': per_page, 'offset': page * per_page}).fetchall()
    #add here page and per_page

def get_all_events():
    return query(GET_ALL_EVENTS).fetchall()

def get_events_by_distance(dist):
    return query(FIND_EVENTS_BY_DISTANCE, {'distance': dist}).fetchall()

def get_archived_events():
    return query(ARCHIVED_EVENTS, {'now': TODAY_DATE}).fetchall()

def get_city_month_events(city, month):
    return query(FIND_EVENTS_BY_CITY_MONTH, {'pol_city': city, 'month': month}).fetchall()