# Client Side Chat Room
import socket
import threading

# Define constants to be used
# Server IP (localhost in this case)
DESTINATION_IP = socket.gethostbyname(socket.gethostname())
DESTINATION_PORT = 12345  # Must match server port
ENCODER = 'utf-8'  # Encoding standard for messages
BYTESIZE = 1024  # Size of messages to be received

# Create a client socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server at the specified IP and PORT
client_socket.connect((DESTINATION_IP, DESTINATION_PORT))


def send_message():
    '''
    Continuously send messages to the server
    Runs in a separate thread to allow simultaneous sending/receiving
    '''
    while True:
        message = input("")  # Get user input for message
        # Encode and send to server
        client_socket.send(message.encode(ENCODER))


def recieve_message():
    '''
    Continuously receive messages from the server
    Runs in a separate thread to handle incoming messages
    '''
    while True:
        try:
            # Receive and decode message from server
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            # Check if server is asking for client's name (initial handshake)
            if message == "NAME":
                name = input("What is your name: ")
                client_socket.send(name.encode(ENCODER))  # Send name to server
            else:
                # Display regular chat message from server
                print(message)
        except:
            # Handle connection errors (server closed, network issues, etc.)
            print("An error occurred...")
            client_socket.close()  # Clean up socket
            break  # Exit the receive loop


# Create and start threads for sending and receiving messages
# This allows simultaneous operation of both functions
recieve_thread = threading.Thread(target=recieve_message)
send_thread = threading.Thread(target=send_message)

# Start both threads to begin chat functionality
recieve_thread.start()
send_thread.start()
