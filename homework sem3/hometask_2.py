# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

N = int(input('введите число N:  '))
X = int(input('введите число X:  '))
A = []
for i in range(1,N+1):
    A.append(i)
print(A)
for i in A:
    if X-i == 1:
        print('близкий элемент равен: ',i)