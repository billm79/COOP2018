# U03_Ex15_ApproxPI.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 14 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   Approximates PI with the finite series 4/1 - 4/3 + 4/5 - 4/7 + ... + 4/(2n-1) * (-1)**(n-1),
#   where n is the current term in the sequence
#
# Algorithm (pseudocode)
#   introduce program
#   get number of terms to sum from user
#   initialize approxPI to zero
#       approxPI = 0
#   in a loop from 1 to n
#       add current term to approxPI
#           approxPI += 4 / (2n-1)
#   calculate difference between approxPI and math.pi
#       diff = math.pi - approxPI
#   display results


import math

def main():
    print("\nThis program approximates PI with the finite series",
          "\n4/1 - 4/3 + 4/5 - 4/7 + ... + 4/(2n-1) * (-1)**(n-1), \nwhere n is the current",
          "term in the sequence\n")
    n = int(input("How many terms of the sequence do you wish to include? "))
    approxPI = 0
    for i in range(1, n+1):
        currentTerm = 4 / (2*i-1) * (-1)**(i-1)
#        print(currentTerm)
        approxPI += currentTerm
    diff = math.pi - approxPI
    print("\nThe approximate value of PI, with {0} terms in the sequence is {1}.".format(n, approxPI))
    print("This differs from the value of math.pi by {0}".format(diff))

main()
