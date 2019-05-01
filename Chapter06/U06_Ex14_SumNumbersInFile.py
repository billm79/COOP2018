# U06_Ex14_SumNumbersInFile.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 14
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Computes the sum of the squares of numbers read from a file specified by user.
#   Assumption: data file contains one number per line
#
# Algorithm (pseudocode)
#   introduce program
#   prompt user for filename using askopenfilename from tkinter library
#   open file
#   read contents using readlines()
#   close file
#   convert to list of numbers with call to toNumbers(contents) from U06_Ex13_StrListToNumbers.py (import this)
#   square each item in list with call to squareEach(contents) from U06_Ex11_SquareEachInList.py (import this)
#   sum numbers in list to listSum with call to sumList(contents) from U06_Ex12_SumList.py (import this)
#   print listSum


from tkinter.filedialog import askopenfilename
from U06_Ex13_StrListToNumbers import toNumbers
from U06_Ex11_SquareEachInList import squareEach
from U06_Ex12_SumList import sumList

def main():
    # introduce program
    print('\nThis program computes the sum of the squares of numbers read from a file specified by user.')

    # prompt user for filename using askopenfilename from tkinter library
    fileName = askopenfilename()

    # open file
    file = open(fileName)

    # read contents using readlines()
    contents = file.readlines()

    # close file
    file.close()

    # convert to list of numbers with call to toNumbers(contents) from U06_Ex13_StrListToNumbers.py (import this)
    toNumbers(contents)

    # square each item in list with call to squareEach(contents) from U06_Ex11_SquareEachInList.py (import this)
    squareEach(contents)

    # sum numbers in list to listSum with call to sumList(contents) from U06_Ex12_SumList.py (import this)
    listSum = sumList(contents)

    # print listSum
    print('The sum of the squares of numbers in {0} is {1}.'.format(fileName, listSum))

main()