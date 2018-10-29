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

    # draw dies 1 - 5 for straight
    for i in range(1, 6):
        drawDie(win, i)
    win.getMouse()

def drawDie(win, rank):
    """
    Draws a single die of given rank
    Algorithm: 1) draw rectangle for die; 2) draw pips based on rank
    :param win: GraphWin object
    :param rank: int -> rank of die
    """
    rect = Rectangle(Point(10 + 110*(rank - 1), 10), Point(110 + 110*(rank - 1), 110))
    rect.setOutline("black")
    rect.setFill("white")
    rect.draw(win)

    # odd ranks have a center pip
    if rank % 2 == 1:
        drawPipCenter(win, rect.getCenter())

    # ranks 2 and 3 have top left and bottom right pips
    if rank == 2 or rank == 3:
        drawPipTL(win, rect.getCenter())
        drawPipBR(win, rect.getCenter())

    # ranks 4 and 5 have all four corner pips
    if rank == 4 or rank == 5:
        drawPipTL(win, rect.getCenter())
        drawPipBL(win, rect.getCenter())
        drawPipTR(win, rect.getCenter())
        drawPipBR(win, rect.getCenter())

def drawPipCenter(win, dieCenter):
    """
    Draws center pip relative to die center
    :param win: GraphWin object
    :param dieCenter: Point -> center point of die
    """
    drawCircle(dieCenter, 7, "black", "black").draw(win)

def drawPipTL(win, dieCenter):
    """
    Draws top left pip relative to die center
    :param win: GraphWin object
    :param dieCenter: Point -> center point of die
    """
    drawCircle(Point(dieCenter.getX() - 30, dieCenter.getY() - 30), 7, "black", "black").draw(win)

def drawPipTR(win, dieCenter):
    """
    Draws top right pip relative to die center
    :param win: GraphWin object
    :param dieCenter: Point -> center point of die
    """
    drawCircle(Point(dieCenter.getX() + 30, dieCenter.getY() - 30), 7, "black", "black").draw(win)

def drawPipBL(win, dieCenter):
    """
    Draws bottom left pip relative to die center
    :param win: GraphWin object
    :param dieCenter: Point -> center point of die
    """
    drawCircle(Point(dieCenter.getX() - 30, dieCenter.getY() + 30), 7, "black", "black").draw(win)

def drawPipBR(win, dieCenter):
    """
    Draws bottom right pip relative to die center
    :param win: GraphWin object
    :param dieCenter: Point -> center point of die
    """
    drawCircle(Point(dieCenter.getX() + 30, dieCenter.getY() + 30), 7, "black", "black").draw(win)

main()