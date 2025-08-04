# Server side chat room
import socket
import threading


# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTSIZE = 1024

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Since we should only add one argument to the bind function
# If we use multiple arguments
#  we have to put our arguments in parentheses and make a tuple
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Create two blank list to store connected client sockets and their names
client_socket_list = []
client_name_list = []


def boadcast_message(message):
    """
        Send a message to all clients connected to the server
    """
    pass


def recieve_message(client_socket):
    """
        Recieve an incoming message from a specific client and forward the message to be broadcast
    """
    pass


def connect_client():
    """
        Connet an incoming client to the server
    """
    pass
