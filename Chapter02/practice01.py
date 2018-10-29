# practice01.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 01 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 2
#
# Program Description
#   This program converts Joules to Calories
#
# Algorithm (pseudocode)
#   Introduce program
#   Loop until exit requested
#       Get input: Joules (0 to quit)
#       Text for exit condition (break if true)
#       Convert Joules to Calories (1 J = 0.239 Cal)
#           calories = joules * 0.239
#       Print result


def main():
    # Introduce program
    print("\nThis program converts Joules to Calories.")

    # Loop until exit requested
    while True:
        #   Get input: Joules (0 to quit)
        joules = float(input("\nPlease enter the number of Joules to convert to Calories (0 to quit): "))

        # Text for exit condition (break if true)
        if joules == 0:
            break

        #   Convert Joules to Calories (1 J = 0.239 Cal)
        #       calories = joules * 0.239
        calories = joules * 0.239

        #   Print result
        print("\n", joules, "Joules is equivalent to", calories, "Calories.")


main()
