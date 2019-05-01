# U06_Ex04_Sums.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Prints the sums of the first n natural numbers (1, 2, 3, ...) and of their cubes
#
# Algorithm (pseudocode)
#   introduce program
#   get number of natural numbers to sum, n, from user
#   call sumN() with parameter n and assign result to nSum
#   call sumNCubes() with parameter n and assign result to nCubedSum
#   print results
#
#   sumN()
#       n is argument
#       initialize accumulator, total, for addition
#       loop n times
#           add current natural number to accumulator
#               Note: looping starts at 0, but first natural number is 1
#       return total
#
#   sumNCubes()
#       n is argument
#       initialize accumulator, total, for addition
#       loop n times
#           add cube of current natural number to accumulator
#               Note: looping starts at 0, but first natural number is 1
#       return total


def main():
    # introduce program
    print('Prints the sums of the first n natural numbers (1, 2, 3, ...) and of their cubes.')

    # get number of natural numbers to sum, n, from user
    n = int(input('How many natural numbers do you want to sum? '))

    # call sumN() with parameter n and assign result to nSum
    nSum = sumN(n)

    # call sumNCubes() with parameter n and assign result to nCubedSum
    nCubedSum = sumNCubes(n)

    # print results
    print('\nThe sum of the first {0} natural numbers is {1}.\nThe sum of their cubes is {2}'.format(n, nSum, nCubedSum))

# sumN()
#     n is argument
def sumN(n):
    # initialize accumulator, total, for addition
    total = 0
    # loop n times
    for i in range(n):
        # add current natural number to accumulator
        #     Note: looping starts at 0, but first natural number is 1
        total += i+1
    # return total
    return total

# sumNCubes()
#     n is argument
def sumNCubes(n):
    # initialize accumulator, total, for addition
    total = 0
    # loop n times
    for i in range(n):
        # add cube of current natural number to accumulator
        #     Note: looping starts at 0, but first natural number is 1
        total += (i+1)**3
    # return total
    return total


if __name__ == '__main__':
    main()
