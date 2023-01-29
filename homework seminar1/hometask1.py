#   Задача 2: Найдите сумму цифр трехзначного числа.
#   123 -> 6 (1 + 2 + 3)
#   100 -> 1 (1 + 0 + 0)
amount = 0
n = int(input("enter a number:  "))
while n>0:
    i = n % 10
    amount +=i
    n = n// 10
print(amount)