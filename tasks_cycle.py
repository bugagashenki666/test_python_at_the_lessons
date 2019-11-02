#task1
sum_ = 0
i = 0
n = 1000
while i <= n:
    sum_ = sum_ + i
    i = i + 1
print(sum_)

#task2v1
layers = 10
i = 1
while i <= layers:
    print(i * "*")
    i = i + 1

#task2v2
i = 1
while i <= layers:
    s = "*"
    j = 1
    while j < i:
        s += "*"
        j += 1
    print(s)
    i += 1

#task3
a = int(input())
b = int(input())
i = a
count = 0
sum_of_numbers = 0
while i <= b:
    sum_of_numbers += i
    i += 1
    count += 1
print(str(sum_of_numbers / count))
