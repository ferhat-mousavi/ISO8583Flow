import socket
import threading
import settings
from server.message_handler import message_handler
from server.tcp_server import TCPServer

if __name__ == "__main__":
    server = TCPServer()
    server.start_server()
