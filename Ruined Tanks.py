n = int(input())
walls = list(map(int, input().split()))

m = 0
d = {}
for i in range(n-1):
    if walls[i]>m:
        m = walls[i]
        d[walls[i]] = i

m1 = 0
d1 = {}
for i in range(n-1, 0, -1):
    if walls[i]>m1:
        m1 = walls[i]
        d1[walls[i]] = i

v = []
for i in d:
    for j in d1:
        v.append(min(i,j)*(abs(d[i]-d1[j])))

print(max(v))