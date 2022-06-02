import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("localhost", 3001))
    server.listen()
    conn, addr = server.accept()
    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode())
            conn.sendall(data)
        