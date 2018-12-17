# U05_Ex06_Numerology_old.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 11 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Determine the "numeric value" of a string of text by assigning
#   each letter a value from 1 to 26 and adding them up.
#
# Algorithm (pseudocode)
#   Print intro
#   Get string input
#   Convert string to lower case
#   For each character
#       Ignore non letters
#       Subtract 96 from its code
#       Accumulate character codes with addition
#   Print results


def main():
    # Print intro
    print('This program determines the "numeric value" of a string of text.')

    # Get string input
    inputStr = input('Please enter a string of text: ')

    # Convert string to lower case
    inputStr = inputStr.lower()

    numVal = 0
    a = 97
    z = 123
    # For each character
    for char in inputStr:
        cCode = ord(char)

        # Ignore non letters
        if cCode >= a and cCode <= z:
            # Subtract 96 from its code
            # Accumulate character codes with addition
            numVal += (cCode - 96)

    #   Print results
    print('The numeric value for\n{0}\nis {1}.'.format(inputStr, numVal))


main()
