import sys
import time
sys.set_int_max_str_digits(100000)
print("Welcome to the Fibonnaci Series Generator!")
def getnatnum():
    while True:
        try:
            n = int(input("Enter the nth digit of the Fibonnaci series: "))
            if n > 0:
                return n
            else:
                print("Enter only a natural number (greater than 0).")
        except ValueError:
            print("Enter only a natural number (an integer).")


num = getnatnum()
fib=[0]*num


fib[0]=0

if num>1:
    
 fib[1]=1
 i=0
 x=time.time()
 for i in range(2,num):
    fib[i]=fib[i-1]+fib[i-2]
 y=time.time()   
 print(f"The {num}th number of the fibonnaci series is: {fib[num-1]} in {y-x}s!")
elif num==1:
    print(f"The 1st number of the fibonnaci series is: 0")
 




     
   




        
        
