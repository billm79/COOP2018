# U08_Ex15_NegImage.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 15
#     Source: Python Programming
#    Chapter: 8
#
# Program Description
#   Converts a color GIF or PPM image to its color negative
#
# Algorithm (pseudocode)
#   create GraphWin
#   introduce program
#   get the image file using askopenfilename from tkinter.filedialog
#   open the file
#   display color image
#   get mouse click (negative button?)
#   get width and height of image
#   convert pixels to color negative
#       using image width and height, get pixel rgb values and set to color negative
#   display color negative image
#   get mouse click (save button?)
#   save image using asksaveasfilename from tkinter.filedialog


from tkinter.filedialog import askopenfilename, asksaveasfilename
from graphics import *

def main():
    # create GraphWin
    win = GraphWin('Grayscale Image', 600, 600)

    # introduce program
    midX = win.getWidth() / 2; midY = win.getHeight() / 2
    msg = Text(Point(midX, midY),
               'This program converts a color image\n(GIF or PPM) to color negative.\n' +
               'Begin by selecting an image.\n\nClick the mouse to continue.')
    msg.draw(win)
    win.getMouse()
    msg.undraw()

    # get the image file using askopenfilename from tkinter.filedialog
    imgFile = askopenfilename(filetypes=(("GIF files", "*.gif"), ("All files", "*.*")))

    if not imgFile:
        return

    # open the file
    img = Image(Point(midX, midY), imgFile)

    # display color image
    img.draw(win)

    # get mouse click (negative button?)
    actionButton = Rectangle(Point(win.getWidth() - 80, 10), Point(win.getWidth() - 10, 40))
    actionButton.draw(win)
    actionText = Text(Point(win.getWidth() - 45, 25), 'Negative')
    actionText.draw(win)
    win.getMouse()

    # get width and height of image
    imgWidth = img.getWidth(); imgHeight = img.getHeight()

    # convert pixels to color negative
    #     using image width and height, get pixel rgb values and set to color negative
    for i in range(imgWidth):
        for j in range(imgHeight):
            rgb = img.getPixel(i, j)
            negR = 255 - rgb[0]; negG = 255 - rgb[1]; negB = 255 - rgb[2]
            img.setPixel(i, j, color_rgb(negR, negG, negB))


    # display color negative image
    img.undraw()
    img.draw(win)

    # get mouse click (save button?)
    actionText.setText('Save')
    win.getMouse()

    # save image using asksavefilename from tkinter.filedialog
    imgNew = asksaveasfilename()
    if imgNew:
        img.save(imgNew)

if __name__ == '__main__':
    main()
