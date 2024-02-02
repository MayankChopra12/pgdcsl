import string

def pad_text(text, block_size):
    padding_size = block_size - (len(text) % block_size)
    padded_text = text + string.ascii_uppercase[:padding_size]
    return padded_text

def unpad_text(text):
    padding_size = ord(text[-1]) - ord('A') + 1
    unpadded_text = text[:-padding_size]
    return unpadded_text

def xor(a, b):
    result = ''
    for x, y in zip(a, b):
        if x.isalpha() and y.isalpha():
            result += chr((ord(x) - ord('A') + ord(y) - ord('A')) % 26 + ord('A'))
        else:
            result += x
    return result

def feistel_cipher(text, rounds, key, block_size):
    text = pad_text(text, block_size)
    left, right = text[:len(text)//2], text[len(text)//2:]

    for round in range(rounds):
        temp = right
        key_round = key + str(round)  # Change the key in each round
        right = xor(left, function(right, key_round))
        left = temp

    final_text = left + right
    return final_text

def feistel_decipher(text, rounds, key, block_size):
    left, right = text[:len(text)//2], text[len(text)//2:]

    for round in range(rounds - 1, -1, -1):
        temp = left
        key_round = key + str(round)  # Change the key in each round
        left = xor(right, function(left, key_round))
        right = temp

    final_text = left + right
    final_text = unpad_text(final_text)  # Unpad after decryption
    return final_text

def function(data, key):
    return xor(data, key)

# Example usage:
plaintext = "HelloFeistelCipher"
key = "SecretKey"
rounds = 16
block_size = 8

# Encryption
cipher_text = feistel_cipher(plaintext, rounds, key, block_size)
print("Original Text:", plaintext)
print("Encrypted Text:", cipher_text)

# Decryption
decrypted_text = feistel_decipher(cipher_text, rounds, key, block_size)
print("Decrypted Text:", decrypted_text)
