# U12_Ex01_HelpScreen.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 18 Apr 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 12
#
# Program Description
#   Adds a help screen to the GUI Dice Poker game
#
# Algorithm (pseudocode)
#   see comments

from graphics import *
from button import Button

class HelpScreen():
    def __init__(self, msg_list):
        """
        HelpScreen class for the GUI Dice Poker game
        :param msg: list -> lines of text to display [[line 1, font size], [line 2, font size], ...]
        """
        winH = 0
        winW = 400
        for line in msg_list:
            winH += line[1] + line[1] / 2   # font size plus half for line spacing
        winH += 70      # to allow for close button
        self.win = GraphWin("Help for Dice Poker", winW, winH)
        self.win.setBackground(color_rgb(80, 0, 0))

        # display lines of help text
        line_pos = 30
        prev_line_ht = msg_list[0][1]

        # first line is heading
        self.display_msg(winW/2, line_pos, msg_list[0][0], 'white', 'white', prev_line_ht)
        prev_line_ht = prev_line_ht / 2
        for line in msg_list[1:]:
            line_pos += prev_line_ht/3 + line[1]
            self.display_msg(winW/2, line_pos+prev_line_ht+line[1], line[0], 'white', 'white', line[1])
            prev_line_ht = line[1]
        self.button_close = Button(self.win, Point(winW/2, winH-40), 75, 35, "Close")
        self.button_close.activate()

    def display_msg(self, x, y, m, c, o, s):
        """
        Helper method to display a message
        :param x: int/float -> x coordinate for center point of message
        :param y: int/float -> y coordinate for center point of message
        :param m: str -> message to display
        :param c: str -> fill color of message
        :param o: str -> outline color of message
        :param s: int -> size of message text
        """
        msg = Text(Point(x, y), m)
        msg.setFill(c)
        msg.setOutline(o)
        msg.setSize(s)
        msg.draw(self.win)

    def get_response(self):
        """
        Event loop to get response from user (clicking the button or pressing Return or Escape)
        :return: boolean -> True when Close is selected
        """
        while True:
            p = self.win.checkMouse()
            k = self.win.checkKey()
            if p and self.button_close.clicked(p) or k == "Return" or k == "Escape":
                self.win.close()
                return True
