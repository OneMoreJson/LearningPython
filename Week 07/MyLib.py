# adding all the functions to the class to be used in the main  code

class Calc:
    a = int
    b = int
    low = int
    high = int
    r = " "
    
    # Move Calc Functions
    def __init__(self, a, b, low, high, r):
        self.a = a
        self.b = b
        self.low = low
        self.high = high
        self.r = r
    
    def addMeth(self, a, b):
        return self.a + self.b
    
    def subMeth(self, a, b):
        return self.b - self.a

    def multMeth(self, a, b):
        return self.a * self.b

    def divMeth(self, a, b):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Unable by zero"

    # Get Low Number
    def getLowMeth(self):
        self.low = int(input("Please select your low number between 100 and -100:  "))
        return self.low

    # Get Low Number
    def getHighMeth(self):
        self.high = int(input("Please select your high number between 100 and -100:  "))
        return self.high

    # Get First Calc Number
    def getFirstNumMeth(self):
        self.a = int(input("Please select the first number between " + str(self.high) + " and " + str(self.low) + " to be calculated:  "))
        return self.a
    
    # Get Second Calc Number
    def getSecondNumMeth(self):
        self.b = int(input("Please select the Second number between " + str(self.high) + " and " + str(self.low) + " to be calculated:  "))    
        return self.b

    # Move and Combine Range Check and All In One
    def allInOne (self, a, b, low, high):
        if self.a > self.low and self.a < self.high and self.b > self.low and self.b < self.high:
            m = self.addMeth(a, b)
            n = self.subMeth(a, b)
            o = self.multMeth(a, b)
            p = self.divMeth(a, b)
            return m, n, o, p
        else:
            return 0, 0, 0, 0
    
    # Move Menu
    def userInputMeth(self):
        menu = ["Add", "Subtract", "Multiply", "Divide", "All", "Exit"]

        r = input("Please select one of the following:\n****Hint: You can select the number or type the word****\n1. " + menu[0] + "\n2. " + menu[1] + "\n3. " + menu[2] + "\n4. " + menu[3] + "\n5. " + menu[4] + "\n6. " + menu[5] + "\n\n")        

        if r == "1" or r.lower() == "add" or r.lower() == "a":
            self.r = "+"
            return self.r
        elif r == "2" or r.lower() == "subtract" or r.lower() == "s":
            self.r = "-"
            return self.r
        elif r == "3" or r.lower() == "multiply" or r.lower() == "m":
            self.r = "*"
            return self.r
        elif r == "4" or r.lower() == "divide" or r.lower() == "d":
            self.r = "/"
            return self.r
        elif r == "5" or r.lower() == "all":
            self.r = "a"
            return self.r
        elif r == '6' or r.lower() == "exit" or r.lower() == "e":
            self.r = "e"
            return self.r
        else:
            self.r = "e"
            return self.r



