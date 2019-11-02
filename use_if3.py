# x = float(input())
# if -15 <= x <= 17 or 25 <= x < 37 or 115 <= x:
#     print(str(x) + "in set -15 <= x <= 17 or 25 <= x < 37 or 115 <=  x")
# else:
#     print(str(x) + "not in set  -15 <= x <= 17 or 25 <= x < 37 or 115 <=  x")
#
# a = float(input())
# b = float(input())
# c = float(input())
#
# if a + b > c and a + c > b and b + c > a:
#     print("a, b, c can make triangle")
# else:
#     print("Not make triangle")

lucky = int(input())
i = 1
sum1 = 0
sum2 = 0
while i <= 3:
    tmp = ((lucky) % (10 ** i)) // (10 ** (i - 1))
    i = i + 1
    sum1 = sum1 + tmp
while i <= 6:
    tmp = ((lucky) % (10 ** i)) // (10 ** (i - 1))
    i = i + 1
    sum2 = sum2 + tmp
# a = lucky % 10 // 1
# b = (lucky % 100) // 10
# c = (lucky % 1000) // 100
# d = (lucky % 10000) // 1000
# e = (lucky % 100000) // 10000
# f = (lucky % 1000000) // 100000

if sum1 == sum2:
    print("lucky ticket")
else:
    print("not lucky ticket")

a = float(input())
b = float(input())
op = input()
if op == '*':
    print(a * b)
elif op == '+':
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "/":
    print(a / b)
else:
    print("unknown operation")

a = float(input())
b = float(input())
c = float(input())
max = a
if b > a:
    max = b
if c > b:
    max = c
print("max(" + str(a) + "," + str(b) + "," + str(c) + ") = " + str(max))
