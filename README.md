# Overview
This project implements a simple client-server architecture using sockets. The client connects to the server and sends a request for the server to generate a random number. The client specifies a maximum limit, and the server generates a random number between 1 and this limit. The server then sends the generated random number back to the client.

## Details
- `client.py`: The server script that listens for client connections, receives the maximum limit, generates a random number, and sends it back to the client.
- `rng.py`: The client script that connects to the server, sends the maximum limit for random number generation, and receives the random number from the server.

## A. Requesting Data from the Microservice

### Instructions
1. Establish a connection to the server - `python rng.py`: Use a socket to connect to the server at the specified host and port. 
2. Send the request - `python client.py`: Once connected, send a request for the server to generate a random number. The request should include the maximum limit for the random number.
3. Send the maximum number to the server. Ex: `22`
4. The server will generate a random number within the specified range and send it back to you. Ex: `8`

Example Call:


![image](https://github.com/GabeMValdez/CS361/assets/166589044/879b7f16-fe86-4516-b46e-476f1d827106)


## B. Receiving Data from the Microservice

### Instructions
1. After connecting, input the maximum number.
2. Read the generated random number sent by the server.


## UML Diagram:


![UML](https://github.com/ValdezGabe/CS361/assets/171638979/c51c836e-bf96-43ce-9bba-a04e0e7cb813)
