import itertools
list=[]
for i in itertools.combinations_with_replacement('01234567',8):
    print (''.join(i),end=' ')