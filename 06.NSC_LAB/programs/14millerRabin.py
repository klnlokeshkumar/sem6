from random import randint

# finding k value 
def findK(n):
    temp = 0
    while (n)%2 == 0:
        temp += 1
        n = n//2
    return (temp, n)

def millerRabin():
    n = int(input("Enter the number: "))
    k, q = findK(n-1)
    a = randint(2, n-2)
    if pow(a, q, n) == 1:
        return True
    for j in range(k):
        if pow(a, 2**(j*q), n) == n-1:
            return True
    return False
        
if millerRabin():
    print("may be a prime")
else:
    print("composite")
