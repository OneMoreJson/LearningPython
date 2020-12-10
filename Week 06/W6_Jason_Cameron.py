# This is the flower box and it is at the begining of each assignment
# Program Name: Wk6_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Dec 2095 2020
# Description: Adding Dictionary to serve as a menu
# Copy Wrong: This is my own work


# Old... As it says...imports the module
import MyLib


# Old... Building User Defined Exceptions
class UserInputOutsideRange(Exception):
    pass

# Old... Begin Loop
cont = True

while cont == True: 
    
    # Old... Gather inputs for user define ranges
    bugA = True
    while bugA == True:
        try:
            low = int(input("Please select your low number between 100 and -100:  "))
            high = int(input("Please select your high number between 100 and -100:  "))
            bugA = False
            if low < -100 or low > 100:
                raise UserInputOutsideRange
            elif high < -100 or high > 100:
                raise UserInputOutsideRange
        except UserInputOutsideRange:
            bugA = True
            print("You selected a number outside the range of -100 and 100")
        except ValueError:
            bugA = True
            print("You did not input a number")

    # Old... Gather inputs for user defined numbers to be calculated
    bugB = True
    while bugB == True:
        try:
            numA = int(input("Please select the first number between " + str(high) + " and " + str(low) + " to be calculated:  "))
            numB = int(input("Please select the second number between " + str(high) + " and " + str(low) + " to be calculated:  "))
            bugB = False
        except ValueError:
            print("You did not input a number")

    # Old... String Function ... It's funny cause we go from intiger->to string-> and later back to an intiger inside the sCalc function

    a = str(numA)
    b = str(numB)
    c = ['+', '-', '*', '/']
    d = 0  

    dMathString = a + ", " + b + ", " + c[0 + d]  # Old... Combining to make 1 final string

    # Old...Error detection function called twice
    if MyLib.isinrange(low,high,numA) == True and MyLib.isinrange(low,high,numB) == True:
        
        # Old... Calc Functions called through the sCacl Function; results printed
        print("When you add", numA, "to", numB, "the sum is", MyLib.sCalc(dMathString))
        d = d + 1 
        dMathString = a + ", " + b + ", " + c[0 + d]

        print("When you subtract", numB, "from", numA, "the difference is",  MyLib.sCalc(dMathString))
        d = d + 1
        dMathString = a + ", " + b + ", " + c[0 + d]

        print("When you multiply", numA, "with", numB, "the product is",  MyLib.sCalc(dMathString))
        d = d + 1
        dMathString = a + ", " + b + ", " + c[0 + d]

        if numB == 0:
            print("no calculations are performed")
            d = d - 3  
            dMathString = a + ", " + b + ", " + c[0 + d]
        else:
            print("When you divide", numA, "by", numB, "the quotent is",  MyLib.sCalc(dMathString))
            d = d - 3  
            dMathString = a + ", " + b + ", " + c[0 + d]
    
    else:
        print("no calculations are performed")
        d = 0  
        dMathString = a + ", " + b + ", " + c[0]
    
    # Old... Continue Loop or Not
    
    response = input("Would you Like To Continue, type 'Y' or 'N'")
    if response == 'y' or response == 'Y':
        numA = False
        numB = False
        highNum = False
        lowNum = False
        bugA = True
        bugB = True
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
        bugA = True
        bugB = True
        cont = True
        