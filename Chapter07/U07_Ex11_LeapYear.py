# U07_Ex11_LeapYear.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Function that calculates if a given year is a leap year. Returns boolean.
#
# Algorithm (pseudocode)
#   introduce program
#   create a list with sample data with which to test
#   for each element in list call isLeapYear() with element as parameter
#   print results
#   
#   isLeapYear():
#       y is argument
#       if y is divisible by 4 and not century year divisble by 400, return true
#       otherwise, return false


def main():
    # introduce program
    print('This program contains the function isLeapYear() which determines if a given year is a leap year.')

    # create a list with sample data with which to test
    years = [1800, 1900, 2000, 2001, 2002, 2003, 2004]

    # for each element in list call isLeapYear() with element as parameter
    for year in years:
        # print results
        print('{0} {1} a leap year'.format(year, 'is' if isLeapYear(year) else 'is not'))

# isLeapYear():
#     y is argument
def isLeapYear(y):
    # if y is divisible by 4 and not century year divisble by 400, return true
    if y % 4 == 0 and not (y % 100 == 0 and not y % 400 == 0):
        return True
    # otherwise, return false
    return False

if __name__ == '__main__':
    main()


'''
RESULTS:
========
isLeapYear(1800)   -->       0 |       0 | [ Pass ]
isLeapYear(1900)   -->       0 |       0 | [ Pass ]
isLeapYear(2000)   -->       1 |       1 | [ Pass ]
isLeapYear(2001)   -->       0 |       0 | [ Pass ]
isLeapYear(2002)   -->       0 |       0 | [ Pass ]
isLeapYear(2003)   -->       0 |       0 | [ Pass ]
isLeapYear(2004)   -->       1 |       1 | [ Pass ]
========
'''