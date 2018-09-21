# U04_Ex07_CircleIntersection.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 28 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Computes the intersection of a circle with an horizontal line
#   Displays the info textually and graphically
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Set window coordinates for text entry
#   Print introduction and input prompts (radius of circle and y-intercept of line)
#   Assign entered info to variables
#   Clear text and inputs
#   Set window coordinates for graphing (-10, -10, 10, 10)
#   Draw graph axes with labels
#   Draw graph title
#   Draw circle centered at (0, 0)
#   Draw horizontal line at y-intercept
#   Compute intersection point(s)
#   Draw intersection points in red
#   Print x values of intersection point(s)
#   Wait for mouse click to close


from graphics import *
from math import sqrt, copysign

def main():
    #   Create GraphWin
    win = GraphWin("Circle Intersection", 600, 600)

    #   Set window coordinates for text entry
    win.setCoords(0, 0, 10, 10)

    #   Print introduction and input prompts (radius of circle and y-intercept of line)
    msgIntro = Text(Point(5, 9), "This program computes and plots the intersection of a circle and line.")
    msgIntro.setStyle("bold")
    msgIntro.draw(win)

    msgRadius = Text(Point(4, 6), "Radius of a circle (≤ 10): ")
    msgRadius.draw(win)

    inputRadius = Entry(Point(8, 6), 10)
    inputRadius.setText("0.0")
    inputRadius.draw(win)

    msgIntercept = Text(Point(3, 4), "y-intercept of an horizontal line (-10 ≤ y ≤ 10): ")
    msgIntercept.draw(win)

    inputIntercept = Entry(Point(8, 4), 10)
    inputIntercept.setText("0.0")
    inputIntercept.draw(win)

    button = Rectangle(Point(4, 0.5), Point(6, 1.5))
    button.setFill('#999999')
    button.draw(win)
    buttonText = Text(Point(5, 1), "Continue")
    buttonText.draw(win)
    win.getMouse()

    #   Assign entered info to variables
    radius = float(inputRadius.getText())
    intercept = float(inputIntercept.getText())

    #   Clear text and inputs
    msgIntro.undraw()
    msgRadius.undraw()
    msgIntercept.undraw()
    inputRadius.undraw()
    inputIntercept.undraw()
    button.undraw()
    buttonText.undraw()

    #   Set window coordinates for graphing (-10, -10, 10, 10)
    win.setCoords(-11, -11, 11, 12)

    drawAxes(win, -10, -10, 10, 10, "Intersection Between Circle & Line")

    #   Draw circle centered at (0, 0)
    circle = Circle(Point(0, 0), radius)
    circle.setOutline("blue")
    circle.draw(win)

    #   Draw horizontal line at y-intercept
    line = Line(Point(-10, intercept), Point(10, intercept))
    line.setOutline("blue")
    line.draw(win)

    #   Compute intersection point(s)
    x2 = sqrt(radius**2 - intercept**2)
    if x2 > 0:
        x1 = x2 * -1
    else:
        x1 = None

    #   Draw intersection points in red
    #   Print x values of intersection point(s)
    negIntercept = 1
    if intercept < 0:
        negIntercept = -1
    count = 0
    xCoord = x1
    while count < 2:
        p1 = Circle(Point(xCoord, intercept), 0.2)
        p1.setOutline("red")
        p1.setFill("red")
        p1.draw(win)
        Text(Point(copysign(abs(xCoord)+1, xCoord), (abs(intercept)+1)*negIntercept), "x = {0:.2f}".format(xCoord)).draw(win)
        if type(x2) == None:
            break
        count += 1
        xCoord = x2
    #   Wait for mouse click to close
    win.getMouse()

def drawAxes(win, minX, minY, maxX, maxY, title):
    #   Draw graph axes with labels
    Line(Point(minX, 0), Point(maxX, 0)).draw(win)
    Line(Point(0, minY), Point(0, maxY)).draw(win)
    for i in range(minX, maxX+1, 2):
        if i != 0:
            Line(Point(i, 0.1), Point(i, -0.1)).draw(win)
            Text(Point(i, -0.5), i).draw(win)
            Line(Point(-0.1, i), Point(0.1, i)).draw(win)
            Text(Point(-0.5, i), i).draw(win)

    #   Draw graph title
    titleText = Text(Point(0, maxY+1), title)
    titleText.setSize(18)
    titleText.setStyle("bold")
    titleText.draw(win)

if __name__ == '__main__':
    main()