import hashlib
import random
from math import gcd

p = 23
g = 5

def generate_private_key(p):
    return random.randint(1, p - 1)

def generate_public_key(p, g, x):
    return pow(g, x, p)

def sign_message(message, p, g, x):
    while True:
        k = random.randint(1, p - 1)
        r = pow(g, k, p) % p
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        s = (x * r + k * h) % (p - 1)
        if gcd(s, p - 1) == 1:
            break
    return r, s

def verify_signature(message, r, s, p, g, y):
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    w = pow(s, -1, p - 1)
    u1 = (h * w) % (p - 1)
    u2 = (r * w) % (p - 1)
    v = (pow(g, u1, p) * pow(y, u2, p)) % p
    return v == r

message = input("Enter the message to sign: ")
x = generate_private_key(p)
y = generate_public_key(p, g, x)
r, s = sign_message(message, p, g, x)
print(f"Message: {message}")
print(f"Public Key (y): {y}")
print(f"Signature (r, s): ({r}, {s})")
print(f"Signature verified: {verify_signature(message, r, s, p, g, y)}")