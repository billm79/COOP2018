# U06_Ex11_SquareEachInList.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 11
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Modifies a list of numbers by squaring each item in list
#
# Algorithm (pseudocode)
#   squareEach():
#       the list nums is argument
#       loop through list
#           set each element to its square
#       return None
#
#   main():
#       test squareEach() with sample list


# squareEach():
#   the list nums is argument
def squareEach(nums):
    # loop through list
    for i in range(len(nums)):
        # set each element to its square
        nums[i] = nums[i]**2
    # return None

# main():
def main():
    # test squareEach() with sample list
    sampleList = [1,2,3,4]
    print('Before: ', sampleList)
    squareEach(sampleList)
    print(' After: ', sampleList)

if __name__ == '__main__':
    main()