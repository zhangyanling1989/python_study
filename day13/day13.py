for i in range(1,8,2): #num 2 means has step count 2 inside, run 1.3.5.7
    print(i)
else:
    print('The loop is over')

while True:
    s= input ('Enter something:')
    if  s == 'quit':
        break
    print('Length of the string is ', len(s))

print('Done')

# -*- coding=UTF-8 -*-
# up is the programing cord about when you want to write chinese use encode


# The different with break and continue
# Break run out all loop, continue only run out the continue sentence loop
while True:
    s=input('Enter something:')
    if s == 'quit':
        break
    if len(s)<3:
        print('Too small')
        continue
    print('Input is of sufficient length')
print('Done')

# comma(,) can connect string and number, "+ "can't
def print_max(a,b):
    if a>b:
        print(a , 'is maximum')
    elif a==b:
        print(a,'is equal to' ,b)
    else:
        print(b,'is maximum')

print_max(12,11)

x=5
y=7
print_max(x,y)

def func(x):
    print('x is',x)
    x=2

x=50
func(x)

# global change variable from function inside to outside

# the function parameters and global string can not be same
x=50
def func(a):
    global x
    x=2
    print('x is',x)

func(x)