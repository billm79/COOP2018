# U03_Ex14_AvgNums.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 14 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   Calculate the average of a series of numbers entered by the user
#
# Algorithm (pseudocode)
#   introduce program
#   get from user how many numbers to average (count)
#   initialize total to zero
#       total = 0
#   loop the number of times previously specified by user
#       get next number from user
#       add this number to total
#   calculate average
#       avg = total / count
#   display results


def main():
    print("\nThis program calculates the average of several numbers entered by user.\n")
    count = int(input("How many numbers do you wish to average? "))
    total = 0
    print()
    for i in range(count):
        nextNum = float(input("Please enter next number to include in average: "))
        total += nextNum
    avg = total / count
    print("\nThe average of the numbers entered is {0}".format(avg))

main()
