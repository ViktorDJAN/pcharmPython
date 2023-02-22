# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова
# , если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение
# Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”
# , если с ритмом все не в порядке
#
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-да
#
# Вывод:
# Парам пам-пам

s = "пара-ра-рам рам-пам-папам па-ра-па-да"
st = s.split(' ')
sp = []

for i in st:
    c = 0
    for j in i:
        if j =='а':
            c +=1
    sp.append(c)
a = sp[0]
summ = 0
for i in sp:
    summ += i
if summ/a == len(sp):      # если сумма деленная на первый элемент в списке == количеству элементов ,значинт ритм есть.
    print('Парам пам-пам')