# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и
# их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3

# print("Значения ax^2+bx+c=0")

p = int(input('введите сумму: '))
q = int(input('введите произведение: '))
D = p**2 - 4*q
x1 = -((p + D**0.5)/(2*1))
x2 = -((p - D**0.5)/(2*1))
x1 = int(x1)
x2 = int(x2)
print( f'число1  = {-x1}, число2 = {-x2}')
