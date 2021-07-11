from jadg.event.event import Event
from jadg.model.logic.user_model.user_model import User


class GameEvent(Event):

    def __init__(self, identifier: int, target: set[User], content: str):
        self.identifier = identifier
        self.target = target
        self.content = content
