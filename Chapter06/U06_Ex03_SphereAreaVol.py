# U06_Ex03_SphereAreaVol.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Solve PE 3.1 using functions sphereArea() and sphereVolume()
#   Calculates the volume and surface area of a sphere from its radius,
#   given as input.
#
# Algorithm (pseudocode)
#   introduce program
#   get radius (float) from user
#   get units (str) for radius
#   call sphereArea() with radius as parameter; assign to area var
#   call sphereVolume() with radius as parameter; assign to volume var
#   display results
#
#   sphereArea()
#       r is argument
#       calculate and return surface area
#          A = 4 * math.pi * r*r
#
#   sphereVolume()
#       r is argument
#       calculate volume and surface area
#           V = 4 / 3 * math.pi * r*r*r




import math

def main():
    # introduce program
    print("\nThis program calculates the volume and surface area of a sphere.\n")

    # get radius (float) from user
    radius = float(input("What is the sphere's radius? "))

    # get units (str) for radius
    units = str(input("What are the units for the radius? "))

    # call sphereArea() with radius as parameter; assign to area var
    area = sphereArea(radius)

    # call sphereVolume() with radius as parameter; assign to volume var
    volume = sphereVolume(radius)

    # display results
    print(("\nA sphere with radius {0:.3f} " + units + " has a volume of {1:.3f} cubic " + \
            units + " and a surface area of {2:.3f} square " + units + ".").format(radius, volume, area))

# sphereArea()
#     r is argument
def sphereArea(r):
    # calculate and return surface area
    #   A = 4 * math.pi * r*r
    area = 4 * math.pi * math.pow(r, 2)
    return area

# sphereVolume()
#     r is argument
def sphereVolume(r):
    # calculate volume and surface area
    #     V = 4 / 3 * math.pi * r*r*r
    volume = 4 / 3 * math.pi * math.pow(r, 3)
    return volume

main()