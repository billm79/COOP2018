# U09_S03a_Racquetball.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 12 Dec 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: Section 3 example
#     Source: Python Programming
#    Chapter: 9
#
# Program Description
#   Simulates racquetball games with assigned probabilities for players
#
# Algorithm (pseudocode)
#   introduce program
#   get winning probabilities for both players
#   get number of games to simulate
#   initialize to 0 int variables for players A and B number of wins
#   initialize variable to indicate current server to 'A'
#   loop for number of games
#       get a random number between 0 and 1
#       increment appropriate player variable, based on \
#           current server and result of random number
#   print nicely formatted report of results


from random import random

def main():
    # introduce program
    print('\nThis program simulates a number of racquetball games based on point scoring probabilities entered by user.\n')

    # get winning probabilities for both players
    probA = float(input('What is the probability player A wins a serve? (enter as decimal ≤ 1) '))
    probB = float(input('What is the probability player B wins a serve? (enter as decimal ≤ 1) '))

    # get number of games to simulate
    numGames = int(input('How many games to simulate? '))

    # initialize to 0 int variables for players A and B number of wins
    winsA = 0; winsB = 0

    # initialize variable to indicate current server to 'A'
    server = 'A'

    # loop for number of games
    for game in range(numGames):
        # get a random number between 0 and 1
        probX = random()

        # increment appropriate player variable, based on \
        #     current server and result of random number
        if server == 'A':
            if probX < probA:
                winsA += 1
            else:
                server = 'B'
        elif server == 'B':
            if probX < probB:
                winsB += 1
            else:
                server = 'A'

    # print nicely formatted report of results
    print('\nGames Simulated: {}'.format(numGames))
    print('Wins for A: {} ({:4.1f}%)'.format(winsA, winsA / numGames * 100))
    print('Wins for B: {} ({:4.1f}%)'.format(winsB, winsB / numGames * 100))

if __name__ == '__main__':
    main()