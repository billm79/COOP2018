# pokerapp.py

from dice import Dice


class PokerApp:
    """
    Play dice poker
    """

    def __init__(self, interface, hi_scores):
        """
        Initialize dice, money, and interface (could be text or GUI)
        :param interface: obj -> interface object
        :param hi_scores: obj -> high scores object
        """
        self.dice = Dice()
        self.money = 100
        self.interface = interface
        self.hi_scores = hi_scores      # added for high score feature
        self.played_once = False        # added for high score feature

    def run(self):
        """
        Runs game continuously until quit or no money left
        """
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()

        # if played at least once, compare score to high score list, add to list if high scorer
        if self.played_once and self.hi_scores.is_top_ten(self.money):
            self.interface.enter_score(self.money)
        self.interface.close()

    def playRound(self):
        """
        Handles all aspects of a round
        """
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)
        self.played_once = True         # added for high score feature

    def doRolls(self):
        """
        Handles all rolls, both initial and any re-rolls
        """
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

