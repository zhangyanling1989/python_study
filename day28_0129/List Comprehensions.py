# -*- coding: utf-8 -*-

print(list(range(1,12)))


print([x * x for x in range(1,12)])

print([m+n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)

print([k+'='+v for k ,v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])



L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = []
for s in L1:
    if isinstance(s,str) is True:
        L2.append(s)
print([s.lower() for s in L2])




