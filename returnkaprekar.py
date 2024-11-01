def return_largest_smallest_num(x: int)->tuple:
    x=str(x)
    x_list=list(x)
    x_list.sort()
    x_ascending=''.join(x_list)
    x_descending=x_ascending[::-1]
    return (int(x_ascending),int(x_descending))


def kaprekarConstant(x:int)->int:
    
    numTuple=return_largest_smallest_num(x)
    return numTuple[1]-numTuple[0]


def composition(func, value, n):
    res=value
    for _ in range(n):
        res=func(res)
        if res==6174:
            break
    return res

print(composition(kaprekarConstant, 61747, 7))
    