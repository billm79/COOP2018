# U04_Ex09_RectangleInfo.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 29 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws a rectangle between two mouse clicks and displays
#   information about the rectangle
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Set window coordinates for graphing (-10, -10, 10, 10)
#   Print introduction & instructions
#   Wait for mouse click to continue
#   Draw graph with a call to U04_Ex07_CircleIntersection.drawAxes()
#   Get first mouse click with prompt using U04_Ex08_LineSegment.getMouseClick()
#   Get second mouse click with prompt using U04_Ex08_LineSegment.getMouseClick()
#   Draw rectangle between two mouse clicks
#   Print perimeter and area of the rectangle
#   Wait for mouse click to close


from graphics import *
from U04_Ex07_CircleIntersection import drawAxes
from U04_Ex08_LineSegment import getMouseClick
from math import sqrt

def main():
    #   Create GraphWin
    win = GraphWin("Line Segment Information", 600, 600)

    #   Set window coordinates for graphing (-10, -10, 10, 10)
    win.setCoords(-11, -11, 11, 12)

    #   Print introduction & instructions
    messages = [Text(Point(0, 11), "This program draws a rectangle between two mouse clicks."),
                Text(Point(0, 8), "On the following page, click once for one point,"),
                Text(Point(0, 7), "and another time for the opposite point of a rectangle."),
                Text(Point(0, 5), "The rectangle will be drawn and information will be displayed."),
                Text(Point(0, 3), "Click Continue when ready to begin.")]
    for msg in messages:
        msg.setSize(16)
        msg.draw(win)
    button = Rectangle(Point(4, 0.5), Point(6, 1.5))
    button.setFill('#999999')
    button.draw(win)
    buttonText = Text(Point(5, 1), "Continue")
    buttonText.draw(win)

    #   Wait for mouse click to continue
    win.getMouse()
    for msg in messages:
        msg.undraw()
    buttonText.undraw()
    button.undraw()

    #   Draw graph with a call to U04_Ex07_CircleIntersection.drawAxes()
    drawAxes(win, -10, -10, 10, 10, "Rectangle Information")

    #   Get first mouse click with prompt using U04_Ex08_LineSegment.getMouseClick()
    p1 = getMouseClick(win, Point(5,-10), "Click for first point...", )

    #   Get second mouse click with prompt using U04_Ex08_LineSegment.getMouseClick()
    p2 = getMouseClick(win, Point(5,-10), "Click for second point...", )

    #   Draw rectangle between two mouse clicks
    Rectangle(p1, p2).draw(win)

    #   Print perimeter and area of the rectangle
    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    Text(Point(-5, -10), "Area: {0:.2f}".format(length * width)).draw(win)
    Text(Point(5, -10), "Perimeter: {0:.2f}".format(2 * (length + width))).draw(win)

    #   Wait for mouse click to close
    win.getMouse()

main()
