'''
api.routers.v1.py
'''
from fastapi import APIRouter

# from fastapi import HTTPException, status

V1 = APIRouter()


@V1.get("/")
async def root():
    return{"message": "Hello, welcome on main page friend"}


@V1.get("/archive")
async def run_archive():
    return{"message": "Here will be run archive"}

@V1.get("/events")
async def all_events(page: int = 0, per_page: int = 10):
    pass

@V1.get("/events/{month}")
async def months_events(month:int):
    return{"message": "List of all running events division into months"}

@V1.get("/distance/{dist}")
async def distance_events(dist: str):
    return{"message": "List of all running events division into distance"}