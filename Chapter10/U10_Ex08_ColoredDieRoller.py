# U10_Ex08_ColoredDieRoller.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 01 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 8
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView. Pips color can be set.
#
# Algorithm (pseudocode)
#
#   
#   
#   
#   


from random import randrange
from graphics import GraphWin, Point, color_rgb

from button import Button
from dieview import DieView

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = Button(win, Point(5,4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            die1.setColor(color_rgb(randrange(256), randrange(256), randrange(256)))
            value2 = randrange(1,7)
            die2.setValue(value2)
            die2.setColor(color_rgb(randrange(256), randrange(256), randrange(256)))
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()

main()
