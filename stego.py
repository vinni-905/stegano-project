import cv2
import numpy as np
import os
from encrypt_decrypt import encrypt_message, decrypt_message

def text_to_binary(text):
    """Converts text to binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_data):
    """Converts binary to readable text."""
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def is_valid_image(image_path):
    """Checks if the image exists and is a valid format."""
    if not os.path.exists(image_path):
        print(f"❌ Error: File not found at {image_path}")
        return None

    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Error: OpenCV could not load the image. Unsupported format or corrupted file: {image_path}")
        return None

    return img

def hide_message(image_path, message, password, output_path="encoded_image.png"):
    """Hides an encrypted message inside an image using LSB Steganography."""
    img = is_valid_image(image_path)
    if img is None:
        return
    
    encrypted_message = encrypt_message(message, password)  # Encrypt the message
    encrypted_message += "~"  # Special delimiter to mark end of the message
    binary_message = text_to_binary(encrypted_message)  # Convert encrypted text to binary

    rows, cols, channels = img.shape
    total_pixels = rows * cols * channels

    # Ensure the image is large enough
    if len(binary_message) > total_pixels:
        print(f"❌ Error: Image is too small to hide the message.")
        print(f"🔍 Image Pixels: {total_pixels}, Required Bits: {len(binary_message)}")
        print(f"💡 Try using a larger image OR a shorter message.")
        return

    data_index = 0

    for row in range(rows):
        for col in range(cols):
            for channel in range(3):  # Iterate over RGB channels
                if data_index < len(binary_message):
                    pixel_value = img[row, col, channel] & 254  # Ensure only LSB is modified
                    bit_value = int(binary_message[data_index]) & 1  # Ensure only 0 or 1 is stored
                    img[row, col, channel] = pixel_value | bit_value
                    data_index += 1
                else:
                    break

    cv2.imwrite(output_path, img)
    print(f"✅ Message successfully hidden in {output_path}.")

def extract_message(image_path, password):
    """Extracts and decrypts the hidden message from the image."""
    img = is_valid_image(image_path)
    if img is None:
        return

    binary_message = ""

    for row in img:
        for pixel in row:
            for channel in pixel:
                binary_message += str(channel & 1)  # Extract only 1-bit per pixel

    # Convert binary to text
    decoded_message = binary_to_text(binary_message)

    # Stop at the delimiter (~) and extract encrypted message
    if "~" in decoded_message:
        encrypted_message = decoded_message[:decoded_message.index("~")]

        # Decrypt the message
        try:
            decrypted_message = decrypt_message(encrypted_message, password)
            print("✅ Decrypted Message:", decrypted_message)
        except:
            print("❌ Error: Incorrect password or corrupted message!")
    else:
        print("❌ No hidden message found.")
