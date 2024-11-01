numString=input("Enter the number: ")


def is_palindrome(x:str)->bool:
    return x==x[::-1]

num=int(numString)

i=num
j=num
while True:
    if is_palindrome(str(i)) or is_palindrome(str(j)):
        break
    
    i+=1
    j-=1
    
print(f"The Closest Palindrome to {num} is {i}" if is_palindrome(str(i)) else f"The Closest Palindrome to {num} is {j}")

