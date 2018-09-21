# U09_Ex02_RacquetballShutouts.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 12 Dec 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 2
#     Source: Python Programming
#    Chapter: 9
#
# Program Description
#   Simulates racquetball games with assigned probabilities for players
#   Takes shutouts into account
#   Reports wins, wins percentage, shutouts, shutout wins percentage for each player
#
# Algorithm (pseudocode)
#   print introduction
#   get inputs: probA, probB, n
#   simulate n games of racquetball using probA and probB
#   print a report on the wins for playerA and playerB


from random import random


def main():
    printIntro()
    probA, probB, numGames = getInputs()
    winsA, winsB, shutoutsA, shutoutsB = simNGames(numGames, probA, probB)
    printSummary(winsA, winsB, shutoutsA, shutoutsB)


def printIntro():
    print(
        '\nThis program simulates a number of racquetball games based on point scoring probabilities entered by user.\n')


def getInputs():
    # get winning probabilities for both players
    a = float(input('What is the probability player A wins a serve? (enter as decimal ≤ 1) '))
    b = float(input('What is the probability player B wins a serve? (enter as decimal ≤ 1) '))

    # get number of games to simulate
    n = int(input('How many games to simulate? '))

    return a, b, n


def simNGames(n, probA, probB):
    '''
    Simulates n games of racquetball
    Algorithm:
        initialize to 0 int variables for players A and B number of wins
        loop for number of games
            simulate a game
            increment appropriate player variable, based on outcome of game
    :param n: int -> number of games to simulate
    :param probA: float -> probability player A wins serve
    :param probB: float -> probability player B wins serve
    :return: int, int -> number of wins for player A, B
    '''
    # initialize to 0 int variables for players A and B number of wins and shutouts
    winsA = 0; winsB = 0; shutoutsA = 0; shutoutsB = 0

    # loop for number of games
    for game in range(n):
        # simulate a game
        scoreA, scoreB = simOneGame(probA, probB)

        # increment appropriate player variable, based on outcome of game
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1

        # increment appropriate player variable, based on shutout outcome for game
        if scoreA * scoreB == 0 and scoreA + scoreB == 7:
            if scoreA == 7:
                shutoutsA += 1
            else:
                shutoutsB += 1

    return winsA, winsB, shutoutsA, shutoutsB


def printSummary(winsA, winsB, shutoutsA, shutoutsB):
    # print nicely formatted report of results
    n = winsA + winsB
    print('\nGames Simulated: {}'.format(n))
    print('Wins for A: {} ({:4.1%})'.format(winsA, winsA / n))
    print('Shutouts A: {} ({:4.1%})'.format(shutoutsA, shutoutsA / winsA))
    print('Wins for B: {} ({:4.1%})'.format(winsB, winsB / n))
    print('Shutouts B: {} ({:4.1%})'.format(shutoutsB, shutoutsB / winsB))


def simOneGame(probA, probB):
    '''
    Simulates one game of racquetball
    Algorithm:
        initialize scores to 0
        set server to 'A'
        loop until game is over
            simulate one serve for current server
            update stats
        return scores
    :param probA: float -> probability player A wins serve
    :param probB: float -> probability player B wins serve
    :return: int, int -> scores for players A, B
    '''
    # initialize scores to 0
    scoreA = 0;
    scoreB = 0

    # set server to 'A'
    server = 'A'

    # loop until game is over
    while not gameOver(scoreA, scoreB):
        # get a random number between 0 and 1
        probX = random()

        # increment appropriate player variable, based on \
        #     current server and result of random number
        if server == 'A':
            if probX < probA:
                scoreA += 1
            else:
                server = 'B'
        elif server == 'B':
            if probX < probB:
                scoreB += 1
            else:
                server = 'A'

    return scoreA, scoreB


def gameOver(a, b):
    return (a == 15 or b == 15) or (a == 7 and b == 0) or (a == 0 and b == 7)


if __name__ == '__main__':
    main()
