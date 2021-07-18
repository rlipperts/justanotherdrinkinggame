from abc import ABC, abstractmethod
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
    """
    Data class containing information to be sent between games, services and clients
    """
    identifier: int
    content: dict

    def __init__(self, content):
        self.identifier = int(uuid.uuid4())
        self.content = content


class BaseMessage(Message):
    """
    Default message without bells or whistles.
    """
    pass


class EmptyMessage(Message):
    """
    Message without data.
    """

    def __init__(self):
        super(EmptyMessage, self).__init__(None)

class TimerMessage(EmptyMessage):
    """
    Specialized Message for timer notifications.
    """
    # todo: is this necessary? We could also just create a base message with content 'timer_notification'
    pass
