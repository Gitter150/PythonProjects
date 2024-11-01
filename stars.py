print("This program displays a diamond shaped star constellation!")
print("Enter the number of rows")

#get a natural number for the rows variable
def getnatnum():
    while True:
        try:
            n = int(input("Here: "))
            if n>0:
                return n
            else:
                print("Enter a positive number!")
        except ValueError:
            print("Enter only integers! Not letters or floating point numbers!")
rows=getnatnum()

#create the upper pyramid with middle row
for i in range(1,rows+1):
    print(" "*(rows-i),'*'*(2*i-1))

#create the lower pyramid without middle row
for i in range(1,rows+1):
    print(" "*i,"*"*(2*rows-2*i-1))


    