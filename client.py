import socket
from encryption import encrypt_image

def send_image(server_ip, port, image_path):
    # Encrypt the image before sending
    AES_KEY = b'Sixteen byte key'  # Use the same secure key as the server
    encrypt_image(AES_KEY, image_path)
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    with open('encrypted_image.enc', 'rb') as file:
        client_socket.sendall(file.read())

    print("Image sent successfully!")
    client_socket.close()

if __name__ == "__main__":
    SERVER_IP = '127.0.0.1'  # Change to server's IP if needed
    PORT = 12345
    IMAGE_PATH = 'imageONE.png'  # Specify the image path
    send_image(SERVER_IP, PORT, IMAGE_PATH)
