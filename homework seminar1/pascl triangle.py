n = int(input('enter size:  '))
p = []
l1 = []
count = 0
for i in range(n+1):
    p.append([1] + [0]*n)

for i in range(1,n+1):
    for j in range(1,n+1):
        p[i][j] = p[i-1][j] + p[i-1][j-1]

for i in range(n+1):
    for j in range(n+1):
        print(p[i][j], end = '    ')
    print()