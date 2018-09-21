# U05_Ex04_Acronym.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 30 Oct 2017
#     IDE: Pythonista for iOS
#
# Assignment Info
#   Exercise: 4
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Creates an acronym from input text
#
# Algorithm (pseudocode)
#   Print intro
#	 Get text from user
#	 Parse string to get first letter of each word
#	 Output result

def main():
    #   Print intro
    print('This program creates an acronym from input text.')

    #	 Get text from user
    inputStr = input('Please enter a text string consisting of multiple words: ')

    #	 Parse string to get first letter of each word
    words = inputStr.split(' ')
    acronym = ''

    for word in words:
        acronym += word[0].upper()

    # Output result
    print('The acronym for...\n{0}\nis...\n{1}'.format(inputStr, acronym))


main()