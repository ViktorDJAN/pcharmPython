# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

a = int(input('enter number a:  '))
b = int(input('enter number b:  '))
def summa(a, b):
    if (b == 1):
        return (a+b)
    if (b != 1):
        return (summa(a+1, b-1 ))

print('result is equal ', summa(a,b))
