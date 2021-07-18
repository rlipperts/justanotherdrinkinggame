from jadg.model.user_model.user_model import User, UserModel
from jadg.event.game_event import GameEvent
from jadg.event.event import Event
from jadg.event.communication import Communication
from jadg.model.games.do_this.do_this import DoThis
import unittest

class CommunicationSpy(Communication):
    def __init__(self):
        self.event_send_log: list[Event] = []
        self.event_request_log: list[Event] = []


    def send(self, event: Event):
        self.event_send_log.append(event)

    def request(self, event: Event, timeout: int = 0):
        self.event_request_log.append(event)
        return GameEvent(set(), "")


class TestGame(unittest.TestCase):
    def setUp(self) -> None:

        self.com = CommunicationSpy()
        self.game = DoThis(self.com)

    def test_game(self):
        pass

if __name__ == '__main__':
    unittest.main()
