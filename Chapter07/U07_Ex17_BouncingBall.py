# U07_Ex17_BouncingBall.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Animates a moving "ball" that "bounces" off the "walls" of the graphics window
#
# Algorithm (pseudocode)
#   create GraphWin
#   create circle object (sized to a fraction of the window width for scale)
#   draw circle in center of window
#   set dx and dy to random float values between -1.0 and 1.0, inclusive
#   loop 10000 times
#       move circle with current dx and dy until an edge is hit (dx or dy is within one radius of edge)
#           randomly select a new dx or dy with opposite sign
#           update(30) to slow execution to 30 fps


from graphics import *
from random import *

def main():
    # create GraphWin
    win = GraphWin('Bouncing Ball', 600, 600)
    rightBound = win.getWidth() / 2
    leftBound = rightBound * -1
    topBound = win.getHeight() / 2
    bottomBound = topBound * -1
    win.setCoords(leftBound, bottomBound, rightBound, topBound)

    # create circle object (sized to a fraction of the window width for scale)
    radius = win.getWidth() / 20
    ball = Circle(Point(0,0), radius)
    ball.setFill('blue')

    # draw circle in center of window
    ball.draw(win)

    # set dx and dy to random float values between -1.0 and 1.0, inclusive
    dx = randrange(-100, 100)
    dy = randrange(-100, 100)

    # show a counter
    count = Text(Point(0, topBound - 10), 'count')
    count.draw(win)

    # show quit message
    Text(Point(0, bottomBound + 10), 'Click to stop').draw(win)

    # loop 10000 times
    for i in range(10000):
        count.setText(str(i))

        # move circle with current dx and dy until an edge is hit (dx or dy is within one radius of edge)
        ball.move(dx, dy)

        # randomly select a new dx or dy with opposite sign
        if dx <= 0 and ball.getCenter().getX() - leftBound <= radius:
            dx = randrange(10, 100)
        if dx >= 0 and rightBound - ball.getCenter().getX() <= radius:
            dx = randrange(-100, -10)
        if dy <= 0 and ball.getCenter().getY() - bottomBound <= radius:
            dy = randrange(10, 100)
        if dy >= 0 and topBound - ball.getCenter().getY() <= radius:
            dy = randrange(-100, -10)

        # check for mouse click
        if win.checkMouse():
            break

        # update(30) to slow execution to 30 fps
        update(30)


main()
