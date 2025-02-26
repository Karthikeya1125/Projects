import cv2
import os

# Corrected image path
image_path = r"C:\Users\valis_8zc26ia\OneDrive\Pictures\Default.jpg"

# Load image and check if it exists
img = cv2.imread(image_path)
if img is None:
    print("Error: Image file not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

m, n, z = 0, 0, 0

# Encode message in the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

# Save the modified image
cv2.imwrite(image_path, img)
os.system(f"start {image_path}")  # Fixed path handling

# Decryption
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
