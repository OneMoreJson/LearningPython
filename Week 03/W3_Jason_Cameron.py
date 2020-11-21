# This is the flower box and it is at the begining of each assignment
# Program Name: Wk3_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Nov 11 2020
# Description: This is a change  to the calculator to include functions and loops
# Copy Wrong: This is my own work 


# Build Calc Functions

def addFunc(numA, numB):
    return numA + numB

def subFunc(numA, numB):
    return numA - numB

def multFunc(numA, numB):
    return numB * numA

def divFunc(numA, numB): 
    return numA / numB

# Check in Range Function

def isinrange (lr, hr, n):
    if n > lr and n < hr:
        return True
    else:
        return False 
    
# Begin Loop

cont = True

while cont == True: 
    
    # Input Values 

    low = int(input("Please select your low number between 100 and -100:  "))
    high = int(input("Please select your high number between 100 and -100:  "))

    numA = int(input("Please select the first number between " + str(high) + " and " + str(low) + " to be calculated:  "))
    numB = int(input("Please select the second number between " + str(high) + " and " + str(low) + " to be calculated:  "))


    # Error detection function called twice
    
    if isinrange(low,high,numA) == True and isinrange(low,high,numB) == True:
        
        # Calc Functions called and reported with print (NO print statments in calc functions)

        print("When you add", numA, "to", numB, "the sum is", addFunc(numA, numB))
        print("When you subtract", numB, "from", numA, "the difference is", subFunc(numA, numB))
        print("When you multiply", numA, "with", numB, "the product is", multFunc(numA, numB))
        if numB == 0:
            print("no calculations are performed")
        else:
            print("When you divide", numA, "by", numB, "the quotent is", divFunc(numA, numB))
    else:
        print("no calculations are performed")  
    
    # Continue Loop or Not
    
    response = input("Would you Like To Continue, type 'Y' or 'N'")
    if response == 'y' or response == 'Y':
        numA = False
        numB = False
        highNum = False
        lowNum = False
        cont = True

    elif response == 'n' or response == 'N':
        cont = False
        print("Thank you for letting us calculate more numbers!")  

    else:
        print("no calculations are performed")
        numA = False
        numB = False
        highNum = False
        lowNum = False
        cont = True
        