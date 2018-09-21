# U07_Ex06_SpeedingTicket.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 23 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 6
#     Source: Python Programming
#    Chapter: 7
#
# Program Description
#   Calculates possible fees for speeding given parameters of speed limit and clocked speed
#
# Algorithm (pseudocode)
#   parameters are speed limit and clocked speed
#   if speed is legal, print legal speed message
#   otherwise, calculate fine(s)
#       base fine is $50
#       add $5 for each mph over the limit
#       add $200 if speed over 90 mph
#       print amount of fine


def checkSpeed(limit, speed):
    # parameters are speed limit and clocked speed
    # if speed is legal, print legal speed message
    if speed <= limit:
        print('\nLimit: {0} mph\t|\tSpeed: {1:0.1f} mph\t|\tStatus: NOT SPEEDING'.format(limit, speed))
    # otherwise, calculate fine(s)
    else:
        # base fine is $50
        fine = 50

        # add $5 for each mph over the limit
        fine += int(speed - limit) * 5

        # add $200 if speed over 90 mph
        if speed > 90:
            fine += 200

        # print amount of fine
        print('\nLimit: {0} mph\t|\tSpeed: {1:0.1f} mph\t|\tStatus: SPEEDING\t|\tFine: ${2:0.2f}'.format(limit, speed, fine))

if __name__ == '__main__':
    limit = int(input('\nEnter the posted speed: '))
    speed = float(input('Enter the clocked speed: '))
    checkSpeed(limit, speed)