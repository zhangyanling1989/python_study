# def judgeHaveXX(formula):
#     flag = False
#     if formula.find('+') != -1:
#        flag = True
#     elif formula.find('-') != -1:
#         flag = True
#     elif formula.find('*') != -1:
#         flag = True
#     elif formula.find('/') != -1:
#         flag = True
#     return  flag
#
# flag = False
# while flag ==False:
# 	formula = input('Enter your formula:')
# flag = judgeHaveXX(formula)
# if flag== False:
# 	print('输入值有误')
# else:
# 	A = formula.replace('+', ',').replace('-',',').replace('*',',').replace('/',',')
# A = A.split(',')
# A = list(map(lambda x: float(x),A))
# B = A[::2]
# C =  A[1::2]
# B = float(" ,".join('%s' %id for id in B))
# C = float( " ,".join('%s' %id for id in C))
# if formula.find('+') != -1:
# 	print(B+C)
# elif formula.find('-') != -1:
# 	print(B-C)
# elif formula.find('*') != -1:
# 	print(B*C)
# elif formula.find('/') != -1:
# 	print(B/C)
# else:
# 	print('Invalid input')

flag = True
Enter_time = 0

try:
    while flag == True and Enter_time <= 4:
        Enter_time += 1
        formula = input('Enter your formula:')
        formula = list(formula)
        num1 = formula[0]
        operator = formula[1]
        num2 = formula[2]
        if operator == '+':
            answer = float(num1) + float(num2)
        elif operator == '-':
            answer = float(num1) - float(num2)
        elif operator == '*':
            answer = float(num1) * float(num2)
        elif operator == '/':
            answer = float(num1) / float(num2)
        print(round(answer, 3))
    else:
        print('You\'ve tried 5 times,you out of system')
except NameError:
    print('OH,You enter something wrong!!')



