from jadg.service.timer import Timer
import unittest
import time
from unittest.mock import MagicMock

class TestServices(unittest.TestCase):

    def mock_side_effect_register_time(self, event):
        print("Side effect called")
        self.handle_event_called_timestamp = time.time()

    def setUp(self) -> None:
        self.handle_event_called_timestamp = 0
        self.game = MagicMock()
        self.game.handle_event = MagicMock(side_effect=self.mock_side_effect_register_time)


    def test_timer(self):
        # timer = Timer(self.game, 1)
        # startTime = time.time()
        self.game.handle_event("test")
        print(self.handle_event_called_timestamp)
