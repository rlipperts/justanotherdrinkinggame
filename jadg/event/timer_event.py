from jadg.event.event import Event

class TimerEvent(Event):

    def __init__(self, identifier: int):
        self.identifier = identifier
