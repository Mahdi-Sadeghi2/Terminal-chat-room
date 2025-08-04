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
    while True:
        while True:
            message = input("Hey how are you doing?")
            client_socket.send(message.decode(ENCODER))


def recieve_message():
    """
        Recieve an incoming message from the server
    """
    while True:
        try:
            # Recieve an incoming message from the server
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            # Check for the name flag, else show the message
            if message == "NAME":
                name = input("What is your name?: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            # An error occured, close the connection
            print("An error occured...")
            client_socket.close()
            break


# Create thread to continuously send and recieve messages
recieve_thread = threading.Thread(target=recieve_message)
send_thread = threading.Thread(target=send_message)

# Start the client
recieve_thread.start()
recieve_thread.start()
