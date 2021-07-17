from time import sleep

from jadg.event.timer_event import TimerEvent
from jadg.model.game import Game
from jadg.service.service import Service


class Timer(Service):

    def __init__(self, game: Game, time: int = 10):
        super(Timer, self).__init__(game)

    def async_action(self, game: Game, **kwargs):
        while True:
            sleep(kwargs['time'])
            self.notify_game(TimerEvent())
