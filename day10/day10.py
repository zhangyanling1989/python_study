def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation+"G"
            else:
                translation=translation+"g"
        else:
            translation=translation+letter
    return translation

print(translate(input("Enter a phrase:")))



try:
    value=10/0
    number= int(input("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("divided by zero")
except ValueError:
    print("Invalid Input")


employee_file = open("test.txt","r")
# for line in employee_file.readlines():
#     print(line)
print(employee_file.readlines()[2])
print(employee_file.readline())
print(employee_file.readline())

#google: list of python modules

employee_file.close()

line=open("test.txt","a")
line.write("\n房东个仔反企，叫我放区驾车出去")
line.close()

line=open("line","w")
line.write("\nToday is a good day, because I am happy")
line.close()
