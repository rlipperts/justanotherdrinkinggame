import uuid

from jadg.event.event import Event
from jadg.model.user_model.user_model import User


class UserEvent(Event):

    def __init__(self, source: User, content: str):
        self.identifier = int(uuid.uuid4())
        self.source = source
        self.content = content
