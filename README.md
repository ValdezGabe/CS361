# Overview
This project implements a simple client-server architecture using sockets. The client connects to the server and sends a request for the server to generate a random number. The client specifies a maximum limit, and the server generates a random number between 1 and this limit. The server then sends the generated random number back to the client.

## Project Structure
- `client.py`: The server script that listens for client connections, receives the maximum limit, generates a random number, and sends it back to the client.
- `rng.py`: The client script that connects to the server, sends the maximum limit for random number generation, and receives the random number from the server.

## A. Requesting Data from the Microservice

### Instructions
1. Establish a connection to the server: Use a socket to connect to the server at the specified host and port. It should display a message "Server is listening on port 8081"
2. Send the request: Once connected, send a request for the server to generate a random number. The request should include the maximum limit for the random number.
3. Receive the server's prompt: The server will prompt you to enter the maximum number.
4. Send the maximum number: Send the maximum number to the server.
5. Receive the random number: The server will generate a random number within the specified range and send it back to you.

Example Call:


![image](https://github.com/GabeMValdez/CS361/assets/166589044/879b7f16-fe86-4516-b46e-476f1d827106)


## B. Receiving Data from the Microservice

### Instructions
1. Read the server's prompt: After connecting, read the prompt message from the server asking for the maximum number.
2. Send the maximum number: Respond to the prompt by sending the maximum number.
3. Read the random number: Read the generated random number sent by the server.


## UML Diagram:


![image](https://github.com/GabeMValdez/CS361/assets/166589044/f6905895-7587-405c-8b01-2d1cca5e001b)
