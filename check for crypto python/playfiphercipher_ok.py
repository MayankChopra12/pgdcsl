def prepare_text(text):
    # Remove spaces and convert to uppercase
    print("removing spaces and replacing J with I")
    text = text.replace(" ", "").upper()
    # Replace 'J' with 'I'
    text = text.replace("J", "I")
    return text

def generate_key_matrix(key):
    key = prepare_text(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []

    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)
            print("in generate_key_matrix (duplicate removing) updated key_matrix: ", key_matrix)

    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
            print("now adding the remaning non duplicate alphabets---------------------------------------------------")
            print("alphabets total" ,"ABCDEFGHIKLMNOPQRSTUVWXYZ")
            print("in generate_key_matrix (duplicate removing) updated key_matrixforAlphabets: ", key_matrix)

    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
   
    

    
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                print("find the position in matrix of char (i, j) : ","alphabet is:", matrix[i][j],"position: ", i, " ",j)
                return i, j

def encrypt_playfair(plaintext, key):
    print("encrypting the cipher")
    plaintext = prepare_text(plaintext)
    key_matrix = generate_key_matrix(key)

    print("printing the matrix first")
    print("[")
    for i in range(5):
        for j in range(5):
                print(key_matrix[i][j],end=",")
                if(j==4):
                    print("")
        if(i==4):
            print("]")
            
    cipher = ""

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]

        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            print("rows are same columns increasing % with 5 to get poisition")
            print("only position change when it is 5%5 =0 otherwise the number only")
            cipher += key_matrix[row1][(col1 + 1) % 5]
            cipher += key_matrix[row2][(col2 + 1) % 5]
            print("updated poistion after cipher" ,"first character :" ,key_matrix[row1][(col1 + 1) % 5]," second character :",key_matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            cipher += key_matrix[(row1 + 1) % 5][col1]
            cipher += key_matrix[(row2 + 1) % 5][col2]
            print("updated poistion after cipher" ,"first character :" ,key_matrix[(row1 + 1) % 5][col1]," second character :",key_matrix[(row2 + 1) % 5][col2])
        else:
            cipher += key_matrix[row1][col2]
            cipher += key_matrix[row2][col1]
            print("updated poistion after cipher" ,"first character :" ,key_matrix[row1][col2]," second character :",key_matrix[row2][col1])

    return cipher

def decrypt_playfair(ciphertext, key):
    print("deencrypting the cipher")
    ciphertext = prepare_text(ciphertext)
    key_matrix = generate_key_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5]
            plaintext += key_matrix[row2][(col2 - 1) % 5]
            print("updated poistion after cipher" ,"first character :" ,key_matrix[row1][(col1 - 1) % 5]," second character :",key_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1]
            plaintext += key_matrix[(row2 - 1) % 5][col2]
            print("updated poistion after cipher" ,"first character :" ,key_matrix[(row1 - 1) % 5][col1]," second character :",key_matrix[(row2 - 1) % 5][col2])
        else:
            plaintext += key_matrix[row1][col2]
            plaintext += key_matrix[row2][col1]
            print("updated poistion after cipher" ,"first character :" ,key_matrix[row1][col2]," second character :",key_matrix[row2][col1])

    return plaintext

# Example usage:
plaintext = input("enter the text to encrypt")
key = input("enter the key to encrypt")
encrypted_text = encrypt_playfair(plaintext, key)
decrypted_text = decrypt_playfair(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text.lower())
