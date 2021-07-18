from time import sleep

from jadg.api.game_communication import TimerMessage
from jadg.model.game import Game
from jadg.service.service import Service


class Timer(Service):
    """
    Service that sends information-free TimerMessages every x seconds.
    """

    def __init__(self, game: Game, time: int = 10):
        """
        Create a timer instance
        Args:
            game: game to notify
            time: time between messages in seconds
        """
        super(Timer, self).__init__(game, time=time)

    def async_action(self, game: Game, **kwargs):
        while True:
            sleep(kwargs['time'])
            self.notify_game(TimerMessage())
