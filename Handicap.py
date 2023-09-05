# Handicap.py
# Ryan Schlimme
# rjs4999
# CS 303E
#
# 29 August 2023
# This program uses a predefined algorithm to calculate a bowler's average
# and handicap after three games. 

import math
import numpy as np

print()
name = str(input("Enter bowler's name: "))
game1 = int(input("Enter Game 1: "))
game2 = int(input("Enter Game 2: "))
game3 = int(input("Enter Game 3: "))

average = math.floor((game1 + game2 + game3) / 3)

handicap = math.floor((200 - average) * 0.80)
handicap = max(0, handicap)

out = str(name + ":")
outs = str(name + "'s")

print()
print("Handicap report for", out)
print(" ", outs, "average is:", average)
print(" ", outs, "handicap is:", handicap)
print()
print("It's time to Bowl!")
print()