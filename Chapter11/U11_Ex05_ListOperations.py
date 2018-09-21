# U11_Ex05_ListOperations.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 20 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 5
#     Source: Python Programming
#    Chapter: 11
#
# Program Description
#   Algorithms and code for these Python List operations:
#       myList.count(), x in myList, myList.index(), myList.reverse(), myList.sort()
#
# Algorithm (pseudocode)
#   count(myList, x) (like myList.count(x)):
#       set accumulator to zero
#       iterate over myList
#           if an element is the same as x, increment an accumulator
#       return the accumulator
#   
#   isin(myList, x) (like x in myList):
#       set return value to false
#       iterate over myList
#           if an element of myList is found that is the same as x
#               set return value to true
#               exit loop
#       return return value
#
#   index(myList, x) (like myList.index(x)):
#       set return value to -1
#       iterate over myList
#           if an element of myList is found that is the same as x
#               set return value to its index
#               exit loop
#       return return value
#
#   reverse(myList) (like myList.reverse()):
#       make an empty accumulator list
#       iterate over myList backwards (end to beginning)
#           append to accumulator list current element of myList
#       return accumulator list
# -OR-
#       iterate over half of myList
#           swap element i with element len-i
#       return myList
#
#   sort(myList) (like myList.sort()):
#       make empty sortedList
#       while length of myList > 1
#           set smallest to index of first element of myList
#           iterate over rest of myList
#               if an element is found smaller than smallest so far
#                   set smallest to index of current element
#           append to sortedList smallest element from myList
#           delete smallest element from myList
#       return sortedList


def count(l, x):
    """
    Counts number of times x occurs in l
    :param l: list -> list to search
    :param x: any -> item to count in l
    :return: int -> number of times x occurs in l
    """
    occurs = 0
    for elem in l:
        if elem == x:
            occurs += 1
    return occurs


def isin(l, x):
    """
    Checks to see if x is in l
    :param l: list -> list to search
    :param x: any -> item to find in l
    :return: boolean -> true if x is found, false otherwise
    """
    found = False
    for elem in l:
        if elem == x:
            found = True
            break
    return found


def index(l, x):
    """
    Finds index of x if it is in l
    :param l: list -> list to search
    :param x: any -> item to find in l
    :return: int -> index of first element equal to x, -1 if x not found
    """
    idx = -1
    for i in range(len(l)):
        if l[i] == x:
            idx = i
            break
    return idx


def reverse(l):
    """
    Reverses a list
    :param l: list -> list to reverse
    :return: list -> reversed list
    """
    endIdx = len(l) // 2
    lenL = len(l) - 1
    for i in range(endIdx):
        l[i], l[lenL - i] = l[lenL - i], l[i]
    return l


def sort(l):
    """
    Sorts l in ascending order
    :param l: list -> list to sort
    :return: list -> sorted list
    """
    sList = []
    while len(l) > 0:
        smallest = 0
        for i in range(1, len(l)):
            if l[i] < l[smallest]:
                smallest = i
        sList.append(l[smallest])
        del l[smallest]
    return sList


if __name__ == '__main__':
    myList = [0,1,2,3,4,5,6,7,8,9]
    print(myList)
    print(reverse(myList))
    reverse([3,2,1])
    reverse([7,7,3,4])
