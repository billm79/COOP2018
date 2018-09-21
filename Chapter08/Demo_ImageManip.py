# Demo_ImageManip.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 04 Jan 2018
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Example: In-class event-loop app demo
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   GUI program to load, manipulate, and save images.
#   Buttons: Load Image, Save Image, Quit, Grayscale, Negative,
#       user defined buttons
#   Esc can be pressed to quit
#
# Algorithm (pseudocode)
#   create GraphWin
#
#   main:
#       call drawMenu()
#       enter into event loop, looking for key and mouse events
#           key press: call handleKeys()
#           mouse clicks: call handleClicks()
#       close window
#
#   drawMenu():
#       use global variables for button locations, size, spacing, etc.
#       draw three buttons at top, a separator line, other buttons below
#       draw horizontal and vertical separator lines
#
#   handleKeys():
#       Esc -> quit
#
#   handleClicks():
#       call buttonClicked()
#       take action based on return value
#       '' -> do nothing
#       'LoadImage' -> loadImage()
#       'SaveImage' -> saveImage()
#       'Quit'      -> quit
#       'Grayscale' -> grayscale()
#       'Negative'  -> negative()
#       Other Effects call appropriate user-defined functions
#
#   buttonClicked():


