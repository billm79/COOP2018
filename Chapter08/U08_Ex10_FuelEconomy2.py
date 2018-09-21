# U08_Ex10_FuelEconomy2.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 23 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 10
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Computes the fuel efficiency of a multi-leg journey
#   Data comes from a file.
#       Format: first line is starting odometer reading
#               subsequent lines contain next odometer reading, space, fuel consumption for this leg
#
# Algorithm (pseudocode)
#   introduce program
#   get the data file using askopenfilename from tkinter.filedialog
#   open the file
#   read the first line and store result in odoStart
#   initialize total miles and total fuel consumed to zero
#   read the next line to get the next odometer reading and fuel consumption
#   loop while not eof
#       split read text into odometer reading and fuel consumption
#       print mpg for this leg (current - (start + total miles)) / fuel consumed
#       update total miles with current odometer reading - starting reading
#       update total fuel consumed
#       read the next line to get the next odometer reading and fuel consumption
#   close file
#   print mpg for entire trip (total miles / total fuel)


from tkinter.filedialog import askopenfilename

def main():
    # introduce program
    print('This program computes the fuel efficiency of a multi-leg journey.\n')

    # get the data file using filedialog from tkinter
    dataFile = askopenfilename()

    # open the file
    content = open(dataFile, 'r')

    # read the first line and store result in odoStart
    odoStart = int(content.readline())

    # initialize total miles and total fuel consumed to zero
    milesTtl = 0; fuelTtl = 0

    # read the next line to get the next odometer reading and fuel consumption
    odoFuel = content.readline()

    # loop while not eof
    while odoFuel != '' and len(odoFuel.split()) == 2:
        # split read text into odometer reading and fuel consumption
        strList = odoFuel.split()
        odoNext = int(strList[0])
        fuelNext = int(strList[1])

        # print mpg for this leg (current - (start + total miles)) / fuel consumed
        print('Fuel efficiency for this leg: {:.1f}'.format((odoNext - (odoStart + milesTtl)) / fuelNext))

        # update total miles with current odometer reading - starting reading
        milesTtl = odoNext - odoStart

        # update total fuel consumed
        fuelTtl += fuelNext

        # read the next line to get the next odometer reading and fuel consumption
        odoFuel = content.readline()

    # close file
    content.close()

    # print mpg for entire trip (total miles / total fuel)
    if fuelTtl > 0:
        print('\nFuel efficiency for entire trip: {:.1f}\n'.format(milesTtl / fuelTtl))
    else:
        print('\nInsufficient data was entered.')

if __name__ == '__main__':
    main()
