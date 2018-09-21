# U03_Ex07_Distance.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 14 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   Calculates the distance between two points entered by user
#
# Algorithm (pseudocode)
#   introduce program
#   get point coordinates from user
#   calculate distance
#       distance = math.sqrt((x2 - x1)** + (y2 - y1)**)
#   display results


import math

def main():
    print("\nThis program calculates the distance between two points.\n")
    print("You will enter the coordinates for two points.\n")
    x1 = float(input("What is the x-coordinate for the first point? "))
    y1 = float(input("What is the y-coordinate for the first point? "))
    x2 = float(input("What is the x-coordinate for the second point? "))
    y2 = float(input("What is the y-coordinate for the second point? "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("\nThe distance between the points ({0}, {1}) and ({2}, {3}) is {4}.".\
          format(x1, y1, x2, y2, distance))

main()
