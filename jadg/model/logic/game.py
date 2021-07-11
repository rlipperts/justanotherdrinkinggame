from abc import ABC

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

    def handle_event(self):
        """
        Handle an event.
        """
        pass

    def finalize(self):
        """
        End the game.
        """
        pass

    # def send(self, event: ):