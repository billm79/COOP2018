# U05_Ex15_ExamScoresGraph.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 12 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Plots a horizontal bar graph of student exam scores
#   from an input file. Graph size is determined by
#   number of students.
#
#   File format:
#       line 1     : number of students
#       lines 2-...: student last name followed by exam score
#
#   Sample data:
#       4
#       Computewell 96
#       Dibblebit 66
#       Jones 88
#       Smith 77
#
# Algorithm (pseudocode)
#   Print intro
#   Get input file name from user
#   Open file for reading
#   Read line one to get number of students
#   Read subsequent lines to get names and scores (store in list)
#   Close file
#   Create GraphWin sized vertically to accommodate number of students
#       Horizontal size is fixed
#   Set coordinates to something like (-55, 0, 105, y), where y
#       depends on number of students
#   In a loop, output student names and bars
#   Wait for mouse click
#   Close GraphWin


from graphics import *

def main():
    # Print intro
    print('This program plots a horizontal bar graph of\n',
          'student exam scores from an input file. Graph\n',
          'size is determined by number of students.')

    # Get input file name from user
    fileName = input('Please enter the filename: ')

    # Open file for reading
    fileHandle = open(fileName, 'r')

    # Read line one to get number of students
    numStudents = int(fileHandle.readline())

    # Read subsequent lines to get names and scores (store in list)
    scores = fileHandle.readlines()     # starts after last readline()

    # print('{0}\n{1}'.format(numStudents, scores))     # debug

    # Close file
    fileHandle.close()

    # Create GraphWin sized vertically to accommodate number of students
    #     Horizontal size is fixed
    winHt = 40 + numStudents * 20
    win = GraphWin('Exam Scores', 400, winHt)

    # Set coordinates to something like (-55, 0, 105, y), where y
    #     depends on number of students
    win.setCoords(-55, 0, 105, numStudents+2)  # +2 for title

    # Print graph title
    Text(Point(25, numStudents+1.5), 'Exam Scores').draw(win)

    # In a loop, output student names and bars
    for i in range(len(scores)):
        student = scores[i].split(' ')  # get name and score for this student
        Text(Point(-25, i+1), student[0]).draw(win)
        Rectangle(Point(0, i+0.6), Point(student[1], i+1.4)).draw(win)

    # Wait for mouse click
    win.getMouse()

    # Close GraphWin
    win.close()

main()