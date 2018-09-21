# U04_Ex06_FutureValue_graph.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 28 Sep 2017
#     IDE: PyCharm Community Edition200
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 4
#
# Program Description
#   Graphical future value program from 4.6 with graphical input using Entry objects
#
# Algorithm (pseudocode)
#   Move introduction and inputs to just after creation of GraphWin
#       as Text and Entry objects
#   Get mouse click after data entry
#   Clear window before drawing graph
#   Get mouse click before closing window


from graphics import *

def main():
    ''' REPLACED BY GRAPHICAL INPUTS BELOW
        # Introduction
        print("This program plots the growth of a 10-year investment.")

        # Get principal and interest rate
        principal = float(input("Enter the initial principal: "))
        apr = float(input("Enter the annulized interest rate: "))
    '''
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")


    # ===================== ADDED CODE =====================

    win.setCoords(0, 0, 10, 10)     # coordinates for text entry -- NEW

    # Introduction -- NEW
    msgIntro = Text(Point(5, 8), "This program plots the growth of a 10-year investment.")
    msgIntro.draw(win)

    # Get principal and interest rate -- NEW
    msgPrincipal = Text(Point(3, 5), "Enter the initial principal: ")
    msgPrincipal.draw(win)

    inputPrincipal = Entry(Point(8, 5), 10)
    inputPrincipal.setText("0.0")
    inputPrincipal.draw(win)

    msgRate = Text(Point(3, 3), "Enter the annualized interest rate: ")
    msgRate.draw(win)

    inputRate = Entry(Point(8, 3), 10)
    inputRate.setText("0.0")
    inputRate.draw(win)

    # Click mouse after data entry -- NEW
    win.getMouse()

    # Set principal and apr to inputs -- NEW
    principal = float(inputPrincipal.getText())
    apr = float(inputRate.getText())

    # Clear text and entry fields -- NEW
    msgIntro.undraw()
    msgPrincipal.undraw()
    msgRate.undraw()
    inputPrincipal.undraw()
    inputRate.undraw()

    # ======================================================


    # Original code to draw graph
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    # input("Press <Enter> to quit.")       # REPLACED WITH getMouse()

    # Click mouse after data entry
    win.getMouse()
    win.close()

main()