import socket
from encryption import decrypt_image

def start_server(port, key):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print(f"Server listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")
        
        with open('encrypted_image.enc', 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        decrypt_image(key, 'encrypted_image.enc')
        client_socket.close()

if __name__ == "__main__":
    PORT = 12345
    AES_KEY = b'Sixteen byte key'  # Use a secure key in production
    start_server(PORT, AES_KEY)
