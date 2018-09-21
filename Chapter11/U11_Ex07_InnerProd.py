# U11_Ex07_InnerProd.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 20 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 7
#     Source: Python Programming
#    Chapter: 11
#
# Program Description
#   Computes the inner product of two arrays (lists). The lists must be the same
#   length as each other. The inner product is the sum of the products of elements
#   with matching indices from each array.
#
# Algorithm (pseudocode)
#   ensure lists are same-length; throw an error if not
#   initialize an accumulator to zero
#   iterate over the length of the lists
#       sum the products of elements with matching indices to the accumulator
#   return the sum


def innerProd(list1, list2):
    """
    Computes the inner product of list1 and list2
    :param list1: list -> first list (elements are either int or float)
    :param list2: list -> second list (elements are either int or float)
    :return: int or float -> inner product
    """
    try:
        a = list2[len(list1)-1]
        b = list1[len(list2)-1]
    except IndexError:
        return "Lists must be of same length."
#        quit(1)

    innerProd = 0
    for i in range(len(list1)):
        innerProd += list1[i] * list2[i]
    return innerProd


if __name__ == '__main__':
    print(innerProd([1,2], [4,5,6]))