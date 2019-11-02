import math

a = -20
b = 20
for i in range(a, b + 1):
    if (i > 0 and i % 10 == 4) or (i < 0 and (-i) % 10 == 4):
        print(i)

a, b = 1, 1
k = 10

while a < k:
    print(b)
    a, b = b, a + b
print(b)

input_s = 'abcllcba'
offset = -1
for i in range(len(input_s) // 2):
    if input_s[i] != input_s[offset]:
        print("string is not palindrome")
        break
    offset -= 1
else:
    print("string is palindrome")

i = 0
while i < len(input_s) // 2:
    if input_s[i] != input_s[-i - 1]:
        print("string is not palindrome")
        break
    i += 1
else:
    print("string is palindrome")
