# U03_Ex16_Fibbonacci.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 03 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   This program prints a Fibonacci sequence with number of terms given by the user.
#
# Algorithm (pseudocode)
#   Introduce program
#   Get number of terms from user
#   If terms is 1, print 1
#   If terms is 2, print 1 1
#   If terms > 2, compute remaining terms up to `terms`, printing as you go


def main():
    # Introduce program
    print("This program prints a Fibonacci sequence with number of terms given by the user.")

    #   Get number of terms from user
    terms = int(input("How many terms of Fibonacci do you wish to print? "))

    #   If terms is 1, print 1
    if terms == 1:
        print("1")

    #   If terms is 2, print 1 1
    elif terms == 2:
        print("1 1")

    #   If terms > 2, compute remaining terms up to `terms`, printing as you go
    else:
        term1 = 1
        term2 = 1
        print(term1, term2, end='')
        for i in range(2, terms):
            term3 = term1 + term2
            print(' ', term3, end='')
            term1 = term2
            term2 = term3


main()
