# U05_Ex16_Histogram.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 12 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 16
#     Source: Python Programming
#    Chapter: 5
#
# Program Description
#   Reads numerical data from a file and displays a histogram
#   Data file is created by U05_Ex16_HistogramData.py
#
# Algorithm (pseudocode)
#   Open data file (U05_Ex16_HistogramData.txt) for reading
#   Read data into list using readlines()
#   Close data file
#   Create accumulator list with 11 items [0,0,0,0,0,0,0,0,0,0,0]
#   For each item in data list
#       Increment element of accumulator list corresponding with
#           data point value
#   Create GraphWin (600, 300)
#   Set coordinates based on largest element of accumulator list
#   Draw graph title
#   Draw labels
#   Draw bars
#   Wait for mouse click
#   Close GraphWin


from graphics import *

def main():
    # Open data file (U05_Ex16_HistogramData.txt) for reading
    fileHandle = open('U05_Ex16_HistogramData.txt', 'r')

    # Read data into list using readlines()
    data = fileHandle.readlines()

    #   Close data file
    fileHandle.close()

    # Create accumulator list with 11 items [0,0,0,0,0,0,0,0,0,0,0]
    hist = [0,0,0,0,0,0,0,0,0,0,0]

    # For each item in data list
    for item in data:
        # Increment element of accumulator list corresponding with
        # data point value
        hist[int(item)] += 1

    # Create GraphWin (600, 300)
    win = GraphWin('Quiz Score Histogram', 600, 300)

    # Set coordinates based on largest element of accumulator list
    win.setCoords(-1, -1, 11, max(hist)+2)

    # Draw graph title
    Text(Point(5, max(hist)+1), 'Quiz Score Histogram').draw(win)

    # Draw labels
    # Draw bars
    for i in range(11):
        Text(Point(i, -0.5), i).draw(win)
        Rectangle(Point(i-0.3, 0), Point(i+0.3, hist[i])).draw(win)

    # Wait for mouse click
    win.getMouse()

    # Close GraphWin
    win.close()

main()