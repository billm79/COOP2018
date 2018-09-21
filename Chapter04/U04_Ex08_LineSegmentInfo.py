# U04_Ex08_LineSegment.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 28 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 8
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws line segment between two mouse clicks and displays
#   information about the line
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Set window coordinates for graphing (-10, -10, 10, 10)
#   Print introduction & instructions
#   Wait for mouse click to continue
#   Draw graph with a call to U04_Ex07_CircleIntersection.drawAxes()
#   Get first mouse click with prompt
#   Get second mouse click with prompt
#   Draw line between two mouse clicks
#   Compute and draw midpoint in cyan
#   Print length and slope of the line
#   Wait for mouse click to close


from graphics import *
from U04_Ex07_CircleIntersection import drawAxes
from math import sqrt

def main():
    #   Create GraphWin
    win = GraphWin("Line Segment Information", 600, 600)

    #   Set window coordinates for graphing (-10, -10, 10, 10)
    win.setCoords(-11, -11, 11, 12)

    #   Print introduction & instructions
    messages = [Text(Point(0, 11), "This program draws a line segment between two mouse clicks."),
                Text(Point(0, 8), "On the following page, click once for one endpoint,"),
                Text(Point(0, 7), "and another time for the other endpoint of a line."),
                Text(Point(0, 5), "The line will be drawn and information will be displayed."),
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
    drawAxes(win, -10, -10, 10, 10, "Line Segment Information")

    #   Get first mouse click with prompt
    p1 = getMouseClick(win, Point(5,-10), "Click for first point...", )

    #   Get second mouse click with prompt
    p2 = getMouseClick(win, Point(5,-10), "Click for second point...", )

    #   Draw line between two mouse clicks
    Line(p1, p2).draw(win)

    #   Compute and draw midpoint in cyan
    mp1 = Circle(Point((p1.getX() + p2.getX()) / 2,
                       (p1.getY() + p2.getY()) / 2), 0.1)
    mp1.setOutline("cyan")
    mp1.setFill("cyan")
    mp1.draw(win)

    #   Print length and slope of the line
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    Text(Point(-5, -10), "Line length: {0:.2f}".format(sqrt(dx**2 + dy**2))).draw(win)
    Text(Point(5, -10), "Slope: {0:.2f}".format(dy / dx)).draw(win)

    #   Wait for mouse click to close
    win.getMouse()

def getMouseClick(win, center, prompt):
    prompt = Text(center, prompt)
    prompt.setSize(14)
    prompt.setStyle("bold")
    prompt.draw(win)
    p1 = win.getMouse()
    prompt.undraw()
    return p1

if __name__ == '__main__':
    main()