def isValidParantheses(p: str)-> bool:

    valid_pars = {   #dictionary for valid pairs of brackets
    ')':'(',
    '}':'{',
    ']':'['
    }   
  
    stack = []   #stack used for checking

    for char in p:   #iterate through each character in the input string
        if char in valid_pars.values():  #checks if par is opening bracket
            stack.append(char)           #push par to stack if its an opening bracket
        elif char in valid_pars:         #checks if its a closing bracket
            if len(stack) and stack[-1]==valid_pars[char]: 
                stack.pop()        #pops if it finds a matching opening bracket
            else:
                return False       #false if string has trailing closing brackets or if it doesn't find a matching opening bracket
    
    return len(stack)==0           #returns whether stack is empty at last

p = input("Enter the expression\n");
print("The parantheses are valid" if isValidParantheses(p) else "The parantheses are not written correctly; try to correct it")
