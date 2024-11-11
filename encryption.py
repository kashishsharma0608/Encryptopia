from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def generate_key():
    """Generate a random 16-byte AES key."""
    return os.urandom(16)

def save_key(key, filename='key.bin'):
    """Save the AES key to a file."""
    try:
        with open(filename, 'wb') as key_file:
            key_file.write(key)
        print(f"Key saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the key: {e}")

def load_key(filename='key.bin'):
    """Load the AES key from a file."""
    try:
        with open(filename, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        print(f"Error: The key file '{filename}' was not found.")
        raise
    except Exception as e:
        print(f"An error occurred while loading the key: {e}")
        raise

def encrypt_image(key, image_path, output_path='encrypted_image.enc'):
    """Encrypt an image file."""
    cipher = AES.new(key, AES.MODE_CBC)
    
    try:
        with open(image_path, 'rb') as file:
            plaintext = file.read()
        
        # Encrypt the plaintext
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        
        # Save the IV and the ciphertext
        with open(output_path, 'wb') as file:
            file.write(cipher.iv + ciphertext)
        
        print(f"Image encrypted successfully! Output saved to {output_path}.")
    except FileNotFoundError:
        print(f"Error: The image file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while encrypting the image: {e}")

def decrypt_image(key, encrypted_image_path, output_path='decrypted_image.png'):
    """Decrypt an encrypted image file."""
    try:
        with open(encrypted_image_path, 'rb') as file:
            file_content = file.read()
            if len(file_content) < 16:
                raise ValueError("The encrypted file is too short to contain a valid IV.")
            iv = file_content[:16]  # Read the first 16 bytes as IV
            ciphertext = file_content[16:]
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        
        # Save the decrypted image
        with open(output_path, 'wb') as file:
            file.write(plaintext)
        
        print(f"Image decrypted successfully! Output saved to {output_path}.")
    except FileNotFoundError:
        print(f"Error: The encrypted image file '{encrypted_image_path}' was not found.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred while decrypting the image: {e}")
# Example Usage
if __name__ == "__main__":
    # Generate a key (do this once and save it)
    # key = generate_key()
    # save_key(key)
    
    # Load the key from the saved file
    key = load_key()

    # Encrypt an image
    encrypt_image(key, 'imageONE.png', 'encrypted_image.enc')

    # Decrypt the image
    decrypt_image(key, 'encrypted_image.enc', 'decrypted_image.png')









