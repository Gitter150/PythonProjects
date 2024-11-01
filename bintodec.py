while True:
     binary=input("Enter the binary number: ")
     bin1={"0","1"}
     bin2=set(binary)
     
     if bin2.issubset(bin1) and len(bin2)>0:
        break
     else:
        print("Invalid Input. Enter a valid binary number.")


intBinary=[int(x) for x in binary]
total=0
n=len(binary)
for i in range(n):
     total+=(2**(n-i-1))*intBinary[i]
print(f"{binary} in base 10 is:      {total}")