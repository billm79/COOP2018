# U07_Ex03_LetterGrades.py
#
#  Author: 
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 
#     Source: Python Programming
#    Chapter: 
#
# Program Description
#   Accepts an exam score as input and prints the corresponding letter grade.
#   Uses a decision structure.
#
# Algorithm (pseudocode)
#   introduce program
#   get exam score from user
#   call letterGrade() passing exam score as parameter assign result to grade
#   print letter returned from letterGrade()
#
#   letterGrade():
#       score is argument
#       if score is >= 89.5, letter grade is A
#       if score is >= 79.5, letter grade is B
#       if score is >= 69.5, letter grade is C
#       if score is >= 59.5, letter grade is D
#       else, letter grade is F


def main():
    # introduce program
    print('\nThis program converts a numeric grade (0-100) to a letter grade (A,B,C,D,F)\n')

    # get exam score from user
    examGrade = float(input('\nPlease enter the exam grade: '))

    # call letterGrade() passing exam score as parameter assign result to grade
    grade = letterGrade(examGrade)

    # print letter returned from letterGrade()
    print('\nAn exam grade of {0} corresponds to a letter grade of {1}.'.format(examGrade, grade))

# letterGrade():
#     score is argument
def letterGrade(score):
    letter = 'F'
    if score >= 89.5:
        letter = 'A'
    elif score >= 79.5:
        letter = 'B'
    elif score >= 69.5:
        letter = 'C'
    elif score >= 59.5:
        letter = 'D'
    return letter

main()