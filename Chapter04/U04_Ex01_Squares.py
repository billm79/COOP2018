# U04_Ex01_Squares.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 18 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws squares at mouse-click location
#   
#   
#
# Algorithm (pseudocode)
#   
#   
#   
#   
#   


from graphics import *

def mainA():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()

def mainB():
    win = GraphWin()
    side = 20
    shape = makeRect(Point(50, 50), Point(50 + side, 50 + side))
    c = shape.getCenter()
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        dx = p.getX() - side/2
        dy = p.getY() - side/2
        shape = makeRect(Point(dx, dy), Point(dx+20, dy+20))
        shape.draw(win)
    win.close()

def mainC():
    win = GraphWin()
    side = 20
    shape = makeRect(Point(50, 50), Point(50 + side, 50 + side))
    c = shape.getCenter()
    shape.draw(win)
    for i in range(1):
        p = win.getMouse()
        dx = p.getX() - side/2
        dy = p.getY() - side/2
        shape = makeRect(Point(dx, dy), Point(dx+20, dy+20))
        shape.draw(win)
    Text(Point(50,20), "Click again to quit...").draw(win)
    win.getMouse()
    win.close()

def makeRect(p1, p2):
    shape = Rectangle(p1, p2)
    shape.setOutline("red")
    shape.setFill("red")
    return shape

# mainA()
# mainB()
mainC()