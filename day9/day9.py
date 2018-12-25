num1=float(input("Enter first number:"))
op=input("Enter operator:")
num2=float(input("Enter second number:"))

if op =="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
else:
  print("invalid operator")

monthconversions={
    "Jan":"January",
     "Feb":"February",
    "Mar":"March",
    "May":"May",
    "Apr":"April",
    "6":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(monthconversions.get("May"))
print(monthconversions["6"])

i=1
while i<=10:
    print(i)
    i+=0.5

print("Done with loop")

secret_word="giraffe"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

while guess!=secret_word and not (out_of_guesses):
    if guess_count <guess_limit:
     guess=input("Enter guess:")
     guess_count+=1
    else:
        out_of_guesses=True


if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
   print("You  win !")



for letter in "Giraffe Academy":
    print(letter)

friends=["Jim", "Karen",  "kavin"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(index)

for index in range(5):
    if index==0:
        print("first iteration")
    else:
        print("Not First")

def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))

number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[1][2])

for row in number_grid:
    for col in row:
        print(col)