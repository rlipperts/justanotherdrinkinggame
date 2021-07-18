import unittest
from jadg.api import game_communication
from jadg.api.api_service import Server, Client
from time import sleep

PORT = 65432
HOST = '127.0.0.1'

class TestAPIExploration(unittest.TestCase):
    def setUp(self):
        self.message = game_communication.Messenger()

    def test_get_hello_world(self):
        self.assertEqual(self.message.hello_world(), "Hello World!")

    @unittest.skip("Takes long to execute")
    def test_simple_client_server_com(self):
        clients = []
        server = Server()
        server.start()
        client = Client()
        client.start()
        sleep(2)
        print("Start Assertion")
        self.assertGreater(len(server.clients), 0)
        for request_number in range(10):
            server.clients[0][0].sendall(f"Hello World {request_number}".encode("utf-8"))
            sleep(1)

        client.close()
        # client.stop()
        sleep(1)
        # server.stop()
        server.close()
        sleep(1)
        print("Join Processes")
        client.join(1)
        server.join(1)
        server.socket.close()
        client.socket.close()


if __name__ == '__main__':
    unittest.main()
