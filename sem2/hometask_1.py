# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
#
# 5 -> 1 0 1 1 0
import random
n = (int(input('введите число монеток:  ')))
coins = []
countGerb = 0
countResh = 0
for i in range(n):
    a = random.randint(0,1)
    coins.append(a)
for i in coins:
    if i == 1:
        countGerb +=1
    else:
        countResh +=1
print(f'список до --> {coins}')
i=0
while i < len(coins):
    if  countGerb > countResh and coins[i] == 0:
        coins[i] = 1
    elif countResh > countGerb and coins[i] == 1:
        coins[i] = 0
    i+=1

print(f'список после --> {coins}')
print(countGerb)
print(countResh)

