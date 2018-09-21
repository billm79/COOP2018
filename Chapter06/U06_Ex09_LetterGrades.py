# U06_Ex09_LetterGrades.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 9
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Solve PE 5.3 using function letterGrade()
#   Accepts an exam score as input and prints the corresponding letter grade
#
# Algorithm (pseudocode)
#   introduce program
#   get exam score from user
#   call letterGrade() passing exam score as parameter assign result to grade
#   print letter returned from letterGrade()
#
#   letterGrade():
#       score is argument
#       get index by integer dividing score by 10
#       set grades to 'FFFFFFDCBAA'
#       return letter grade using index to access grades


def main():
    # introduce program
    print('This program converts a numeric grade (0-100) to a letter grade (A,B,C,D,F)\n')

    # get exam score from user
    examGrade = int(input('Please enter the exam grade: '))

    # call letterGrade() passing exam score as parameter assign result to grade
    grade = letterGrade(examGrade)

    # print letter returned from letterGrade()
    print('An exam grade of {0} corresponds to a letter grade of {1}.'.format(examGrade, grade))

# letterGrade():
#     score is argument
def letterGrade(score):
    # get index by integer dividing by 10
    idx = score // 10
    letters = 'F' * 6 + 'DCBAA'
    return letters[idx]

main()