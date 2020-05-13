DEZ = [1,10,100,1000,10000,100000,1000000]
T = [0]*20
D = [0]*20
def digit(a):
    sum1 = 0
    while(a):
        sum1+=1
        a/=10
    return sum1
def contain(a):
    while (a):
        for i in range (n):
            if a%DEZ[D[i]] == T[i]:
                return True
        a /= 10
    return False
s,e,p,n = map(int,raw_input().split())
for i in range (n):
    T[i] = input()
    if T[i]>1000000:
        i-=1
        n-=1
    else:
        D[i] = digit(T[i])
count = 0
for j in range (s,e+1):
    if(contain(j)):
        count+=1
    if count==p:
        print j
        break
if count<p:
    print "DOES NOT EXIST"