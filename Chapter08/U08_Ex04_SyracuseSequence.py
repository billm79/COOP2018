# U08_Ex04_SyracuseSequence.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Prints the Syracuse sequence for a given starting natural number
#       syr(x) = x / 2, x is even
#       syr(x) = 3x + 1, x is odd
#
# Algorithm (pseudocode)
#   introduce program
#   get starting natural number (int > 0) from user
#   loop until syr(x) is 1
#       if x is odd, use syr(x) = 3x + 1
#       if x is even, use syr(x) = x / 2
#       print syr(x)


def syr(x):
    '''
    Return next term in the Syracuse sequence
    :param x: int previous_term
    :return: int next_term
    '''
    # if x is even, use syr(x) = x / 2
    if x % 2 == 0:
        return int(x / 2)
    # if x is odd, use syr(x) = 3x + 1
    return 3 * x + 1

def main():
    # introduce program
    print('This program prints the Syracuse sequence, starting from a user-supplied natural number.\n')

    # get starting natural number (int > 0) from user
    x = int(input('Enter a starting natural number (integer > 0): '))

    print('{}{}'.format(x, ', '), end='')
    # loop until syr(x) is 1
    while x != 1:
        # print syr(x)
        x = syr(x)
        print('{}{}'.format(x, ', ' if x != 1 else ''), end='')


if __name__ == '__main__':
    main()