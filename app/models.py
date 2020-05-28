'''
app.models.py
'''
from pydantic import BaseModel

class AddEvent(BaseModel):
    title: str = None
    time: str = None
    website: str = None
    place: str = None
    distance: str = None
    author: str = None


class EventParams(BaseModel):
    city: str
    month: str