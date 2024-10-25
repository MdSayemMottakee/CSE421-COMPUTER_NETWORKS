import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION...] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == "End":
                connected = False
                conn.send("Goodbye".encode(FORMAT))
            else:
                hours_worked = int(msg)
                if hours_worked > 40:
                    salary = 8000 + (hours_worked - 40) * 300
                else:
                    salary = hours_worked * 200
                conn.send(str(salary).encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print("[LISTENING] Server is listening.......")  
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #print(f"Total clients connected currently: {threading.activeCount() - 1}")
start()