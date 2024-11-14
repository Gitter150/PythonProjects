def isValidParantheses()-> bool:

    valid_pars = {
    ')':'(',
    '}':'{',
    ']':'['
    }

    p = input("Enter the expression\n") 
  
    stack = []

    for par in p:
        if par in valid_pars.values():
            stack.append(par)
        elif par in valid_pars:
            if len(stack) and stack[-1]==valid_pars[par]:
                stack.pop()
            else:
                return False
    
    return len(stack)==0

print(isValidParantheses())
