# button.py
#
#  Author: 
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Feb 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 
#     Source: Python Programming
#    Chapter: 
#
# Program Description
#   A button class for creating and using GUI buttons
#
# Algorithm (pseudocode)
#   
#   
#   
#   
#   

from graphics import *

class Button:
    def __init__(self, win, p1, p2, lbl):
        """
        Creates a rectangular button, e.g.:
        myButton = Button(win, Point(40, 80), Point(140, 100), "Quit")

        :param win: window object -> window in which to draw button
        :param p1: Point -> one corner of button rectangle
        :param p2: Point -> diagonally opposite corner of button rectangle
        :param lbl: str -> button label
        """
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('#cccccc')
        self.xmin = min(p1.getX(), p2.getX())
        self.xmax = max(p1.getX(), p2.getX())
        self.ymin = min(p1.getY(), p2.getY())
        self.ymax = max(p1.getY(), p2.getY())
        self.label = Text(self.rect.getCenter(), lbl)
        self.rect.draw(win)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        """Sets this button to 'active'. """
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, pt):
        """RETURNS True if button active and pt is inside"""
        return self.active and \
            self.xmin <= pt.getX() <= self.xmax and \
            self.ymin <= pt.getY() <= self.ymax
