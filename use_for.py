# a = 5
# b = 15
# for i in range(a + 3 - a % 3, b, 3):
#     if i % 3 == 0:
#         print(i)
#
# num = 123456
# i = 1
# sum1 = 0
# while i <= len(str(num)):
#     sum1 = sum1 + ((num) % (10 ** i)) // (10 ** (i - 1))
#     i = i + 1
# print(sum1)

# n = 47
# i = 2
# is_prime_number = True
# for i in range(2, n, 1):
#     if n % i == 0:
#         is_prime_number = False
#         break
# if is_prime_number:
#     print(str(n) + " is prime")
# else:
#     print(str(n) + " is not prime")
#
# a = 2
# b = 100
# for i in range(a, b, 1):
#     is_prime_number = True
#     for j in range(2, i, 1):
#         if i % j == 0:
#             is_prime_number = False
#             break
#     if is_prime_number:
#         print(i)

# a = 2
# b = 100
# for i in range(a, b, 1):
#     for j in range(2, i, 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

name = "Ivanov Ivan Ivanovich"
count = 0
SEARCH = 'a'
for symbol in name:
    if symbol == SEARCH:
        count += 1
print(count)

i = 0
while i < len(name):
    print(name[i])
    i += 1

is_palindrome = False
i=0