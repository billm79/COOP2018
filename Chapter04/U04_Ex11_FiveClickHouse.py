# U04_Ex11_FiveClickHouse.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 29 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws a house with five clicks
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Set window coordinates for graphing (-10, -10, 10, 10)
#   Print introduction & instructions
#   Wait for mouse click to continue
#   Get first mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Get second mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Draw house frame (rectangle)
#   Get third mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Draw door using mouse click for center; width is 1/5 width of bottom edge of house
#   Get fourth mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Draw square centered at mouse click; half as wide as door
#   Get fifth mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
#   Draw triangular roof using this click and top two points of house frame
#   Wait for mouse click to close


from graphics import *
from math import sqrt
from Chapter04.U04_Ex08_LineSegmentInfo import getMouseClick

def main():
    #   Create GraphWin
    win = GraphWin("Five-Click House", 600, 600)

    #   Set window coordinates for graphing (-10, -10, 10, 10)
    win.setCoords(-11, -11, 11, 12)

    #   Print introduction & instructions
    messages = [Text(Point(0, 11), "This program draws a house using five mouse clicks."),
                Text(Point(0, 8), "On the following page, click five times, according"),
                Text(Point(0, 7), "to the guide and image below. "),
                Text(Point(0, 4), "• Clicks 1 & 2 define rectangle for house frame\n" +
                                  "• Click 3 is center of door frame                         \n" +
                                  "• Click 4 is for the window                                  \n" +
                                  "• Click 5 is for peak of roof                                  "),
                Text(Point(0, 1), "Click Continue when ready to begin.")]
    for msg in messages:
        msg.setSize(16)
        msg.draw(win)
    button = Rectangle(Point(4, -2.5), Point(6, -1.5))
    button.setFill('#999999')
    button.draw(win)
    buttonText = Text(Point(5, -2), "Continue")
    buttonText.draw(win)

    img = Image(Point(-5, -5), "FiveClickHouse.gif").draw(win)

    #   Wait for mouse click to continue
    win.getMouse()
    for msg in messages:
        msg.undraw()
    buttonText.undraw()
    button.undraw()
    img.undraw()

    #   Get first mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p1 = getMouseClick(win, Point(5,-10), "Click for first point...", )

    #   Get second mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p2 = getMouseClick(win, Point(5,-10), "Click for second point...", )

    #   Draw house frame (rectangle)
    Rectangle(p1, p2).draw(win)

    #   Get third mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p3 = getMouseClick(win, Point(5,-10), "Click for third point...", )

    #   Draw door using mouse click for center; width is 1/5 width of bottom edge of house
    doorWidth = abs(p1.getX() - p2.getX()) / 5
    Rectangle(Point(p3.getX() - doorWidth / 2, p1.getY()),
              Point(p3.getX() + doorWidth / 2, p3.getY())).draw(win)

    #   Get fourth mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p4 = getMouseClick(win, Point(5,-10), "Click for fourth point...", )

    #   Draw square centered at mouse click; half as wide as door
    Rectangle(Point(p4.getX() - doorWidth / 4, p4.getY() - doorWidth / 4),
              Point(p4.getX() + doorWidth / 4, p4.getY() + doorWidth / 4)).draw(win)

    #   Get fifth mouse click with prompt using U04_Ex08_LineSegmentInfo.getMouseClick()
    p5 = getMouseClick(win, Point(5,-10), "Click for fifth point...", )

    #   Draw triangular roof using this click and top two points of house frame
    Polygon(Point(p1.getX(), p2.getY()), p2, p5).draw(win)

    #   Wait for mouse click to close
    win.getMouse()

main()