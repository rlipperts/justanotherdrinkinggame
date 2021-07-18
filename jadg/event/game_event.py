import uuid

from jadg.event.event import Event
from jadg.model.user_model.user_model import User


class GameEvent(Event):

    def __init__(self, target: set[User], content: str):
        self.identifier = int(uuid.uuid4())
        self.target = target
        self.content = content
