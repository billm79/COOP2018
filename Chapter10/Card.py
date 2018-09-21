# Card.py
"""Class for playing cards"""
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 12 Feb 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Example: Card Class
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
#   Implementation of a class for a playing card
#
# Algorithm (pseudocode)
#   
#   
#   
#   
#   

from random import randrange
from graphics import *


class Card:
    def __init__(self, suit, rank):
        """
        Card constructor method
        :param suit: int -> 0 = hearts, 1 = diamonds, 2 = clubs, 3 = spades
        :param rank: int -> number rank of card
        """
        self.suit = suit
        self.rank = rank
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['null', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def setSuit(self, arg):
        """Sets the suit (int, 0-4) of an individual card"""
        self.suit = arg

    def setRank(self, arg):
        self.rank = arg

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def getSuitName(self):
        return self.suits[self.suit]

    def getRankName(self):
        return self.ranks[self.rank]

    def draw(self, win, center):
        """
        Draws the card
        :param win: Graphics -> window in which to draw
        :param center: Point -> center of card
        :return: None
        """
        _cards = {(0, 1): 'images/ace_of_hearts.gif', (0, 2): 'images/2_of_hearts.gif',
                  (0, 3): 'images/3_of_hearts.gif', (0, 4): 'images/4_of_hearts.gif',
                  (0, 5): 'images/5_of_hearts.gif', (0, 6): 'images/6_of_hearts.gif',
                  (0, 7): 'images/7_of_hearts.gif', (0, 8): 'images/8_of_hearts.gif',
                  (0, 9): 'images/9_of_hearts.gif', (0, 10): 'images/10_of_hearts.gif',
                  (0, 11): 'images/jack_of_hearts2.gif', (0, 12): 'images/queen_of_hearts2.gif',
                  (0, 13): 'images/king_of_hearts2.gif',
                  (1, 1): 'images/ace_of_diamonds.gif', (1, 2): 'images/2_of_diamonds.gif',
                  (1, 3): 'images/3_of_diamonds.gif', (1, 4): 'images/4_of_diamonds.gif',
                  (1, 5): 'images/5_of_diamonds.gif', (1, 6): 'images/6_of_diamonds.gif',
                  (1, 7): 'images/7_of_diamonds.gif', (1, 8): 'images/8_of_diamonds.gif',
                  (1, 9): 'images/9_of_diamonds.gif', (1, 10): 'images/10_of_diamonds.gif',
                  (1, 11): 'images/jack_of_diamonds2.gif', (1, 12): 'images/queen_of_diamonds2.gif',
                  (1, 13): 'images/king_of_diamonds2.gif',
                  (2, 1): 'images/ace_of_clubs.gif', (2, 2): 'images/2_of_clubs.gif',
                  (2, 3): 'images/3_of_clubs.gif', (2, 4): 'images/4_of_clubs.gif',
                  (2, 5): 'images/5_of_clubs.gif', (2, 6): 'images/6_of_clubs.gif',
                  (2, 7): 'images/7_of_clubs.gif', (2, 8): 'images/8_of_clubs.gif',
                  (2, 9): 'images/9_of_clubs.gif', (2, 10): 'images/10_of_clubs.gif',
                  (2, 11): 'images/jack_of_clubs2.gif', (2, 12): 'images/queen_of_clubs2.gif',
                  (2, 13): 'images/king_of_clubs2.gif',
                  (3, 1): 'images/ace_of_spades.gif', (3, 2): 'images/2_of_spades.gif',
                  (3, 3): 'images/3_of_spades.gif', (3, 4): 'images/4_of_spades.gif',
                  (3, 5): 'images/5_of_spades.gif', (3, 6): 'images/6_of_spades.gif',
                  (3, 7): 'images/7_of_spades.gif', (3, 8): 'images/8_of_spades.gif',
                  (3, 9): 'images/9_of_spades.gif', (3, 10): 'images/10_of_spades.gif',
                  (3, 11): 'images/jack_of_spades2.gif', (3, 12): 'images/queen_of_spades2.gif',
                  (3, 13): 'images/king_of_spades2.gif'}
        cardImg = Image(center, _cards.get((self.suit, self.rank))).draw(win)

    def __str__(self):
        return 'Suit: {} ({})\tRank: {} ({})'.format(self.getSuitName(), self.getSuit(), self.getRankName(), self.getRank())


class Deck:
    def __init__(self):
        self.cards = []

        for s in range(4):
            for r in range(1, 14):
                self.cards.append(Card(s, r))

    def getDeck(self):
        return self.cards

    def shuffle(self):
        for i in range(self.getLength()):
            card1 = randrange(self.getLength()); card2 = card1
            while card2 == card1:
                card2 = randrange(self.getLength())
            self.swap(card1, card2)

    def swap(self, card1, card2):
        self.cards[card1], self.cards[card2] = self.cards[card2], self.cards[card1]

    def cut(self):
        _length = len(self.cards)
        cutPoint = randrange(_length // 2 - _length // 10, _length // 2 + _length // 10)
        cut1 = self.cards[:cutPoint]
        cut2 = self.cards[cutPoint+1:]
        self.cards = cut2 + cut1

    def getLength(self):
        return len(self.cards)

    def toString(self):
        for card in self.cards:
            print(card)


def main():
    deck = Deck()
    deck.shuffle()
    deck.toString()

if __name__ == '__main__':
    main()
