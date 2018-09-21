# U09_S00_Racquetball.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 25 Jan 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 9
#
# Program Description
#   Simulate multi-game matches of racquetball for two players
#
# Algorithm (pseudocode)
#   Print an introduction 
#   Get the inputs: probA, probB, matches (m), games (g)
#    Simulate m matches, each with g games, of racquetball using probA and probB 
#   Print a report on the matches won for playerA and playerB

from random import random

def main():
    printIntro()
    matches, games, probA, probB = getInputs()
    winsA, winsB = simNMatches(matches, games, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print('\nThis program simulates a number of racquetball games based on point scoring probabilities entered by user.\n')

def getInputs():
    # get winning probabilities for both players
    a = float(input('What is the probability player A wins a serve? (enter as decimal ≤ 1) '))
    b = float(input('What is the probability player B wins a serve? (enter as decimal ≤ 1) '))

    # get number of games per match
    n = int(input('How many games per match (odd)? '))

    # get number of matches to simulate
    m = int(input('How many matches to simulate? '))

    return m, n, a, b


def simNMatches(m, g, a, b):
    """
    Simulates m matches of racquetball
    :param m: int -> number of matches to simulate
    :param g: int -> number of games per match
    :param a: float -> probability player A wins serve
    :param b: float -> probability player B wins serve
    :return: int, int -> matches won by players
    """
    matchesA = 0; matchesB = 0

    for match in range(m):
        gamesA, gamesB = simOneMatch(g, a, b)
        if gamesA > g / 2:
            matchesA += 1
        else:
            matchesB += 1
    return matchesA, matchesB


def simOneMatch(g, a, b):
    """
    Simulates one match
    :param g: int -> games per match
    :param a: float -> probability player A wins serve
    :param b: float -> probability player B wins serve
    :return: int, int -> games won by players
    """
    gamesA = 0; gamesB = 0; game = 1

    while not matchOver(g, gamesA, gamesB):
        scoreA, scoreB = simOneGame(game, a, b)
        if scoreA > scoreB:
            gamesA += 1
        else:
            gamesB += 1
        game += 1

    return gamesA, gamesB


def matchOver(g, a, b):
    return a > g / 2 or b > g / 2


def simNGames(n, a, b):
    """
    Simulates n games of racquetball
    Algorithm:
        initialize to 0 int variables for players A and B number of wins
        loop for number of games
            simulate a game
            increment appropriate player variable, based on outcome of game
    :param n: int -> number of games to simulate
    :param a: float -> probability player A wins serve
    :param b: float -> probability player B wins serve
    :return: int, int -> number of wins for player A, B
    """
    winsA = 0; winsB = 0
    for game in range(n):
        scoreA, scoreB = simOneGame(a, b)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def simOneGame(g, a, b):
    """
    Simulates one game of racquetball
    Algorithm:
        initialize scores to 0
        set server to 'A'
        loop until game is over
            simulate one serve for current server
            update stats
        return scores
    :param a: float -> probability player A wins serve
    :param b: float -> probability player B wins serve
    :return: int, int -> scores for players A, B
    """
    scoreA = 0; scoreB = 0

    if g % 2 == 0:
        server = 'B'
    else:
        server = 'A'

    while not gameOver(scoreA, scoreB):
        prob = random()
        if server == 'A':
            if prob < a:
                scoreA += 1
            else:
                server = 'B'
        else:
            if prob < b:
                scoreB += 1
            else:
                server = 'A'
    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b == 15


def printSummary(a, b):
    n = a + b
    print('\nMatches simulated:', n)
    print('Matches won for A: {} ({:4.1%})'.format(a, a / n))
    print('Matches won for B: {} ({:4.1%})'.format(b, b / n))


if __name__ == '__main__':
    main()