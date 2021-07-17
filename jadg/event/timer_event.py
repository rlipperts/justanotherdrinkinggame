import uuid

from jadg.event.event import Event

class TimerEvent(Event):

    def __init__(self):
        self.identifier = int(uuid.uuid4())
