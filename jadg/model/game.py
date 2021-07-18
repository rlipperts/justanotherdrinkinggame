from abc import ABC
from jadg.api.game_communication import Message, BaseMessage


class Game(ABC):
    """
    Superclass of all games
    """

    def __init__(self, communication_service):
        """
        Create the game class.
        Args:
            communication_service: interface to talk to the client with
        """
        self._communication_service = communication_service

    def setup(self):
        """
        Begin setup of the game and its logic and data.
        """
        pass

    def run(self):
        """
        Start the game.
        """

    def handle_message(self, message: Message):
        """
        Handle an event.
        """
        pass

    def finalize(self):
        """
        End the game.
        """
        pass

    def send(self, text: str):
        msg = BaseMessage(text)
        self._communication_service.send(msg)

    def request(self, text: str, timeout: int = 0) -> Message:
        """
        Request something from the Client and block until there is an answer
        """
        msg = BaseMessage(text)
        return self._communication_service.request(msg,  timeout)
