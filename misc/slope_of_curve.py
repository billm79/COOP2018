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
    print("\nThis program will find the slope of a curve at a point. The equation may be entered")
    print("as it would be written, with a few exceptions. There are no implicit operations.")
    print("For example, multiplication (e.g. 2x) must be specified using an asterisk (e.g. 2*x).")
    print("Exponentiation is indicated using the caret symbol, ^ (e.g. x squared is x^2).")
    print("Do not enter 'y='.\n")
    expr = input("Enter equation: y = ")
    print(expr)     # debug

    # remove spaces
    expr = remove_spaces(expr)
    print(expr)     # debug

    # debug--begin: print position numbers below expr to help debugging
    for i in range(len(expr)):
        print('0' if i < 10 else '1', end='')
    print()
    for i in range(len(expr)):
        print(i % 10, end='')
    print()
    # debug--end

    # determine coefficients and exponents
    for i in range(len(expr)):
        # consider a single character in expr
        c = expr[i]

        # if 'x' is found, find coefficient and exponent
        if c == 'x' and i != 0:                             # 'x' found
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


def remove_spaces(s):
    ret_str = ''
    for c in s:
        if c != ' ':
            ret_str += c
    return ret_str


main()
