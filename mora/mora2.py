from itertools import permutations 

def spell1(L): #1
    M=[]
    for i in L:
        if(i=='1'):M.append('0')
        else:M.append('1')
    return M


def spell2(L):  #2
    M=[]
    for i in range(len(L)):
        if (i%2==1):
            if(L[i]=='1'):M.append('0')
            else:M.append('1')
        else:M.append(L[i])
    return M

def spell3(L):  #3
    M=[]
    for i in range(len(L)):
        if (i%2==0):
            if(L[i]=='1'):M.append('0')
            else:M.append('1')
        else:M.append(L[i])
    return M


def spell4(L):  #4
    M=[]
    for i in range(len(L)):
        if ((i-1)%3==0):
            if(L[i]=='1'):M.append('0')
            else:M.append('1')
        else:M.append(L[i])
    return M

def check(L):
    s1=2
    s2=2
    for i in reds:
        if L[i-1]=='0':
            s1=0
            break
    else:s1=1
        
    for j in yels:
        if L[j-1]=='1':
            s2=0
            break
    else:s2=1
    
    if(s1==1 and s2==1):
        return 1
    else:
        return 0
            

n=int(raw_input())
s=int(raw_input())

global reds
global yels

reds=map(int,raw_input().split())
yels=map(int,raw_input().split())

reds.pop(-1)
yels.pop(-1)


# 1- red 0 - yellow



input_=[]
final1=[]
for i in range(n):
    input_.append('1')
    final1.append('N')


A=[]
all_spell=[]

for i in range(0,s):
    A.append(1)
    A.append(2)
    A.append(3)
    A.append(4)
    
perm = permutations(A,s)
answers=[]

for i in list(perm):
    I=list(i)
    I.sort()
    if ((2 in I) and (3 in I)):
        I.remove(2)
        I.remove(3)
        I=I+[1]
        
    AA=''.join(map(str,I))
    if (AA not in all_spell):
        all_spell.append(AA)
    for i in range(I.count(1)-1):
        I.remove(1)
        
for sp in all_spell:
    x=input_[:]
    for sp_ in list(sp):
        y=[]
        if(sp_=='1'):
            y=spell1(x)
        elif(sp_=='2'):
            y=spell2(x)
        elif(sp_=='3'):
            y=spell3(x)
        elif(sp_=='4'):
            y=spell4(x)
        x=y[:]
    if (check(x)==1 and (x not in answers)):
        answers.append(''.join(x))


answers.sort()
ans=list(set(answers))
ans.sort()
for z in ans:
    print z
