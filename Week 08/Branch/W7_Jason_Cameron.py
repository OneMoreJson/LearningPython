# This is the flower box and it is at the begining of each assignment
# Program Name: Wk7_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Dec 2095 2020
# Description: Moving all functions to a class
# Copy Wrong: This is my own work

# Week 07: Imports the class from the MyLib module
from MyLib import Calc

# Old... Building User Defined Exceptions
class UserInputOutsideRange(Exception):
    pass

# Week 07: Build OBJ from imported Class
calcObj = Calc(int, int, int, int, str)

# Week 07: Selection from menu
calcObj.userInputMeth()

# Old... Begin Loop
cont = True
while cont == True:
    
    if calcObj.r == 'e':
        cont = False
        break
    else:
        # Week 07: Get Range Numbers OBJ
        bugA = True
        while bugA == True:
            try:
                calcObj.getLowMeth()
                calcObj.getHighMeth()
                bugA = False
                if calcObj.low < -100 or calcObj.low > 100 or calcObj.high < -100 or calcObj.high > 100:
                    raise UserInputOutsideRange
            except UserInputOutsideRange:
                bugA = True
                print("You selected a number outside the range of -100 and 100")
            except ValueError:
                bugA = True
                print("You did not input a number")

        # Week 07: Get Calc Numbers with OBJ
        bugB = True
        while bugB == True:
            try:
                calcObj.getFirstNumMeth()
                calcObj.getSecondNumMeth()
                if calcObj.a < calcObj.low or calcObj.a > calcObj.high or calcObj.b < calcObj.low or calcObj.b > calcObj.high:
                    bugB = True
                    print("You selected a number outside", calcObj.low, "and", calcObj.high)
                else:
                    bugB = False
            except ValueError:
                print("You did not input a number")

        # Week 07: Establishing the res dictionary with OBJ
        res = {'Add': 0, 'Subtract': 0, 'Multiply': 0, 'Divide': 0}

        res['Add'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[0]
        res['Subtract'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[1]
        res['Multiply'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[2]
        res['Divide'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[3]

        # Week 07: Mod with OBJ and Keeping the Local Dictionary
        if calcObj.r == '+':
            print(calcObj.a, calcObj.r, calcObj.b, "=", res['Add'])
            print("I also attached the library:\n", res, "\n")

        elif calcObj.r == '-':
            print(calcObj.b, calcObj.r, calcObj.a, "=", res['Subtract'])
            print("I also attached the library:\n", res, "\n")

        elif calcObj.r == '*':
            print(calcObj.a, calcObj.r, calcObj.b, "=", res['Multiply'])
            print("I also attached the library:\n", res, "\n")

        elif calcObj.r == '/':
            print(calcObj.a, calcObj.r, calcObj.b, "=", res['Divide'])
            print("I also attached the library:\n", res, "\n")

        elif calcObj.r == 'a':
            print(calcObj.a, "+", calcObj.b, "=", res['Add'])
            print(calcObj.b, "-", calcObj.a, "=", res['Subtract'])
            print(calcObj.a, "*", calcObj.b, "=", res['Multiply'])
            print(calcObj.a, "/", calcObj.b, "=", res['Divide'])
            print("I also attached the library:\n", res, "\n")
            
        else:
            print("Thank You. Your Final Res Dictionary Is:\n", res, "\n")
            cont = False
            break
        
        # Week 07: Loop starts over with obj method
        calcObj.userInputMeth()
        if calcObj.r == 'e':
            print("Thank You. Your Final Res Dictionary Is:\n", res)
            cont = False
            break
        else:
            cont = True
