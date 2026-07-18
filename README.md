# Py-Encrypt
This python script is designed to encrypt and decrypt files using fernet. This is a symmetric form of encryption. The script is complete with a graphical interface and ability to store the encryption key locally on the device. The path to store the key and path of the file can be provided. Keys can be generated or custom made however do note that a custom key will also be converted into 32 bytes encoded with URL-safe base64. This allows for users to easily change and remember the key meanwhile the actual key being used in the script is much more secure. Please note that if the check box to save the master key to a local file is enabled and wipe memory button is pressed, the key will be removed from not only the local memory but also from the file. Be mindful to not overwrite the encryption key and do not use this software to create any form of ransomware.

## Overview
Py-Encrypt is a simple file encryption utility built with Python and `tkinter`. It uses the `cryptography.fernet` module for symmetric encryption and provides a lightweight user interface for managing encryption keys and encrypting or decrypting a selected file.

## Features
- Graphical user interface for easy use
- Symmetric encryption with `Fernet`
- Generate secure encryption keys automatically
- Use a custom key phrase and convert it securely to a valid Fernet key
- Optionally save the active key to a local file
- Encrypt and decrypt files from a specific path
- Clear the in-memory key value from the GUI

## How It Works
1. The script loads or generates a Fernet key.
2. A custom string key is converted to a 32-byte secret by hashing with SHA-256 and then encoding with URL-safe base64.
3. The GUI allows the user to choose whether to save the active key to a local file.
4. The user enters the path to the target file and clicks `Encrypt File` or `Decrypt File`.

## Versions

### Desktop Version (`main.py`)
Traditional tkinter GUI application for local use on your computer.

### Web Version (`app.py`)
Streamlit web application - deploy to the cloud and access from any browser.

## Requirements
- Python 3.7+
- `cryptography` Python package
- `tkinter` for the desktop version (standard library)
- `streamlit` for the web version

## Installation

### Desktop Version
1. Install Python if it is not already installed.
2. Install the required package:

```bash
pip install cryptography
```

### Web Version (Streamlit)
```bash
pip install -r requirements.txt
```

## Usage

### Desktop Version (local)
1. Place the script `main.py` in the same folder as your target files, or run it from any folder.
2. Run the script:

```bash
python main.py
```

3. In the GUI:
- Click `Generate Key` to create a secure new key.
- Enter a custom key in the text box if you want to use a memorable password-like value.
- Check `Local key = File Saved Key` to save the key to disk, then provide the key file path.
- Enter the path of the file you want to encrypt or decrypt.
- Click `Encrypt File` or `Decrypt File`.
- Click `Clear key memory` to reset the current key in the GUI.

### Web Version (Streamlit - Local)
```bash
streamlit run app.py
```

### Web Version (Deploy to Cloud)

**Option 1: Streamlit Cloud (Recommended)**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click "New app" and connect your GitHub repository
4. Select the repository, branch, and set `app.py` as the main file
5. Click Deploy
6. Your app will be live at a URL like: `https://yourname-cryptography.streamlit.app`

**Features of the web version:**
- Upload files directly from your browser
- Generate or paste encryption keys
- Download encrypted/decrypted files
- Works on any device with internet access
- No installation required

## Notes and Warnings
- Do not overwrite your encryption key file once it is created unless you intend to lose access to previously encrypted files.
- If key saving is enabled and you clear the key memory, the saved key file may also be cleared depending on script behavior.
- This tool is designed for legitimate file protection only. Do not use it to create ransomware or any malicious software.
- Always keep backup copies of important files before encrypting them.

## File Structure
- `main.py` - main application script
- `test.py` - any test or helper script present in the repository
- `encryption_key.key` - default key file used by the application if present

## Custom Key Behavior
When a custom key is entered, the script:
- hashes the input string with SHA-256,
- converts the hash to a URL-safe base64-encoded key,
- then uses that result as the actual Fernet key.

This means your chosen phrase is easier to remember, while the real key used for encryption is secured in a format accepted by Fernet.

## Disclaimer
Py-Encrypt is intended for educational and personal use. Encryption is a powerful tool, but it must be used responsibly. Always test encryption and decryption on non-critical files first.
