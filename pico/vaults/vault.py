array = bytearray("jU5t_a_sna_3lpm13gc49_u_4_m0rf41", "utf-8")
result = bytearray("jU5t_a_sna_3lpm13gc49_u_4_m0rf41" , "utf-8")
for i in range(8,16):
    result[i] = array[23-i]

for i in range(16, 32):
    result[i] = array[46-i]

i = 31
while i >= 17:
    result[i] = array[i]
    i -= 2

print(result)

str = ""
dec = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98]
res = []
hex = "\x55\x6e\x43\x68\x5f\x30\x66\x5f"
oct = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o62 , 0o60]
let = ['1' , 'b' , '3' , '5' , '2' , 'd' , '6' , 'c']
for i in dec:
    res.append(chr(i))

res.append(hex)
for i in oct:
    res.append(chr(i))

res = res + let

print(str.join(res))

str = "w1{1wq80haib767"
result = ""
index = 0
for i in str:
    if index % 2 == 0:
        result += chr(ord(i) - 5)
    else:
        result += chr(ord(i) + 2)
    index += 1
print(result)
