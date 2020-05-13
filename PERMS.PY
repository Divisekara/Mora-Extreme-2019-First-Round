'''s = 'abc'
d =( (x,y,z) for x in s for y in s for z in s)
d.next()
d.next()
'''



def product(x):
        final = [[]]
        l = len(x)
        groups = [list(x)] * l
        for i in groups:
            final = [x+[y] for x in final for y in i]
        for k in final:
            yield ''.join(k)

name='1234123412341234123412341234123412341234'
name_=name[0:20]
print list(product(name_))
