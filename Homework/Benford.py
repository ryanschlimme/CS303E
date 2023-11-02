# Benford.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 30 October 2023
# This program accepts from the user the name of a file containing data. If no file exists, it prints
# an error message and quits. Then, it creates an empty set to store unique population values. Then, it
# creates a dictionary for leading digit counts with entries of the from [digit:count] where digit is a
# character not a number. All counts are initially 0 for 9 possible digits [1,2,...,9]. It then outputs
# a file called benford.txt the total county population values, how many unique population values, a table
# of results for the leading digits. Then it closes benford.txt before exiting.

import os

dict = {}
unique = set()

for i in range(1,10):
    dict[str(i)] = 0

file = str(input("Enter the name of a file: "))

if os.path.isfile(file) == False:
    print("File does not exist")
    exit()

inFile = open(file, "r")
lineCount = 0
line = inFile.readline()
while line:
    if "#" in line: 
        line = inFile.readline()
    else: 
        vals = line.split("&")
        pop = vals[-1]
        pop = pop.strip()
        unique.add(pop)
        for i in range(1,10):
            if pop[0] == str(i):
                dict[str(i)] += 1
        lineCount += 1
        line = inFile.readline()
inFile.close()

outFile = open("benford.txt", "w")
outFile.write("Total number of counties: " + str(lineCount) + "\n")
outFile.write("Unique population counts: " + str(len(unique)) + "\n")
outFile.write("First digit frequency distributions: \n")
outFile.write("Digit" + "   " + "Count" + "   " + "Percentage" )
for i in range(1,10):
    percent = dict[str(i)]/lineCount*100
    z = str(i)
    outFile.write("\n" + z.ljust(5) + "   " + str(dict[z]).ljust(5) + "   " + format(percent, "0.1f").ljust(10))
outFile.close()

print("Output written to benford.txt")