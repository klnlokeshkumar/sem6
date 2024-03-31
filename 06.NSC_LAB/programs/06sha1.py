import struct # used to covert python values and c structs

def leftShift(n, b):
    return ((n << b) | (n >> (32-b))) & 0xffffffff

def sha1(message):
    # bytes and bits calculation
    orgByteLen = len(message)
    orgBitlen = orgByteLen * 8

    #appending padding and message length to the original message
    message += b'\x80' # appends 10000000 sequence byte to message
    message += b'\x00' * ((56 - (orgByteLen + 1) % 64) % 64) # appending remaining 00000000 bits
    message += struct.pack('>Q', orgBitlen) # appending length
    
    # initialising registers
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # divide the padded message into 512 bit blocks or 64 byte blocks
    for i in range(0, len(message), 64):
        chunk = message[i: i + 64]
        
        # dividing them furthur into 32 bit blocks or 4 byte blocks
        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j * 4: j * 4 + 4])[0]
        
        # generating remaining words from previous
        for j in range(16, 80):
            w[j] = leftShift(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
        
        # initialise abcde with h values
        a, b, c, d, e = h0, h1, h2, h3, h4

        # process block i.e f(t)
        for j in range(80):
            if j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
        
            tempE = e + f + leftShift(a, 5) + w[j] + k & 0xffffffff
            e = d
            d = c
            c = leftShift(b, 30)
            b = a
            a = tempE

        # update outer h values 
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
    
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


message = input("Enter the message: ").encode()
hashCode = sha1(message)
print("Hash code of ", message, " is ", hashCode)
transferredMessage = input("Enter the transferred message: ").encode()
hashCode1 = sha1(transferredMessage)
if(hashCode == hashCode1):
    print("Authenticated")
else:
    print("Not a Autorised....")