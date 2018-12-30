def func(a,b=5,c=10):
    print('a is ',a , 'and b is ',b , 'and c is ',c)

func(3,7)
func(25, c=24)
func(c=50, a = 100)
# print_out
# a is  3 and b is  7 and c is  10
# a is  25 and b is  5 and c is  24
a is  100 and b is  5 and c is  50

def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return 'The umber are equal'
    else:
        return y

print(maximum(2,3))

def some_function():
    pass

def print_max(x,y):
    '''Pints the maximum if two numbers .

    The two values must be intergers .'''
    #convert to integers, if possible
    x=int(x)
    y=int(y)

    if x>y:
        print(x, ' is maxinum')
    else:
        print(y, ' is maxinum')

print_max(3,5)
print(print_max. __doc__)

if __name__=='question.py':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
