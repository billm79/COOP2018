# U05_Ex14_WordCount.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 11 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Displays counts of lines, words, and characters in a file
#
# Algorithm (pseudocode)
#   Print intro
#   Get filename from user
#   Open file for reading
#   Read lines with lines = readlines()
#   Close file
#   Loop through lines, counting words and characters
#   Print results


def main():
    # Print intro
    print('This program displays counts of lines, words, and characters in a file input by the user.')

    # Get filename from user
    fileName = input('Please enter the filename: ')

    # Open file for reading
    fileHandle = open(fileName, 'r')

    # Read lines with lines = readlines()
    lines = fileHandle.readlines()

    # Close file
    fileHandle.close()

    # Loop through lines, counting words and characters
    wordCount = 0
    charCount = 0

    for line in lines:
        words = line.split(' ')
        wordCount += len(words)

        for word in words:
            charCount += len(word)

    # Print results
    print('Lines: {0}\nWords: {1}\nChars: {2}'.format(len(lines), wordCount, charCount))

main()