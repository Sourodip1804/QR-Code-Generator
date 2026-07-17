import qrcode

# required_libraries = ["qrcode"]

url =input("Enter the URL to generate QR code: ")
file_path = "C:\\Users\\user\\OneDrive\\Desktop\\"folder name"\\qrcode.png"

# creating a object for the QR code

qr = qrcode.QRCode()

# adding data to the object
qr.add_data(url)

# creating an image object for the QR code
img = qr.make_image()

# to save the image in the specified file path
img.save(file_path)

print("QR code was generated and saved successfully at:", file_path)
