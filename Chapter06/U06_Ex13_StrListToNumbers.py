# U06_Ex13_StrListToNumbers.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 13
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Function to convert a list of strings to a list of numbers
#
# Algorithm (pseudocode)
#   toNumbers():
#       the list strList is argument
#       loop through strList, changing each element to a number using eval()
#       return None
#
#   getTypes(): (extra, needed to test)
#       the list lst is argument
#       initialize accumulator list
#       loop through lst, appending data type to accumulator list
#       return accumulator list
#
#   main():
#       test toNumbers() with sample list


# toNumbers():
#   the list strList is argument
def toNumbers(strList):
    # loop through strList, changing each element to a number using eval()
    for i in range(len(strList)):
        strList[i] = eval(strList[i])
    # return None

# getTypes(): (extra, needed to test)
#     the list lst is argument
def getTypes(lst):
    # initialize accumulator list
    typesList = []

    # loop through lst, appending data type to accumulator list
    for item in lst:
        typesList.append(type(item))
    # return accumulator list
    return typesList

#   main():
#       test toNumbers() with sample list
def main():
    sampleList = ['1', '2.0', '3']
    listTypes = getTypes(sampleList)
    print('Before List: {0}; Types: {1}'.format(sampleList, listTypes))
    toNumbers(sampleList)
    listTypes = getTypes(sampleList)
    print(' After List: {0}; Types: {1}'.format(sampleList, listTypes))

if __name__ == '__main__':
    main()