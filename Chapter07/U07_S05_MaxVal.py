# U07_S05_MaxVal.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: Section 5 example
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Prints max value of three input by user
#
# Algorithm (pseudocode)
#   get three numbers from user (x1, x2, x3)
#   compare x1, x2
#       compare greater to x3, set maxVal to result
#   print maxVal
#   


def main():
    x1, x2, x3 = eval(input('Please enter three values: '))

    if x1 >= x2:
        if x1 >= x3:
            maxVal = x1
        else:
            maxVal = x3
    elif x2 >= x3:
        maxVal = x2
    else:
        maxVal = x3

    print('The largest value is', maxVal)

main()