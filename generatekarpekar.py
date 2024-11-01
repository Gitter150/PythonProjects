def is_karpekarForm(x: int) -> bool:
    if x == 1 or x == 9:
        return True
    
    square_str = str(x ** 2)
    for i in range(1, len(square_str)):
        left_part = int(square_str[:i])
        right_part = int(square_str[i:])
        if right_part != 0 and left_part + right_part == x:
            return i
    
    return False

for num in range(10, 1000000):
    pos = is_karpekarForm(num)
    if pos:
        square_str = str(num ** 2)
        left_part = int(square_str[:pos])
        right_part = int(square_str[pos:])
        print(f"{num} is a Kaprekar number because its square is {square_str} and {left_part} + {right_part} = {num}")
