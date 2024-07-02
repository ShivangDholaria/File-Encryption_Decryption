from cryptography.fernet import Fernet
import os

# Key generator
def generate_key():
    return Fernet.generate_key()                    #Returns generated key

# Save key in a file
def save_generate_key(key, key_file):
    with open(key_file, 'wb') as f:
        f.write(key)

# Load key from the file
def load_key_file(key_file):
    with open(key_file, 'rb') as f:
        return f.read()

# File encryption
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        file_data = file.read()

    f = Fernet(key)                                 # Fernet object for encryption/decryption
    encrypted_data = f.encrypt(file_data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
        
# File decryption
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

if __name__ == '__main__':
    file_name = input("Enter the file name to encrypt it: ")

    # Check if file exists
    if not open(file_name):                             
        print("File not found")
        SystemExit

    # Opening file
    file_to_encrypt = file_name

    splt_file_name = file_name.split(".")

    encrypted_file = f"{splt_file_name[0]}_encrypted.txt"
    decrypted_file = f"{splt_file_name[0]}_decrypted.txt"

    if not os.path.isfile('./key.key'):
        # Generating and storing key
        key = generate_key()
        key_file = 'key.key'
        save_generate_key(key, key_file)
    else:
        key = load_key_file('key.key')

    # Encrypting file
    encrypt_file(file_to_encrypt, encrypted_file, key)
    print(f"File encrypted successfully.\n Saved as {encrypted_file}")

    # Decrypting file
    decrypt_file(encrypted_file, decrypted_file, key)
    print(f"File decrypted successfully.\n Saved as {decrypted_file}")
