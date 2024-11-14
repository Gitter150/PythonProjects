def isValidParantheses()-> bool:

    valid_pars = {   #dictionary for valid pairs of brackets
    ')':'(',
    '}':'{',
    ']':'['
    }

    p = input("Enter the expression\n")   #accepting the input string
  
    stack = []   #stack used for checking

    for par in p:   #iterate through each character in the input string
        if par in valid_pars.values():  #checks if par is opening bracket
            stack.append(par)           #push par to stack if its an opening bracket
        elif par in valid_pars:         #checks if its a closing bracket
            if len(stack) and stack[-1]==valid_pars[par]: 
                stack.pop()        #pops if it finds a matching opening bracket
            else:
                return False       #false if string has trailing closing brackets or if it doesn't find a matching opening bracket
    
    return len(stack)==0           #returns whether stack is empty at last

print(isValidParantheses())
