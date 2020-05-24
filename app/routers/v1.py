'''
app.routers.v1.py
'''
from fastapi import APIRouter
from ..db.crud import get_all_events, get_events
# from fastapi import HTTPException, status

V1 = APIRouter()


@V1.get("/")
async def root():
    return{"message": "Hello, welcome on main page, type /docs to see swagger"}


@V1.get("/archive")
async def run_archive():
    return{"message": "Here will be run archive"}

@V1.get("/events")
async def events(page: int = 0, per_page: int = 10):
    return get_events()

@V1.get("/events/all")
async def all_events():
    return get_all_events()

@V1.get("/events/{month}")
async def months_events(month:int):
    return{"message": "List of all running events division into months"}

@V1.get("/distance/{dist}")
async def distance_events(dist: str):
    return{"message": "List of all running events division into distance"}