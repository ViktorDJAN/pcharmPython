n = 4
p = []
l1 = []
count = 0
for i in range(n+1):
    p.append([1] + [0]*n)

for i in range(1,n+1):
    for j in range(1,n+1):
        p[i][j] = p[i-1][j] + p[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(p[i][j], end = ' ')
    print()