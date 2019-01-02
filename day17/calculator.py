num1 = input('Enter your number:')
operator = input('Enter your operator:')
num2 = input('Enter your number :')

try:
  if operator == '+' :
      num = float(num1)+float(num2)
      print(round(num,2))
  elif operator == '-':
      num = float(num1) - float(num2)
      print(round(num, 2))
  elif operator == "*":
      num = float(num1) * float(num2)
      print(round(num, 2))
  elif operator == '/':
      num = float(num1) / float(num2)
      print(round(num, 2))
  else:
      print('Invalid input')
except  ZeroDivisionError:
    print('ERROR')

