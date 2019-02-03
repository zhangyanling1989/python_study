# -*- coding: utf-8 -*-

from functools import reduce

def add(x,y):
    return x+y

print(reduce(add,[1,3,5,7,9]))


def fn(x,y):
    return x*10 +y

print(reduce(fn,[1,3,5,7,9]))

def fn(x,y):
    return x*10+y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'13579')))



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))

print(str2int(DIGITS))





def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

print(str2int(DIGITS))


L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    name_new = name[:1].upper() + name[1:].lower()
    return name_new

print(list(map(normalize,L1)))


def prod(x,y):
    return x*y
print(reduce(prod,[3,5,7,9]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
# def str2float(s):
#     def fn(x,y):
#         return (x*10 + y)*0.001
#     def char2num(s):
#         return number[s]
#     return reduce(fn,map(char2num,s))

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))/1000

print(str2int(DIGITS)-123.456)
