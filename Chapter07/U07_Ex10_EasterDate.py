# U07_Ex10_EasterDate.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Calculates the date for Easter in the year range 1900-2099
#
# Algorithm (pseudocode)
#   introduce program
#   get year from user
#   call easterDate with year as parameter
#   print result
#
#   easterDate():
#       year is argument
#       test year to see if it is in range 1900-2099
#       use the following expressions to calculate the date for Easter (all vars represent days)
#           March 22 + d + e, where
#               d = (19a + 24)%30, e = (2b + 4c + 6d + 5)%7, and where
#               a = year%19, b = year%4, c = year%7
#       if year is 1954, 1981, 2049, or 2076 then subtract 7 days
#       set date to 22 (from March 22) plus days previously calculated
#       if days (day date) exceeds 31 (March has 31 days), month is April
#       set suffix (extra)


def easterDate(year):
    # test year to see if it is in range 1900-2099
    if year < 1900 or year > 2099:
        print('\nERROR: Year must be between 1900 and 2099.')
        return None, -1, None

    # use the following expressions to calculate the date for Easter (all vars represent days)
    #     March 22 + d + e, where
    #         d = (19a + 24)%30, e = (2b + 4c + 6d + 5)%7, and where
    #         a = year%19, b = year%4, c = year%7
    a = year % 19; b = year % 4; c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    days = d + e

    # if year is 1954, 1981, 2049, or 2076 then subtract 7 days
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        days -= 7

    # set date to 22 (from March 22) plus days previously calculated
    easter = 22 + days

    # if days (day date) exceeds 31 (March has 31 days), month is April
    month = 'March'
    if easter > 31:
        month = 'April'
        easter -= 31

    # set suffix (extra)
    suffix = ordSuffix(easter)

    return month, easter, suffix

# ordSuffix(): (extra)
#     n (int) is argument
def ordSuffix(n):
    # convert n to string in nStr var
    nStr = str(n)

    # create suffixList = ['st', 'nd', 'rd']
    suffixList = ['st', 'nd', 'rd']

    # if last character of nStr is 1, 2, or 3 AND last two is not in the teens
    if contains(nStr[-1], '123') and not (n > 10 and nStr[-2] == '1'):
        # return matching suffix from suffixList
        return suffixList[int(nStr[-1])-1]
    # otherwise return 'th'
    else:
        return 'th'

# contains(): (extra, needed by ordSuffix())
#     nStr and string are arguments
def contains(nStr, string):
    # loop through string
    for char in string:
        # if an element of string == nStr, return true
        if char == nStr:
            return True
    # otherwise return false
    return False

def main():
    print('\nThis program calculates the date for Easter in the year range 1900-2099.')
    year = int(input('\nEnter the year for which you want to know the Easter date: '))
    month, easter, suffix = easterDate(year)

    if easter != -1:
        # print result
        print('\nFor the year {0}, Easter occurs on {1} {2}{3}'.format(year, month, easter, ordSuffix(easter)))


if __name__ == '__main__':
    main()


'''
RESULTS:
========
contains("1", "123")   -->       1 |       1 | [ Pass ]
contains("1", "231")   -->       1 |       1 | [ Pass ]
contains("1", "312")   -->       1 |       1 | [ Pass ]
contains("0", "123")   -->       0 |       0 | [ Pass ]
========

RESULTS:
========
ordSuffix(0)   -->   th |   th | [ Pass ]
ordSuffix(1)   -->   st |   st | [ Pass ]
ordSuffix(2)   -->   nd |   nd | [ Pass ]
ordSuffix(3)   -->   rd |   rd | [ Pass ]
ordSuffix(4)   -->   th |   th | [ Pass ]
ordSuffix(5)   -->   th |   th | [ Pass ]
ordSuffix(6)   -->   th |   th | [ Pass ]
ordSuffix(7)   -->   th |   th | [ Pass ]
ordSuffix(8)   -->   th |   th | [ Pass ]
ordSuffix(9)   -->   th |   th | [ Pass ]
========

ERROR: Year must be between 1900 and 2099.

ERROR: Year must be between 1900 and 2099.

RESULTS:
========
easterDate(1899)   -->      (None, -1, None) |      (None, -1, None) | [ Pass ]
easterDate(1900)   -->   ('April', 15, 'th') |   ('April', 15, 'th') | [ Pass ]
easterDate(2099)   -->   ('April', 12, 'th') |   ('April', 12, 'th') | [ Pass ]
easterDate(2100)   -->      (None, -1, None) |      (None, -1, None) | [ Pass ]
easterDate(1981)   -->   ('April', 19, 'th') |   ('April', 19, 'th') | [ Pass ]
easterDate(1954)   -->   ('April', 18, 'th') |   ('April', 18, 'th') | [ Pass ]
easterDate(2018)   -->    ('April', 1, 'st') |    ('April', 1, 'st') | [ Pass ]
easterDate(2019)   -->   ('April', 21, 'st') |   ('April', 21, 'st') | [ Pass ]
========
'''