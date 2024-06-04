import socket

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 8081

def main():
    # Create a socket object using IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # Get the maximum number from the user
        max_number = input()

        # Send the maximum number to the server
        client_socket.sendall(max_number.encode())

        # Receive the random number from the server
        random_number = client_socket.recv(1024).decode()

        print(random_number)

if __name__ == "__main__":
    main()
