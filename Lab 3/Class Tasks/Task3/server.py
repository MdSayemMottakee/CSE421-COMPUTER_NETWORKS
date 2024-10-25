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
                vowels = 'aeiouAEIOU'
                num_vowels = 0
                for char in msg:
                    if char in vowels:
                        num_vowels += 1
                if num_vowels == 0:
                    conn.send("Not enough vowels".encode(FORMAT))
                elif num_vowels <= 2:
                    conn.send("Enough vowels I guess".encode(FORMAT))
                else:
                    conn.send("Too many vowels".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print("[LISTENING] Server is listening......")  
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"\nTotal clients connected currently: {threading.activeCount() - 1}")
start()