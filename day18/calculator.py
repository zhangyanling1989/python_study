def judgeHaveXX(formula):
    flag = False
    if formula.find('+') != -1:
       flag = True
    elif formula.find('-') != -1:
        flag = True
    elif formula.find('*') != -1:
        flag = True
    elif formula.find('/') != -1:
        flag = True
    return  flag

flag = False
while flag ==False:
	formula = input('Enter your formula:')
	flag = judgeHaveXX(formula)
	if flag== False:
		print('输入值有误')
	else:
		A = formula.replace('+', ',').replace('-',',').replace('*',',').replace('/',',')
		A = A.split(',')
		A = list(map(lambda x: float(x),A))
		B = A[::2]
		C =  A[1::2]
		B = float(" ,".join('%s' %id for id in B))
		C = float( " ,".join('%s' %id for id in C))
		if formula.find('+') != -1:
			print(B+C)
		elif formula.find('-') != -1:
			print(B-C)
		elif formula.find('*') != -1:
			print(B*C)
		elif formula.find('/') != -1:
			print(B/C)
		else:
			print('Invalid input')






