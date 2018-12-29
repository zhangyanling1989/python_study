def say_hi(name,age):
    print("hello " ,name , ", you are " ,age)
    print(f'Hello {name},you are {age}')

print("top")
say_hi("mike" ,35)
say_hi("steve", 60)
print("bottom")

def cube(num):
    return num*num*num

print(cube(4))

def worker(a,b,c):
    x=a+b
    y=x*c
    return x+y

result=worker(1,3,4)
print(result)

is_female=True

if is_female:
    print("you are a female")

is_male=True
is_tall=False
if is_male or is_tall:
   print("you are a male or tall or both")
else:
    print("you are neither male nor tall")

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("you are either not male or not tall or both")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(17,9,14))

def max_num(num1,num2,num3):
    if num1!=num3 and num2<num3:
       return num3
    elif num1>num3 and num2>num3:
       return num1
    else:
       return num2

print(max_num(2,1,2))

