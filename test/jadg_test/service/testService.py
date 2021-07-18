from jadg.api.game_communication import Message
from jadg.service.timer import Timer
import unittest
import time
from unittest.mock import MagicMock

class TestServices(unittest.TestCase):

    def mock_side_effect_register_time(self, message: Message):
        print("Side effect called")
        self.handle_msg_called_timestamp = time.time()

    def setUp(self) -> None:
        self.handle_msg_called_timestamp = 0
        self.game = MagicMock()
        self.game.handle_message = MagicMock(side_effect=self.mock_side_effect_register_time)


    def test_timer(self):
        timer = Timer(self.game, 2)
        startTime = time.time()
        timer.start()
        time.sleep(3)
        timer.stop()
        print(self.handle_msg_called_timestamp)
        print(self.game.handle_message.called)
        self.assertAlmostEqual(2, self.handle_msg_called_timestamp -startTime)
