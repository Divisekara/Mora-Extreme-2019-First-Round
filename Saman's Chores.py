inp = [int(x) for x in raw_input().split()]
n, m = inp[0], inp[1]

lis = []
for i in range(m):
    lis.append([int(x) for x in raw_input().split()])

todo = [int(x) for x in raw_input().split()]

done = 1
for i in lis:
    if todo.index(i[0])>todo.index(i[1]):
        done = 0
        break

if done==1:
    print "YES"
elif done==0:
    print "NO"