# Client side chat room
import socket
import threading


# Define constants to be used
DESTINATION_IP = socket.gethostbyname(socket.gethostname())
DESTINATION_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DESTINATION_IP, DESTINATION_PORT))


def send_message():
    """
        Send a message to the server to be broadcast
    """
    pass


def recieve_message():
    """
        Recieve an incoming message from the server
    """
    pass
