from jadg.event.event import Event
from jadg.model.logic.user_model.user_model import User


class UserEvent(Event):

    def __init__(self, identifier: int, source: User, content: str):
        self.identifier = identifier
        self.source = source
        self.content = content
