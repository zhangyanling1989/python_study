lucky_numbers=[5,15,28,67,81,35,47]
friends=["kevin","karen","jim","tom" ,"lucy"]
friends.extend(lucky_numbers)
print(friends)
friends.append("celine")
print(friends)
friends.insert(1,"kelly")
print(friends)
friends.remove("tom")
print(friends)
friends.remove(friends[0])
friends.pop()
print(friends)
print(friends.index("jim"))
print(friends.count("jim"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2=friends.copy()
print(friends2)
friends2=friends
print(friends2)
coordinates=(4,5)
print(coordinates[0])
def really():
    print("hello python")

print("i am so tired")
really()
print("i want to sleep")