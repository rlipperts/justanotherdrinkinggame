import socket
from time import sleep
from threading import Thread
from jadg.service.service import Service

PORT = 65416
HOST = '127.0.0.1'

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.clients: list[tuple[socket.socket, socket.AddressInfo]] = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.closed = True

    def run(self):
        self.socket.bind((HOST, PORT))
        self.closed = False
        print("Starting Connection Service")
        while not self.closed:
            print("Wait for client")
            self.socket.listen(1)
            conn, addr = self.socket.accept()
            self.clients.append((conn, addr))
            print(len(self.clients))
            print("Accepting client")
        print("Server Terminated!")
        self.socket.shutdown(1)
        self.socket.close()

    def close(self):
        self.closed = True

class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.closed = True

    def run(self):
        self.socket.connect((HOST, PORT))
        self.closed = False
        print("Starting Client")
        while not self.closed:
            sleep(1)
            data = self.socket.recv(1024)
            if data:
                print(data)
        self.socket.shutdown(1)
        self.socket.close()
        print("Client Terminated!")

    def close(self):
        self.closed = True
