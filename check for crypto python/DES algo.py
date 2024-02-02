from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad_text(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad_text(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text.rstrip(b' ')

def get_key():
    key = input("Enter the 8-byte key in hexadecimal format (e.g., 0011223344556677): ").encode('utf-8')
    if len(key) != 8:
        print("Invalid key length. Key must be 8 bytes.")
        return get_key()
    return key

def main():
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the text to encrypt: ").encode('utf-8')
            key = get_key()
            ciphertext = encrypt(plaintext, key)
            print("Encrypted Text:", ciphertext.hex())

        elif choice == '2':
            ciphertext = bytes.fromhex(input("Enter the ciphertext to decrypt: "))
            key = get_key()
            decrypted_text = decrypt(ciphertext, key)
            print("Decrypted Text:", decrypted_text.decode('utf-8'))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
