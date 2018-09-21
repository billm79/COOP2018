# U08_Ex03_DoubleInv.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Determines how many years are required to double an investment at a given APR
#
# Algorithm (pseudocode)
#   introduce program
#   get APR from user
#   set investment to an arbitrary value, perhaps $1
#   initialize initialize current value (val)
#   initialize a counter (years)
#   loop until investment is at least doubled
#       apply interest rate
#   print years


def main():
    # introduce program
    print('This program determines the amount of time (in years) required for an investment to at least double, given an APR.\n')

    # get APR from user
    apr = float(input('What is the annual percentage rate? (10% should be entered as 0.1): '))

    # set investment to an arbitrary value, perhaps $1
    inv = 1.0

    # initialize current value (val)
    val = inv

    # initialize a counter (years)
    years = 0

    # loop until investment is at least doubled
    while val < 2 * inv:
        # apply interest rate
        val = val * (1 + apr)
        years += 1

    # print years
    print('Years required to at least double the investment: {}'.format(years))

if __name__ == '__main__':
    main()