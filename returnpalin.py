from itertools import permutations

string=input("Enter the string: ")

delete=['.',',','?','!',' ']

for x in delete:
   string=string.replace(x,"")


def is_palindrome(x):
   return x.lower()==x[::-1].lower() and len(x)>1

allperms=list(list(permutations(string,i+1)) for i in range(len(string)))
newallperms=[''.join(item) for i in range(len(string)) for item in allperms[i] ]
resallperms=list(set([item for item in newallperms if is_palindrome(item)]))

if len(resallperms)>0:
  for item in resallperms:
    print(item, end=', ' if item!=resallperms[-1] else '')
else:
   print("No Palindromes are possible")



   
