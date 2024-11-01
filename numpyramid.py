n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),(int('1'*i))*(int('1'*i)))
m=n
while m>1:
   print((" ")*(n-m+1),(int('1'*(m-1)))*(int('1'*(m-1))))
   m-=1


