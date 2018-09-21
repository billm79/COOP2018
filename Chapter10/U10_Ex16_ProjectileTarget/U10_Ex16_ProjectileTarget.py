# U10_Ex16_ProjectileTarget.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 08 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
#   Single-shot cannonball animation with target added
#
# Algorithm (pseudocode)
#   create Target class
#
#   in main():
#       create Target object and place randomly along ground
#       in event loop...
#           test for hit and display results
#           quit if target hit (after mouse click)
#
#   added to ShotTracker: self.radius, getRadius()


from math import sqrt, sin, cos, radians, degrees
from graphics import *
from projectile import Projectile
from button import Button
from random import randrange

class InputDialog:

    """ A custom window for getting simulation values (angle, velocity,
    and height) from the user."""

    def __init__(self, angle, vel, height):
        """ Build and display the input window """
        
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0,4.5,4,.5)
        
        Text(Point(1.8-len("Angle")*.1,1), "Angle").draw(win)
        self.angle = Entry(Point(2.8,1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1.8-(len("Velocity")-2)*.1,2), "Velocity").draw(win)
        self.vel = Entry(Point(2.8,2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1.8-(len("Height")-1)*.1,3), "Height").draw(win)
        self.height = Entry(Point(2.8,3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire!")
        self.fire.activate()

        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    def getValues(self):
        """ return input values """
        
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a,v,h

    def interact(self):
        """ wait for user to click Quit or Fire button
        Returns a string indicating which button was clicker
        """
        
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def close(self):
        """ close the input window """
        self.win.close()


class ShotTracker:

    """ Graphical depiction of a projectile flight using a Circle """

    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot, angle, velocity, and
        height are initial projectile parameters.
        """
        
        self.proj = Projectile(angle, velocity, height)
        self.radius = 2
        self.marker = Circle(Point(0,height), self.radius)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

        
    def update(self, dt, win):
        """ Move the shot dt seconds farther along its flight """

        _greyCircle = Circle(Point(self.proj.getX(), self.proj.getY()), .05)
        _greyCircle.setFill("grey")
        _greyCircle.setOutline("grey")
        _greyCircle.draw(win)
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

        
    def getX(self):
        """ return the current x coordinate of the shot's center """
        return self.proj.getX()

    def getY(self):
        """ return the current y coordinate of the shot's center """
        return self.proj.getY()

    def getRadius(self):
        """ return the radius of the shot """
        return self.radius

    def destroy(self):
        """ undraw the shot """
        self.marker.undraw()


class Target:
    def __init__(self, win, minX, maxX, xAxis):
        """ create and place target rectangle """
        self.minX = minX if minX else 0
        self.maxX = maxX if maxX else 100
        self.centerX = randrange(minX, maxX)
        self.target = Rectangle(Point(self.centerX-5, 5), Point(self.centerX+5, xAxis))
        self.target.setFill('blue')
        self.target.draw(win)

    def hitTarget(self, proj):
        """ check for shot within or touching target """
        return proj.getX() >= self.target.getP1().getX() - proj.getRadius() and \
                proj.getX() <= self.target.getP2().getX() + proj.getRadius()

    def destroy(self):
        """ undraw the target """
        self.target.undraw()


def main():

    # create animation window
    win = GraphWin("Projectile Animation", 640, 480, autoflush=False)
    win.setCoords(-20, -10, 420, 310)
    Line(Point(0,0), Point(420,0)).draw(win)
    Line(Point(0,0), Point(0,310)).draw(win)
    Text(Point(-10, -5), "0").draw(win)
    for x in range(50, 420, 50):
        Text(Point(x,-5), str(x)).draw(win)
        Line(Point(x,0), Point(x,2)).draw(win)
    for y in range(50, 310, 50):
        Text(Point(-10,y), str(y)).draw(win)
        Line(Point(0,y), Point(2,y)).draw(win)

    angle, vel, height = 45.0, 40.0, 2.0

    # create and place target
    target = Target(win, 0, 420, 0)

    # event loop
    while True:
        # interact with the user
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()
        
        if choice == "Quit": # loop exit
            break
        
        # otherwise choice is "Fire!"
        # create a shot and track until it hits ground or leaves window
        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 420:
            shot.update(1/50, win)
            update(50)
        Text(Point(shot.getX(), shot.getY()+5), "x = {0:0.1f}".format(shot.getX())).draw(win)
        if target.hitTarget(shot):
            Text(Point(shot.getX(), shot.getY() + 15), "Hit!").draw(win)
            Text(Point(shot.getX(), shot.getY() + 35), "click to quit").draw(win)
            win.getMouse()
            break
        #shot.destroy()
        
    win.close()
    

if __name__ == "__main__":
    main()
