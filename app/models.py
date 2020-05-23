'''
api.models.py
'''
from pydantic import BaseModel

class Event(BaseModel):
    title: str = None
    time: str = None
    website: str = None
    place: str = None
    distance: str = None