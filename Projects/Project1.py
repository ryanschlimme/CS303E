# Project1.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 05 October 2023
# This program takes in a user integer input for month, validates it, then
# prints the calendar corresponding to the month they inputted for 2024.

YEAR = 2024

SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12


def monthName(n):
    if (n == JAN): return "January"
    if (n == FEB): return "February"
    if (n == MAR): return "March"
    if (n == APR): return "April"
    if (n == MAY): return "May"
    if (n == JUN): return "June"
    if (n == JUL): return "July"
    if (n == AUG): return "August"
    if (n == SEP): return "September"
    if (n == OCT): return "October"
    if (n == NOV): return "November"
    if (n == DEC): return "December"


def firstDayofMonth(n):
    if (n == JAN): return MON
    if (n == FEB): return THU
    if (n == MAR): return FRI
    if (n == APR): return MON
    if (n == MAY): return WED
    if (n == JUN): return SAT
    if (n == JUL): return MON
    if (n == AUG): return THU
    if (n == SEP): return SUN
    if (n == OCT): return TUE
    if (n == NOV): return FRI
    if (n == DEC): return SUN


def daysInMonth2024(n):
    if (n == JAN): return 31
    if (n == FEB): return 29
    if (n == MAR): return 31
    if (n == APR): return 30
    if (n == MAY): return 31
    if (n == JUN): return 30
    if (n == JUL): return 31
    if (n == AUG): return 31
    if (n == SEP): return 30
    if (n == OCT): return 31
    if (n == NOV): return 30
    if (n == DEC): return 31


def firstSpaces(n):
    if (n == SUN): return ""
    if (n == MON): return 3*" "
    if (n == TUE): return 6*" "
    if (n == WED): return 9*" "
    if (n == THU): return 12*" "
    if (n == FRI): return 15*" "
    if (n == SAT): return 18*" "


def printMonth(m):
    monthYear = monthName(m)+" 2024"
    spaces = firstSpaces(firstDayofMonth(m))
    print()
    print(monthYear.center(21))
    print("Su Mo Tu We Th Fr Sa")
    print(spaces, end="")
    col = firstDayofMonth(m)
    for i in range(1, daysInMonth2024(m)+1):
        print(format(i, ">2")+" ", sep = " ", end = "")
        if col == 6:
            col = 0
            print(end = "\n")
        else:
            col += 1
    if col != 0:
        print("\n")
    else: 
        print(end = "\n")

while(True):
    month = int(input("Enter the number of a month [1..12]: "))
    if (month < 1) or (month > 12):
        print("  Month must be between 1 and 12.  Try again!")
    else:
        printMonth(month)