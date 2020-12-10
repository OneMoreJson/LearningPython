# Old... Build Calc Functions for Calculator

def addFunc(numA, numB):
    return numA + numB

def subFunc(numA, numB):
    return numA - numB

def multFunc(numA, numB):
    return numB * numA

def divFunc(numA, numB): 
    return numA / numB

# Old... Check in Range Function for Calculator

def isinrange (lr, hr, n):
    if n > lr and n < hr:
        return True
    else:
        return False 

# Old... New Function taking in the one string, parses it, then calls calc 
# functions according to the expression found in the string

def sCalc(expression):
    breakString = expression.split(", ")
    
    if breakString[2] == "+":
        answer = addFunc(int(breakString[0]), int(breakString[1]))
        return answer
        
    elif breakString[2] == "-":
        answer = subFunc(int(breakString[0]), int(breakString[1]))
        return answer
        
    elif breakString[2] == "*":
        answer = multFunc(int(breakString[0]), int(breakString[1]))
        return answer

    elif breakString[2] == "/":
        answer = divFunc(int(breakString[0]), int(breakString[1]))
        return answer
        
    else:
        answer = "no operator found"
        