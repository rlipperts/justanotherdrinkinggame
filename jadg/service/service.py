import multiprocessing
from abc import ABC

from jadg.event.event import Event
from jadg.model.game import Game


class Service(ABC):
    """
    Services are background-running tasks that can send events to the game server.
    For the simplest example check the Timer class
    """

    _background_action: multiprocessing.Process

    def __init__(self, game: Game, **kwargs):
        self._game = game
        self._background_action = multiprocessing.Process(target=self._async_wrapper, name='background service', args=(game, kwargs))

    def start(self):
        """
        Begins the service execution
        """

    def _async_wrapper(self, game: Game, kwargs):
        try:
            self.async_action(game, **kwargs)
        except InterruptedError:
            print('Service externally interrupted!')
        finally:
            print('Service ended.')

    def async_action(self, game: Game, **kwargs):
        pass

    def notify_game(self, event: Event):
        self._game.handle_event(event)

    def stop(self):
        """
        Stop the service.
        """
        self._background_action.terminate()
