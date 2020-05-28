'''
app.db.queries.py
'''

GET_ALL_EVENTS = '''
            SELECT 
                *
            FROM 
                running_events'''

ALL_EVENTS_FROM_TODAY = '''
            SELECT 
                *
            FROM 
                running_events
            WHERE 
                Time > :now
            ORDER BY Time
            LIMIT :limit
            OFFSET :offset
'''

FIND_EVENTS_BY_DISTANCE = '''
            SELECT
                *
            FROM 
                running_events
            WHERE 
                Distance == :distance
            ORDER BY Time'''

ARCHIVED_EVENTS = '''
            SELECT 
                *
            FROM 
                running_events
            WHERE 
                Time < :now
            ORDER BY Time DESC'''


FIND_EVENTS_BY_CITY_MONTH = '''
            SELECT  
                *
            FROM
                running_events
            WHERE
                Place == :pol_city AND strftime ('%m', Time) = :month
            ORDER BY Time
'''
ADD_NEW_EVENT = '''
            INSERT INTO add_events (Title, Time, Website, Place, Distance, Author)
                VALUES ( :title, :time, :website, :place, :distance, :author)
'''

CHECK_IF_EVENT_EXISTS = '''
            SELECT
                *
            FROM 
                add_events
            WHERE
                Title = :title'''