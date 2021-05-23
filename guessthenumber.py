#    This code is a game guess the number. The number is 18
while(True):
    a=int(input("Enter the magic number:\n"))
    if a>18:
        print("The number you entered is greater than the magic number")
        print("Please try again")
    elif a<18:
        print("The number you entered is less than the magic number")
        print("Please try again")
    else:
        print(" Woohoo!!\n You guessed it right!!!!!")
        break