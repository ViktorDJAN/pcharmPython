a = int(input("введите четырех значное число "))
counter = 0
summa = 0
while a > 0:
    i = a % 10
    a = a//10
    counter += 1
    print(counter)


