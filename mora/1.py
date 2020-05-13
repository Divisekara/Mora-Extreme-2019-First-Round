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
    s1=1
    s2=1
    for i in reds:
        if L[i-1]=='0':
            s1=0
            break
        
    for j in yels:
        if L[j-1]=='1':
            s2=0
            break
        
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

for j in reds:
    final1[j]='1'

for k in yels:
    final1[k]='0'
    

A=[]
all_spell=[]

for i in range(0,40):
    A.append(1)
    A.append(2)
    A.append(3)
    A.append(4)
    
perm = permutations(A,s) 
  
answers=[]

for i in list(perm):
    AA=''.join(map(str,list(i)))
    all_spell.append(AA)


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
    








