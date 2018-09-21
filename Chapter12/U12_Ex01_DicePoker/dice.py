# dice.py

from random import randrange


class Dice:
    """
    Representation of five dice
    """
    def __init__(self):
        """
        Create five dice and rolls to set random values
        """
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        """
        Rolls dice specified in which
        :param which: list -> integers representing which dice to roll
        """
        for pos in which:
            self.dice[pos] = randrange(1,7)

    def rollAll(self):
        """
        Calls self.roll() to roll all dice
        """
        self.roll(range(5))

    def values(self):
        """
        Values of all dice
        :return: list -> copy of self.dice[] containing die values
        """
        return self.dice[:]

    def score(self):
        """
        Determines score of hand
        :return: str, int -> name of hand, if any; score of hand in dollars as integer
        """
        # Create the counts list
        counts = [0] * 7  
        for value in self.dice:
            counts[value] = counts[value] + 1

        # score the hand
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1]==0 or counts[6] == 0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0
