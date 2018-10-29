# practice02.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 01 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program is an interactive calculator that accepts mathematical expressions.
#
# Algorithm (pseudocode)
#   Introduce program
#   Loop until exit requested
#      Get input (mathematical expression; 0 to quit)
#      Test for exit
#      Evaluate mathematical expression
#      Print result
#   


def main():
    #   Introduce program
    print("This program is an interactive calculator that accepts mathematical expressions.")

    #   Loop until exit requested
    while True:
        #      Get input (mathematical expression; 0 to quit)
        expr = input("Please enter a mathematical expression to evaluate (0 to quit): ")

        #      Test for exit
        if expr == "0":
            break

        #      Evaluate mathematical expression
        result = eval(expr)

        #      Print result
        print('The expression {} is equivalent to {:>6.2f}'.format(expr, result))


main()
