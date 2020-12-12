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

# Week 06: Needed to simplify user response for later
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


# Week 06: Submitting sCalc responses to the dictionary
def allInOne(a, b, operator):
    # Week 06: Establishing the dictionary 
    preRes = {'Add': 0, 'Subtract': 0, 'Multiply': 0, 'Divide': 0}

    if operator == "+":
        preRes['Add'] = addNum(a, b)
        preRes['Subtract'] = 0
        preRes['Multiply'] = 0
        preRes['Divide'] = 0
        return preRes['Add'], preRes['Subtract'], preRes['Multiply'], preRes['Divide']

    elif operator == "-":
        preRes['Add'] = 0
        preRes['Subtract'] = subNum(a, b)
        preRes['Multiply'] = 0
        preRes['Divide'] = 0
        return preRes['Add'], preRes['Subtract'], preRes['Multiply'], preRes['Divide']

    elif operator == "*":
        preRes['Add'] = 0
        preRes['Subtract'] = 0
        preRes['Multiply'] = multNum(a, b)
        preRes['Divide'] = 0
        return preRes['Add'], preRes['Subtract'], preRes['Multiply'], preRes['Divide']

    elif operator == "/":
        preRes['Add'] = 0
        preRes['Subtract'] = 0
        preRes['Multiply'] = 0
        preRes['Divide'] = divNum(a, b)
        return preRes['Add'], preRes['Subtract'], preRes['Multiply'], preRes['Divide']

    elif operator == "a":
        preRes['Add'] = addNum(a, b)
        preRes['Subtract'] = subNum(a, b)
        preRes['Multiply'] = multNum(a, b)
        preRes['Divide'] = divNum(a, b)
        return preRes['Add'], preRes['Subtract'], preRes['Multiply'], preRes['Divide']

    elif operator == 'e':
        preRes['Add'] = 0
        preRes['Subtract'] = 0
        preRes['Multiply'] = 0
        preRes['Divide'] = 0
        return preRes['Add'], preRes['Subtract'], preRes['Multiply'], preRes['Divide']

    else:
        preRes['Add'] = 0
        preRes['Subtract'] = 0
        preRes['Multiply'] = 0
        preRes['Divide'] = 0
        return preRes['Add'], preRes['Subtract'], preRes['Multiply'], preRes['Divide']
