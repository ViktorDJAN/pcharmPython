# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input('введите значение первого элемента:  '))
d = int(input("введите значение разности:  "))
n = int(input('введите число элементов: '))
list_1 = []
for i in range(1,n+1):
    an = a1 + (i-1)*d
    list_1.append(an)
print(list_1)