# Permutations 
FIXED_IP = [2, 6, 3, 1, 4, 8, 5, 7]
FIXED_EP = [4, 1, 2, 3, 2, 3, 4, 1]
FIXED_IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
FIXED_P4 = [2, 4, 3, 1]

# Key generation permutations
FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9]

# S-boxes for lookup to generate keys
S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

# Driver key
KEY = '1010000010'

# Permute bits using original and fixed permutations
def permutate(original, fixed):
    result = ""
    for i in fixed:
        result += original[i - 1]
    return result

# Extract left half bits
def left_half(bits):
    return bits[: len(bits)//2]

# Extract right half bits
def right_half(bits):
    return bits[len(bits)//2:]

# Shift the left half and right half by 1 circular shift and then concatenate them as a result
def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half

# Generate key 1
def key1():
    return permutate(shift(permutate(KEY, FIXED_P10)), FIXED_P8)

# Generate key 2
def key2():
    return permutate(shift(shift(shift(permutate(KEY, FIXED_P10)))), FIXED_P8)

# XOR operation between two strings with binary representation
def xor(bits, key):
    result = ""
    for bit, keyBit in zip(bits, key):
        result += str(((int(bit) + int(keyBit)) % 2))
    return result

# Lookup in S-boxes
def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])

# F function for regular process
def f_k(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(R, FIXED_EP)
    bits = xor(bits, key)
    bits = lookup_in_sbox(left_half(bits), S0) + \
        lookup_in_sbox(right_half(bits), S1)
    bits = permutate(bits, FIXED_P4)
    return xor(bits, L)

# Encryption 
def encryption(plain_text):
    bits = permutate(plain_text, FIXED_IP)
    temp = f_k(bits, key1())
    bits = right_half(bits) + temp
    bits = f_k(bits, key2())
    return permutate(bits + temp, FIXED_IP_INVERSE)

# Decryption 
def decryption(cipher_text):
    bits = permutate(cipher_text, FIXED_IP)
    temp = f_k(bits, key2())
    bits = right_half(bits) + temp
    bits = f_k(bits, key1())
    return permutate(bits + temp, FIXED_IP_INVERSE)

# Main code 
message = input("Enter the message: ")
cipherText = encryption(message)
print("Cipher text:", cipherText)
plainText = decryption(cipherText)
print("Plain text:", plainText)
