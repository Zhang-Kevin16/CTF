def switchBits(n, p1, p2):

    ''' Move p1'th to rightmost side '''
    bit1 = (n >> p1) & 1

    ''' Move p2'th to rightmost side '''
    bit2 = (n >> p2) & 1

    ''' XOR the two bits '''
    x = (bit1 ^ bit2)

    ''' Put the xor bit back to their
        original positions '''
    x = (x << p1) | (x << p2)

    ''' XOR 'x' with the original number
        so that thetwo sets are swapped '''
    result = n ^ x
    return result

arr = [0xF4,
0xC0,
0x97,
0xF0,
0x77,
0x97,
0xC0,
0xE4,
0xF0,
0x77,
0xA4,
0xD0,
0xC5,
0x77,
0xF4,
0x86,
0xD0,
0xA5,
0x45,
0x96,
0x27,
0xB5,
0x77,
0xF1,
0xC1,
0xF0,
0x94,
0xC1,
0xA5,
0xC1,
0xC2,
0xA4]

def unscramble(c):
    c = switchBits(c, 1, 2)
    c = switchBits(c, 0, 3)
    c = switchBits(c, 5, 6)
    c = switchBits(c, 4, 7)
    c = switchBits(c, 0, 1)
    c = switchBits(c, 3, 4)
    c = switchBits(c, 2, 5)
    c = switchBits(c, 6, 7)
    return c

ret = []
str = ""
for c in arr:
    str += chr(unscramble(c))
print(unscramble(0xF4))

print(str)
