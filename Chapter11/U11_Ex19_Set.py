# U11_Ex19_Set.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 22 Mar 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 19
#     Source: Python Programming
#    Chapter: 11
#
# Program Description
#   Classical set class with the following methods:
#       Set(elements) -- creates a set
#       addElement(x) -- adds x to the set
#       deleteElement(x) -- removes x from the set, if present
#       member(x) -- returns true if x is in the set; false otherwise
#       intersection(set2) -- returns a new set containing just those
#           elements that are common to this set and set2
#       union(set2) -- returns a new set containing all the elements
#           that are in this set, set2, or both
#       subtract(set2) -- returns a new set containing all the elements
#           of this set that are not in set2
# Algorithm (pseudocode)
#   Notes are provided for each method in Set


class Set:
    def __init__(self, elements):
        """
        Constructor for Set
        :param elements: list -> list of elements to add to set
        """
        self.set = {}
        for elem in elements:
            # value in {key: value} pairs is number of occurrences; forced to 1 at construction
            self.set[elem] = self.set.get(elem, 1)

    def add_element(self, x):
        """
        Adds an element to set; if already in set, increments value
        :param x: any -> element to add
        :return: None
        """
        self.set[x] = self.set.get(x, 0) + 1

    def delete_element(self, x):
        """
        Deletes by decrementing value; zero value keys get deleted
        :param x: any -> element to delete
        :return: None
        """
        if x in self.set:
            self.set[x] -= 1
        if self.set[x] == 0:
            del self.set[x]

    def member(self, x):
        """
        Checks to see if x is a member of set
        :param x: any -> element to check against set
        :return: boolean -> True if x in set; False otherwise
        """
        if x in self.set:
            return True
        return False

    def intersection(self, set2):
        """
        Returns a new set containing all elements that are in set (this object)
        and also in set2 (passed Set parameter)
        :param set2: Set -> other Set object
        :return: Set -> newSet contains the intersection of the two sets
        """
        newSet = Set([])
        for item in self.set:
            if item in set2:
                newSet.set[item] = 1
        return newSet

    def union(self, set2):
        """
        Returns a new set containing all elements of both sets; value is
        incremented for duplicates
        :param set2: Set -> other Set object
        :return: Set -> newSet contains the union of the two sets
        """
        newSet = Set([])
        for item in self.set:
            newSet.set[item] = 1
        for item in set2:
            newSet.set[item] = newSet.set.get(item, 0) + 1
        return newSet

    def subtract(self, set2):
        """
        Returns a new set containing elements in set (this object) not in set2
        :param set2: Set -> other Set object
        :return: Set -> newSet contains set minus set2
        """
        newSet = Set([])
        for item in self.set:
            if not item in set2:
                newSet.set[item] = 1
        return newSet

    def __str__(self):
        """Returns set as a string (only the keys), stripping all the values"""
        retStr = "{"
        for item in self.set:
            retStr += str(item) + ", "
        retStr = retStr[:-2] + "}"
        return retStr


if __name__ == '__main__':
    thisSet = Set([2,4,6,8])
    set2 = Set([1,3,5,7])
    print("                   thisSet:", thisSet)
    print("                      set2:", set2)
    set2.add_element(9)
    print("     set2 after adding '9':", set2)
    thisSet.add_element(7)
    print("  thisSet after adding '7':", thisSet)
    print("is '7' a member of thisSet?", thisSet.member(7))
    print("is '0' a member of thisSet?", thisSet.member(0))
    print("      intersection of sets:", thisSet.intersection(set2.set))
    print("             union of sets:", thisSet.union(set2.set))
    print("            thisSet - set2:", thisSet.subtract(set2.set))
    print("            set2 - thisSet:", set2.subtract(thisSet.set))
