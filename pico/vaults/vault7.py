from pwn import *

a = [1096770097,1952395366,1600270708,1601398833,1716808014,1734293603,959591523,842097204]
b = []
for x in a:
    b.append(p32(x, endian='big'))
print(b''.join(b))
