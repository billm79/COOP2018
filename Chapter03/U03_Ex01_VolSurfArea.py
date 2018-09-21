# U03_Ex01_VolSurfArea.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 14 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   Calculates the volume and surface area of a sphere from its radius,
#   given as input.
#
# Algorithm (pseudocode)
#   introduce program
#   get radius (float) from user
#   get units (str) for radius
#   calculate volume and surface area
#       V = 4 / 3 * math.pi * r*r*r
#       A = 4 * math.pi * r*r
#   display results


import math

def main():
    print("\nThis program calculates the volume and surface area of a sphere.\n")
    radius = float(input("What is the sphere's radius? "))
    units = str(input("What are the units for the radius? "))
    volume = 4 / 3 * math.pi * math.pow(radius, 3)
    area = 4 * math.pi * math.pow(radius, 2)
    print(("\nA sphere with radius {0:.3f} " + units + " has a volume of {1:.3f} cubic " + \
            units + " and a surface area of {2:.3f} square " + units + ".").format(radius, volume, area))

main()