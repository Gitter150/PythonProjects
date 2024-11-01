while True:
   
    string=input("Enter the message you want to encrypt: ")
    stri=string.replace(' ','')
    stri=stri.replace('!','')
    stri=stri.replace(',','')
    stri=stri.replace('.','')
    
       
    
    

    if stri.isalpha():
     break
    else:
      print("Invalid Input. Non-alphabetical Characters are not allowed. ")

string=list(string)
def caesar_cipher_char_down(char, key):
    if char.isupper():
        start = ord('A')
        return chr((ord(char) - start - key) % 26 + start)
    elif char.islower():
        start = ord('a')
        return chr((ord(char) - start - key) % 26 + start)
    return char
res=[]
while True:
    k=int(input("Enter the secret key (0 to 25): "))
    if 0<=k<=25:
      break
    elif not isinstance(k, int):
      print("")
    else:
      print("Invalid Input. Please Enter the secret key between 0 and 25.")
    
   
for x in string:
   res.append(caesar_cipher_char_down(x, k))
print("The Encrypted Message is:",''.join(res))
   



   
   
   
   
    
