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

# Week 06: Setting up the menu as a list
menu = ["Add", "Subtract", "Multiply", "Divide", "All", "Exit"]

# Week 06: Asking the user what they want to do
userSelect = input("Please select one of the following:\n***Hint: You can select the number for your selection***\n1. " + menu[0] + "\n2. " + menu[1] + "\n3. " + menu[2] + "\n4. " + menu[3] + "\n5. " + menu[4] + "\n6. " + menu[5] + "\n\n")

# Old... Begin Loop
cont = True

while cont == True: 

    finalSimpleUI = MyLib.simpleUI(userSelect)
    
    if finalSimpleUI == 'e':
        cont = False
        pass
    else:
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

        # Week 06: Establishing the dictionary 
        res = {'Add': 0, 'Subtract': 0, 'Multiply': 0, 'Divide': 0}


        conMemoryDict = MyLib.allInOne(numA, numB, finalSimpleUI)
        res['Add'] = conMemoryDict[0]
        res['Subtract'] = conMemoryDict[1]
        res['Multiply'] = conMemoryDict[2]
        res['Divide'] = conMemoryDict[3]

        # Old...Error detection function called twice
        if MyLib.isinrange(low,high,numA) == True and MyLib.isinrange(low,high,numB) == True:
        
        # Week 06: Changed Print Response to Reflect Assignment Requirements
            if finalSimpleUI == '+':
                print(str(numA) + " + " + str(numB) + " = " + str(res['Add']))
            elif finalSimpleUI == '-':
                print(str(numB) + " - " + str(numA) + " = " + str(res['Subtract']))
            elif finalSimpleUI == '*':
                print(str(numA) + " * " + str(numB) + " = " + str(res['Multiply']))
            elif finalSimpleUI == '/':
                print(str(numA) + " / " + str(numB) + " = " + str(res['Divide']))
            elif finalSimpleUI == 'a':
                print(str(numA) + " + " + str(numB) + " = " + str(res['Add']))
                print(str(numB) + " - " + str(numA) + " = " + str(res['Subtract']))
                print(str(numA) + " * " + str(numB) + " = " + str(res['Multiply']))
                print(str(numA) + " / " + str(numB) + " = " + str(res['Divide']))
            else:
                print("Thank You. Your Final Res Dictionary Is:\n", res)
                cont = False

            userSelect = input("Please select one of the following:\n***Hint: You can select the number for your selection***\n1. " + menu[0] + "\n2. " + menu[1] + "\n3. " + menu[2] + "\n4. " + menu[3] + "\n5. " + menu[4] + "\n6. " + menu[5] + "\n\n")
            
            finalSimpleUI = MyLib.simpleUI(userSelect)
            
            if finalSimpleUI == 'e':
                print("Thank You. Your Final Res Dictionary Is:\n", res)
                cont = False
            else:
                pass

        else:
            print("No Calculations Made")
            cont = False
            # numA = False
            # numB = False
            # highNum = False
            # lowNum = False
            # bugA = True
            # bugB = True
