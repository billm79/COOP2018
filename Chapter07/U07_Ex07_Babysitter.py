# U07_Ex07_Babysitter.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Calculates babysitting bill based on hourly rates, start time, and end time.
#   Times are given in hh:mm 24-hour format. Partial hours are prorated.
#
# Algorithm (pseudocode)
#   earlyRate and lateRate are parameters
#   introduce program
#   get start time and end time from user (hh:mm 24-hour format)
#   parse into hour and minute variables for start and end
#   apply hourly rate of $2.50 for time before 21:00, prorate partial hours
#   apply hourly rate of $1.75 for time after 21:00, prorate partial hours
#   print resulting babysitting bill

EARLY_RATE = 2.5
LATE_RATE  = 1.75


def main():
    # introduce program
    print('\nThis program calculates babysitting bill based on hourly rates, start time, and end time.')

    # get start time and end time from user (hh:mm 24-hour format)
    start = input('\nWhat time did the babysitter arrive? (hh:mm 24-hr) ')
    end = input('What time did the babysitter leave? (hh:mm 24-hr) ')

    sitterBillAmt = sitterBill(start, end)

    # print resulting babysitting bill
    print('\nTotal babysitting bill is ${0:0.2f}.'.format(sitterBillAmt))


def sitterBill(start, end):
    # earlyRate and lateRate are parameters
    # parse into hour and minute variables for start and end
    startTime = start.split(':'); startNum = float(startTime[0]) + float(startTime[1]) / 60
    endTime = end.split(':'); endNum = float(endTime[0]) + float(endTime[1]) / 60

    # apply hourly rate of $2.50 for time before 21:00, prorate partial hours
    if startNum < 21 and endNum < 21:
        sitterBillAmt = (endNum - startNum) * EARLY_RATE
    # apply hourly rate of $1.75 for time after 21:00, prorate partial hours
    elif startNum >= 21 and endNum >= 21:
        sitterBillAmt = (endNum - startNum) * LATE_RATE
    else:
        sitterBillAmt = (21 - startNum) * EARLY_RATE + (endNum - 21) * LATE_RATE

    return sitterBillAmt


if __name__ == '__main__':
    main()


'''
RESULTS:
========
sitterBill("18:00", "20:00")   -->   5.0 |   5.0 | [ Pass ]
sitterBill("19:00", "21:00")   -->   5.0 |   5.0 | [ Pass ]
sitterBill("19:00", "23:00")   -->   8.5 |   8.5 | [ Pass ]
sitterBill("21:00", "23:00")   -->   3.5 |   3.5 | [ Pass ]
========
'''