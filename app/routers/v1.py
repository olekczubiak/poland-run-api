'''
api.routers.v1.py
'''
from fastapi import APIRouter

V1 = APIRouter()

@V1.get("/")
async def root():
    return{"message": "Hello, welcome on main page friend"}