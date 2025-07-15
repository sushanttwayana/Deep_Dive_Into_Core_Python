import datetime

class Calendar:

    def __init__(self) -> None:
        self.events = []

    def add_event(self, event):

        if type(self).is_weekend(event.date):
            raise ValueError("NO")
        
        self.events.append(event)


    @staticmethod
    def is_weekend(date):
        return date.weekday() > 4 # M T W T F

    @classmethod
    def from_json(cls, filename):
        c = cls()
        ...
        return c

class WorkCalendar(Calendar):
    pass