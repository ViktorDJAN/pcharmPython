# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('размер шоколодки по длине = '))
m = int(input("размер школодки по ширине = "))
k = int(input('количество возможных отломленных долек = '))
q = n * m
if (q / k == n) or (q / k == m):
    print('yes')
else:
    print("no")