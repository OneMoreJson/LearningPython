# This is the flower box and it is at the begining of each assignment
# Program Name: Wk3_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Nov 11 2020
# Description: This is a change  to the calculator to include functions and loops
# Copy Wrong: This is, REALLY, my own work (It was challenging but worth it)

# Vars Set Up

cont = True

highNum = False
lowNum = False

numA = False
numB = False

# Build Calc Functions

def addFunc(numA, numB):
    answer1 = numA + numB
    return answer1

def subFunc(numA, numB):
    answer2 = numB - numA
    return answer2

def multFunc(numA, numB):
    answer3 = numB * numA
    return answer3

def divFunc(numA, numB):
    if numA == 0 or numB == 0:
        answer4 = "an error, you cannot divide by 0."
        return answer4
    else:
        answer4 = numA / numB
        return answer4

# Build Range Number Requests Functions

def highNumFunc(highNum):
    while highNum == False or highNum < -100 or highNum > 100:
        highNum = int(input("Please provide a number as your high number:   "))
        print()
        if highNum < -100 or highNum > 100:
            print("Please select BETWEEN -100 and 100.")
            print()
        else:
            print("Thank you.  Your high number is:", highNum)
            print()
            return highNum


def lowNumFunc(lowNum,highNum):
    while lowNum == False or lowNum < -100 or lowNum > highNum:
        lowNum = int(input("Please provide a number as your low number:   "))
        print()
        if lowNum < -100 or lowNum > 100:
            print("Please select BETWEEN -100 and 100.")
            print()
        elif lowNum > highNum:
            print("Please select a number lower than your high number.   ")
            print()
        else:
            print("Thank you.  Your low number is:   ", lowNum)
            print()
            return lowNum

        
# Build Number Requests for Calc Functions
    
def numAFunc(numA):
    print("Now please select two numbers between", highNum, "and", lowNum, "and we will provide their sum, difference, product and quotient.")
    print()
    while numA == False or numA < lowNum or numA > highNum:
        numA = int(input("Please select a number:   "))
        print()
        if numA < lowNum or numA > highNum:
            print("Please choose a number between the range of", lowNum, "and", highNum)
            print()
        else:
            print("Thank you.  You chose:   ", numA)
            print()
            return numA


def numBFunc(numB):
    while numB == False or numB < lowNum or numB > highNum:
        numB = int(input("Please select a Second number:   "))
        print()
        if numB < lowNum or numB > highNum:
            print("Please choose a number between the range of", lowNum, "and", highNum)
            print()
        else:
            print("Thank you.  You chose:   ", numB)
            print()
            return numB

# Loop Set Up

while cont == True: 
    if cont == False:
        break
    else:
    # Greeting Set Up
    
        print("Hello. Please give us a range to work with between -100 and 100")
        print()

        # Get High Number for Range

        highNum = highNumFunc(highNum)

        # Get Low Number for Range

        lowNum = lowNumFunc(lowNum, highNum)

        # Get First number for Calc

        numA = numAFunc(numA)

        # Get Second number for Calc

        numB = numBFunc(numB)

        # Call Fuctions and Store in CalcAnswers
        
        addAnswer = addFunc(numA, numB)
        
        subAnswer = subFunc(numA, numB)
        
        multAnswer = multFunc(numA, numB)
        
        divAnswer = divFunc(numA, numB)
        

        # Print CalcAnswers

        print("When you add", numA, "to", numB, "the sum is", addAnswer)
        print()
        print("When you subtract", numB, "from", numA, "the difference is", subAnswer)
        print()
        print("When you multiply", numA, "with", numB, "the product is", multAnswer)
        print()
        print("When you divide", numA, "by", numB, "the quotent is", divAnswer)
        print()

        # Ask to Continue

        response = input("Would you Like To Continue, type 'Y' or 'N'   ")
        
        if response == 'y' or response == 'Y':
            numA = False
            numB = False
            highNum = False
            lowNum = False
            cont = True
        
        elif response == 'n' or response == 'N':
            cont = False
            print()
            print("Thank you for letting us calculate more numbers!")  
            
        else:
            print()
            print("I'm sorry.  You did not select either 'Y' or 'N.' Goodbye.")
            break