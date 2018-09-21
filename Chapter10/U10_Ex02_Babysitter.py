# U10_Ex02_Babysitter.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 2
#     Source: Python Programming
#    Chapter: 10
#
# Program Description
#   Calculates babysitting bill based on hourly rates, start time, and end time.
#   Times are given in hh:mm 24-hour format. Partial hours are prorated.
#
#   Added GUI for Unit 10
#
# Algorithm (pseudocode)
#   earlyRate and lateRate are parameters
#   introduce program
#   get start time and end time from user (hh:mm 24-hour format)
#   parse into hour and minute variables for start and end
#   apply hourly rate of $2.50 for time before 21:00, prorate partial hours
#   apply hourly rate of $1.75 for time after 21:00, prorate partial hours
#   print resulting babysitting bill


from graphics import *
from button import Button

def main():
    win = GraphWin("Babysitter Payment Calculator", 600, 300)
    win.setCoords(0, 0, 100, 100)
    # introduce program
    msg = Text(Point(50, 50), 'This program calculates babysitting bill based on hourly rates, start time, and end time.')
    msg.draw(win)
    msg2 = Text(Point(50, 10), 'Click to dismiss')
    msg2.draw(win)
    win.getMouse()
    msg.undraw(); msg2.undraw()

    # get start time and end time from user (hh:mm 24-hour format)
    # make Text, Entry, and Button objects ahead of while loop
    startMsg = Text(Point(40, 70), "What time did the babysitter arrive? (hh:mm 24-hr)")
    endMsg = Text(Point(40, 50), " What time did the babysitter leave? (hh:mm 24-hr)")
    startBox = Entry(Point(70, 70), 7)
    endBox = Entry(Point(70, 50), 7)

    # draw prompts and entry fields
    startMsg.draw(win); endMsg.draw(win)
    endBox.draw(win); startBox.draw(win)

    # create buttons
    calcButton = Button(win, Point(34, 33), Point(48, 27), 'Calculate')
    quitButton = Button(win, Point(52, 33), Point(66, 27), 'Quit')
    calcButton.activate()
    quitButton.activate()

    # initialize pt as a valid Point object so the while loop doesn't blow up
    pt = Point(0, 0)

    while not quitButton.clicked(pt):
        if calcButton.clicked(pt):
            # undraw input objects
            startMsg.undraw(); endMsg.undraw()
            endBox.undraw(); startBox.undraw()

            # call output
            output(win, sitterBill(2.5, 1.75, str(startBox.getText()), str(endBox.getText())))

            # redraw input objects
            startMsg.draw(win); endMsg.draw(win)
            endBox.draw(win); startBox.draw(win)
        elif quitButton.clicked(pt):
            break
        pt = win.getMouse()     # changed this from checkMouse() after class


def sitterBill(earlyRate, lateRate, start, end):
    # earlyRate and lateRate are parameters
    # parse into hour and minute variables for start and end
    startTime = start.split(':'); startNum = float(startTime[0]) + float(startTime[1]) / 60
    endTime = end.split(':'); endNum = float(endTime[0]) + float(endTime[1]) / 60

    # apply hourly rate of $2.50 for time before 21:00, prorate partial hours
    if startNum < 21 and endNum < 21:
        sitterBillAmt = (endNum - startNum) * earlyRate
    # apply hourly rate of $1.75 for time after 21:00, prorate partial hours
    elif startNum >= 21 and endNum >= 21:
        sitterBillAmt = (endNum - startNum) * lateRate
    else:
        sitterBillAmt = (21 - startNum) * earlyRate + (endNum - 21) * lateRate
    return sitterBillAmt


def output(win, sitterBillAmt):
    # print resulting babysitting bill

    # create a 'dialog box'
    rect = Rectangle(Point(30, 45), Point(70, 25))
    rect.setWidth(1)
    rect.setOutline('black')
    rect.setFill('white')
    rect.draw(win)

    # make it look like a window (-ish)
    titlebar = Rectangle(Point(30, 52), Point(70, 45))
    titlebar.setFill('grey')
    titlebar.setOutline('black')
    titlebar.setWidth(1)
    titlebar.draw(win)
    title = Text(Point(50, 48), 'Payment')
    title.draw(win)
    msg = Text(Point(50, 35), 'Total babysitting bill is ${0:0.2f}.'.format(sitterBillAmt))
    msg.draw(win)
    msg2 = Text(Point(50, 10), 'Click to dismiss')
    msg2.draw(win)
    win.getMouse()

    # undraw 'dialog box' after mouse click
    msg.undraw(); msg2.undraw(); rect.undraw(); titlebar.undraw(); title.undraw()


if __name__ == '__main__':
    main()