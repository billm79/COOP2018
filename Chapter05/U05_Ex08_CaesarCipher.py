# U05_Ex08_CaesarCipher.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 11 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 8
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Encode and decode Caesar ciphers
#
# Algorithm (pseudocode)
#   Print intro
#   Get input string
#   Convert to upper case (arbitrary)
#   Get key (negative decodes)
#   
#   New Encode/Decode:
#       For each character
#           Calculate code plus key minus 65
#           Add new code mod 26 plus 65 to output string
#
#   Print results
#
# OLD CODE...
#   Encode:
#       For each character
#           Calculate code plus key
#           If new code exceeds letter Z
#               Wrap around to beginning
#           Add new code to output string
#
#   Decode:
#       For each character
#           Calculate code plus -1*key
#           If new code precedes letter A
#               Wrap around to end
#           Add new code to output string


def main():
    # Print intro
    print('This program encodes & decodes Caesar ciphers.')

    # Get input string
    inputStr = input('Please enter a string to encode: ')

    # Convert to upper case (arbitrary)
    inputStr = inputStr.upper()

    # Get key (Negative decodes)
    key = int(input('Please enter the offset key (negative decodes): '))

    outputStr = ''
    # For each character
    for char in inputStr:
        # If char is a letter...
        if char >= 'a' and char <= 'z' or \
           char >= 'A' and char <= 'Z':

            # Calculate code plus key minus 65
            newCode = ord(char) + key - 65      # offsets by key, then subtracts
                                                # ord('A') so mod can be used below

            # Add new code mod 26 plus 65 to output string
            outputStr += chr(newCode % 26 + 65) # uses mod to find position relative
                                                # to zero (beginning of alphabet),
                                                # then adds ord('A') and converts
                                                # back to letter
        # add space, ignore others
        elif char == ' ':
            outputStr += char

    print(' Input: {0}\n'
          'Output: {1}'.format(inputStr, outputStr))

main()