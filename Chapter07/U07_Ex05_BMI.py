# U07_Ex05_BMI.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Calculates BMI given weight in pounds and height in inches.
#   Prints message telling whether BMI is above, within, or below healthy range.
#
# Algorithm (pseudocode)
#   introduce program
#   get weight and height from user
#   calculate BMI: weight * 720 / height**2
#   set status based on BMI
#   print status of above, within, or below healthy range (19-25, inclusive)


def main():
    # introduce program
    print('\nThis program calculates BMI given weight in pounds and height in inches.')
    print(' BMI Status is printed for above, within, or below healthy range (19-25)')

    # get weight and height from user
    weight = float(input('\nEnter weight in pounds: '))
    height = float(input('Enter height in inches: '))

    # calculate BMI: weight * 720 / height**2
    bmi = weight * 720 / height ** 2

    # set status based on BMI
    status = 'below'
    if bmi > 25:
        status = 'above'
    elif bmi >= 19:
        status = 'within'

    # print status of above, within, or below healthy range (19-25, inclusive)
    print('\nThe BMI for a weight of {0} pounds and height of {1} inches is {2:0.2f}'.format(weight, height, bmi))
    print('This is {0} the normal range of 19 - 25.'.format(status))

main()