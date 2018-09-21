# U12_Ex01_HighScore.py
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
#   Adds a high score feature to the GUI Dice Poker game
#
# Algorithm (pseudocode)
#   see comments

from graphics import *
from button import Button

class HighScore():
    """
    HighScore class for GUI game
    """
    def __init__(self):
        self.heading = "High Scores"
        self.heading_fontsize = 18
        self.scores = []
        self.get_scores()                       # populate self.scores from high scores file
        self.scores_fontsize = 12
        self.list_pointer = 0                   # current item index in self.scores

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

    def get_heading(self):
        return self.heading

    def get_heading_fontsize(self):
        return self.heading_fontsize

    def get_scores_fontsize(self):
        return self.scores_fontsize

    def get_next_score(self):
        """
        Gets next score from list, using self.list_pointer to know the current index
        :return: str, int -> name, score (score is stored as a string in file)
        """
        if self.list_pointer < len(self.scores):
            score_info = self.scores[self.list_pointer]
            self.list_pointer += 1
            return score_info[0], int(score_info[1])
        return None, None

    def get_scores(self):
        """
        High scores are stored in a file. Each line is in Name, Score order.
        """
        try:
            file = open('hi-scores.txt', 'r')

            for line in file:
                self.scores.append(line[:-1].split(","))
            file.close()
        except FileNotFoundError:
            pass

    def scores_exist(self):
        """
        :return: boolean -> True if scores exist; False otherwise
        """
        return len(self.scores) > 0

    def is_top_ten(self, score):
        """
        Is this score in the top ten?
        :param score: int -> score to check
        :return: True if score is in the top ten
        """
        return len(self.scores) < 10 or score > int(self.scores[-1][1])

    def set_score(self, name, score):
        """
        Writes top ten scores to hi-scores.txt
        :param name: str -> name of user
        :param score: int -> user's score
        """
        self.scores.append([name, score])                       # append score to list
        self.scores.sort(key=self.__get_score, reverse=True)    # sort in descending order
        range_len = min(10, len(self.scores))                   # only take top ten
        outfile = open('hi-scores.txt', 'w')
        for i in range(range_len):
            print("{},{}".format(self.scores[i][0], self.scores[i][1]), file=outfile)

    def __get_score(self, entry):
        """
        Internal helper method to return score from entry
        :param entry: list -> [name], [score]
        :return: int -> score
        """
        return int(entry[1])

    def set_pointer(self, idx):
        """
        Sets self.list_pointer to idx
        :param idx: int -> new index value
        """
        self.list_pointer = idx
