# slope_of_curve.py
#
# Authors: Bill Montana & Jake Couzens
#  Course: Coding for OOP
# Section: A3
#    Date: 11 Oct 2018
#     IDE: PyCharm Professional
#
# Program Description
#   This program takes user input (equation of curve, x value for point on curve)
#   and determines the slope of the curve at that point.
#
# Algorithm (pseudocode)
#   Introduce program
#   Get equation of curve from user (e.g. 3 * x ^ 2 + 2 * x + 20)
#   Parse equation to get degree and coefficients (expand this)
#   Use a "small" ∆x to get two points on curve bounding point entered by user (expand this)
#   Calculate slope using those two points (slope = (y2 - y1) / (x2 - x1))


def main():
    expr = input("Enter equation: y = ")
    for i in range(len(expr)):
        c = expr[i]
        if c == 'x' and i != 0:
            x_loc = i

            # find coefficient
            j = x_loc
            while j > 0:
                # if this character is an operator, stop looking for coefficient
                if is_contained_in(expr[j-1], ['+', '-']):
                    break
                print(j-1, expr[j-1])
                j -= 1


def is_contained_in(char, str_list):
    for c in str_list:
        if char == c:
            return True
    return False


main()
