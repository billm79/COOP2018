# U05_Ex10_AvgWordLen.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 11 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Calculates the average word length in a sentence
#   entered by the user
#
# Algorithm (pseudocode)
#   Print intro
#   Get sentence from user
#   Split sentence into words
#   Accumulate total length of words (stripping non-letters)
#   Divide by number of words to get average word length
#   Print results


def main():
    avgWrdLen = 0

    # Print intro
    print('This program calculates the average word length in a sentence entered by the user.')

    # Get sentence from user
    inputStr = input('Please enter a sentence: ')

    # Split sentence into words
    words = inputStr.split()

    # Accumulate total length of words
    ttlLen = 0
    for word in words:
        word = strip(word)
        # print("[{}]: {}".format(word, len(word)))   # uncomment to see "[word]: len(word)"
        ttlLen += len(word)

    # Divide by number of words to get average word length
        avgWrdLen = ttlLen / len(words)

    # Print results
    print('    Number of words: {0}\nAverage word length: {1:.2f}'.format(len(words), avgWrdLen))
    

def strip(word):
    """
    consider each character of lower case word, adding it to a return value if between 'a' and 'z', inclusive
    :param word: str -> a word
    :return: str -> stripped word
    """
    stripped = ''
    
    for char in word.lower():
        if char >= 'a' and char <= 'z':
            stripped += char
    return stripped


main()