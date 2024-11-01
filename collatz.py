def collatz_series(n):
    sequence = []
    while n != 0:  
        
        sequence.append(n)
        if n==1:
            break
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    return sequence
n=1000
for i in range(1,n):
    print(f"{len(collatz_series(i))}",end=", ")
print(len(collatz_series(n)))


