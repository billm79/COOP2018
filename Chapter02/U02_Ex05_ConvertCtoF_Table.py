# U02_Ex05_ConvertCtoF_Table.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 18 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   Computes and prints a table of Celsius temperatures and the Fahrenheit equivalents from 0°C to 100°C
#
# Algorithm (pseudocode)
#   introduce program
#   print table headings
#   loop from 0 to 100 in increments of 10
#       calculate °F from loop variable (°C)
#       print results in table


def main():
    print('This program computes and prints a table of Celsius temperatures and the Fahrenheit equivalents from 0°C to 100°C.')
    print('\n{:^3}\t{:^5}'.format('°C', '°F'))
    print('{:^3}\t{:^5}'.format('---', '-----'))
    for celsius in range(0, 101, 10):
        fahrenheit = 1.8 * celsius + 32
        print('{:>3}\t{:>5.1f}'.format(celsius, fahrenheit))

main()