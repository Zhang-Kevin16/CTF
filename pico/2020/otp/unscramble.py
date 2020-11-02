def jumble(char):
    num = ord(char)
    if 96 < num:
        num = num + 9
    num = (num & 0xf) * 2
    if 0xf < num:
        num = num + 1
    return num

str = "jbgkfmgkknbiblpmibgkcneiedgokibmekffokamknbkhgnlhnajeefpekiefmjgeogjbflijnekebeokpgngjnfbimlkdjdjhan"

res = ""

# Our input set
candidates = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

# First character
for c in candidates:
    j = jumble(c)
    j = j & 0xf
    j = chr(j + 0x61)
    if j == 'j':
        res += c

# Subsequent characters depend on previous character
for i in range(1, 100):
    for c in candidates:
        j = jumble(c)
        previous = ord(str[i-1]) - ord("a")
        final = (j + previous) & 0xf
        final = final + ord("a")
        if chr(final) == str[i]:
            res += c
print(res)
