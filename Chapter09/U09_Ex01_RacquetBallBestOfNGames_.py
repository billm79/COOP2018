"""
U09_Ex01_RacquetBallBestOfNGames_.py

  Author: 
  Course: Coding for OOP
 Section: 
    Date: 2019-04-10
     IDE: PyCharm
     
Assignment Info
  Exercise: 01
    Source: Python Programming
   Chapter: 09
   
Program Description
    Simulates N racquetball matches and computes results for best of N game matches.
    First service alternates: A in odd games of match; B in even.
    Inputs are N matches and G games per match, and player probabilities.

Algorithm
    program introduction
    get inputs from user (N matches, G games per match, probA, probB)
    simulate N matches
    print summary results
"""

from random import random
from math import ceil


def main():
    intro()
    matches, games, probA, probB = getInput()
    matchesA, matchesB = simulateNMatches(matches, games, probA, probB)
    summary(matchesA, matchesB, matches, games, probA, probB)


def intro():
    print('\nThis program simulates N racquetball matches and returns results based off user input.')


def getInput():
    """
    Get user input: m matches, g games per match, a probability for player A, b for player B
    :return: int -> m; int -> g; float -> a; float -> b
    """
    m = input('\nHow many matches do you wish to simulate? ')
    g = 2
    while g % 2 == 0:
        g = int(input('How many games per match (must be odd)? '))
    a = input('Probability for player A (greater than 0 and less than 1): ')
    b = input('Probability for player B (greater than 0 and less than 1): ')
    # this is where errors could be trapped...not doing that now
    m = int(m)      #; g = int(g)
    a = float(a); b = float(b)
    return m, g, a, b


def simulateNMatches(matches, games, probA, probB):
    """
    Algorithm
        loop matches times
            simulate one match
            update match counts
    :param matches: int -> number of matches to simulate
    :param games: int -> max games per match
    :param probA: float -> probability that A wins serve
    :param probB: float -> probability that B wins serve
    :return: int -> matchesA; int -> matchesB ... matches won by each player
    """
    matchesA = 0; matchesB = 0
    for match_count in range(matches):
        gamesA, gamesB = simulateOneMatch(games, probA, probB)
        if gamesA > gamesB:
            matchesA += 1
        else:
            matchesB += 1
    return matchesA, matchesB


def simulateOneMatch(games, probA, probB):
    """
    Algorithm
        while match not over
            simulate ONE game
            update player game count
            flip server
    :param games: int -> max games per match
    :param probA: float -> probability that A wins serve
    :param probB: float -> probability that B wins serve
    :return: int -> gamesA; int -> gamesB
    """
    gamesA = 0; gamesB = 0
    server = 'A'
    while not matchOver(gamesA, gamesB, games):
        scoreA, scoreB = simulateOneGame(probA, probB, server)
        if scoreA > scoreB:
            gamesA += 1
        else:
            gamesB += 1
        server = 'A' if server == 'B' else 'B'
    return gamesA, gamesB


def simulateOneGame(probA, probB, server):
    """
    Algorithm
        while game not over
            alternate service (A serves odd games; B even)
            use probabilities to determine service outcome
            update scores
    :param probA: float -> probability that A wins serve
    :param probB: float -> probability that B wins serve
    ;param server: str -> either 'A' or 'B' for server A or server B
    :return: int -> scoreA; int -> scoreB
    """
    scoreA = 0; scoreB = 0
    while not gameOver(scoreA, scoreB):
        if server == 'A':
            if random() < probA:
                scoreA += 1
            else:
                server = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                server = 'A'
    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b == 15


def matchOver(a, b, g):
    # g / 2 plus something (or rounded up)
    return a == ceil(g / 2) or b == ceil(g / 2)


def summary(matchesA, matchesB, matches, games, probA, probB):
    print('\nRacquetball Simulation\n--------------------------------------')
    print('Best of {} matches played: {}'.format(games, matches))
    print('Probability player A wins serve: {}'.format(probA))
    print('Probability player B wins serve: {}'.format(probB))
    print('Matches won by player A: {}'.format(matchesA))
    print('Matches won by player B: {}'.format(matchesB))


if __name__ == '__main__':
    # main()
    # a, b, = simulateOneGame(.9, .3, 'B')
    # print(a, b)
    # a, b = simulateOneMatch(5, .55, .5)
    # print(a, b)
    a, b = simulateNMatches(40000, 5, .5, .5)
    print(a, b)
