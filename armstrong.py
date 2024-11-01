listofnums=[x+1 for x in range(1000000)]
for x in listofnums:
   n=len(str(x))
   if sum(int(digit)**n for digit in str(x))==x and len(str(x))>1:
      print(f"{x} is a Narcissistic Number")