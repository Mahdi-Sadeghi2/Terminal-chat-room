# Server Side Chat Room
import socket
import threading

# Define constants to be used
HOST_IP = socket.gethostbyname(
    socket.gethostname())  # Get the local machine IP
HOST_PORT = 12345  # Port to listen on (non-privileged ports are > 1023)
ENCODER = 'utf-8'  # Encoding standard for message encoding/decoding
BYTESIZE = 1024  # Size of messages to be received

# Create a server socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))  # Bind the socket to the IP and PORT
server_socket.listen()  # Start listening for incoming connections

# Create two blank lists to store connected client sockets and their names
client_socket_list = []  # Stores active client socket connections
client_name_list = []  # Stores names corresponding to the client sockets


def broadcast_message(message):
    '''Send a message to ALL clients connected to the server'''
    for client_socket in client_socket_list:
        client_socket.send(message)


def recieve_message(client_socket):
    '''
    Receive an incoming message from a specific client and forward the message to be broadcast
    Runs in a separate thread for each client
    '''
    while True:
        try:
            # Get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Receive message from the client and format it with color codes
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            # Format message with green color and bold text
            message = f"\033[1;92m\t{name}: {message}\033[0m".encode(ENCODER)
            broadcast_message(message)
        except:
            # This block executes if there's an error (likely client disconnected)

            # Find the index of the client socket in our list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # Close the client socket
            client_socket.close()

            # Broadcast that the client has left the chat (with red blinking text)
            broadcast_message(
                f"\033[5;91m\t{name} has left the chat!\033[0m".encode(ENCODER))
            break  # Exit the loop as the client has disconnected


def connect_client():
    '''Connect an incoming client to the server and handle initial setup'''
    while True:
        # Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        # Send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        # Add new client socket and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # Update the server, individual client, and ALL clients
        # Server console update
        print(f"Name of new client is {client_name}\n")
        # Send welcome message to the new client
        client_socket.send(
            f"{client_name}, you have connected to the server!".encode(ENCODER))
        # Broadcast arrival to all other clients
        broadcast_message(
            f"{client_name} has joined the chat!".encode(ENCODER))

        # Now that a new client has connected, start a thread to handle their messages
        recieve_thread = threading.Thread(
            target=recieve_message, args=(client_socket,))
        recieve_thread.start()


# Start the server
print("Server is listening for incoming connections...\n")
connect_client()  # This will run indefinitely to accept new connections
