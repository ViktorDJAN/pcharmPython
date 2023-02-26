# ДОП ЗАДАЧА.
#
#   Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной данной
#   работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
#           Сколько минут на это потребуется?
#           Номер трубы соответствует номеру строки, в которой записана ее производительность.
#           Результат запишите в файл time.txt
#   Пример
#   Ввод
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
# Вывод
# 32.72727272727273

# s = input()
# s = s.split(', ')
# d = {}
# for word in s:
#     d[word] = d.get(word, 0) + 1
# print (d)

with open('pipes.txt','r',encoding = 'utf-8') as pipe:
    d = {}
    V = 1
    speed = 0
    number = 0
    s = [index for index in pipe.read().split()]
    for value in s:
        number+=1
        d[number] = d.get(int(number),float(value))
    print(d)
    n = int(input('Enter pipes quantity: '))
    for i in range(n):
        d[i] = d[int(input('Enter the pipe number:'))]
        speed += V/d[i]
        time = (V/ speed)*60
    print('Multi-pipe filling is equal =',time,'min')



