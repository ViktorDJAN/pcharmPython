# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

li = [11,22,1,45,47,83,90,34,63,2,7,3,2,1,'a',2,'ad','re','o','r','w']
start = int(input('enter strat value:  '))
end = int(input('enter last value:  '))
total = [li[start:end]]
print(total)