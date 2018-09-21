# U08_Ex08_GCDEuclid.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 8
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Finds the greatest common divisor using Euclid's algorithm
#       n, m = m, n%m repeatedly until m is 0
#
# Algorithm (pseudocode)
#   introduce program
#   get two integers from user, m & n
#   call gcd() with m and n as parameters
#   print result
#
#   gcd:
#       m & n are arguments
#       calculate n, m = m, n%m repeatedly until m is 0
#       return n


def gcd(m, n):
    '''
    Computers greatest common divisor of m and n using Euclid's algorithm
    Calculate n, m = m, n%m repeatedly until m is 0
    :param m: int
    :param n: int
    :return: n which is the greatest common divisor
    '''
    # calculate n, m = m, n%m repeatedly until m is 0
    while m != 0:
        n, m = m, n % m
    # return n
    return n

def main():
    # introduce program
    print("This program computes the greatest common divisor using Euclid's algorithm.")

    # get two integers from user, m & n
    m = int(input('Enter first integer: '))
    n = int(input('Enter second integer: '))

    # call gcd() with m and n as parameters
    div = gcd(m, n)

    # print result
    print('The greatest common divisor of {} and {} is {}.'.format(m, n, div))

if __name__ == '__main__':
    main()