# 🔳 QR Code Generator using Python

A simple and beginner-friendly Python project that generates QR codes from user-provided URLs using the `qrcode` library. The generated QR code is saved as a PNG image at a specified file location.

## 📌 Features

- Generate QR codes for any URL or text.
- Save the generated QR code as a PNG image.
- Simple command-line interface.
- Easy to understand and beginner-friendly code.
- Customizable output file path.

## 🛠️ Technologies Used

- Python 3
- qrcode
- Pillow (PIL)

## 📂 Project Structure

```
QR-Code-Generator/
│── main.py
└── README.md
```

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/QR-Code-Generator.git
```

2. Navigate to the project folder:

```bash
cd QR-Code-Generator
```

3. Install the required library:

```bash
pip install qrcode[pil]
```

## ▶️ Usage

Run the Python script:

```bash
python main.py
```

You will be prompted to enter a URL:

```text
Enter the URL to generate QR code:
```

Example:

```text
Enter the URL to generate QR code: https://github.com
```

After entering the URL, the QR code will be generated and saved to the specified file path.

## 📄 Example Output

```text
Enter the URL to generate QR code: https://github.com

QR code was generated and saved successfully at:
C:\Users\kouli\OneDrive\Desktop\sourodip engineering\qrcode.png
```

## 💻 Code Overview

The program performs the following steps:

1. Imports the `qrcode` library.
2. Accepts a URL from the user.
3. Creates a `QRCode` object.
4. Adds the URL to the QR code.
5. Generates the QR code image.
6. Saves the image as a PNG file.
7. Displays a success message.

## 📸 Output

The generated QR code will look similar to this:

```
█████████████████████
██ ▄▄▄▄▄ ██ ▄▄▄▄▄ ██
██ █   █ ██ █   █ ██
██ █▄▄▄█ ██ █▄▄▄█ ██
██▄▄▄▄▄▄▄██▄▄▄▄▄▄▄██
██ ▄ ▄▄▄▄ ▄▄ ▄ ▄▄ ██
██▄▄██▄▄▄▄▄▄██▄▄▄▄██
█████████████████████
```

*(The actual QR code will depend on the URL entered.)*

## 🚀 Future Improvements

- Allow users to choose the output file name.
- Generate QR codes for text, email addresses, phone numbers, and Wi-Fi credentials.
- Add support for custom colors and logos.
- Create a graphical user interface (GUI) using Tkinter or PyQt.
- Save QR codes in multiple image formats.

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, improve the project, and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
