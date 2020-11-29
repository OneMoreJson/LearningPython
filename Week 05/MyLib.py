# Build Calc Functions for Calculator

def addFunc(numA, numB):
    return numA + numB

def subFunc(numA, numB):
    return numA - numB

def multFunc(numA, numB):
    return numB * numA

def divFunc(numA, numB): 
    return numA / numB

# Check in Range Function for Calculator

def isinrange (lr, hr, n):
    if n > lr and n < hr:
        return True
    else:
        return False 