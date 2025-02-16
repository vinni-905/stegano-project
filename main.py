from stego import hide_message, extract_message

if __name__ == "__main__":
    choice = input("Choose operation - Encode (e) / Decode (d): ").strip().lower()
    
    if choice == 'e':
        image_path = input("Enter image file path: ")
        secret_message = input("Enter secret message: ")
        password = input("Enter a password: ")
        output_path = "encoded_image.png"
        hide_message(image_path, secret_message, password, output_path)
    
    elif choice == 'd':
        image_path = input("Enter encoded image file path: ")
        password = input("Enter the password for decryption: ")
        extract_message(image_path, password)
    
    else:
        print("Invalid choice. Please enter 'e' for encoding or 'd' for decoding.")
