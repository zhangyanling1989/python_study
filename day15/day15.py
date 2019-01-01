shoppinglist = ['apple', 'mango', 'carrit', 'banana']

print('I have', len(shoppinglist), 'item to purchase.')

print('These items are:' ,end= '  ')
for item in shoppinglist:
    print(item,end='  ')

print('\nI also have to buy rice.')
shoppinglist.append('rice')
print('My shoppinglist is now', shoppinglist)

print('I will sort my list now')
shoppinglist.sort()
print('sorted shoppinglist is ', shoppinglist[0])

print('The first item I will buy is ' , shoppinglist[0])
olditem = shoppinglist[0]
del shoppinglist[0]
print('I bought the',olditem)
print('My shoppinglist is now', shoppinglist)

for num in range(10):
    list=num*num
    print(list, end=' ')


# list use [] and list is mutable, tuple use()and tuple is immutable ,dictionary use{]


zoo=('python', 'elephant', 'penguin' )
print('\nNumber of animals in the zoo is ' ,len(zoo) )

new_zoo = 'monkey' , 'camel', 'peacock' , zoo # parentheses not required but is a good idea
print('Number of cages in the new zoo is ', len(new_zoo))
print('Animals brought for old zoo are', new_zoo[3])
print('Last animal brought from old zoo is', new_zoo[3][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[3]))

t=(2)  #This is a string
d=(2,) #This is a tuple
print(t,d)


ab = {
      'Swaroop': ' swaroop@swaroop.com ',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matsumoto@rube-long.org',
      'Spammer': 'spammer@hotmail.com'
}

# in dictionary, the key-value will separate the lowercase and uppercase, I use ab['swaroop] amd it was wrong
print('Swaroop\'s address is ', ab['Swaroop'])

del ab['Spammer']

print('\nThere are {} contacts in the address book\n'. format(len(ab)))

for name, address in ab.items():
    print('contact {} at{}'.format(name,address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nGuido\'s address is ', ab['Guido'])


shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('character 0 is', name[0])

print('Item 1 to 3 is ', shoplist[1:3])
print('Item 2 to end is ', shoplist[2:])
print('Item 1 to -1 is ', shoplist[1:-1])
print('Item start to end is ', shoplist[:])
print('Item start to end is ', shoplist[::2])  # 多加一个冒号就可以间隔，这个就是间隔2

print('character 1 to 3 is ', name[1:3])
print('character 2 to end is ', name[2:])
print('character 1 to -1 is ', name[1:-1])
print('character 1 to -1 is ', name[:])

bri = set(['brazil', 'russia', 'india'])
print('india' in bri)
print('usa' in bri)

bric = bri.copy()
print(bric)
bric.add('china')
print(bric)
print(bric.issuperset(bri))
bric.remove('russia')
print(bric&bri)

print('Simple Assignment')
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist=shoplist
# print('shoplist is', shoplist)
# print('mylist is', mylist)
# print('\ncopy by making a full slice')
# mylist=shoplist[:]
# del mylist[0]
# print('shoplist is ', shoplist)
# print('mylist is', mylist)

name = 'David'

if name.startswith('Da'):
    print('Yes, the string starts with "Da"')
if 'b' in name:
    print('Yes, it contains the string "a" ')
else:
    print('No, this character is not in the name')
if name.find('Da') != -1:
    print('Yes, it contains the string "Da" ')

if name.find('d')==-1:
    print('False')
else:
    print('True')

delimiter = '-'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

