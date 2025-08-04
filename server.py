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


def broadcast_message(message):
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
    while True:
        # Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        # Send a name flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTSIZE).decode(ENCODER)

        # Add new client socket and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)
        # Update the server, individual client, and all clients
        print(f"Name of new client is {client_name}\n")
        client_socket.send(
            f"{client_name}, you have connected to server!".encode(ENCODER))
        broadcast_message(
            f"{client_name} has joined the chat!".encode(ENCODER))
