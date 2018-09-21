# U12_Ex01_SplashScreen.py
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
#   Adds a splash screen to the GUI Dice Poker game
#
# Algorithm (pseudocode)
#   see comments

from graphics import *
from Chapter12.U12_Ex01_DicePoker.button import Button
from Chapter12.U12_Ex01_DicePoker.shadowtext import ShadowText

class SplashScreen():
    """
    SplashScreen class for the GUI Dice Poker game
    """
    def __init__(self, hi_scores):
        """
        The splash screen is set up and displayed in the constructor.
        High scores are displayed in the splash screen. Screen height
        is dynamically determined based on the length of the high score list.
        :param hi_scores: obj -> HighScore object
        """
        winW = 300
        winH = 200

        if hi_scores.scores_exist:
            for score in hi_scores.scores:
                winH += hi_scores.get_scores_fontsize() * 1.5   # font size plus half for line spacing
            winH += hi_scores.get_heading_fontsize() * 1.3      # allow for heading and space after

        self.win = GraphWin("Dice Poker", winW, winH)
        self.win.setBackground(color_rgb(80, 0, 0))
        self.display_msg(150, 40, "Welcome to Dice Poker", 'white', 'white', 24)
        self.display_msg(150, 80, "Play poker using five dice.", 'white', 'white', 12)
        self.display_msg(150, 100, "Up to two re-rolls are allowed.", 'white', 'white', 12)

        if hi_scores.scores_exist():
            # display high scores list
            line_pos = 150

            # first line is heading
            self.display_msg(winW/2, line_pos, hi_scores.get_heading(),
                             'white', 'white', hi_scores.get_heading_fontsize())

            # display scores
            while True:
                score_info = hi_scores.get_next_score()
                name = score_info[0]
                hi_score = score_info[1]
                if name == None:
                    break
                line_pos += hi_scores.get_scores_fontsize() * 1.1
                self.display_msg(winW/2, line_pos+hi_scores.get_scores_fontsize(),
                                 '{}\t{}'.format(name, hi_score),
                                 'white', 'white', hi_scores.get_scores_fontsize())

        self.button_play = Button(self.win, Point(95, winH - 40), 75, 35, "Let's Play")
        self.button_exit = Button(self.win, Point(207, winH - 40), 75, 35, "Exit")
        self.button_play.activate()
        self.button_exit.activate()

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
        msg_shadow = ShadowText(msg, offset_x=2, offset_y=2)
        msg_shadow.draw(self.win)
        msg.draw(self.win)

    def get_response(self):
        """
        Event loop to get response from user (clicking a button or pressing Return or Escape)
        :return: boolean -> True if Play is selected; otherwise False
        """
        while True:
            p = self.win.checkMouse()
            k = self.win.checkKey()
            if p and self.button_play.clicked(p) or k == "Return":
                self.win.close()
                return True
            if p and self.button_exit.clicked(p) or k == "Escape":
                self.win.close()
                return False
