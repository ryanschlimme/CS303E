# CS 303E Quiz 1C
# do NOT rename this file, otherwise Gradescope will not accept your submission
import math

# Problem 1: Distance Evaluation
def distanceEvaluation():
    # write your solution to problem 1 here
    x = float(input())
    y = float(input())
    z = float(input())
    dist = math.sqrt((3*x)**2 + y**2 + ((z-7)/12)**2)
    dist = format(dist, "0.3f")
    print("The total distance is", dist)
    pass


# Problem 2: Height Unit Conversion
def heightUnitConversion():
    # write your solution to problem 2 here
    inches = int(input())
    yards = inches // 36
    inches = inches - 36*yards
    feet = inches // 12
    inches = inches - 12*feet
    print(yards, feet, inches)
    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    distanceEvaluation()
    #heightUnitConversion()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT