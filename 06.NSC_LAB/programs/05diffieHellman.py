# calculate pow with modulo p
def moduloPower(base, exp, mod):
    result = 1
    for i in range(exp):
        result = result*base%mod
    return result

# Comman shared values prime number and primitive root
p = int(input("Enter the prime number(p): "))
a = int(input("Enter the Primitive root of p(alpha): "))
prA = int(input("Enter the private key of A: "))
prB = int(input("Enter the private key of B: "))
puA = moduloPower(a, prA, p) # pow(base, exp, mod)
puB = moduloPower(a, prB, p) # for k inverse => pow(k, -1, mod)
print("Public Key of A: ", puA)
print("Public key of B: ", puB)

# checking 
if moduloPower(puB, prA, p) == moduloPower(puA, prB, p):
    print("Key exhange successful")
else :
    print("Not successful")
