MOD = 10**9+7

n = int(input().strip())
ar = list(map(int,input().strip().split()))

arrMax = max(ar)
freq = [0 for _ in range(arrMax+1)]
for i in ar:
    freq[i] += 1
q = int(input())

subsets = {}
for i in range(arrMax):
    subsets[i] = 0

for i in range(arrMax,0,-1): 
    sub = 0
    add = freq[i]

    j = 2
    while (i*j<=arrMax):
        add += freq[j*i]
        sub += subsets[j*i]
        j+=1
    subsets[i] = (1<<add) - 1 - sub

for _ in range(q):
    x = int(input().strip())
    if x > arrMax:
        print(0)
    else:
        ans = subsets[x]%MOD
        print(ans)