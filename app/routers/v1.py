'''
app.routers.v1.py
'''
from fastapi import APIRouter
from ..db.crud import (get_all_events, get_events, get_events_by_distance, 
                    get_archived_events, get_city_events)
from fastapi import HTTPException, status

V1 = APIRouter()


@V1.get("/")
async def root():
    return{"message": "Hello, welcome on main page, type /docs to see swagger"}


@V1.get("/new")
async def events(per_page: int = 10, page: int = 0):
    '''Shows all running events from today with page and per_page'''
    return get_events(per_page, page)

@V1.get("/events/all")
async def all_events():
    '''Show all events from today'''
    return get_all_events()

# @V1.get("/events/{month}")
# async def months_events(month: str):
#     return{"message": "List of all running events division into months"}


@V1.get("/events")
async def city_events(*, city: str):
    '''shows all running events by city'''
    # if not city:
    #     return get_events()
    return get_city_events(city)

@V1.get("/distance/{dist}")
async def distance_events(dist: str):
    '''shows all running events by distance'''
    if not get_events_by_distance(dist):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Distance not found")
    return get_events_by_distance(dist)

@V1.get("/archive")
async def run_archive():
    '''Shows archive of all running events'''
    return get_archived_events()

