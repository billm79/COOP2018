# U03_Ex03_MolecularWt.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 14 Sep 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 3
#     Source: Python Programming
#    Chapter: 3
#
# Program Description
#   Calculates the molecular weight of a carbohydrate molecule, given user inputs for
#   the number of hydrogen, carbon, and oxygen atoms in the molecule.
#
# Algorithm (pseudocode)
#   introduce program
#   set constants for molecular weights for hydrogen, carbon, and oxygen
#       (H = 1.00794, C = 12.0107, O = 15.9994, all in grams/mole)
#   get from user number of hydrogen, carbon, and oxygen atoms in molecule
#   calculate molecular weight of molecule
#   display results


def main():
    print("\nThis program calculates the molecular weight of a carbohydrate molecule,",
          "given user inputs for the number of hydrogen, carbon, and oxygen atoms in the molecule.\n")
    hWt = 1.00794
    cWt = 12.0107
    oWt = 15.9994
    hAtoms = int(input("How many hydrogen atoms are present in the molecule? "))
    cAtoms = int(input("How many carbon atoms are present in the molecule? "))
    oAtoms = int(input("How many oxygen atoms are present in the molecule? "))
    molWt = hWt * hAtoms + cWt * cAtoms + oWt * oAtoms
    print(("\nThe molecular weight of a molecule containing {0} hydrogen atoms, \
{1} carbon atoms, and {2} oxygen atoms is {3} grams/mole.").format(hAtoms, cAtoms, oAtoms, molWt))

main()