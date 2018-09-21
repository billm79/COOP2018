# U09_S00_Racquetball.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 23 Jan 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Sample problem 0
#     Source: Python Programming
#    Chapter: 9
#
# Program Description
#   Simulate N games of racquetball for two players
#
# Algorithm (pseudocode)
#   Print an introduction 
#   Get the inputs: probA, probB, n
#    Simulate n games of racquetball using probA and probB 
#   Print a report on the wins for playerA and playerB

from random import random

def main():
    printIntro()
    n, probA, probB = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print('\nThis program simulates a number of racquetball games based on point scoring probabilities entered by user.\n')

def getInputs():
    # get winning probabilities for both players
    a = float(input('What is the probability player A wins a serve? (enter as decimal ≤ 1) '))
    b = float(input('What is the probability player B wins a serve? (enter as decimal ≤ 1) '))

    # get number of games to simulate
    n = int(input('How many games to simulate? '))

    return n, a, b

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

def simOneGame(a, b):
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
    print('\nGames simulated:', n)
    print('Wins for A: {} ({:4.1%})'.format(a, a / n))
    print('Wins for B: {} ({:4.1%})'.format(b, b / n))


if __name__ == '__main__':
    main()