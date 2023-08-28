# EasterSunday.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 28 August 2023
# This program asks the user to input a year as a positive integer. It then performs a calculation to determine what date
# Easter Sunday falls on for that year using a pre-written algorithm. It prints this result.

y = int(input("Enter year: "))              # asks for input year, assume positive integers only, stores as y

a = y % 19                                  # store remainder as a
b = y // 100                                # store quotient as b (def: quotient ignores decimals)
c = y % 100                                 # store remainder as c
d = b // 4                                  # store quotient as d
e = b % 4                                   # store remainder as e
g = (8 * b + 13) // 25                      # store quotient as g
h  = (19 * a + b - d - g + 15) % 30         # store remainder as h
j = c // 4                                  # store quotient as j
k = c % 4                                   # store remainder as k
m = (a + 11 * h) // 319                     # store quotient as m
r = (2 * e + 2 * j - k - h + m + 32) % 7    # store remainder as r
n = (h - m + r + 90) // 25                  # store quotient as n, represents number of month
p = (h - m + r + n + 19) % 32               # store remainder as p, respresents number of day

print("In", y, "Easter Sunday is on month", int(n), "and day", int(p))