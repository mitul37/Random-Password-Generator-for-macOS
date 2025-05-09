# MacPasswordGen 🔐

A simple, lightweight macOS password generator app built with Python and Tkinter.  
Easily generate random, secure passwords with customizable length and character types!

## ✨ Features
- Select password length
- Choose character sets:
  - Uppercase (A-Z)
  - Lowercase (a-z)
  - Digits (0-9)
  - Symbols (!@#$...)
- Simple, clean GUI
- Native `.app` packaging for macOS

## 🚀 How to Run

1️⃣ **Install Dependencies**
```bash
pip install pyinstaller

2️⃣ **Run the Script Directly**
python main.py

3️⃣ **Package as macOS App**
pyinstaller --onefile --windowed --name "MacPasswordGen" main.py

The app will be available in the dist folder.

🏗 Build Requirements
Python 3.x

Tkinter (usually comes pre-installed)

PyInstaller (for packaging)

📜 License
This project is licensed under the MIT License. See LICENSE for details.

❤️ Credits
Developed with 💛 by [Mitul_Joarder].
