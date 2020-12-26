# file = open("lessonFile.txt", "w")
# print(file)
# file.write("hello class this is my file")
# file.write("\nand this is another line")
# file.close

# file = open('lessonFile.txt', 'r')
# lineno = 0
# for line in file:
#   lineno += 1 
#   print(lineno, " ", line)
#   file.close


# file = open("test8.txt", "w")
# print(file)
# # file.write("Another Test")
# file.close

# with open("test8.txt", "w") as out_file:      

#   out_file.write("this Text is going to out file\nLook at it and see!")
#   myinput = input("enter a phrase")
#   out_file.write(myinput)

# out_file.close

# with open("test8.txt", "r") as in_file:
#   text = in_file.read()

# print(text)

# in_file.close

# with open('jc.txt', 'a') as file:
#   text = file
#   # file.write("Writing something")
#   myInput = input("Tell me more of the story")
#   file.write(myInput)

# file.close

# with open('jc.txt', 'r') as file:
#   text = file.read()
#   print(text)

# file.close

# with open('jc.txt', 'r') as file:
#   text = file.read()
#   print(text.upper())

# file.close

#-------------------Creating CSV

# import csv 

# foodPricePairs = [['pear', 0.80], ['celery', 0.50], ['apple', 0.50]]

# with open("food.csv","w") as outFile:
#   for item in foodPricePairs:
#     lineStr = "{0},{1}".format(item[0], item[1])
#     lineStr = lineStr + "\n"
#     outFile.write(lineStr)
# outFile.close()

# print("Saved in food.csv")

# -------------------Adding to CSV

# import csv 

# foodPricePairs = [['pear', 0.80], ['celery', 0.50], ['apple', 0.50]]
# with open("food.txt", "a") as outFile:
#   for item in foodPricePairs:
#     lineStr = "{0},{1}".format(item[0], item[1])
#     lineStr = lineStr + "\n"
#     outFile.write(lineStr)
# outFile.close()
# print("Saved in food.txt")

# ------------------------Reading CSV

# import csv
# with open("food.txt", "r") as inFile:
#   strIn = inFile.read()
#   print(strIn)
# inFile.close()

# --------------------Reading one line at a time

# import csv
# with open("food.txt", "r", newline="\n") as inFile:
#   myReader = csv.reader(inFile)
#   for item in myReader:
#     print(item)
# inFile.close()

# ---------------------Updating file

# import csv

# outStr = " "
# lineStr = " "

# with open("food.txt", "r", newline="\n") as inFile:
#   myReader = csv.reader(inFile)
#   for item in myReader:
#     oldCost = float(item[1])
#     newCost = oldCost * 1.25

#     lineStr = "{0},{1}".format(item[0], newCost)
#     lineStr = lineStr + "\n"

#     outStr = outStr + lineStr

# inFile.close()

# with open('foodNew.txt', 'w') as outFile:
#   outFile.write(outStr)
# outFile.close()

# ------------------------Deleting a file

# import os
# os.remove("food.txt")
# print("food.txt was removed")

# 