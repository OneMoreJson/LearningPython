# This is the flower box and it is at the begining of each assignment
# Program Name: Wk6_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Dec 2095 2020
# Description: Adding Dictionary to serve as a menu
# Copy Wrong: This is my own work


# Old... Imports the module
import MyLib

# Old... Building User Defined Exceptions
class UserInputOutsideRange(Exception):
    pass

# Week 06: Calling Function to Ask the user what they want to do
#          Note: Because of this, I pushed the "menu" list to MyLib; 
#          I hope this is ok.  
finalSimpleUI = MyLib.userInputFunc()

# Old... Begin Loop
cont = True
while cont == True: 
    
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

        # Week 06: Establishing the res dictionary per Assignment Requirements
        res = {'Add': 0, 'Subtract': 0, 'Multiply': 0, 'Divide': 0}

        # Week 06: Storing allInOne Function's data into local list 
        convAllInOneList = MyLib.allInOne(numA, numB, finalSimpleUI)

        # Week 06: Storing data from conversion list (data from allInOne) into
        # each item of the res dictionary
        res['Add'] = convAllInOneList[0]
        res['Subtract'] = convAllInOneList[1]
        res['Multiply'] = convAllInOneList[2]
        res['Divide'] = convAllInOneList[3]

        # Old...Error detection function called twice
        if MyLib.isinrange(low,high,numA) == True and MyLib.isinrange(low,high,numB) == True:
        
        # Week 06: Changed Print Response to Reflect Assignment Requirements
        #          All results are pulled from res dictionary per assignment requirements 
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

            # Week 06: Again calling Func to Ask the user what they want to do
            finalSimpleUI = MyLib.userInputFunc()
            
            # Week 06: Loop starts over if user selects anything but "exit"
            if finalSimpleUI == 'e':
                print("Thank You. Your Final Res Dictionary Is:\n", res)
                cont = False
            else:
                pass

        else:
            print("No Calculations Made")
            cont = False

