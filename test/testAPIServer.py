import unittest
from jadg.api import api_server
from jadg.api import gameCommunication

class TestAPIExploration(unittest.TestCase):
    def setUp(self):
        self.message = gameCommunication.Messenger()

    def testGetHelloWorld(self):
        self.assertEqual(self.message.helloWorld(), "Hello World!")


if __name__ == '__main__':
    unittest.main()
