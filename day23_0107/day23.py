# -*- coding: utf-8 -*-

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print(name, end=' , ')

n = 1
while n <= 100:
    print(n)
    n += 1
print('END')

a = 'fnigjgadgkioajgiosdagkpfgjhuiganiohnguoaajgio'
a = list(a)
a.reverse()
a= ''.join(a)
print(a)


import time
n = 1
while n<=10:
    time.sleep(3)
    print(n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}   # dictionary
print(d['Michael'])

s = set([1, 2, 2,4,1,3])
print(s)
s.add(5)
print(s)
s.remove(5)
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])
s = s1 & s2   #交集
print(s)
s= s1 | s2  #并集
print(s)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-56))


import math
def quadratic(a,b,c):
    if a != 0 and b**2-4*a*c > 0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2 -4*a*c))/(2*a)
        return x1,x2
    elif a !=0 and b**2-4*a*c == 0:
        x= -b/(2*a)
        return x
    elif a == 0:
        return ZeroDivisionError
    elif b**2 - 4*a*c <0:
        return ValueError


print('quadratic(0,3,1)=',quadratic(0,3,1))
print('quadratic(1,3,4)=',quadratic(1,3,4))
print(quadratic(1,3,-4))
print(quadratic(1,4,4))

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,3))

import os


