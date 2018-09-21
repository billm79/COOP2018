# U03_Ex06_Slope.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 14 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   Calculates the slope of a line, given two points entered by user
#
# Algorithm (pseudocode)
#   introduce program
#   get point coordinates from user
#   calculate slope
#       slope = (y2 - y1) / (x2 - x1)
#   display results


def main():
    print("\nThis program calculates the slope of a line, given two points.\n")
    print("You will enter the coordinates for two points on a line.\n")
    x1 = float(input("What is the x-coordinate for the first point? "))
    y1 = float(input("What is the y-coordinate for the first point? "))
    x2 = float(input("What is the x-coordinate for the second point? "))
    y2 = float(input("What is the y-coordinate for the second point? "))
    slope = (y2 - y1) / (x2 - x1)
    print("\nThe slope of a line containing the points ({0}, {1}) and ({2}, {3}) is {4}.".\
          format(x1, y1, x2, y2, slope))

main()