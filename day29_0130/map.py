# -*- coding: utf-8 -*-

def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

print(list(map(str,[1,2,3,4,5,6,7,8,9])))



def square(x):
    return x**2
print(list(map(square,[1,2,3,4,5])))

print(list(map(lambda x:x**2,[1,2,3,4,5])))

print(list(map(lambda x,y : x+y, [1,3,5,7,9],[2,4,6,8,10])))

