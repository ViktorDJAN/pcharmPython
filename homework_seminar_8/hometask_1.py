# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем
# функцию на файле «article.txt» со следующим содержимым:

lines = int(input('enter quantity of last strings: '))
def read_list(lines,file):
    with open('article.txt', 'r', encoding ='utf-8') as toread:
        wish = toread.read().splitlines()
        if lines > 0:
            wish = (wish[(-lines)::])
        for i in wish:
            print(i)

print(read_list(lines,'article.txt'))