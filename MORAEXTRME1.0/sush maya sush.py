t=int(raw_input())

'''
4
ssssshsssh
hhhhhs
sshshshssh
hshsh
'''

'''answer
sh
h


'''


L=[]
for i in range(t):
    L.append(raw_input())

answers=[]

for j in L:
    while(True):
        m=0
        if (('ss' not in j) & ('hh' not in j)):
            answers.append(j)
            break
        new_list=[]
##        print j
        length=len(j)
        while(len(j)>m):
            if (m==length-1):
                new_list.append(j[m])
##                print j[m]
                break
            if((j[m]+j[m+1])=='ss'):
                new_list.append('h')
##                print 'h'
                m+=1
            elif((j[m]+j[m+1])=='hh'):
                new_list.append('s')
##                print 's'
                m+=1
            else:
                new_list.append(j[m])
##                print j[m]
            m+=1
            
        j=''.join(new_list)
                  
for u in answers:
    s_count=u.count('s')
    h_count=u.count('h')
    print s_count,h_count



