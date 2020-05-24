'''
app.db.queries.py
'''

GET_ALL_EVENTS = '''
            SELECT *
            FROM events'''

ALL_EVENTS_FROM_TODAY= '''
            SELECT *
            FROM events
            WHERE TIME > :now
            ORDER BY TIME'''


