a=input("Enter a number or a character:")
if (a.isnumeric()):
    print(" a is a number")
elif (a.isupper()):
    print(" a is an uppercase character")
elif (a.islower()):
    print(" a is a lower case character")
else:
    print(" a is a special character")

