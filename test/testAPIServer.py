import unittest
from jadg.api import api_server

class TestAPIExploration(unittest.TestCase):
    def setUp(self):
        pass

    def test_open_web_server(self):
        pass

    def testGetHelloWorld(self):
        jadgApi = api_server.MainApi()
        self.assertEqual(jadgApi.helloWorld(), "Hello World!")


if __name__ == '__main__':
    unittest.main()
