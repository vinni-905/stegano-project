import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import cv2
import numpy as np
from stego import extract_message  # Import the function from stego.py

def open_and_decode():
    """Function to open an encoded image and extract the hidden message."""
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG Images", "*.png")])
    
    if file_path:
        password = simpledialog.askstring("Password", "Enter the decryption password:", show="*")  # Ask for password
        
        if not password:
            messagebox.showerror("Error", "Password cannot be empty.")
            return
        
        try:
            extracted_message = extract_message(file_path, password)  # Call the extract function

            if extracted_message:
                messagebox.showinfo("Decoded Message", f"🔍 Hidden Message:\n{extracted_message}")
            else:
                messagebox.showerror("Error", "❌ Incorrect password or no hidden message found.")

        except Exception as e:
            messagebox.showerror("Error", f"⚠️ An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Steganography Decoder")
root.geometry("400x200")

label = tk.Label(root, text="🔍 Click below to select an image and extract a hidden message:", pady=10)
label.pack()

btn = tk.Button(root, text="Open Encoded Image", command=open_and_decode, bg="#3498db", fg="white", padx=10, pady=5)
btn.pack()

root.mainloop()
