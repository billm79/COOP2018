# U04_Ex04_WinterScene.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 27 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Draws a winter scene with a Christmas tree and a snowman
#
# Algorithm (pseudocode)
#   Create GraphWin
#   Draw sky
#   Draw snow-covered ground
#   Draw sun
#   Draw tree
#   Draw snowman


from graphics import *
from math import sin, pi, cos

def main():
    win = GraphWin("Winter Scene", 600, 600)
    drawSky(win)
    drawGround(win)
    drawSun(win)
    drawTree(win)
    drawSnowman(win)
    win.getMouse()

def drawSky(win):
    """
    Draws skyblue rectangle for sky
    :param win: GraphWin object
    """
    drawRect(Point(0,0), Point(600,600), "skyblue", "skyblue").draw(win)

def drawGround(win):
    """
    Draws white rectangle for snow-covered ground
    :param win: GraphWin object
    """
    drawRect(Point(0,200), Point(600, 600), "white", "white").draw(win)

def drawSun(win):
    """
    Draws sun
    Algorithm: 1) draw sun circle; 2) draw 8 rays radiating out from sun circle
    :param win: GraphWin object
    """
    center = Point(100,70)
    radius = 30
    drawCircle(center, radius, "orange", "yellow").draw(win)
    for i in range(45, 361, 45):
        sunRay = Line(Point(center.getX()+30*cos(i*pi/180), center.getY()+30*sin(i*pi/180)),
                      Point(center.getX() + 50 * cos(i*pi/180), center.getY() + 50 * sin(i*pi/180)))
        sunRay.setFill("orange2")
        sunRay.draw(win)

def drawTree(win):
    """
    Draws tree
    Algorithm: 1) define points for first triangle; 2) draw rectangle for trunk;
               3) draw 3 triangles for leaves, positioning each successive triangle above last
    :param win: GraphWin object
    """
    p1x = 90
    p1y = 480
    p2x = 210
    p2y = 480
    p3x = 150
    p3y = 394
    drawRect(Point(145,500), Point(155,450), "brown4", "brown").draw(win)
    for i in range(3):
        drawTriangle([Point(p1x, p1y),
                      Point(p2x, p2y),
                      Point(p3x, p3y)], "green4", "green").draw(win)
        p1x = p1x+10
        p1y = p1y-40
        p2x = p2x-10
        p2y = p2y-40
        p3y = p1y-sin(60*180/pi)*(p2x-p1x)

def drawSnowman(win):
    """
    Draws snowman
    Algorithm: 1) draw body; 2) draw face
    :param win: GraphWin object
    """
    center = drawSBody(win, 400, 450)
    drawSFace(win, center)

def drawSBody(win, x, y):
    """
    Draws snowman body
    Algorithm: 1) draw 3 body circles, starting with bottom; 2) draw arms attached to top circle
    :param win: GraphWin object
    :param x: x-coord of center point
    :param y: y-coord of center point
    :return: Point -> center of top circle
    """
    radius = 40
    center = Point(x, y)
    for i in range(3):
        center = Point(400, center.getY() - 2 * radius)
        drawCircle(center, radius, "blue", "white").draw(win)
        if i == 1:
            drawArms(win, center, radius)
        radius -= 10
    return center

def drawArms(win, c, r):
    """
    Draws snowman arms
    Algorithm: draw two lines a distance r from a center point c
    :param win: GraphWin object
    :param c: Point -> center point between arms
    :param r: int -> distance from center to start arms
    """
    Line(Point(c.getX()-r, c.getY()), Point(c.getX()-r-17, c.getY()-5)).draw(win)
    Line(Point(c.getX()+r-3, c.getY()), Point(c.getX()+r+20, c.getY()-7)).draw(win)

def drawSFace(win, p):
    """
    Draws snowman face
    Algorithm: 1) draw eyes; 2) draw mouth; 3) draw nose
    :param win: GraphWin object
    :param p: Point -> center point of face
    """
    drawEyes(win, p)
    drawMouth(win, p)
    drawNose(win, p)

def drawEyes(win, p):
    """
    Draws snowman eyes
    Algorithm: draw left and right eyes
    :param win: GraphWin object
    :param p: Point -> center point of face
    """
    drawCircle(Point(p.getX() - 4, p.getY() - 4), 2, "black", "black").draw(win)
    drawCircle(Point(p.getX() + 4, p.getY() - 4), 2, "black", "black").draw(win)

def drawNose(win, p):
    """
    Draws snowman nose
    Algorithm: draw triangle with base at center of face, extending downwards
    :param win: GraphWin object
    :param p: Point -> center of face
    """
    drawTriangle([Point(p.getX()-2, p.getY()),
                  Point(p.getX()+2, p.getY()),
                  Point(p.getX()-2, p.getY()+10)], "orange4", "orange").draw(win)

def drawMouth(win, p):
    """
    Draws snowman mouth
    Algorithm: draw two lines that are not colinear, meeting at middle of face below nose
    :param win: GraphWin object
    :param p: Point -> center of face
    """
    Line(Point(p.getX()-5, p.getY()+6), Point(p.getX(), p.getY()+8)).draw(win)
    Line(Point(p.getX(), p.getY()+8), Point(p.getX()+5, p.getY()+7)).draw(win)

def drawRect(p1, p2, outline, fill):
    """
    Defines a rectangle object with outline and fill
    :param p1: Point -> first point for rectangle
    :param p2: Point -> second point for rectangle
    :param outline: str -> color name for outline
    :param fill: str -> color name for fill
    :return: Rectangle -> rectangle object
    """
    rect = Rectangle(p1, p2)
    rect.setOutline(outline)
    rect.setFill(fill)
    return rect

def drawCircle(center, radius, outline, fill):
    """
    Defines a circle object with outline and fill
    :param center: Point -> center of circle
    :param radius: int -> radius of circle
    :param outline: str -> color name for outline
    :param fill: str -> color name for fill
    :return: Circle -> circle object
    """
    circ = Circle(center, radius)
    circ.setOutline(outline)
    circ.setFill(fill)
    return circ

def drawTriangle(points, outline, fill):
    """
    Defines triangle object with outline and fill
    :param points: List[Point, Point, Point] -> list of three points for triangle
    :param outline: str -> color name for outline
    :param fill: str -> color name for fill
    :return: Polygon -> polygon object
    """
    tri = Polygon(points)
    tri.setOutline(outline)
    tri.setFill(fill)
    return tri

if __name__ == '__main__':
    main()
