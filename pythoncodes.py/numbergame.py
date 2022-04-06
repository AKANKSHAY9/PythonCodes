#You win if you enter a number greater than 100
while(True):
    a=int(input("Enter a number:\n"))
    if a>100:
        print("Congrats you entered a number greater than 100\n")
        break
    else:
        print('Enter again \n')
        continue