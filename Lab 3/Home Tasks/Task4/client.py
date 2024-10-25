import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = str(msg).encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    salary = client.recv(2048).decode(FORMAT)
    
    if salary == "Goodbye":
        print(salary)
    else:
        print(f"Salary: Tk {salary}")

connected = True

while connected:
    input_message= input("Enter the number of hours worked: ")
    if input_message== "Done":
        connected = False
        send(DISCONNECT_MESSAGE)
    else: 
        send(input_message)