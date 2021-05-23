#To print only numeric values greater than 6 from a given list
list1=["harry", 1, 6,"larry", 10, "haylor"]
for i in list1:
    if str(i).isnumeric() and i>6:
        print(i)