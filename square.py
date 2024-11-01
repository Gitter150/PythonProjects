def getnatnum():
    while True:
        try:
            n = int(input("Enter the side length of the square in the units of '|' :"))
            if n>0:
                return n
            else:
                print("Invalid Input. Enter a positive number. ")
        except ValueError:
            print("Invalid Input. Only Enter Natural Numbers.")
x=getnatnum()
print('---'*x)
for i in range(x):
    print('|'," "*(3*x-2), '|',sep='')
print('---'*x)
