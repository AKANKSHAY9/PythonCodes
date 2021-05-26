a=int(input("Enter the number: "))
b=int(input('Enter a boolean number 1 or 0:'))
if b==0:
    for i in range (0,a):
        for j in range(0,i+1):
            print('*',end="")
        print("\r")
else:
    for i in range (a,0,-1):
        for j in range(0,i):
            print('*',end="")
        print("\r")
 
   
    