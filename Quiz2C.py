# CS 303E Quiz 2C
# do NOT rename this file, otherwise Gradescope will not accept your submission
import math

# Problem 1: Movie Offer
def movieOffer():
    # write your solution to problem 1 here
    runtime = int(input())
    action = int(input())
    bored = int(input())
    if bored == 1:
        print("I'll watch anything!")
    else:
        if (runtime < 90 or runtime > 140) & (action < 6 or action > 8):
            print("I'd rather watch something else.")
        elif (runtime < 90 or runtime > 140):
            print("It's either too short or too long.")
        elif (action < 6 or action > 8):
            print("The action isn't balanced.")
        else:
            print("I love a good action movie.")
    pass

# Problem 2: Small Product
def smallProduct():
    # write your solution to problem 2 here
    product = 1
    num = int(input())
    while(num != 0):
        if num < 10:
            product = product * num
        num = int(input())
    print(product)
    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    #movieOffer()
    #smallProduct()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT