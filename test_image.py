import cv2

image_path = r"C:\Users\own\Pictures\icon.png"  # Make sure the path is correct
img = cv2.imread(image_path)

if img is None:
    print("❌ Error: OpenCV could not load the image. Check the file path and format.")
else:
    print("✅ Success: Image loaded!")
    print("Image Shape:", img.shape)
