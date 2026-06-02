from cryptography.fernet import Fernet
import tkinter as tk
import base64
import hashlib

#symmetric encryption

with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()


key=None
fernet = Fernet(key)

def convert_key(input_key):
    try:
        print(input_key)
        decoded = base64.urlsafe_b64decode(input_key.encode())

        # Fernet keys decode to exactly 32 bytes
        if len(decoded) == 32:
            return input_key.encode()
        if input_key=="":
            return ""

    except Exception:
        pass

    # Convert normal password/string into Fernet key
    hashed_key = hashlib.sha256(input_key.encode()).digest()
    return base64.urlsafe_b64encode(hashed_key)

def generate_key():
    key = Fernet.generate_key()
    if check_var.get():
        with open(str(key_path_entry.get()), 'wb') as key_file:
            key_file.write(key)
    user_key.set(key.decode())

def show_check():
    if check_var.get():
        key_change(None, None, None)
        key_label.pack()
        key_path_entry.pack()
    else:
        key_label.pack_forget()
        key_path_entry.pack_forget()

def encrypt_file(path):
    print(key)
    file_path = path
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(path):
    file_path = path
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

def clear():
    user_key.set("")
    #key = user_key.get().encode()

def key_change(var_name, index, mode):
    global fernet, key
    new_key = convert_key(user_key.get())
    if not new_key:
        return
    key = new_key
    fernet = Fernet(key)
    if check_var.get():
        try:
            with open(str(key_path_entry.get()), 'wb') as key_file:
                key_file.write(key)
        except:
            pass

root = tk.Tk()

default_path = tk.StringVar(value="encryption_key.key")
user_key = tk.StringVar(value=key.decode())

root.title("Encryption Key Generator")
root.geometry("720x480")
gen_button = tk.Button(root, text="Generate Key", command=generate_key)
gen_button.pack(pady=10)


key_label = tk.Entry(root, width=70, textvariable=user_key)
key_label.pack(pady=5)
user_key.trace_add("write",key_change)

check_var = tk.BooleanVar()
check_button = tk.Checkbutton(root, text="Local key = File Saved Key", variable=check_var,command=show_check)
check_button.pack()


key_label = tk.Label(root, text="Saved Key Path:")
key_label.pack_forget()
key_path_entry = tk.Entry(root, width=30,text="encryption_key.key",textvariable=default_path)
key_path_entry.pack_forget()

label = tk.Label(root, text="Enter the path of the file to encrypt:")
label.pack(pady=5)
path_entry = tk.Entry(root, width=30)
path_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt File", command=lambda: encrypt_file(path_entry.get()))
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt File", command=lambda: decrypt_file(path_entry.get()))
decrypt_button.pack(pady=10)

done_label = tk.Button(root, text="Clear key memory",command=lambda: clear())
done_label.pack(pady=5)

root.mainloop()
