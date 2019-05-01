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


DEBUG = False


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
    method1(lines)
    method2(lines)


def method1(lines):
    print("METHOD 1\n--------")
    # Loop through lines, counting words and characters
    wordCount = 0
    charCount = 0

    for line in lines:
        words = line.split(' ')
        wordCount += len(words)

        for word in words:
            if DEBUG:
                print('|', end='')
                print(word.strip('\n'), end='')
                if len(word.strip('\n')) == 0:
                    for char in word:
                        print(ord(char), end='')
            charCount += len(word.strip('\n'))
        if DEBUG:
            print('|')

    # Print results
    print('Lines: {0}\nWords: {1}\nChars: {2}'.format(len(lines), wordCount, charCount))


def method2(lines):
    print("\n\nMETHOD 2\n--------")
    # Loop through lines, counting words and characters
    wordCount = 0
    charCount = 0
    lineCount = 0

    for line in lines:
        lineCount += 1
        for word in line.split():
            wordCount += 1
            if DEBUG:
                print('|', end='')
            for char in word.strip('\n'):
                if DEBUG:
                    print(char, end='')
                charCount += 1
        if DEBUG:
            print('|')

    # Print results
    print('Lines: {0}\nWords: {1}\nChars: {2}'.format(len(lines), wordCount, charCount))


main()