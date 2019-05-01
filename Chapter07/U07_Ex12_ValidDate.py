# U07_Ex12_ValidDate.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Function that validates dates supplied in mm/dd/yyyy format
#
# Algorithm (pseudocode)
#   introduce program
#   create a list with sample data with which to test
#   for each element in list call isValidDate() with element as parameter
#   print results
#
#   isValidDate()
#       d is date argument in mm/dd/yyyy format
#       parse d into month, day, and year variables
#       make them ints
#       create dayRanges list
#       set validDate to False
#       if month in range 1-12
#           if day in correct range for month
#               if not (month is February AND day is 29 AND year not isLeapYear)
#                   set validDate to True
#       return validDate


from Chapter07.U07_Ex11_LeapYear import isLeapYear

# globals: mth, day, yr
mth = ''    #input("mth: ")
day = ''    #input("day: ")
yr = '' #input("yr: ")


def setInputs(m, d, y):
    global mth, day, yr
    mth = m
    day = d
    yr = y


def main():
    # introduce program
    print('\nThis program contains the function isValidDate() which determines if a given date (mm/dd/yyyy) is valid.\n')

    # create a list with sample data with which to test
    dates = ['1/1/1970', '9/31/2000', '2/29/2017', '2/28/2017', '2/29/2000', '2/28/2000']

    # for each element in list call isValidDate() with element as parameter
    for date in dates:
        # print results
        print('{0} {1} a valid date'.format(date, 'is' if isValidDate(date) else 'is not'))

# isValidDate()
#     d is date argument in mm/dd/yyyy format
def isValidDate(m, d, y):
    setInputs(m, d, y)
    # uses globals
    # parse d into month, day, and year variables
    month, day, year = d.split('/')

    # make them ints
    month = int(month); day = int(day); year = int(year)

    # create dayRanges list
    dayRanges = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # set validDate to False
    validDate = False

    # if month in range 1-12
    if (month - 1) in range (12):
        # if day in correct range for month
        if (day - 1) in range(dayRanges[month - 1]):
            # if not (month is February AND day is 29 AND year not isLeapYear)
            if not (month == 2 and day == 29 and not isLeapYear(year)):
                # set validDate to True
                validDate = True
    # return validDate
    return validDate

if __name__ == '__main__':
    main()


'''
RESULTS:
========
isValidDate("1/1/1970")     -->       1 |       1 | [ Pass ]
isValidDate("9/31/2000")    -->       0 |       0 | [ Pass ]
isValidDate("2/29/2017")    -->       0 |       0 | [ Pass ]
isValidDate("2/28/2017")    -->       1 |       1 | [ Pass ]
isValidDate("2/29/2000")    -->       1 |       1 | [ Pass ]
isValidDate("2/28/2000")    -->       1 |       1 | [ Pass ]
isValidDate("13/28/2000")   -->       0 |       0 | [ Pass ]
========
'''