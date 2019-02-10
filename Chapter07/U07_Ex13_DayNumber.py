# U07_Ex13_DayNumber.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 13
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Function that returns day number for date supplied in mm/dd/yyyy format
#
# Algorithm (pseudocode)
#   introduce program
#   create a list with sample data with which to test
#   for each element in list validate with isValidDate() and call dayNumber() with element as parameter
#   print results
#
#   dayNumber():
#       d is date argument in mm/dd/yyyy format
#       verify date to be valid by calling isValidDate(), return -1 if not
#       parse d into month, day, and year variables
#       make them ints
#       use three-step process to compute dayNum
#           dayNum = 31(month - 1) + day
#           if month after Feb, subtract 4(month + 23) // 10
#           if leap year and after 29 Feb, add 1
#       return dayNum


from Chapter07.U07_Ex12_ValidDate import isValidDate
from Chapter07.U07_Ex11_LeapYear import isLeapYear

def main():
    # introduce program
    print('\nThis program contains the function dayNumber() which computes the day number for a given date (mm/dd/yyyy).\n')

    # create a list with sample data with which to test
    dates = ['1/1/1970', '9/31/2000', '2/29/2017', '2/28/2017', '2/29/2000', '12/31/2000', '12/31/1999']

    # for each element in list validate with isValidDate() and call dayNumber() with element as parameter
    for date in dates:
        dayNum = dayNumber(date)
        if dayNum == -1:
            print('{0} is not a valid date.'.format(date))
        else:
            # print results
            print('The day number for {0} is {1}'.format(date, dayNumber(date)))

#   dayNumber():
#       d is date argument in mm/dd/yyyy format
def dayNumber(d):
    # verify date to be valid by calling isValidDate(), return -1 if not
    if not isValidDate(d):
        return -1

    # parse d into month, day, and year variables
    month, day, year = d.split('/')

    # make them ints
    month = int(month); day = int(day); year = int(year)

    # use three-step process to compute dayNum
    # dayNum = 31(month - 1) + day
    dayNum = 31 * (month - 1) + day

    # if month after Feb, subtract 4(month + 23) // 10
    if month > 2:
        dayNum -= (4 * month + 23) // 10

    # if leap year and after 29 Feb, add 1
    if isLeapYear(year) and month > 2:
        dayNum += 1

    # return dayNum
    return dayNum

if __name__ == '__main__':
    main()


'''
RESULTS:
========
dayNumber("1/1/1970")     -->     1 |     1 | [ Pass ]
dayNumber("9/31/2000")    -->    -1 |    -1 | [ Pass ]
dayNumber("2/29/2017")    -->    -1 |    -1 | [ Pass ]
dayNumber("2/28/2017")    -->    59 |    59 | [ Pass ]
dayNumber("2/29/2000")    -->    60 |    60 | [ Pass ]
dayNumber("12/31/2000")   -->   366 |   366 | [ Pass ]
dayNumber("12/31/1999")   -->   365 |   365 | [ Pass ]
========
'''