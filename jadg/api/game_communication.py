from abc import ABC, abstractmethod
from jadg.event.event import Event

class Messenger:
    def hello_world(self) -> str:
        return "Hello World!"

class Communication(ABC):

    @abstractmethod
    def send(self, event: Event):
        pass

    @abstractmethod
    def request(self, event: Event, timeout: int = 0):
        pass
