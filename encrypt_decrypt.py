import base64
import hashlib
from Crypto.Cipher import AES

def pad_message(message):
    """Pads the message to be a multiple of 16 bytes (AES block size)."""
    return message + (16 - len(message) % 16) * " "

def encrypt_message(secret_message, password):
    """Encrypts a message using AES-256 encryption."""
    key = hashlib.sha256(password.encode()).digest()  # Generate 256-bit key
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad_message(secret_message).encode())
    return base64.b64encode(encrypted_bytes).decode()  # Convert to readable format

def decrypt_message(encrypted_message, password):
    """Decrypts an AES-256 encrypted message."""
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_bytes.decode().strip()  # Remove padding
