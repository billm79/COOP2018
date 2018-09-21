# U05_Ex03_GradingScale.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 30 Oct 2017
#     IDE: Pythonista for iOS
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Accepts an exam score as input and prints the corresponding letter grade
#
# Algorithm (pseudocode)
#   Print intro
#	 Get exam score from user
#	 Get index by integer dividing by 10
#	 Print letter grade using index

def main():
    #   Print intro
    print('This program converts a numeric grade (0-100) to a letter grade (A,B,C,D,F)\n')

    #	 Get exam score from user
    examGrade = int(input('Please enter the exam grade: '))

    #	 Get index by integer dividing by 10
    idx = examGrade // 10
    # letters = ['F'*6, 'D', 'C', 'B', 'A']
    letters = 'F' * 6 + 'DCBAA'

    #	 Print letter grade using index
    print('An exam grade of {0} corresponds to a letter grade of {1}.'.format(examGrade, letters[idx]))


main()