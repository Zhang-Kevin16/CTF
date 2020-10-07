def reverse(char):
    num = ord(char)
    num = num - 1
    num = num / 2

    if not ret.isdigit():
        char = chr(ord(char) - 9)


str1 = "b4cbb83d4a7f83550fd73ec65ff938a736bda45a4a5fb08311afbef1fc42d48945062661b3d76dd4358ef91c5d16cc0104b3"
str2 = "jbgkfmgkknbiblpmibgkcneiedgokibmekffokamknbkhgnlhnajeefpekiefmjgeogjbflijnekebeokpgngjnfbimlkdjdjhan"

res = ""
for c1, c2 in zip(str1, str2):
    n1 = ord(c1)
    n2 = ord(c2)
    res += chr(n1 ^ n2)
print(res)
