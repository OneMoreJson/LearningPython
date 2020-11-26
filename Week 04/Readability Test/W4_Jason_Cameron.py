# This is the flower box and it is at the begining of each assignment
# Program Name: Wk4_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Nov 25 2020
# Description: We Get To ADD EXCEPTIONS!!! 
# Copy Wrong: This is my own work...I really liked working on this!

##################################################################################
#                                  Explination                                   #
#                                                                                #
# Alright, this is going to be interesting since I've not done long explanation  #
# in a commented out piece of code before.  I’ve seen it done (I thought it      #
# looked to cool!)… I didn’t realize the work involved.  NTL… I wanted to put    #
# exceptions in for the two places that drove me crazy in the prior assignments. #
# (1) I wanted to meet the criteria that the user provided an input range number #
# between the numbers of -100 and 100.  I originally did this with if-then and   #
# while statements, not knowing that exceptions was a thing.  (2) I wanted to    # 
# keep the code from crashing due to an error that would occur when a user input # 
# something other than a integer.  For the first reason, I created a user        #
# exception labeled “UserInputOutsideRange.” I got the idea from our reading     # 
# material.  I needed to combine the < and > errors into one complete error.     # 
# At first this worked incredibly well.  That is, until I ended up with an error # 
# that my variables were not defined.  I found out that these exceptions will    # 
# “capture errors” and let the program continue.  However, if you capture the    # 
# error that was suppose to define a variable, your code will still crash.  I    # 
# could have simply put a exception on this part of the code to excuse the       # 
# undefined variable but I would have run into more errors that needed to be     # 
# captured in the long run.  Instead, I decided to force the user to input       #
# something the code could use.  This is why I decided to create a “while” loop  #
# (something we learned about in this week’s lessons).  This worked except I was #
# getting some interesting logical errors.  The issue was that the criteria	 that# 
# let the while loop break also allowed the variables to hold data that didn’t   #
# meet the desired result.  For example, I would still get a integer of 1000     #
# result after the exception notified the user that it was not meeting the       #
# required parameters.  To resolve this, I simply had to ensure the while loop   # 
# would replay after the exception was triggered.  I did this for both input     # 
# request that created a range for the upcoming calculations.                    #
#                                                                                # 
# The second exception I placed within the code is a simple ValueError exception # 
# that ensured whatever the user input did not break the code because it wasn’t a#
# integer.  I included this exception in both the selection of the range numbers #
# and the calculations numbers.  I remained consistant with what was expected in #
# the original assignment, letting the code “boot” you from the original "while" # 
# statement.                                                                     #
#                                                                                #
##################################################################################


# Building User Defined Exceptions
class UserInputOutsideRange(Exception):
    pass

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
        