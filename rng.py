import socket
import random

# Server configuration
HOST = 'localhost'
PORT = 8081

def generate_random_number(max_number):
    # Generate a random number between 1 and the provided maximum number
    return random.randint(1, max_number)

def main():
    # Create a socket object using IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the server to the host and port
        server_socket.bind((HOST, PORT))

        # Listen for incoming connections (allow up to 5 connections to queue up)
        server_socket.listen(5)

        while True:
            # Accept a connection from a client
            conn, addr = server_socket.accept()

            max_number = int(conn.recv(1024).decode())

            # Generate a random number
            random_number = generate_random_number(max_number)

            # Send the random number to the client
            conn.sendall(str(random_number).encode())

            # Close the connection
            conn.close()

if __name__ == "__main__":
    main()
