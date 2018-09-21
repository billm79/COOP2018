# U10_Ex07_CircularButtons.py
#
#  Author: 
#  Course: Coding for OOP
# Section: A3
#    Date: 01 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 
#     Source: Python Programming
#    Chapter: 
#
# Program Description
# Graphics program to roll a pair of dice. Uses custom widgets
# CButton and DieView.
#   
#
# Algorithm (pseudocode)
#   
#   
#   
#   
#   


from random import randrange
from graphics import GraphWin, Point

from cbutton import CButton
from dieview import DieView

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = CButton(win, Point(5,3.5), 1.25, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(5,1), 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()

main()
