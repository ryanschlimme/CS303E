# FindPrimeFactors.py
# Ryan Schlimme
# rjs4499
# CS 303E
# 
# 16 October 2023
# This program asks the user for an input, assuming it is an integer.
# If the input is 0, the program ends after printing a Goodbye message.
# Otherwise, it prints the prime factorization, except if the input is 1
# when it will print that one does not exist. If the input is negative,
# that is reported.

import math

def isPrime(x):
    if (x < 2 or x % 2 == 0):
        return (x == 2)
    divisor = 3
    while (divisor <= math.sqrt(x)):
        if (x % divisor == 0):
            return False
        else:
            divisor += 2
    return True
    

def findNextPrime(x):
    if x < 2:
        return 2
    if x % 2 == 0:
        x -= 1
    guess = x + 2
    while (not isPrime(guess)):
        guess += 2
    return guess

while (1):
    num = int(input("Enter a positive integer (or 0 to stop): "))
    if num == 1:
        print("  1 has no prime factorization.")
        print()
    elif num == 0:
        print("Goodbye!")
        print()
        break
    elif num < 0:
        print("  Negative integer entered. Try again.")
        print()
    elif isPrime(num):
        factors = [num]
        print("  The prime factorization of", num, "is:", factors)
        print()
    else:
        d = 2
        factors = []
        while num > 1:
            if (num % d == 0):
                factors.append(d)
                num = num // d
            else: 
                d = findNextPrime(d)
        print("  The prime factorization of", num, "is:", factors)
        print()