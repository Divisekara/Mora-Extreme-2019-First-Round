import bisect
P,Q,R=map(int,raw_input().split())
arr=map(int,raw_input().split())
arr+=arr
arr0=arr[0:Q]
arr0.sort()
del arr0[R:]
min1= arr0[-1]
min2=min1
def index(x, y):
    i = bisect.bisect_left(x, y)
    if i != len(x) and x[i] == y:
        return i
    raise ValueError
for i in xrange(P):
    inn = arr[i+Q]    
    out = arr[i]     
    if inn <= min1 and out > min1:
        if len(arr0) == R:
            del arr0[-1]
        bisect.insort_left(arr0, inn)
        min1 = arr0[-1]
    elif inn <= min1 and out <= min1:
        del arr0[index(arr0, out)]
        bisect.insort_left(arr0, inn)
        min1 = arr0[-1]
    elif out < min1:
        del arr0[index(arr0, out)] 
    if len(arr0) == R:
        min2 = min(min1, min2)
print min2