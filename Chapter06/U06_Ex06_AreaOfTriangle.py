# U06_Ex06_AreaOfTriangle.py
#
#  Author: 
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 
#     Source: Python Programming
#    Chapter: 
#
# Program Description
#   Solve PE 3.9 using function area()
#   Calculates the area of a triangle, given the length of its three sides.
#
# Algorithm (pseudocode)
#   Get and draw three vertices of triangle
#   calculate side lengths and put in a list
#   check to see if a triangle with these points is possible (extra)
#       Use Polygon object to draw the triangle
#       Calculate the perimeter of the triangle
#       print results
#       call areaCalc() with points as parameters (p1, p2, p3)
#       print results
#   if triangle not possible
#       print error message
#
#   checkTriangle():
#       list with side lengths is argument
#       returns Boolean representing whether a triangle can be formed
#       find max in list
#       if sum of other two > max, return true
#       otherwise, return false
#
#   areaCalc():
#       list with side lengths is argument
#       calculate s = (a + b + c) / 2
#       calculate area = math.sqrt(s(s - a)(s - b)(s - c))
#       return area
#
#   NOTE: This file includes old, text-based code from first, improper attempt
#           (I didn't follow the directions in the problem statement :)


from math import sqrt
from graphics import *

def square(x):
    return x ** 2

def distance(p1, p2):
    dist = sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    results = Text(Point(5, 1.5), "")
    results.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # calculate side lengths and put in a list
    sideLengths = [distance(p1, p2), distance(p2, p3), distance(p3, p1)]

    # check to see if a triangle with these points is possible (extra)
    if checkTriangle(sideLengths):
        # Use Polygon object to draw the triangle
        triangle = Polygon(p1, p2, p3)
        triangle.setFill("peachpuff")
        triangle.setOutline("cyan")
        triangle.draw(win)

        # Calculate the perimeter of the triangle
        perim = sum(sideLengths)

        # print results
        results.setText("Perimeter = {0:0.2f}".format(perim))
        message.setText('Click for area')
        win.getMouse()

        # call areaCalc() with points as parameters (p1, p2, p3)
        area = areaCalc(sideLengths)

        # print results
        results.setText('Area = {0:0.2f}'.format(area))
        message.setText('Click to quit')
    else:
        results.setText('ERROR--It is not possible to make')
        message.setText('a triangle with the chosen points.')

    # Wait for another click to exit
    win.getMouse()
    win.close()

# checkTriangle():
#     list with side lengths is argument
#     returns Boolean representing whether a triangle can be formed
def checkTriangle(sides):
    # find max in list
    longest = max(sides)

    # if sum of other two > max, return true
    # otherwise, return false
    return sum(sides) - longest > longest

# areaCalc():
#     list with side lengths is argument
def areaCalc(sides):
    # calculate s = (a + b + c) / 2
    a = sides[0]; b = sides[1]; c = sides[2]
    s = (a + b + c) / 2
    # calculate area = math.sqrt(s(s - a)(s - b)(s - c))
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    # return area
    return area

def mainOld():
    # introduce program
    print('\nThis program calculates the area of a triangle, given the length of its three sides.')

    # get length of three sides from user
    side1, side2, side3 = eval(input('\nEnter the lengths of the sides of a triangle, separated by commas. '))
    side1 = float(side1); side2 = float(side2); side3 = float(side3)

    # check to see if a triangle with these side lengths is possible (extra)
    if checkTriangleOld(side1, side2, side3):
        # call areaCalc() with side lengths as parameters (side1, side2, side3)
        area = areaCalcOld(side1, side2, side3)

        # print results
        print('\nThe area of a triangle with sides {0}, {1}, and {2} is {3}'.format(side1, side2, side3, area))
    else:
        print('\nERROR!\nIt is not possible to make a triangle with sides of {0}, {1}, and {2}'.format(side1, side2, side3))

# checkTriangle():
#     a, b, c are arguments
def checkTriangleOld(a, b, c):
    # add a, b, c to a list
    sides = [a, b, c]

    # find max in list
    longest = max(sides)

    # if sum of other two > max, return true
    # otherwise, return false
    return (sum(sides) - longest > longest)

# areaCalc():
#     a, b, c are arguments
def areaCalcOld(a, b, c):
    # calculate s = (a + b + c) / 2
    s = (a + b + c) / 2
    # calculate area = math.sqrt(s(s - a)(s - b)(s - c))
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    # return area
    return area

main()
