# U06_Ex01_OldMacDonald.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 21 Oct 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 1
#     Source: Python Programming
#    Chapter: 6
#
# Program Description
#   Prints the lyrics of the song "Old MacDonald" for five different animals.
#
# Algorithm (pseudocode)
#   Make a list containing animals and sounds.
#       Element n is the animal and n+1 is its sound.
#   For each animal/sound pair
#       Call song(), passing the animal/sound pair as parameters.
#
#   song():
#       animal and sound are arguments
#       Call firstLast() for first line of song
#       Call middleThree() for middle three lines, passing animal and sound
#       Call firstLast() for last line of song
#
#   firstLast():
#       Print "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
#
#   middleThree():
#       animal and sound are arguments
#       Print middle three lines of song with passed animal and sound.


def main():
    # Make a list containing animals and sounds.
    #     Element n is the animal and n+1 is its sound.
    animals = ['cow', 'moo', 'chicken', 'cluck', 'dog', 'woof', 'horse', 'whinnie', 'goat', 'blaaah']

    # For each animal/sound pair
    for idx in range(0, len(animals), 2):
        # Call song(), passing the animal/sound pair as parameters.
        song(animals[idx], animals[idx+1])
        print()

# song():
#   animal and sound are arguments
def song(animal, sound):
    # Call firstLast() for first line of song
    firstLast()

    # Call middleThree() for middle three lines, passing animal and sound
    middleThree(animal, sound)

    # Call firstLast() for last line of song
    firstLast()

# firstLast():
def firstLast():
    # Print "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

# middleThree():
#   animal and sound are arguments
def middleThree(animal, sound):
    # Print middle three lines of song with passed animal and sound.
    print('And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!'.format(animal))
    print('With a {0}, {0} here and a {0}, {0} there.'.format(sound))
    print('Here a {0}, there a {0}, everywhere a {0}, {0}.'.format(sound))

main()