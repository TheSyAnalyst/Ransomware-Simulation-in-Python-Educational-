from cryptography.fernet import Fernet
import os

# Load the key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)
target_dir = "test_files"

# Decrypt all .txt files except ransom note
for file in os.listdir(target_dir):
    if file == "ransom_note.txt":
        continue
    file_path = os.path.join(target_dir, file)
    with open(file_path, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(file_path, "wb") as f:
        f.write(decrypted)

print("[+] Files decrypted.")
