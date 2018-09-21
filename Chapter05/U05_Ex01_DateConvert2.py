# U05_Ex01_DateConvert2.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 30 Oct 2017
#     IDE: Pythonista for iOS
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Redo dateconvert2.py using string formatting
#
# Algorithm (pseudocode)
#
#

def main():
    # get date
    dateStr = input('Enter a date (mm/dd/yyyy): ')

    # split into components
    monthStr, dayStr, yearStr = dateStr.split('/')

    # convert monthStr to the month name
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', ' September', 'October', 'November', 'December']

    monthStr = months[int(monthStr) - 1]

    # output result in month day, year format
    print('The converted date is {0} {1}, {2}'.format(monthStr, dayStr, yearStr))


main()
