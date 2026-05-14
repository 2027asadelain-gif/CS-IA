import socket
from database import insert_message
HEADER = 64
PORT = 8080
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = "10.18.113.157" 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# function to send messages to the server
def send(msg):
    message = msg.encode(FORMAT)

    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    response = client.recv(2048).decode(FORMAT)
    print(response)

# Main loop to send messages to the server
print("[CONNECTED] You are connected to the server.")
print(f"Type {DISCONNECT_MESSAGE} to disconnect.")

while True:
    msg = input("Message: ")
    send(msg)
    insert_message(msg)

    if msg == DISCONNECT_MESSAGE:
        break

client.close()
print("[CLIENT CLOSED]")