# U04_Ex05_Dice.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 28 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws 5 dice depicting a straight
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Draw dice
#       rectangle
#       pips


from graphics import *
from U04_Ex04_WinterScene import drawCircle

def main():
    win = GraphWin("Dice", 560, 120)
    win.setBackground("green4")
    for i in range(1,7):
        drawDie(win, i)
    win.getMouse()

def drawDie(win, rank):
    rect = Rectangle(Point(10 + 110*(rank - 1), 10), Point(110 + 110*(rank - 1), 110))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)
    if rank % 2 == 1:
        drawPipCenter(win, rect.getCenter())
    if rank == 2 or rank == 3:
        drawPipTL(win, rect.getCenter())
        drawPipBR(win, rect.getCenter())

    if rank == 4 or rank == 5:
        drawPipTL(win, rect.getCenter())
        drawPipBL(win, rect.getCenter())
        drawPipTR(win, rect.getCenter())
        drawPipBR(win, rect.getCenter())

def drawPipCenter(win, dieCenter):
    drawCircle(dieCenter, 7, "black", "black").draw(win)

def drawPipTL(win, dieCenter):
    drawCircle(Point(dieCenter.getX() - 30, dieCenter.getY() - 30), 7, "black", "black").draw(win)

def drawPipTR(win, dieCenter):
    drawCircle(Point(dieCenter.getX() + 30, dieCenter.getY() - 30), 7, "black", "black").draw(win)

def drawPipBL(win, dieCenter):
    drawCircle(Point(dieCenter.getX() - 30, dieCenter.getY() + 30), 7, "black", "black").draw(win)

def drawPipBR(win, dieCenter):
    drawCircle(Point(dieCenter.getX() + 30, dieCenter.getY() + 30), 7, "black", "black").draw(win)

main()