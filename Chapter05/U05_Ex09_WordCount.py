# U05_Ex09_WordCount.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 11 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Counts the number of words in a sentence entered by the user
#
# Algorithm (pseudocode)
#   Print intro
#   Get sentence from user
#   Count words with len(str.split(' '))
#   Print word count


def main():
    #   Print intro
    print('This program counts the number of words in a sentence entered by the user.')

    #   Get sentence from user
    inputStr = input('Please enter a sentence: ')

    #   Count words with len(str.split(' '))
    wordCount = len(inputStr.split(' '))

    #   Print word count
    print('Word count: {0}'.format(wordCount))

main()