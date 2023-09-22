# FunctionExamples.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 19 September 2023
# This program creates several functions without input type validation.
# However, it does check for sign if that is important to the function.
# If there is an error, the function prints an error message. Additionally,
# none of these functions use recursion in their solution implementation.
# Each function also has a descriptive comment.

import math

def sum3Numbers(x,y,z):
    """Return the sum of the three paramters."""
    return x + y + z


def multiply3Numbers(x,y,z):
    """Return the product of the three parameters."""
    return x * y * z


def sumUpTo3Numbers(x, y=0, z = 0):
    """Returns the sum of up to three numbers, but at least one number."""
    return x + y + z


def multiplyUpTo3Numbers(x, y = 1, z = 1):
    """Return the product of up to three numbers, but at least one number."""
    return x * y * z


def printInOrder(x, y):
    """Prints two input arguments in ascending order"""
    if x > y:
        print(y, x)
    else:
        print(x, y)


def areaOfSquare(side):
    """Returns the area of a square given one side length. Prints an error message if side is negative."""
    if side<0:
        print("Negative value entered")
    else:
        return side ** 2


def perimeterOfSquare(side):
    """Returns the perimeter of a square given one side length. Prints an error message if side is negative."""
    if side<0:
        print("Negative value entered")
    else:
        return side * 4
    

def areaOfCircle(radius):
    """Returns the area of a circle given the radius. Prints an error message if radius is negative."""
    if radius<0:
        print("Negative value entered")
    else:
        return math.pi * radius ** 2
    

def circumferenceOfCircle(radius):
    """Return the circumference of a circle given the radius. Prints an error message if radius is negative."""
    if radius<0:
        print("Negative value entered")
    else:
        return 2 * math.pi * radius
    

def bothFactors(d1, d2, x):
    """Returns whether d1 and d2 are both factors of x, assuming all are integers"""
    if (x % d1 == 0)&(x % d2 == 0):
        return True
    else:
        return False


def squareAndCircle(x):
    """Prints the area and circumference of a circle with radius x and an area and perimeter of a square with side x using previous functions."""
    print()
    print("Circle with radius", x, " has:")
    print("   Area:", areaOfCircle(x))
    print("   Circumference:", circumferenceOfCircle(x))
    print("Square of side", x, " has:")
    print("   Area:", areaOfSquare(x))
    print("   Perimeter:", perimeterOfSquare(x))
    print()


def factorial(n):
    """Returns factorial of positive integer input using a loop. Prints an error message if it's not positive."""
    if n<0:
        print("Negative value entered")
    else:
        while(n<0):
            factorial *= n
            n -= 1


def numberLength(n):
    """Returns the number of digits in the decimal representation of a positive integer, n."""
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count