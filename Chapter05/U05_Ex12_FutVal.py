# U05_Ex12_FutVal.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 11 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Nicely formatted version of futval.py from Chapter 2
#
# Algorithm (pseudocode)
#   After apr, get years from user
#   Print headings
#   Inside for loop, print each year's data


def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    #   After apr, get years from user
    years = int(input('Enter number of years for investment: '))

    #   Print headings
    print('Year\t  Value')
    print('----\t---------')

    for year in range(years):
        principal = principal * (1 + apr)

        # Inside for loop, print each year's data
        print('{0:4}\t${1:.2f}'.format(year+1, principal))

main()
