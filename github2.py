a=input("Enter your sex f or m: ")
b=int(input("Enter your salary:"))
if (a=='f' and b>10000):
    d=1.10*b
    print("YOUR SALARY IS :",d)
if (a=='m' and b>10000):
    c=1.05*b 
    print(" YOUR SALARY IS:",c)
if (a=='f' and b<10000):
    e=1.12*b
    print("YOUR SALARY IS :",e)
if (a=='m' and b<10000):
    f=1.07*b
    print("YOUR SALARY IS :",f)   