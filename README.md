# 🖼️ Secure Data Hiding in Images Using Steganography

This project implements **LSB (Least Significant Bit) Steganography** to securely **hide and extract secret messages inside images**. It also uses **AES encryption** to protect the data before embedding it into an image.

## 🚀 Features
✔ **Hide Secret Messages** – Encrypt and store messages inside images  
✔ **Extract Messages** – Retrieve and decrypt hidden messages  
✔ **Password Protection** – Only the correct password can decrypt the message  
✔ **Supports Small & Large Images** – Works with PNG, BMP, and non-lossy formats  
✔ **Error Handling** – Prevents data loss due to small images  

## 🛠️ Technologies Used
- **Python**
- **OpenCV (`cv2`)** – Image Processing
- **NumPy** – Data Manipulation
- **PyCryptodome** – AES Encryption & Decryption

---

## 📥 Installation
1️⃣ **Clone the Repository**  
   ```sh
   git clone https://github.com/vinni-905/stegano-project.git
   cd stegano-project
