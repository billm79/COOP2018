# U04_Ex10_TriangleInfo.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 29 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws a triangle between three mouse clicks and
#   displays information about the triangle
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Set window coordinates for graphing (-10, -10, 10, 10)
#   Print introduction & instructions
#   Wait for mouse click to continue
#   Draw graph with a call to U04_Ex07_CircleIntersection.drawAxes()
#   Get first mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Get second mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Get third mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Draw triangle between three mouse clicks
#   Print perimeter and area of the triangle
#   Wait for mouse click to close


from graphics import *
from Chapter04.U04_Ex07_CircleIntersection import drawAxes
from Chapter04.U04_Ex08_LineSegmentInfo import getMouseClick
from math import sqrt

def main():
    #   Create GraphWin
    win = GraphWin("Line Segment Information", 600, 600)

    #   Set window coordinates for graphing (-10, -10, 10, 10)
    win.setCoords(-11, -11, 11, 12)

    #   Print introduction & instructions
    messages = [Text(Point(0, 11), "This program draws a triangle between three mouse clicks."),
                Text(Point(0, 8), "On the following page, click once for each of the,"),
                Text(Point(0, 7), "vertices of a triangle."),
                Text(Point(0, 5), "The triangle will be drawn and information will be displayed."),
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
    drawAxes(win, -10, -10, 10, 10, "Triangle Information")

    #   Get first mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p1 = getMouseClick(win, Point(5,-10), "Click for first point...", )

    #   Get second mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p2 = getMouseClick(win, Point(5,-10), "Click for second point...", )

    #   Get third mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p3 = getMouseClick(win, Point(5,-10), "Click for third point...", )

    #   Draw rectangle between two mouse clicks
    Polygon(p1, p2, p3).draw(win)

    #   Print perimeter and area of the rectangle
    pXs = [p1.getX(), p2.getX(), p3.getX()]
    pYs = [p1.getY(), p2.getY(), p3.getY()]
    perimeter = 0
    side = 0
    s = 0
    sides = [0]
    for i in range(3):
        dx = pXs[i] - pXs[(i + 1) % 3]
        dy = pYs[i] - pYs[(i + 1) % 3]
        side = sqrt(dx**2 + dy**2)
        s += side / 2
        sides.append(side)
        perimeter += side
    area = 1
    for side in sides:
        area *= sqrt(s - side)
    Text(Point(-5, -10), "Area: {0:.2f}".format(area)).draw(win)
    Text(Point(5, -10), "Perimeter: {0:.2f}".format(perimeter)).draw(win)

    #   Wait for mouse click to close
    win.getMouse()

main()
