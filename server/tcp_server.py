import socket
import threading
import settings
from server.message_handler import message_handler


class TCPServer:
    def __init__(self):
        self.host = settings.HOST
        self.port = settings.PORT
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Method to start the server
    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server is running on {self.host}:{self.port}...")

        while True:
            # Accept incoming connections
            conn, addr = self.server_socket.accept()
            # Handle each connection in a separate thread
            client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            client_thread.start()

    # Method that handles client connections in a separate thread
    def handle_client(self, conn, addr):
        print(f"Connection established with {addr}.")
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                print(f"Received data: {data.decode()}")

                # Send the data to the message_handler and get the response
                response_message = message_handler(data.decode())

                # Send the response back to the client
                conn.sendall(response_message.encode())
        except Exception as e:
            print(f"Connection error: {e}")
        finally:
            conn.close()
            print(f"Connection with {addr} closed.")

    # Method to stop the server (optional)
    def stop_server(self):
        self.server_socket.close()
        print("Server stopped.")
