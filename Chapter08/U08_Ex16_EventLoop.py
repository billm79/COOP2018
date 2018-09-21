# U08_Ex16_EventLoop.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Modification to event_loop3 to handle pressing the Esc key
#
# Algorithm (pseudocode)
#   modification steps:
#       move entry.undraw() and Text... lines under test for "Return"
#       add test for "Escape"
#       undraw `entry` and break


# event_loop3.py
#      Color changing window with clicks to enter text

from graphics import *


def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")


def handleClick(pt, win):
    # create an Entry for user to type in
    entry = Entry(pt, 10)
    entry.draw(win)

    # Go modal: wait until user types Return or Escape Key
    while True:
        key = win.getKey()
        if key == "Return":
            # undraw the entry and draw Text
            entry.undraw()
            Text(pt, entry.getText()).draw(win)
            break
        if key == "Escape":
            entry.undraw()
            break

    # clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()


def main():
    win = GraphWin("Click and Type", 500, 500)

    # Event Loop: handle key presses and mouse clicks until the user
    #    presses the "q" key.
    while True:
        key = win.checkKey()
        if key == "q":  # loop exit
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()


main()

