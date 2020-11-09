# OTP Implementation picoCTF 2020 Mini-competition

For the challenge we are given a binary and a text file that holds the encrypted flag. Assuming that the binary is used to encrypt the flag lets open that up.

Once we open up the binary in our favourite disassembler we see a interesting set of strings in the binary.

![](/pico/2020/otp/strings.PNG)

Considering that the long string is near the string that mentions getting the key we should see what the long string is used for.

![](/pico/2020/otp/decompiled.PNG)

Using Ghidra to decompile the binary we can see that the long string is being checked against our input string after it has been scrambled by the program. My first instinct was to work backwards from the long string to see what our input string could be but that was not possible since the characters are being bitwise ANDed with `0xF` which means we only have the lower 4 bits of the input character.

But if you were to look at the `valid_char()` function note that the valid inputs are only from `0-9` and `a-f` which means we have a total of 16 possible inputs.

![](/pico/2020/otp/valid_char.PNG)

This means that for each character in the output there is 16 possibilities for the input character so for the 100 character key there is only 1600 possibilities which is easily brute forced by selecting each input choice and checking if it matches the corresponding character. Here is the python script.

```
# What the jumble function in the binary does
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

# Subsequent characters depend on the previous character
for i in range(1, 100):
    for c in candidates:
        j = jumble(c)
        previous = ord(str[i-1]) - ord("a")
        final = (j + previous) & 0xf
        final = final + ord("a")
        if chr(final) == str[i]:
            res += c
print(res)
```
Voila! Here is the key `c4a2db52092bc52e6ca24db26f9467cd43d0c636792cefb7639cd085a3768bee7549423e82b35e956abbc9246b2ffc3537ce`. We can throw this key into the program and see if its right.

```
./flag.o c4a2db52092bc52e6ca24db26f9467cd43d0c636792cefb7639cd085a3768bee7549423e82b35e956abbc9246b2ffc3537ce                         
You got the key, congrats! Now xor it with the flag!
```

Note that all of it looks like hex characters and all the contents of flag.txt (`b4cbb83d4a7f83550fd73ec65ff938a736bda45a4a5fb08311afbef1fc42d48945062661b3d76dd4358ef91c5d16cc0104b3`) look like hex characters as well. So a XOR yields hex `7069636f4354467b63757374306d5f6a756d626c33735f3472336e745f345f67304f645f316433415f35303836393034337d`. Plug this into your favourite hex to ASCII tool and get the flag.

`picoCTF{cust0m_jumbl3s_4r3nt_4_g0Od_1d3A_50869043}`
