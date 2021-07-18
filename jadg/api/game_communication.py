from abc import ABC, abstractmethod
from jadg.event.event import Event
import uuid
import json

class Messenger:
    def hello_world(self) -> str:
        return "Hello World!"


class Communication(ABC):

    @abstractmethod
    def send(self, msg: 'Message'):
        """
        Send message
        """

    @abstractmethod
    def request(self, msg: 'Message', timeout: int = 0) -> dict:
        """
        Send request and expect response in json format
        """

class Message(ABC):
    idetifier: int
    content: dict

    def __init__(self, content):
        self.idetifier = int(uuid.uuid4())
        self.content = content

class BaseMessage(Message):
    pass
