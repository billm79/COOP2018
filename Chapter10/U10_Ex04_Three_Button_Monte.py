"""
U10_Ex04_Three_Button_Monte.py

  Author: Bill Montana
  Course: Coding for OOP
 Section: A2
    Date: 2019-05-01
     IDE: PyCharm
     
Assignment Info
  Exercise: 04
    Source: Python Programming
   Chapter: 10
   
Program Description
    Simulate the 3-door Monte game using graphical buttons for the doors

Algorithm
    main():
        create GraphWin
        place three buttons in window
        place Quit button in window
        place blank message text in window
        get mouse click
        event loop...until Quit clicked
            randomly determine which door is correct
            take action for button clicked (1, 2, 3, or Quit)
                action will print win/lose message in graphics window
            get mouse click
"""

from graphics import GraphWin, Point, Text
from button import Button
from random import randrange
from time import sleep


def main():
    # create GraphWin
    win = GraphWin("Three Button Monte", 800, 600)
    win.setCoords(0, 0, 10, 10)

    # place three buttons in window
    doors = [Button(win, Point(2, 5), 2, 4, door1()),
             Button(win, Point(5, 5), 2, 4, door2()),
             Button(win, Point(8, 5), 2, 4, door3())]
    for door in doors:
        door.activate()

    # place Quit button in window
    quitButton = Button(win, Point(8.5, 1.5), 1, 1, "Quit")
    quitButton.activate()

    # place blank message text in window
    result = Text(Point(3.5, 1.5), '')
    result.draw(win)

    # get mouse click
    pt = win.getMouse()

    # event loop...until Quit clicked
    while not quitButton.clicked(pt):
        # randomly determine which door is correct
        secretDoor = randrange(0, 3)

        # take action for button clicked (1, 2, 3, or Quit)
        if doors[secretDoor].clicked(pt):
            result.setText('Congratulations, you are correct!')
        else:
            result.setText('Sorry, the correct door was door #{}'.format(secretDoor + 1))

        sleep(2)
        result.setText('')

        # get mouse click
        pt = win.getMouse()

    win.close()


def door1():
    return """\
\u220e\u220e\u220e
\u220e\u220e\u220e
\u220e\u220e\u220e
\u220e\u220e\u220e
\u220e\u220e\u220e
\u220e\u220e\u220e
\u220e\u220e\u220e
\u220e\u220e\u220e
\u220e\u220e\u220e
"""


def door2():
    return """\
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e

"""


def door3():
    return """\
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
\u220e\u220e\u220e      \u220e\u220e\u220e      \u220e\u220e\u220e
"""


if __name__ == '__main__':
    main()
