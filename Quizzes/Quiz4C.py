# CS 303E Quiz 4C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

import math

# Problem 1: Large Elements
def largeElements(lst):
    newList = []
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            newList.append(lst[i])
    return newList


# Problem 1: Unequal Midterms
def computeCourseGrade(m1, m2, m3):
    grades = [m1, m2, m3]
    maxGrade = max(grades)
    grades.remove(maxGrade)
    out = maxGrade * 0.4
    for i in grades:
        out += 0.3*i
    return math.floor(out)


def getStudentGrades(lst):
    out = []
    for student in lst:
        name = student[0]
        m1 = student[1]
        m2 = student[2]
        m3 = student[3]
        grade = computeCourseGrade(m1,m2,m3)
        out.append([name, grade])
    return out


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(largeElements([6, -1, 28, 27, -6, 29, -1, -21, -20, -28, 13, 15, 2]))
    # print(largeElements([5, 4, 3, 2, 1, 0]))
    # print(largeElements([1, 2, 4, 8, 16, 32]))

    # print(computeCourseGrade(85, 79, 85))
    # print(computeCourseGrade(85, 92, 83))

    print(getStudentGrades([["Hannah", 85, 79, 85], ["Eli", 85, 92, 83], ["Elena", 96, 95, 100]]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT