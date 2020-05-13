n = int(input())
for _ in range(n):
    F,U,K,M = map(int,input().split())
    A,P = [],[]
    for _ in range(F):
        a,p = map(int,input().split())
        A.append(a)
        P.append(p)
    A,P=zip(*sorted(zip(A,P)))
    A,P=list(A),list(P)
    
    K -= A[0]
    if K<0:
        print(-1)
        continue
    
    A.append(M)
    P.append(0)
    cc = A[0]
    for i in range(len(A)):
        A[i] -= cc
    
    
    total = 0
    fuel = K
    for now in range(0,F):
        
        k = now+1
        buy = now
        base = A[now+1]-A[now]
        while k<F and U >= base:
            if(P[k]<=P[now]):
                break
            base += A[k+1]-A[k]
            k += 1

        if U < base:
            base = U

        base -= fuel
        
        
        if(base>0):
            total += P[buy]*base
            fuel += base
            
        dist = A[now+1]-A[now]
        fuel -= dist
        if fuel <0:
            total = -1
            break
    print(total)