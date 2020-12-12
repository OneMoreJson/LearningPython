# Week 06: Kept the calc functions but pushed 0 division error detect to divNum Function
def addNum(y, z):
    return y + z

def subNum(y, z):
    return z - y

def multNum(y, z):
    return y * z

def divNum(y, z):
    if z == 0:
        return "Not able to divide by 0"
    else:
        return y / z


# Old... Check in Range Function for Calculator
def isinrange (lr, hr, n):
    if n > lr and n < hr:
        return True
    else:
        return False 


# Week 06: Needed to simplify user response for later use
def simpleUI(r):
    if r == "1" or r.lower() == "add" or r.lower() == "a":
        return '+'
    elif r == "2" or r.lower() == "subtract" or r.lower() == "s":
        return '-'
    elif r == "3" or r.lower() == "multiply" or r.lower() == "m":
        return '*'
    elif r == "4" or r.lower() == "divide" or r.lower() == "d":
        return '/'
    elif r == "5" or r.lower() == "all":
        return 'a'
    elif r == '6' or r.lower() == "exit"or r.lower() == "e":
        return 'e'
    else:
        return 'e'


# Week 06: Added this as a function in MyLib because we call the action twice
def userInputFunc():
    # Week 06: Setting up the menu as a list...
    #          Please note there was some confusion with the examples.  
    #          Last week's sCalc became the "All" selection.  When you "exit"
    #          you will see the dictionary receipt of what was calculated last.
    menu = ["Add", "Subtract", "Multiply", "Divide", "All", "Exit"]

    # Week 06: Pulls menu list to create a "menu" for the user to select
    selection = input("Please select one of the following:\n\n****Hint: You can select the number or type the word****\n1. " + menu[0] + "\n2. " + menu[1] + "\n3. " + menu[2] + "\n4. " + menu[3] + "\n5. " + menu[4] + "\n6. " + menu[5] + "\n\n")
    
    # Week 06: Actually call this function within MyLib to simplify the User's 
    #          response.  --> Code Above
    return simpleUI(selection)


# Week 06: Changed sCalc to AllInOne Function.  Based on what the User wants to do
#          the function returns the calculations as a list.  The list is later
#          placed into the "res" dictionary and will be printed accordingly
def allInOne(a, b, operator):
    if operator == "+":
        m = addNum(a, b)
        return m, 0, 0, 0
    elif operator == "-":
        n = subNum(a, b)
        return 0, n, 0, 0
    elif operator == "*":
        o = multNum(a, b)
        return 0, 0, o, 0
    elif operator == "/":
        p = divNum(a, b)
        return 0, 0, 0, p
    elif operator == "a":
        m = addNum(a, b)
        n = subNum(a, b)
        o = multNum(a, b)
        p = divNum(a, b)
        return m, n, o, p
    elif operator == 'e':
        return 0, 0, 0, 0
    else:
        return 0, 0, 0, 0
