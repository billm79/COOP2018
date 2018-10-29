# U03_Ex17_SquareRoot.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 25 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   This program computes the square root of a user-specified number using Newton's method.
#   Newton's method for calculating next guess: next_guess = (guess + x / guess) / 2
#
# Algorithm (pseudocode)
#   Introduce program
#   Get number to find the square root of from user (num)
#   Get number of guesses from user (guesses)
#   Start with guess = num / 2
#   Loop guesses times
#       Calculate next guess using: guess = (guess + x / guess) / 2
#   Print value of guess and difference between guess and math.sqrt()


from math import sqrt


def main():
    # Introduce program
    print("\nThis program computes the square root of a user-specified number using Newton's method.")
    print("Newton's method for calculating next guess: next_guess = (guess + x / guess) / 2")

    #   Get number to find the square root of from user (num)
    num = float(input("\nEnter the number for which you wish to calculate the square root: "))

    #   Get number of guesses from user (guesses)
    guesses = int(input("How many guesses do you want to use in the calculation? "))

    #   Start with guess = num / 2
    guess = num / 2

    #   Loop guesses times
    for i in range(guesses):
        #   Calculate next guess using: guess = (guess + x / guess) / 2
        guess = (guess + num / guess) / 2

    #   Print value of guess and difference between guess and math.sqrt()
    print("\nThe calculated square root of {} using Newton's method with {} guesses is {}.".format(num, guesses, guess))
    print("The square root calculated using math.sqrt() is {}.".format(sqrt(num)))
    print("These differ by {}.".format(abs(sqrt(num) - guess)))


main()
