from jadg.service.timer import Timer
import unittest
import time
from unittest.mock import MagicMock

class TestServices(unittest.TestCase):

    def register_time(self, event):
        print("Side effect called")
        self.event_called_time = time.time()

    def setUp(self) -> None:
        self.event_called_time = 0
        self.game = MagicMock()
        self.game.handle_event = MagicMock()


    def test_timer(self):
        timer = Timer(self.game, 1)
        startTime = time.time()
