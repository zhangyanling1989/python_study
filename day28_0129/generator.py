# -*- coding: utf-8 -*-

L = [x*x for x in range(10)]   # lit comprehensions
g = ( x*x for x in range(10))   # generator
for n in g:
    print(n)


def fib(max):
    n,a,b = 0,0 ,1
    while n<max:
        yield b
        a,b = b,a+b
        n=n+1
    return "done"

g = fib(6)
while True:
    try:
        x= next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value', e.value)
        break


def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]

print(triangles(6))