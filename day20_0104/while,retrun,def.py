# -*- coding: UTF-8 -*-


count = 0
while ( count<9 ):
    print('The count is :', count)
    count += 1
print('Good bye!')

i = 1
while i < 10:
    i += 1
    if i%2 > 0:
        continue
    print(i)

i = 1
while 1:
    print(i)
    i+=1
    if i>10:
        break


var = 1
while var <5: # This condition always be true,this loop will always execute.
    var += 1
    num =input('Enter a number:')
    print('You entered', num)
    if num == 3:
        break
print('Good bye')

count = 0
while count <5:
    print(count,'is less than 5')
    count += 1
else:
    print(count,'is not less than 5')

flag = 1
while(flag):print('Given flag is really true')
print('Good bye')

def functionname(parameters):
    function_suite
    return [expression]

def printme(str):
    print(str)
    return

printme('Hello, I am yanling zhang')

def changeme(mylist):
    mylist.append([1,2,3,4])
    print('My list', mylist)
    return
mylist = [10,12,23]
changeme(mylist)

try:
    text = input('Enter something')
except  EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('You entered {}'.format(text))

