# This is the flower box and it is at the begining of each assignment
# Program Name: Wk5_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Nov 25 2020
# Description: This now works with the module MyLib 
# Copy Wrong: This is my own work

import MyLib


# Building User Defined Exceptions
class UserInputOutsideRange(Exception):
    pass




    
# Begin Loop

cont = True

while cont == True: 
    
    # Input Values with Exception Control

    # First exception begins here with a while loop to control the response...
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

    # Second exception begins here with a while loop to control the response...
    bugB = True
    while bugB == True:
        try:
            numA = int(input("Please select the first number between " + str(high) + " and " + str(low) + " to be calculated:  "))
            numB = int(input("Please select the second number between " + str(high) + " and " + str(low) + " to be calculated:  "))
            bugB = False
        except ValueError:
            print("You did not input a number")


    # Error detection function called twice
    
    if MyLib.isinrange(low,high,numA) == True and MyLib.isinrange(low,high,numB) == True:
        
        # Calc Functions called and reported with print (NO print statments in calc functions)

        print("When you add", numA, "to", numB, "the sum is", MyLib.addFunc(numA, numB))
        print("When you subtract", numB, "from", numA, "the difference is", MyLib.subFunc(numA, numB))
        print("When you multiply", numA, "with", numB, "the product is", MyLib.multFunc(numA, numB))
        if numB == 0:
            print("no calculations are performed")
        else:
            print("When you divide", numA, "by", numB, "the quotent is", MyLib.divFunc(numA, numB))
    else:
        print("no calculations are performed")  
    
    # Continue Loop or Not
    
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
        