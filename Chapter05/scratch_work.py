# scratch_work.py
#
#  Author: 
#  Course: Coding for OOP
# Section: A3
#    Date: 13 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 
#     Source: Python Programming
#    Chapter: 
#
# Program Description
#   Displays line count, word count, and character count
#   for a file input from user
#   
#
# Algorithm (pseudocode)
#   Print info
#   Get filename from user
#   Open file for reading
#   Read contents into variable using read()
#   Close file
#   Split by lines and return length of list for line count
#   Split by words and return length of list for word count
#   Strip line breaks in content and return resulting string
#       length for character count
#   Display results

def main():
    # Print info
    print('This program displays line count, word count, and character count for a file input from the user.')

    # Get filename from user
    fileName = input('Please enter the name of a file to process: ')

    # Open file for reading
    fileH = open(fileName, 'r')

    # Read contents into variable using read()
    content = fileH.read()

    #   Close file
    fileH.close()

    # Split by lines and return length of list for line count
    lines = len(content.splitlines())

    # Split by words and return length of list for word count
    words = len(content.split())

    # Strip line breaks in content and return resulting string
    #     length for character count
    chars = len(content)

    # Display results
    print('Totals for {0}:\nLines: {1}\nWords: {2}\nChars: {3}'.format(fileName, lines, words, chars))

main()