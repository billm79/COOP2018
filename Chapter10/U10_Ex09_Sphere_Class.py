"""
U10_Ex09_Sphere_Class.py

  Author: Bill Montana
  Course: Coding for OOP
 Section: A2
    Date: 2019-05-01
     IDE: PyCharm
     
Assignment Info
  Exercise: 09
    Source: Python Programming
   Chapter: 10
   
Program Description
    Sphere class with methods to get the radius, surface area, and volume of a sphere

Algorithm
    program introduction
    get inputs from user (radius, units)
    create Sphere object with given radius
    print results using methods of Sphere
"""

import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * math.pow(self.radius, 2)

    def volume(self):
        return 4 / 3 * math.pi * math.pow(self.radius, 3)


def main():
    print("\nThis program calculates the volume and surface area of a sphere.\n")
    radius = float(input("What is the sphere's radius? "))
    units = str(input("What are the units for the radius? "))
    mySphere = Sphere(radius)
    print(("\nA sphere with radius {r:.3f} {u} has a volume of {v:.3f} "\
           "cubic {u} and a surface area of {a:.3f} square {u}.").
          format(r=mySphere.getRadius(), v=mySphere.volume(), a=mySphere.surfaceArea(), u=units))


if __name__ == '__main__':
    main()
