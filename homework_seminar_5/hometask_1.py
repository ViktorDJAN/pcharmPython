# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
a = int(input('enter number a:  '))
b = int(input('enter number b:  '))
def exp(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * exp(a, b - 1))

print('result is equal ', exp(a,b))