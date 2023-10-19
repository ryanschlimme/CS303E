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

def isPrime(x):
    return

def findNextPrime(x):
    return

num = int(input("Enter a positive integer (or 0 to stop): "))

if num == 0:
    print("Goodbye!")
    exit()

while num != 0:
    factors = []
    if num == 1:
        print("1 has no prime factorization.")
    elif num < 0:
        print("Negative integer entered. Try again.")
    elif isPrime(num == True):
        factors = factors.append(num)
        print("The prime factorization of ", factors, "is: ", [num])
    else:
        factors = []
        d = 2
        