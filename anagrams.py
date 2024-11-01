print("Enter 2 strings to check if they are Anagrams!")
s1=input("Enter the string 1: ")
s2=input("Enter the string 2: ")
if sorted(s1)==sorted(s2):
    print(f"{s1} and {s2} are Anagrams!")
else: print(f"{s1} and {s2} are not Anagrams!")



     
