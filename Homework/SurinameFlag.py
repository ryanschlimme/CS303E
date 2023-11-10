# SurinameFlag.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 09 November 2023
# This program uses Turtle Graphics to draw the flag of Suriname using a modular solution. I define functions to build
# a reusable drawing toolkit including a function to draw a rectangle and a function to draw a star. The drawing is saved
# to a png file. 

import turtle
import math

def drawRectangle(ttl, x, y, L, W, c):
    """Draws a rectangle using turtle ttl with upper left corner at (x,y), length L, and width W.
    Fills with color c"""
    ttl.speed(1000)
    ttl.pensize(1)
    ttl.screen.colormode(255)
    ttl.fillcolor(c)
    ttl.begin_fill()
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(0)
    ttl.pendown()
    for count in range(2):
        ttl.forward(L)
        ttl.right(90)
        ttl.forward(W)
        ttl.right(90)
    ttl.penup
    ttl.end_fill()
    ttl.ht()


def drawStar(ttl, x, y, R, c):
    """Draws a star at center (x,y) whose size is determined by the circle circumscribing it
     with radius R. Fills with color c"""
    a = 2*R*math.sin(math.radians(180/5))   # Side length of pentagon around star
    gamma = (1+math.sqrt(5))/2              # Golden Ratio
    L = a/gamma                             # Exterior side length of star from outer point to inner point
    ttl.speed(1000)
    ttl.pensize(1)
    ttl.screen.colormode(255)
    ttl.fillcolor(c)
    ttl.begin_fill()
    ttl.penup()
    ttl.goto(x,y+R)
    ttl.setheading(-72)
    ttl.pendown()
    for count in range(5):
        ttl.forward(L)
        ttl.left(72)
        ttl.forward(L)
        ttl.right(180-36)
    ttl.penup()
    ttl.end_fill()
    ttl.ht()

Test = turtle.Turtle()
center = (3-math.sqrt(5))/2*20
# 600 x 400 flag
drawRectangle(Test, -300, 200, 600, 80, (55, 126, 63))  # 4/20 tall = 80 tall
drawRectangle(Test, -300, 200-80, 600, 40, (255, 255, 255))    # 2/20 tall = 40 tall
drawRectangle(Test, -300, 200-80-40, 600, 160, (180, 10, 45))    # 8/20 tall = 160 tall
drawRectangle(Test, -300, 200-80-40-160, 600, 40, (255, 255, 255))    # 2/20 tall = 40 tall
drawRectangle(Test, -300, 200-80-40-160-40, 600, 80, (55, 126, 63))  # 4/20 tall = 80 tall
drawStar(Test, 0, -center, 4/30*600, (236, 200, 29))

turtle.ht()
turtle.done()