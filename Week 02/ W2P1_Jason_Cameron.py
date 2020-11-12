# This is the flower box and it is at the begining of each assignment
# Program Name: Wk2P1_Jason_Cameron.py
# Student Name: Jason Cameron
# Course: ENTD220
# Instructor: Dr. Randy Bower
# Date: Nov 02 2020
# Description: This Code will be a type of calculator
# Copy Wrong: This is, REALLY, my OWN work

# Greeting
print("Hello. If you give us two numbers, we will give you their sum, difference, product and quotient.")
print()
# Number Collection
num01 = int(input("Please select a number between 0 and 100:  "))
print()

num02 = int(input("Please select another number between 0 and 100:  "))
print()
# Calculations
addAnswer = num01 + num02
subAnswer = num02 - num01
multAnswer = num01 * num02
divAnswer = num01 / num02
# Answers
print("When you add", num01, "to", num02, "the sum is", addAnswer)
print("When you subtract", num01, "from", num02, "the difference is", subAnswer)
print("When you multiply", num01, "with", num02, "the product is", multAnswer)
print("When you divide", num01, "by", num02, "the quotent is", divAnswer)
# Farewell 
print()
print("Thank you for letting us calculate your numbers!")