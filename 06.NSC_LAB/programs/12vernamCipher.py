# Encryption and decryption 
def encDec(text, key):
    result= ""
    for i in range(len(text)):
        temp = (ord(text[i]) - ord('a')) ^ (ord(key[i]) - ord('a'))  # Performing XOR operation
        result += chr(ord('a') + temp)  # Converting back to character
    return result

message = input("Enter the message: ")
key = input("Enter the key: ")

# Enumerate key to length of message
while len(key) < len(message):
    key += key

cipherText = encDec(message, key)
print("Cipher text: ", cipherText)

# Decryption
plainText = encDec(cipherText, key)
print("Plain text: ", plainText)
