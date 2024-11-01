string=input("Enter the string: ")
delete=['.',',','?','!',' ']
for x in delete:
   string=string.replace(x,"")
def can_form_palindrome(x):
   count=0
   for char in set(string):
      if not string.count(char)%2==0:
         count+=1
   return count<=1
   
print(f"{can_form_palindrome(string)}")



