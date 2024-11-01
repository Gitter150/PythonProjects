from math import gcd
from functools import reduce
print("This program calculates GCD and LCM of a list of numbers!")
while True:
    num=input("Enter the numbers: ")
    num2=num.replace(" ","").replace(",","")
    nums=num.replace(',',' ').split(" ")
    if num2.isdigit():
        break
    else:
        print("Invalid Input. Enter numbers separated by space or ','")

numlist=[int(x) for x in nums]
GCD=reduce(gcd, numlist)
print(f"The GCD of the above numbers is {GCD}")
LCM=reduce(lambda x,y:x*y//gcd(x,y) , numlist)
print(f"The LCM of the above numbers is {LCM}")

     


