
print("{name} was {age} years old when he wrote this book" .format(name="David",age="20"))

print("Why is {name} playing with that python?". format(name="Mike"))

age="20"
name="Helen"
print("{age} is a young age, {name} is 30 already". format(age=age,name=name))

# if we don't write something in {}, program will run in sequence inside the format,
# the first start write in {} is o,second is 1 ,instead of the format(0,1,2)
age="20"
name="Helen"
print("{} is a young age, {} is 30 already". format(age,name))

age="30"
name="Helen"
print(name + "  is "  +  str(age) + "  years old ! ")

#format also can call f-string
#notice the "f" before the string
age="20"
name="Helen"
print(f"My name is {name}, I am {age} years old plus 10 years")

#[round] keep the decimal precision round you want
a=1/3
print(round(a,3))

# end ="" means string don't change the line only blank in print
print("a" ,end ="")
print("b" ,end ="")
print("c")

print('waht\'s your name')
print("Helen told me :\"if I died, can you take care of my cats?\"")
print('This is a first sentence.\nand this is second sentence')

# Identify variable naming rule
# The first character must be letter, not space(use underscore instead )

# add backslash\ can connect the multiple line into one line
s='How can you do this?\
 Are you crazy?'
print(s)

i=\
5
print(i)

'''
[**] means power 
[//] means the answer will get down the nearest integer value
[%] returns the remainder of the division
'''
length=5
breadth=2
print('Area is', length* breadth)
print('perimeter is', 2*(length+breadth))

number=29
guess=int(input('Enter an integer:'))

if guess==number:
    print('congratulations, You win!')
elif guess<number:
    print('No, it is little higher than that ')
else:
    print('No, it is little lower than that')

print('done')

number=23
running = True

while running:
    guess = int(input('Enter an integer:'))
    if guess== number:
        print('congratulations,you guess it.')
        running = False
    elif guess < number:
        print('No,it is a little higher than that.')
    elif guess > number:
        print('No, it is a little lower than that.')
else:
        print('The while loop is over.')

print('Done')
