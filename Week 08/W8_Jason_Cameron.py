# This is the flower box and it is at the begining of each assignment
# Program Name: Wk_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Dec 25 2020
# Description: Adding a "save" feature to the menu
# Copy Wrong: This is my own work

# Old... Imports the class from the MyLib module
from MyLib import Calc

# Old... Building User Defined Exceptions
class UserInputOutsideRange(Exception):
    pass

# Week 08: Replaced int with numbers and a string
calcObj = Calc(0, 0, 0, 0, " ")

# Old... Selection from menu
calcObj.userInputMeth()

# Week 08: Added if else to keep from errors on initial menu selection
if calcObj.r == 'e':
    print("You selected 'Exit.' ")
elif calcObj.r == 'sc':
    print("You do not have any calculations to show.")
elif calcObj.r == 'sl':
    print("You do not have any calculations to save.")
else: 
    # Old... Begin Loop
    cont = True
    while cont == True:
        
        # Week 08: Added additional elif statement to handle new menu selections
        if calcObj.r == 'e':
            cont = False
            break
        elif calcObj.r == 'sc':
            try:
                print("Here is the res library... This library comes from the All-In-One Function located in the MyLib module holding the Calc Class:\n", res, "\nHowever, you might have wanted all the different operations so I provided them here:\n", answer)
            except NameError: 
                print("At the moment, no caclulations can be displayed")
                calcObj.userInputMeth()
        elif calcObj.r == 'sl':
            fileTitle = input("Please provide the name of the file you want to save your responses:  ")
            fileTitle = fileTitle.lower() + ".txt"
            with open(fileTitle, "w") as outFile:
                outFile.write(str(answer))
            outFile.close()
            print("The", fileTitle, "was saved with the last library of operations:\n" + answer)
            calcObj.userInputMeth()

        elif calcObj.r == 'rf':
            try:
                fileTitle = input("Please provide the name of the file you want to read:  ")
                fileTitle = fileTitle.lower() + ".txt"
                with open(fileTitle, "r") as inFile:
                    stringIn = inFile.read()
                    print("The Information found in this file is as follows:\n" + stringIn)                
                    inFile.close()
                print("File with the title:", fileTitle, "is now closed")
            except FileNotFoundError:
                print("File is not found")
            finally:
                calcObj.userInputMeth()

        else:
            # Old... Get Range Numbers OBJ
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

            # Old... Get Calc Numbers with OBJ
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

            # Old... Establishing the res dictionary with OBJ
            res = {'Add': 0, 'Subtract': 0, 'Multiply': 0, 'Divide': 0}

            res['Add'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[0]
            res['Subtract'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[1]
            res['Multiply'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[2]
            res['Divide'] = calcObj.allInOne(calcObj.a, calcObj.b, calcObj.low, calcObj.high)[3]

            # Week 08: Changed all to string results; I know there are other 
            #          things I could do, but this let me simply write the 
            #          results in a file.  I believe THIS was optional so I 
            #          chose to write data to a file in this manner
            if calcObj.r == '+':
                answer = str(calcObj.a) + str(calcObj.r) + str(calcObj.b) + "=" + str(res['Add'])
                print(answer)

            elif calcObj.r == '-':
                answer = str(calcObj.b) + str(calcObj.r) + str(calcObj.a) + "=" + str(res['Subtract'])
                print(answer)

            elif calcObj.r == '*':
                answer = str(calcObj.a) + str(calcObj.r) + str(calcObj.b) + "=" + str(res['Multiply'])
                print(answer)

            elif calcObj.r == '/':
                answer = str(calcObj.a) + str(calcObj.r) + str(calcObj.b) + "=" + str(res['Divide'])
                print(answer)

            elif calcObj.r == 'a':
                answer = str(calcObj.a) + "+" + str(calcObj.b) + "=" + str(res['Add']) + "\n" + str(calcObj.b) + "-" + str(calcObj.a) + "=" + str(res['Subtract']) + "\n" + str(calcObj.a) + "*" +  str(calcObj.b) + "=" + str(res['Multiply']) + "\n" + str(calcObj.a) + "/" + str(calcObj.b) + "=" + str(res['Divide'])
                print(str(answer))
                
            else:
                print("Thank You. Your Final Res Dictionary Is:\n", res, "\n")
                cont = False
                break
            
            # Week 08: Loop starts over; added more responses for the new menu
            #          results
            calcObj.userInputMeth()
            if calcObj.r == 'e':
                print("Thank You. Your Final Res Dictionary Is:\n", res)
                cont = False
                break

            elif calcObj.r == 'sc':
                print("Here is the res library... This library comes from the All-In-One Function located in the MyLib module holding the Calc Class:\n", res, "\nHowever, you might have wanted all the different operations so I provided them here:\n", answer)
                calcObj.userInputMeth()
            
            elif calcObj.r == 'sl':
                fileTitle = input("Please provide the name of the file you want to save your responses:  ")
                fileTitle = fileTitle.lower() + ".txt"
                with open(fileTitle, "w") as outFile:
                    outFile.write(str(answer))
                outFile.close()
                print("The", fileTitle, "was saved with the last library of operations:\n" + answer)
                calcObj.userInputMeth()

            elif calcObj.r == 'rf':
                try:
                    fileTitle = str(input("Please provide the name of the file you want to read:  "))
                    fileTitle = fileTitle.lower() + ".txt"
                    with open(fileTitle, "r") as inFile:
                        stringIn = inFile.read()
                        print("The Information found in this file is as follows:\n" + stringIn)
                    inFile.close()
                    print("File with the title:", fileTitle, "is now closed")
                except FileNotFoundError:
                    print("File is not found")
                finally:
                    calcObj.userInputMeth()

            else:
                cont = True
