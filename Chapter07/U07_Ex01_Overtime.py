# U07_Ex01_Overtime.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Calculates weekly wages, taking overtime into account.
#   User inputs hours worked and hourly rate. Overtime after 40 hours.
#
# Algorithm (pseudocode)
#   introduce program
#   get hours worked and hourly rate from user
#   calculate weekly wages by multiplying hours times rate
#   if hours exceed 40, add difference times half-rate to weekly wages
#   print results


def main():
    # introduce program
    print('\nThis program calculates weekly wages, taking overtime into account.')

    # get hours worked and hourly rate from user
    hours = float(input('\nHow many hours were worked this week? '))
    rate = float(input('What is the hourly rate? '))

    # calculate weekly wages by multiplying hours times rate
    wages = hours * rate

    # if hours exceed 40, add difference times half-rate to weekly wages
    if hours > 40:
        wages += (hours - 40) * rate / 2

    # print results
    print('\nFor {0:0.2f} hours at an hourly rate of ${1:0.2f}, weekly pay is ${2:0.2f}.'.format(hours, rate, wages))

main()