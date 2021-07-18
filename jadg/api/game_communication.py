from abc import ABC, abstractmethod
from jadg.event.event import Event
import uuid

class Messenger:
    def hello_world(self) -> str:
        return "Hello World!"


class Communication(ABC):

    @abstractmethod
    def send(self, msg: 'Message'):
        pass

    @abstractmethod
    def request(self, msg: 'Message', timeout: int = 0) -> Event:
        pass

class Message(ABC):
    idetifier: int
    content: str

    def __init__(self):
        self.idetifier = int(uuid.uuid4())

class BaseMessage(Message):
    pass
