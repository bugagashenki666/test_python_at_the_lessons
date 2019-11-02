# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(str(year) + " является вескокосным")
# else:
#     print(str(year) + " не является вескокосным")
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a != b and b != c and a != c:
#     print("имеем 3 различных числа")
# elif (a != b and b != c and a == c) or (a == b and b != c and a != c) or (a != b and b == c and a != c):
#     print("имеем 2 различных числа")
# else:
#     print("имеем одно уникальное число")

x = float(input())
y = float(input())

# if x > 0 and y > 0:
#     print("I четверть")
# elif x > 0 and y < 0:
#     print("IV четверть")
# elif x < 0 and y < 0:
#     print("III четверть")
# elif x != 0 and y == 0:
#     print("на оси x")
# elif x == 0 and y != 0:
#     print("на оси y")
# elif x == 0 and y == 0:
#     print("0,0")
# else:
#     print("II четверть")

if x > 0:
    if y > 0:
        print("I")
    elif y < 0:
        print("IV")
    else:
        print("на оси X")
elif x < 0:
    if y > 0:
        print("III")
    elif y < 0:
        print("II")
    else:
        print("на оси X")
else:
    if y == 0:
        print("0,0")
    else:
        print("на оси Y")
