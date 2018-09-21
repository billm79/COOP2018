# U06_Ex12_SumList.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 12
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Function to return the sum of a list of numbers
#
# Algorithm (pseudocode)
#   sumList():
#       list nums is argument
#       initialize accumulator listSum for addition
#       loop through nums, adding current num to accumulator
#       return accumulator
#
#   main():
#       test sumList() with sample list


# sumList():
#   list nums is argument
def sumList(nums):
    # initialize accumulator listSum for addition
    listSum = 0

    # loop through nums, adding current num to accumulator
    for num in nums:
        listSum += num

    # return accumulator
    return listSum

# main():
#   test sumList() with sample list
def main():
    sampleList = [1,2,3,4]
    print('The sum of items in {0} is {1}.'.format(sampleList, sumList(sampleList)))

if __name__ == '__main__':
    main()