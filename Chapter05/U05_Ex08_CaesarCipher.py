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
#   main()
#       Print intro
#       Get input string
#       Convert to upper case (arbitrary)
#       Get key (negative decodes)
#       Call methods 1 and 2 to encode/decode using two different methods
#       Print results
#
#   method1(string, key)
#       For each character in string
#           Ignore non letters (pass through unchanged)
#           Calculate code plus key minus 65
#           Add new code mod 26 plus 65 to output string
#       return output string
#
#   method2(string, key)
#       For each character in string
#           Find character in "ABC..XYZ" string, noting its index
#           Ignore non letters (pass through unchanged)
#           Change index by key value
#           Mod new index with 26 to make sure it is in 1..26 range
#           Accumulate to output string
#       return output string
#
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

    outputStr1 = method1(inputStr, key)
    outputStr2 = method2(inputStr, key)

    print('\nMETHOD 1\n'
          ' Input: {0}\n'
          'Output: {1}'.format(inputStr, outputStr1))
    print('\nMETHOD 2\n'
          ' Input: {0}\n'
          'Output: {1}'.format(inputStr, outputStr2))


def method1(inputStr, key):
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
    return outputStr


def method2(inputStr, key):
    outputStr = ''
    abcStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # For each character in string
    for char in inputStr:
        # Find character in "ABC..XYZ" string, noting its index
        idx = abcStr.find(char)

        # Ignore non letters (pass through unchanged)
        if idx == -1:
            # Accumulate to output string
            outputStr += char
        else:
            # Change index by key value
            idx += key

            # Mod new index with 26 to make sure it is in 1..26 range
            idx = idx % 26

            # Accumulate to output string
            outputStr += abcStr[idx]

    # return output string
    return outputStr


main()