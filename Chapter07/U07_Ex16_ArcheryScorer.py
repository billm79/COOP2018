# U07_Ex16_ArcheryScorer.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Uses archery target from Unit 4, Exercise 2. Five clicks from user,
#   representing five arrows into the target, are recorded. Each time,
#   the score for that shot and for the running total are displayed.
#
# Algorithm (pseudocode) using functions
#   GLOBAL VARS:
#       totalScore=0, shotMsg, ttlMsg (for scoreboard)
#       bands = [bullsEye=1, band2=2, band3=3, band4=4, band5=5] (radii for target)
#       points = [points1=9, points2=7, points3=5, points4=3, points5=1] (points per band)
#
#   main():
#       create GraphWin (600 x 600)
#       set coordinates to (-5.5, -5.5, 7, 7) --leaves room for scoreboard in upper right
#       call drawTarget() with win as parameter
#       draw scoreboard using Text and Line objects
#       call updateScore() with zero as parameter to display scoreboard
#       get five shots from user (win.getMouse())
#           get score for shot by calling getScore() with point object as parameter
#           call updateScore() with shot score as parameter to update scoreboard
#
#   drawTarget():
#       win is argument
#       create circles list
#           each element is a circle object created with a call to makeCircle()
#               with center (0,0), radius, and color as parameters
#       draw each circle in a loop
#
#   makeCircle():
#       center, radius, and color are arguments
#       create circle object with center and radius arguments as parameters
#       set outline to black
#       set fill to color argument
#       return circle object
#
#   updateScore():
#       shotScore (int) is argument
#       replace shot score Text object with shotScore
#       increment total score Text object by shotScore
#
#   getScore():
#       win is argument
#       wait for mouse click
#       determine distance from mouse click to center by calling distance()
#           with (0,0) and mouse click point as parameters
#       set shotScore to zero
#       for each band, starting from middle (index 0)
#           if distance is <= radius, set shotScore to points for this band
#       return shotScore
#
#   distance():
#       two point objects are arguments
#       use distance formula
#       return distance


from graphics import *
from math import sqrt

# GLOBAL VARS:
#     totalScore=0, shotMsg, ttlMsg (for scoreboard)
#     bands = [bullsEye=1, band2=2, band3=3, band4=4, band5=5] (radii for target)
#     points = [points1=9, points2=7, points3=5, points4=3, points5=1] (points per band)

totalScore = 0
shotMsg = Text(Point(4.5, 5.5), '')
ttlMsg = Text(Point(6, 5.5), '')
dbgMsg = Text(Point(0, 6.5), '')
bands = [5, 4, 3, 2, 1]
points = [1, 3, 5, 7, 9]

#   main():
def main():
    # create GraphWin (600 x 600)
    win = GraphWin("Archery Scorer", 600, 600)

    # set coordinates to (-5.5, -5.5, 7, 7) --leaves room for scoreboard in upper right
    win.setCoords(-5.5, -5.5, 7, 7)
    title = Text(Point(-4, 6.5), 'Archery Scorer')
    title.setSize(14); title.setStyle('bold'); title.draw(win)

    # call drawTarget() with win as parameter
    drawTarget(win)

    # draw scoreboard using Text and Line objects
    txt = Text(Point(5.25, 6.5), 'Scoreboard'); txt.setStyle('bold'); txt.draw(win)
    txt = Text(Point(4.5, 6), 'Shot Score'); txt.setStyle('bold'); txt.draw(win)
    txt = Text(Point(6, 6), 'Total Score'); txt.setStyle('bold'); txt.draw(win)
    Line(Point(3.75, 5.75), Point(6.75, 5.75)).draw(win)
    Line(Point(5.25, 6.25), Point(5.25, 5.25)).draw(win)
    shotMsg.draw(win)
    ttlMsg.draw(win)
    dbgMsg.draw(win)

    # call updateScore() with zero as parameter to display scoreboard
    updateScore(0)

    # get five shots from user (win.getMouse())
    for shotNo in range(5):
        shotPt = win.getMouse()
#        shotPt.draw(win)
        drawShot(win, shotPt)

        # get score for shot by calling getScore() with point object as parameter
        shotScore = getScore(shotPt)

        # call updateScore() with shot score as parameter to update scoreboard
        updateScore(shotScore)

    # wait for mouse click
    button = Rectangle(Point(4.75, -4.75), Point(6.75, -5.25))
    button.setFill('#999999')
    button.draw(win)
    buttonText = Text(Point(5.75, -5), "Click to quit")
    buttonText.draw(win)
    win.getMouse()

#   drawTarget():
#       win is argument
def drawTarget(win):
    # create circles list
    #     each element is a circle object created with a call to makeCircle()
    #         with center (0,0), radius, and color as parameters
    center = Point(0, 0)
    circles = [makeCircle(center, bands[0], "white"),
               makeCircle(center, bands[1], "black"),
               makeCircle(center, bands[2], "blue"),
               makeCircle(center, bands[3], "red"),
               makeCircle(center, bands[4], "yellow")]

    # draw each circle in a loop
    for circle in circles:
        circle.draw(win)

#   makeCircle():
#       center, radius, and color are arguments
def makeCircle(c, r, color):
    # create circle object with center and radius arguments as parameters
    circ = Circle(c, r)

    # set outline to black
    circ.setOutline("black")

    # set fill to color argument
    circ.setFill(color)

    # return circle object
    return circ

#   updateScore():
#       shotScore (int) is argument
def updateScore(shotScore):
    global totalScore

    # replace shot score Text object with shotScore
    shotMsg.setText(str(shotScore))

    # increment total score Text object by shotScore
    totalScore += shotScore
    ttlMsg.setText(str(totalScore))

#   getScore():
#       pt is argument
def getScore(pt):
    # determine distance from mouse click to center by calling distance()
    #     with (0,0) and mouse click point as parameters
    dist = distance(Point(0, 0), pt)

    # set shotScore to zero
    shotScore = 0

    # for each band, starting from middle (index 0)
    for i in range(len(bands)):
        # if distance is <= radius, set shotScore to points for this band
        if dist <= bands[i]:
            shotScore = points[i]

    # return shotScore
    return shotScore

#   distance():
#       two point objects are arguments
def distance(p1, p2):
    # use distance formula
    dist = sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))

    # return distance
    return dist

def square(x):
    return x ** 2

def drawShot(win, shotPt):      # for prettier shots on target
    x = shotPt.getX(); y = shotPt.getY()
    s = 0.1; o = 0.02
    ln = Line(Point(x - s + o, y - o), Point(x + s + o, y - o)); ln.setOutline('gray'); ln.draw(win)
    ln = Line(Point(x + o, y - s - o), Point(x + o, y + s - o)); ln.setOutline('gray'); ln.draw(win)
    ln = Line(Point(x - s, y), Point(x + s, y)); ln.setOutline('black'); ln.draw(win)
    ln = Line(Point(x, y - s), Point(x, y + s)); ln.setOutline('black'); ln.draw(win)
    shotPt.draw(win)


main()
