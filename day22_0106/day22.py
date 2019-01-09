# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r = s1/s2
name = 'xiaoming'
print('%s\'s score improves %.2f %%'%(name,r))

print('%2d-%2d' % (3, 1))
print('%.2f' % 3.1415926)  # %.2f 意思是两个小数点，有一个period

classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('Adem')   #后面加element
print(classmates)
classmates.insert(1,'Jack')  #在1 插入element
print(classmates)
classmates.pop()              #删掉后面的element
print(classmates)
classmates[1] = 'Sarah'    #替换element
print(classmates)

# tuple 定义
t = (1)   #这是一个数字
t = (1,)  #这是一个tuple

t= ('a','b',['c','d'])
t[2][0] ='x'
print(t)    #tuple本身element can not change,but the list inside it can change

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


max_Enter = 0
flag = True
while max_Enter <4 and flag == True:
    max_Enter += 1
    height = float(input('Enter your height:'))
    weight = float(input('Enter your weight:'))
    BMI = weight / (height * height)
    if BMI < 18.5:
        print('你的BMI是', round(BMI, 2), '过轻')
    elif 18.5 <= BMI < 25:
        print('你的BMI是', round(BMI, 2), '正常')
    elif 25<= BMI<28:
        print('你的BMI是',round(BMI, 2),'过重')
    elif 28 <= BMI < 32:
        print('你的BMI是', round(BMI, 2), '肥胖')
    elif BMI >= 32:
        print('你的BMI是', round(BMI, 2), '严重肥胖')
else :
    print('You are dooe with BMI test ')


import sys
sys.path.append('complete_path')
import my_abs

print(my_abs(-9))

