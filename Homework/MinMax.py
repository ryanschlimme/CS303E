# MinMax.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 18 September 2023
# This program takes an arbitrary number of integer inputs and prints the count of numbers entered and the minimum and maximum
# of the numbers entered without using loops. The user ends the input loop by typing "stop" which causes the program to output
# a blank line and the outputs. If the user stops before entering any numbers, then there is a separate output message.

a = input("Enter an integer or 'stop' to end: ")

if a == "stop":
    print("\nYou didn't enter any numbers")
    exit()
else:
    a = int(a)
    lengthNums = int(0)
    maxNum = a
    minNum = a

b = a
while(b != "stop"):
    b = int(b)
    lengthNums = lengthNums + 1
    if b > maxNum:
        maxNum = b
    elif b < minNum:
        minNum = b
    b = input("Enter an integer or 'stop' to end: ")

if lengthNums == 1:
    string = "number"
else:
    string = "numbers"

print()
print("You entered", lengthNums, string)
print("The maximum is", maxNum)
print("The minimum is", minNum)