'''
Title: Machine Learning
Author: Riley Carpenter
'''
import random
import os
import sys
import time
if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
def clear_screen():
    os.system(clearorcls)
print("Type any number and through the magic of machine learning this program will tell you what your number is")
previousnumbers = []
number = int(input("What's the number: "))
guessnumber = random.randint(0,9223372036854775807)
previousnumbers.append(guessnumber)
while number != guessnumber:
    clear_screen()
    print(guessnumber)
    if number != guessnumber:
        guessnumber *= -1
        previousnumbers.append(guessnumber)
    clear_screen()
    print(guessnumber)
    guessnumber = random.randint(0,9223372036854775807)
    if guessnumber in previousnumbers == True or (guessnumber * -1) in previousnumbers == True:
        guessnumber = random.randint(0,9223372036854775807)
else:
    print("Your number is",guessnumber)
