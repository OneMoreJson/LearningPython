# This is the flower box and it is at the begining of each assignment
# Program Name: Wk2P2_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Nov 02 2020
# Description: This Code will be a type of calculator
# Copy Wrong: This is, REALLY, my OWN work

# Greating
print("Hello. Please give us a range to work with between -100 and 100")
print()

# Setting Variables
high = False
low = False

numA = False
numB = False

# Setting the Range with the user
while high == False or high < -100 or high > 100:
    high = int(input("Please provide a number as your high number:   "))
    print()
    if high < -100 or high > 100:
        print("Please select BETWEEN -100 and 100.")
        print()
    else:
        print("Thank you.  Your high number is:", high)
        print()
        
while low == False or low < -100 or low > high:
    low = int(input("Please provide a number as your low number:   "))
    print()
    if low < -100 or low > 100:
        print("Please select BETWEEN -100 and 100.")
        print()
    elif low > high:
        print("Please select a number lower than your high number.   ")
        print()
    else:
        print("Thank you.  Your low number is:   ", low)
        print()

# Calc prep instructions
print("Now please select two numbers between", high, "and", low, "and we will provide their sum, difference, product and quotient.")
print()

# Setting numbers for calc
while numA == False or numA < low or numA > high:
    numA = int(input("Please select a number:   "))
    print()
    if numA < low or numA > high:
        print("Please choose a number between the range of", low, "and", high)
        print()
    else:
        print("Thank you.  You chose:   ", numA)
        print()
        
while numB == False or numB < low or numB > high:
    numB = int(input("Please select a Second number:   "))
    print()
    if numB < low or numB > high:
        print("Please choose a number between the range of", low, "and", high)
        print()
    else:
        print("Thank you.  You chose:   ", numB)
        print()

# Calc w/ "Error Detection"
addAnswer2 = numA + numB
subAnswer2 = numB - numA
multAnswer2 = numA * numB

if numA == 0 or numB == 0:
    divAnswer2 = "an error, you cannot divide by 0"
else:
    divAnswer2 = numA / numB

# Giving the Answers
print("When you add", numA, "to", numB, "the sum is", addAnswer2)
print("When you subtract", numA, "from", numB, "the difference is", subAnswer2)
print("When you multiply", numA, "with", numB, "the product is", multAnswer2)
print("When you divide", numA, "by", numB, "the quotent is", divAnswer2)

# Farewell 
print()
print("Thank you for letting us calculate more numbers!")