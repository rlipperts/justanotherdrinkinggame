from jadg.api.game_communication import Communication, EmptyMessage, Message
from jadg.model.games.do_this.do_this import DoThis
import unittest

class CommunicationSpy(Communication):
    def __init__(self):
        self.msg_send_log: list[Message] = []
        self.msg_request_log: list[Message] = []

    def send(self, message: Message):
        self.msg_send_log.append(message)

    def request(self, message: Message, timeout: int = 0):
        self.msg_request_log.append(message)
        return EmptyMessage()


class TestGame(unittest.TestCase):
    def setUp(self) -> None:

        self.com = CommunicationSpy()
        self.game = DoThis(self.com)

    def test_game(self):
        pass

if __name__ == '__main__':
    unittest.main()
