# Student.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 05 October 2023
# This program uses a class containing a student name (string) and two exam grades
# which can either be floats or integers. It requires that you always supply a student
# name when creating the class, with the option to include exam grades, defaulting to 
# None. The exam scores can be negative. 

# Define a __str__ method to print things nicely
# Shouldn't crash when asking for the average score if none are available

# Student class must have setters and getters for each of two exam grades
# Getter for name, no setter for name
# Name methods as follows
# getName()
# getExam1Grade()
# getExam2Grade()
# getAverage()
#   Prints "Some exam grades not available." if either exam score missing
# Allowed to have extra subsidiary functions inside and out of class if I want
# Make class data private, only available through setters and getters of class