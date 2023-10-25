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

class Student:
    def __init__(self, Name, Exam1 = None, Exam2 = None):
        self.__studentName = Name
        self.__Exam1Grade = Exam1
        self.__Exam2Grade = Exam2

    def __str__(self):
        return("Student: " + str(self.__studentName) + "\n" + "  Exam1: " + 
               str(self.__Exam1Grade) + "\n" + "  Exam2: " + str(self.__Exam2Grade))

    def getName(self):
        return self.__studentName
    
    def setExam1Grade(self, grade):
        self.__Exam1Grade = grade

    def setExam2Grade(self, grade):
        self.__Exam2Grade = grade
    
    def getExam1Grade(self):
        return self.__Exam1Grade
    
    def getExam2Grade(self):
        return self.__Exam2Grade
    
    def getAverage(self):
        if (self.__Exam1Grade == None) or (self.__Exam2Grade == None):
            print("Some exam grades not available.")
        else:
            return (self.__Exam1Grade + self.__Exam2Grade)/2