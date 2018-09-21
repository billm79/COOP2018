# U05_Ex16_HistogramData.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 12 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Populates a data file for use with U05_Ex16_Histogram.py
#   Each of 100 lines contains an integer from zero to ten.
#
# Algorithm (pseudocode)
#   Open file for writing
#   Each of 100 times
#       Write a random number between 0 & 10, inclusive, and \n
#   Close file

import random

def main():
    file = open('U05_Ex16_HistogramData.txt', 'w')
    for i in range(100):
        file.write(str(random.randint(0, 10)) + '\n')
    file.close()

if __name__ == '__main__':
    main()