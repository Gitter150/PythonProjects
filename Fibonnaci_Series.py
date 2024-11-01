
print("Welcome to the Fibonnaci Series Generator!")
def getnatnum():
    while True:
        try:
            n = int(input("Enter the limit of the series: "))
            if n > 0:
                return n
            else:
                print("Enter only a natural number (greater than 0).")
        except ValueError:
            print("Enter only a natural number (an integer).")


num = getnatnum()
fib=[]
m=0
while (m<num):
  fib.append(0)
  m+=1

fib[0]=0
fib[1]=1
i=0

for i in range(2,num):
    fib[i]=fib[i-1]+fib[i-2]
fibs=[str(x) for x in fib]
    
print(f"The Fibonnaci Series is: {", ".join(fibs)}")
 




     
   




        
        
