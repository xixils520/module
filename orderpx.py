import itertools
a=[x for x in range(10)]
b=[chr(x) for x in range(ord('a'), ord('z') + 1)]
c=[]
for i in b:
    i=i.upper()
    c.append(i)
list=(a+b+c)
mm="".join(str(s) for s in list)
for i in itertools.combinations_with_replacement(mm, 8):
    print(''.join(i), end=' ')
    mima=''.join(i)
    f = open("logorderby.txt", 'a')
    f.write(mima+'    ')
    f.close()





