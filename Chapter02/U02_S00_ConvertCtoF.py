# U02_S00_ConvertCtoF.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Aug 2018
#  Edited: 5 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: Sample 0
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program converts temperature from Celsius to Fahrenheit.
#
# Algorithm (pseudocode)
#   Print program introduction
#   Get °C from user and assign to celsius
#   Calculate °F using 9/5 * °C + 32 and assign to fahrenheit
#   Print °F
#   ...and we're done!


def main():
    # Print program introduction
    print("This program converts temperature from Celsius to Fahrenheit.")

    #   Get °C from user and assign to celsius
    celsius = eval(input("Enter °C to convert: "))

    #   Calculate °F using 9/5 * °C + 32 and assign to fahrenheit
    fahrenheit = 9 / 5 * celsius + 32

    #   Print °F
    print(celsius, "°C is equivalent to", fahrenheit, "°F")


main()
