# -*- coding: utf-8 -*-

for x in [1,2,3,4,5]:
    if x == 3:
        pass
        print('Wrong Number!!')
    print('This is',x)
print('Over.')


it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break

print(it)