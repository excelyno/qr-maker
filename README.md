# qr-maker
## 🚀 QR Maker

Welcome to **QR Maker** – the simplest way to generate QR codes with Python!

---

### 🧩 What is this?

This project is a collection of minimal Python scripts to create QR codes from any link or text you want. Just edit the script, run it, and your QR code image is ready instantly!

---

### 🛠️ How does it work?

- Uses the powerful [`qrcode`](https://pypi.org/project/qrcode/) library.
- You provide your link or text in the script.
- The script generates a QR code and saves it as a PNG image.

---

### 📦 Usage

1. **Install dependencies:**
   ```
   pip install qrcode[pil]
   ```

2. **Edit the script:**
   - For simple usage, open `qr_code1.py`
     - Change `"your link"` to the data you want to encode.
     - Change `"your output name png"` to your desired output file name (e.g., `"my_qr.png"`).
   - For more advanced features and customization, open `qr_code2.py`
     - You can set the QR version, error correction level, box size, QR code color, background color, and output file name.
     - Example parameters you can modify:
       - `version`: QR code complexity level (1-40)
       - `error_correction`: error tolerance level (`qrcode.constants.ERROR_CORRECT_L`, `M`, `Q`, or `H`)
       - `box_size`: size of each QR box
       - `border`: border width
       - `fill_color`: QR code color (e.g., `"black"`, `"red"`, etc.)
       - `back_color`: background color (e.g., `"white"`, `"blue"`, etc.)
       - Data and output file name as you wish

3. **Run the script:**
   ```
   python qr_code1.py
   ```
   or for the more flexible version:
   ```
   python qr_code2.py
   ```

4. **Find your QR code image in the same folder!**

---

### ✨ Example

- **Simple:**  
  Generate a QR code from a link with default settings (`qr_code1.py`).
- **Custom & Advanced:**  
  Generate a QR code with custom color, size, and error correction (`qr_code2.py`).

---

### 📄 File Descriptions

- `qr_code1.py`  
  The simplest script to generate a QR code in just one line.

- `qr_code2.py`  
  A more flexible and customizable script. Perfect if you want to adjust the color, size, error correction, and other QR code parameters.

---
