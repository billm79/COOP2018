# U10_Ex17_RegressionLine.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 15 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 13
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Graphically draws a linear regression line after user specifies points
#   Uses drawAxes() from U04_Ex07_CircleIntersection.py (copied into this program)
#   New: Regression class (algorithm changes accordingly)
#
# Algorithm (pseudocode)
#   create GraphWin
#   Set window coordinates for text entry
#   introduce program
#   Set window coordinates for graphing (-11, -11, 11, 12)
#   call drawAxes() to draw axes
#   draw Done box in lower left corner
#   display instructions
#   initialize Regression object
#   while True
#       get mouse click
#       if Done, exit loop
#           Done is true when mouse click is within borders of Done rectangle (button)
#       otherwise
#           otherwise, draw point and add point to bestFit
#   calculate y coordinates for min and max x coordinates (y = meanY + slope(x - meanX))
#   draw line between those two coordinate pairs
#   calculate y-intercept
#   display equation of line in y = mx + b format
#   wait for mouse click


from graphics import *
from math import copysign


class Regresion:
    def __init__(self):
        self.Xs = []
        self.Ys = []
        self.sumX = 0
        self.sumY = 0
        self.sumSqXs = 0
        self.sumXY = 0

    def addPoint(self, pt):
        """ Adds point and updates sums of X, Y, X**2, and XY """
        _x = pt.getX(); _y = pt.getY()
        self.Xs.append(_x)
        self.Ys.append(_y)
        self.sumX += _x
        self.sumY += _y
        self.sumSqXs += _x * _x
        self.sumXY += _x * _y

    def __meanX(self):
        """ Returns mean of Xs """
        return sum(self.Xs) / len(self.Xs)

    def __meanY(self):
        """ Returns mean of Ys """
        return sum(self.Ys) / len(self.Ys)

    def slope(self):
        """ Returns slope if best-fit line """
        _numPts = len(self.Xs)
        return (self.sumXY - _numPts * self.__meanX() * self.__meanY()) / (self.sumSqXs - _numPts * self.__meanX() ** 2)

    def predict(self, x):
        """ Returns Y on line of best fit, given X """
        return self.__meanY() + self.slope() * (x - self.__meanX())


def main():
    # create GraphWin
    win = GraphWin('Linear Regression', 600, 600)

    # Set window coordinates for text entry
    win.setCoords(0, 0, 10, 10)

    # introduce program
    msg = Text(Point(5, 7), 'After user creates points, a linear regression is drawn.')
    msg.draw(win)
    win.getMouse()
    msg.undraw()

    # Set window coordinates for graphing (-11, -11, 11, 12)
    win.setCoords(-11, -11, 11, 12)

    # call drawAxes() to draw axes
    drawAxes(win, -10, -10, 10, 10, "Linear Regression")

    # draw Done box in lower left corner
    buttonLL = Point(-10.5, -10.5); buttonUR = Point(-8.5, -9.5)
    button = Rectangle(buttonLL, buttonUR)
    button.draw(win)
    buttonText = Text(Point(-9.5, -10), 'Done')
    buttonText.draw(win)

    # display instructions
    msg = Text(Point(5, 7),
               "Create points by clicking on the graph.\nClick 'Done' when finished.\n\nClick anywhere to start.")
    msg.draw(win)
    win.getMouse()
    msg.undraw()

    #   initialize Regression object
    bestFit = Regresion()

    # while True
    while True:
        # get mouse click
        graphPt = win.getMouse()

        # if Done, exit loop
        #     Done is true when mouse click is within borders of Done rectangle (button)
        graphPtX = graphPt.getX(); graphPtY = graphPt.getY()
        if graphPtX >= buttonLL.getX() and graphPtX <= buttonUR.getX() and \
            graphPtY >= buttonLL.getY() and graphPtY <= buttonUR.getY():
            break
        # otherwise, draw point and add point to bestFit
        bestFit.addPoint(graphPt)
        Point(graphPtX, graphPtY).draw(win)

    # calculate y coordinates for min and max x coordinates (y = meanY + slope(x - meanX))
    y1 = bestFit.predict(-10)
    y2 = bestFit.predict(10)

    # draw line between those two coordinate pairs
    Line(Point(-10, y1), Point(10, y2)).draw(win)

    # calculate y-intercept
    yInt = bestFit.predict(0)

    # display equation of line in y = mx + b format
    Text(Point(5, copysign(min(abs(y2), 10), y2)), 'y = {:.2f}x + {:.2f}'.format(bestFit.slope(), yInt)).draw(win)

    # wait for mouse click
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