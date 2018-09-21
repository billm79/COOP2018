# U09_Ex04_VolleyballRally.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 15 Dec 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 9
#
# Program Description
#   Simulates the game of volleyball. Games are played to 25, but must be won by
#   2 points. A team scores by winning a rally. Matches are best of 5 games. First
#   serve alternates each game.
#
# Algorithm (pseudocode)
#   introduce program
#   get inputs
#   simulate matches
#   print report (output)
#
#   INPUT
#       probabilities that teams A and B will win a rally when serving (pSrvA, pSrvB)
#       number of matches to play (numMatches)
#   
#   OUTPUT
#       Matches simulated: ###
#       Matches won A: ### (##.#%)
#       Matches won B: ### (##.#%)


from random import random

def main():
    introProg()
    pSrvA, pSrvB, numMatches = getInput()
    matchesA, matchesB = simNMatches(pSrvA, pSrvB, numMatches)
    printReport(matchesA, matchesB)

def introProg():
    print('\nThis program simulates the game of volleyball. Games are played')
    print('to twenty-five points and must be won by two points. A team scores')
    print('by winning a rally. Matches are played to the best of five games.')
    print('First serve alternates each game. Team A serves first each match.')
    input('(press Return to continue)')

def getInput():
    aS = float(input('\nWhat is the probability (0.0 - 1.0) that team A wins when serving? '))
    bS = float(input('What is the probability (0.0 - 1.0) that team B wins when serving? '))
    n = int(input('How many matches are to be simulated? '))
    return aS, bS, n

def simNMatches(pSrvA, pSrvB, n):
    matchesA = 0; matchesB = 0

    for match in range(n):
        winner = simOneMatch(pSrvA, pSrvB)

        if winner == 'A':
            matchesA += 1
        else:
            matchesB += 1

    return matchesA, matchesB

def simOneMatch(pSrvA, pSrvB):
    gamesA = 0; gamesB = 0
    server = 'A'

    # for each match (input)
    while not matchOver(gamesA, gamesB):
        # simulate games until one team wins 3 games
        scoreA, scoreB = simOneGame(pSrvA, pSrvB, server)

        if scoreA > scoreB:
            gamesA += 1
            server = 'B'
        else:
            gamesB += 1
            server = 'A'
    return 'A' if gamesA >= 3 else 'B'

def matchOver(gA, gB):
    return gA >= 3 or gB >= 3

def simOneGame(pSrvA, pSrvB, server):
    scoreA = 0; scoreB = 0

    while not gameOver(scoreA, scoreB):
        randNum = random()
        if server == 'A':
            if randNum < pSrvA:
                scoreA += 1
            else:
                scoreB += 1
            server = 'B'
        else:
            if randNum < pSrvB:
                scoreB += 1
            else:
                scoreA += 1
            server = 'A'

    return scoreA, scoreB

def gameOver(sA, sB):
    return (sA >= 25 or sB >= 25) and (abs(sA - sB) >= 2)

def printReport(mA, mB):
    m = mA + mB
    print('\nMatches simulated: {}'.format(m))
    print('Matches won A: {} ({:.1%})'.format(mA, mA / m))
    print('Matches won B: {} ({:.1%})'.format(mB, mB / m))

if __name__ == '__main__':
    main()
