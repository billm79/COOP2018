# U04_Ex02_Target.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 26 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 2
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws an archery target in which the center is yellow surrounded by concentric
#   rings of red, blue, black, and white. Each ring has the same width, which is
#   the same as the radius of the center circle.
#
# Algorithm (pseudocode)
#   Create a GraphWin
#   Define a list with five circle objects
#   The radius of each successive circle is the next integer multiple of the center circle.
#   Draw circles, starting from the outside.


from graphics import *

def main(winSide):
    win = GraphWin("Target", winSide, winSide)
    radius = win.getWidth()/12
    center = Point(win.getWidth()/2, win.getHeight()/2)
    circles = [makeCircle(center, radius*5, "white"),
               makeCircle(center, radius*4, "black"),
               makeCircle(center, radius*3, "blue"),
               makeCircle(center, radius*2, "red"),
               makeCircle(center, radius, "yellow")]
    for circle in circles:
        circle.draw(win)

def makeCircle(c, r, color):
    """
    Make a circle object centered at c with radius r and filled with color
    :param c: Point -> center of circle
    :param r: int -> radius of circle
    :param color: str -> color name for fill
    :return: Circle -> circle object
    """
    circ = Circle(c, r)
    circ.setOutline("black")
    circ.setFill(color)
    return circ

main(600)
input("Press <Enter> to close graphics window.")