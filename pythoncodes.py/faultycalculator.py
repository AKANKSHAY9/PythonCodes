#Calculates all the values except 45*3 and 56+9
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
print('Enter the operator:\nadd\nsub\nmul\ndiv')
c=input()
if (c=="add"):
    if (a==56 and b==9):
        print('77')
    else:
        print(a+b)
elif(c=="sub"):
    print(a-b)
elif(c=="mul"):
    if (a==45 and b==3):
        print('555')
    else:
        print(a*b)
else:
    print(a/b)



