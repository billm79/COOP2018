# U10_Ex12_Five_Cards.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 7 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
#   Uses Deck and Card classes to "deal" a five-card hand of cards to a Graphwin
#
# Algorithm (pseudocode)
#   main():
#       create GraphWin and set coordinates
#       create Deck object, shuffle, and cut
#       deal five cards from top of deck (every other card, like a real hand with two players)
#       draw each card to window, overlapping (because of their large size)
#       wait for mouse click to close window

from graphics import *
from Card import *


def main():
    win = GraphWin("Five Cards", 1200, 800)
    win.setCoords(0, 0, 10, 10)
    deck = Deck()
    deck.shuffle()
    deck.cut()
    i = 0
    while i < 5:
        deck.getDeck()[i*2].draw(win, Point(i+3, 5))
        i += 1
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
