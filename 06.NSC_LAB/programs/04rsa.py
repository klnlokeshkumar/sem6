# RSA Encryption and Decryption

import random

# Function to perform RSA encryption
def rsaEncryption(message, e, n):
    return " ".join([str(chr(pow(ord(char), e, n))) for char in message])

# Function to perform RSA decryption
def rsaDecryption(cipherText, d, n):
    return "".join([str(chr(pow(ord(char), d, n))) for char in cipherText.split()])

# Function to calculate the greatest common divisor (gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to generate public and private keys
def generateKeys(p, q):
    n = p * q
    totient = (p - 1) * (q - 1)

    # Choose a random integer e such that 1 < e < totient and gcd(e, totient) = 1
    e = random.randint(2, totient - 1)
    while gcd(e, totient) != 1:
        e = random.randint(2, totient - 1)

    # Compute d, the modular multiplicative inverse of e modulo totient
    d = pow(e, -1, totient)

    return ((e, n), (d, n))

# Input prime numbers p and q
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

# Generate public and private keys
public_key, private_key = generateKeys(p, q)

e, n = public_key
d, n = private_key

print("Public key (e, n):", public_key)
print("Private key (d, n):", private_key)

message = input("Enter the message to be encrypted: ")

# Encryption
cipherText = rsaEncryption(message, e, n)
print("Encrypted message (cipherText):", cipherText)

# Decryption
decrypted_message = rsaDecryption(cipherText, d, n)
print("Decrypted message:", decrypted_message)