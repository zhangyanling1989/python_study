
guess=int(input('请输入年份:'))
num=guess
num1= num%4
num2= num%100
num3= num%400

if num1==0 and num2 != 0:
   print('这是闰年')
elif num3==0:
    print('这是闰年')
else:
   print('这不是闰年')
