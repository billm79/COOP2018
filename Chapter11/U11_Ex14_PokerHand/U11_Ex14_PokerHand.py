# U11_Ex14_PokerHand.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 7 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 11
#
# Program Description
#   Uses Deck and Card classes to "deal" a five-card hand of cards to a GraphWin
#   Then analyze the hand and display the results to the GraphWin
#
# Algorithm (pseudocode)
#   main():
#       create GraphWin and set coordinates
#       create Deck object, shuffle, and cut
#       deal five cards from top of deck (every other card, like a real hand
#           with two players)
#       these cards are added to a PokerHand object
#       sort hand by suit and rank
#       draw each card to window, overlapping (because of their large size)
#       analyze hand and print results to console
#       wait for mouse click to close window

from Chapter11.U11_Ex14_PokerHand.Card import *


class PokerHand:
    """A PokerHand object is five Card objects in a list"""
    def __init__(self):
        self.hand = []
        self.xHigh = ''                 # highest card in hand
        self.isPair = False
        self.isTwoPair = False
        self.isThreeOfAKind = False
        self.isStraight = False
        self.isFlush = False
        self.isFullHouse = False
        self.isFourOfAKind = False
        self.isStraightFlush = False
        self.isRoyalFlush = False
        self.theHand = ''

    def add_card(self, card):
        """Adds card which is a Card object to hand list"""
        self.hand.append(card)

    def update(self):
        """Analyzes hand"""
        self._x_high()
        self._is_pair()
        self._is_two_pair()
        self._is_three_of_a_kind()
        self._is_straight()
        self._is_flush()
        self._is_full_house()
        self._is_four_of_a_kind()
        self._is_straight_flush()
        self._is_royal_flush()
        self._the_hand()

    def _the_hand(self):
        """Helper function for hand analysis; checks for highest value hands first"""
        if self.isRoyalFlush:
            self.theHand = 'Royal Flush'
        elif self.isStraightFlush:
            self.theHand = 'Straight Flush, {} high'.format(self.xHigh)
        elif self. isFourOfAKind:
            self.theHand = 'Four of a Kind, {} high'.format(self.xHigh)
        elif self.isFullHouse:
            self.theHand = 'Full House, {} high'.format(self.xHigh)
        elif self.isFlush:
            self.theHand = 'Flush, {} high'.format(self.xHigh)
        elif self.isStraight:
            self.theHand = 'Straight, {} high'.format(self.xHigh)
        elif self.isThreeOfAKind:
            self.theHand = 'Three of a Kind, {} high'.format(self.xHigh)
        elif self.isTwoPair:
            self.theHand = 'Two Pair, {} high'.format(self.xHigh)
        elif self.isPair:
            self.theHand = 'Pair, {} high'.format(self.xHigh)
        else:
            self.theHand = '{} high'.format(self.xHigh)

    def sort(self, keyFunc):
        """
        Sorts the hand list with the given key function
        :param keyFunc: str -> function in Card class on which to sort
        """
        self.hand.sort(key=eval(keyFunc))

    def _is_flush(self):
        """All cards of same suit"""
        _suit = self.hand[0].getSuit()
        self.isFlush = all(card.getSuit() == _suit for card in self.hand)

    def _is_straight(self):
        """Five cards with consecutive ranks"""
        self.hand.sort(key=Card.getRank)
        _isStraight = True

        # special case of A2345 straight
        if self.hand[-1].getRank() == 14 and self.hand[0].getRank() == 2:
            _previousRank = 1
            for card in self.hand[:-1]:
                if not card.getRank() == _previousRank + 1:
                    _isStraight = False
                    break
                _previousRank = card.getRank()
        else:
            _previousRank = self.hand[0].getRank()
            for card in self.hand[1:]:
                if not card.getRank() == _previousRank + 1:
                    _isStraight = False
                    break
                _previousRank = card.getRank()
        self.isStraight = _isStraight

    def _is_straight_flush(self):
        """A straight flush is both a straight and a flush"""
        self.isStraightFlush = self.isStraight and self.isFlush

    def _is_royal_flush(self):
        """10JQKA in same suit"""
        self.isRoyalFlush = self.isFlush and self.isStraight and self.hand[0].getRank() == 10

    def _is_four_of_a_kind(self):
        """Four of the five cards have the same rank"""
        self.isFourOfAKind = self._in_a_row(4, 0) or self._in_a_row(4, 1)

    def _is_full_house(self):
        """
        Two of the five cards have one rank while the other three have another
        same rank.
        """
        self.isFullHouse = self._in_a_row(3, 0) and self._in_a_row(2, 3) or \
                           self._in_a_row(2, 0) and self._in_a_row(3, 2)

    def _is_three_of_a_kind(self):
        """Three of the five cards have the same rank"""
        self.isThreeOfAKind = self._in_a_row(3, 0) or \
                              self._in_a_row(3, 1) or \
                              self._in_a_row(3, 2)

    def _is_two_pair(self):
        """Two cards with same rank, and two other cards with another same rank"""
        self.isTwoPair = self._in_a_row(2, 0) and self._in_a_row(2, 2) or \
                         self._in_a_row(2, 0) and self._in_a_row(2, 3) or \
                         self._in_a_row(2, 1) and self._in_a_row(2, 3)

    def _is_pair(self):
        """Two of the five cards with the same rank"""
        self.isPair = self._in_a_row(2, 0) or \
                      self._in_a_row(2, 1) or \
                      self._in_a_row(2, 2) or \
                      self._in_a_row(2, 3)

    def _in_a_row(self, num, start):
        """
        Helper function to check for num cards in a row with same rank,
        beginning at start position.
        """
        i = start + 1
        while i < start + num:
            if not self.hand[i].getRank() == self.hand[start].getRank():
                return False
            i += 1
        return True

    def _x_high(self):
        """The rank of the highest card"""
        self.xHigh = self.hand[-1].getRankName()


def main():
    win = GraphWin("Five Cards", 1200, 800)
    win.setCoords(0, 0, 10, 10)
    deck = Deck()
    deck.shuffle()
    deck.cut()

    while len(deck.cards) > 4:
        pokerHand = PokerHand()

        # deal, then burn first five cards
        i = 0
        while i < 5:
            card = deck.getDeck()[0]
            pokerHand.add_card(card)
            del deck.cards[0]
            i += 1

        pokerHand.sort("Card.getSuit")
        pokerHand.sort("Card.getRank")

        i = 0
        for card in pokerHand.hand:
            card.draw(win, Point(i + 3, 5))
            i += 1

        pokerHand.update()
        output(win, pokerHand.theHand)

        for card in pokerHand.hand:
            card.undraw()

        # win.getMouse()
    win.close()


def output(win, msgText):
    # create a 'dialog box'
    rect = Rectangle(Point(3, 6), Point(6, 4))
    rect.setWidth(1)
    rect.setOutline('black')
    rect.setFill('white')
    rect.draw(win)

    # make it look like a window (-ish)
    titlebar = Rectangle(Point(3, 6.3), Point(6, 6))
    titlebar.setFill('grey')
    titlebar.setOutline('black')
    titlebar.setWidth(1)
    titlebar.draw(win)
    title = Text(Point(4.5, 6.15), 'Your Poker Hand')
    title.draw(win)
    msg = Text(Point(4.5, 5.25), msgText)
    msg.setSize(24)
    msg.draw(win)
    msg2 = Text(Point(4.5, 4.4), 'Click to dismiss')
    msg2.draw(win)
    win.getMouse()

    # undraw 'dialog box' after mouse click
    msg.undraw(); msg2.undraw(); rect.undraw(); titlebar.undraw(); title.undraw()


if __name__ == '__main__':
    main()
