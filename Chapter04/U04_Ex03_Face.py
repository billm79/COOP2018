# U04_Ex03_Face.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 26 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws a face
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Make face outline using circle
#   Make left eye using two ovals
#   Clone left eye bits for right eye and move
#   Make left eyebrow and clone for right eyebrow
#   Move right eyebrow
#   Make nose
#   Make mouth


from graphics import *
from math import pi, cos, sin

def main(winWidth, winHeight, centerPoint):
    win = GraphWin("Face", winWidth, winHeight)
    drawFace(win, winWidth, winHeight)
    drawEyes(win, winWidth, winHeight)
    drawMouth(win, winWidth, winHeight)
    drawEyebrows(win, winWidth, winHeight)
    drawNose(win, winWidth, winHeight)

def drawFace(win, winW, winH):
    face = Circle(Point(winW/2, winH/2), min(winW, winH)*11/24)
    face.setOutline("black")
    face.setFill("burlywood")
    face.draw(win)

def drawEyes(win, winW, winH):
#    leftEye = Oval(Point(300-120-40, 300-80-20), Point(300-120+40, 300-80+20))
    leftEye = Oval(Point(winW/2-winW/5-winW/15, winH/2-winH/7.5-winH/30),
                   Point(winW/2-winW/5+winW/15, winH/2-winH/7.5+winH/30))
    leftEye.setFill("white")
    leftEye.setOutline("black")
    leftEye.draw(win)
    leftIris = Circle(Point(winW/2-winW/5, winH/2-winH/7.5), winH/40)
    leftIris.setOutline("black")
    leftIris.setFill("darkcyan")
    leftIris.draw(win)
    leftPupil = Circle(Point(winW/2-winW/5, winH/2-winH/7.5), winH/120)
    leftPupil.setOutline("black")
    leftPupil.setFill("black")
    leftPupil.draw(win)
    rightEye = leftEye.clone()
    rightEye.move(winW/2-winW/10,0)
    rightEye.draw(win)
    rightIris = leftIris.clone()
    rightIris.move(winW/2-winW/10,0)
    rightIris.draw(win)
    rightPupil = leftPupil.clone()
    rightPupil.move(winW/2-winW/10,0)
    rightPupil.draw(win)

def drawMouth(win, winW, winH):
    drawArc(win, winW/2, winH/2, winH/4, 60, 1.5)                # draw mouth

def drawEyebrows(win, winW, winH):
    drawArc(win, winW/2-winW/5, winH/2-winH/7.5+winH/10, winH/6, 30, 0.5)      # left eyebrow
    drawArc(win, winW/2+winW/5, winH/2-winH/7.5+winH/10, winH/6, 30, 0.5)      # right eyebrow

def drawNose(win, winW, winH):
    noseRad = winW/12
    nose = Circle(Point(winW/2, winH/2+winH/15), noseRad)
    nose.setOutline("red4")
    nose.setFill("red")
    nose.draw(win)
    spot = Polygon(Point(winW/2+noseRad*0.7, winH/2+noseRad*0.6),
                   Point(winW/2+noseRad*0.7, winH/2+noseRad*0.4),
                   Point(winW/2+noseRad*0.8, winH/2+noseRad*0.5),
                   Point(winW/2+noseRad*0.8, winH/2+noseRad*0.7))
    spot.setOutline("white")
    spot.setFill("white")
    spot.draw(win)

def drawArc(win, centerX, centerY, arcRadius, arcLengthDeg, midRad):
    arcCenter = Point(centerX, centerY)
    arcRad = arcLengthDeg * (pi / 180)
    i = midRad*pi-arcRad/2
    endRad = midRad*pi+arcRad/2
    while i <= endRad:
        x = arcCenter.getX() - arcRadius * cos(i)    # a + r cos t
        y = arcCenter.getY() - arcRadius * sin(i)    # b + r sin t
        Point(x,y).draw(win)
        i += 0.01   #pi/1000

if __name__ == 'main':
    main(200, 200)
    main(300, 300)
    main(400, 400)
    main(600, 600)
    main(800, 800)
    main(200, 300)
    main(300, 200)
    input("Press <Enter> to close graphics window.")