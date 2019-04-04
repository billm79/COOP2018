# U08_Ex17_ImageManipulation.py
#
#  Author: Bill Montana
#  Course: Coding for OOP
# Section: A3
#    Date: 24 Nov 2017
#     IDE: PyCharm Community Edition
#
# Assignment Info
#   Exercise: 17
#     Source: Python Programming
#    Chapter: 8
#
# Problem Description
#   Write a program that provides a vertical menu on right side of window for image manipulation algorithms.
#   The menu should include Load Image, Save Image, and Quit buttons at the top. Image manipulation algorithm
#   buttons should be displayed below, separated from the top buttons by a separator line. A vertical separator
#   line should divide the menu from image space. The program should accept mouse clicks for the buttons. When
#   image manipulation algorithm buttons are clicked, their fill color should toggle. Clicking again will
#   untoggle and reverse the effect. The user should also be allowed to press Ctrl/Command O to Load Image,
#   Ctrl/Command S to Save Image, and the Esc key to quit. The image should be displayed centered in the image
#   space. The image may need to be scaled if it is too big for the image space. The GraphWin should be 800
#   pixels in height and 1000 pixels in width (200 pixels are reserved for menu space).
#
# Program Description
#   Adds a menu to code for exercises 14 and 15.
#   Buttons: Load Image, Save Image, Quit, Grayscale, Negative, user defined buttons
#   Esc can be pressed to quit.
#
# Algorithm (pseudocode)
#   global variables: button objects, button constant values (e.g. LOADIMAGE = 0), image height and width, win
#   create GraphWin
#
#   main:
#       call drawMenu()
#       enter into event loop, looking for mouse clicks and key presses
#           key press: call handleKeys()
#           mouse clicks: call handleClicks()
#
#   drawMenu:
#       at top of program, define global variables for button locations (they get set here)
#       set standard height, width, and separation space for buttons
#       draw three buttons at top, a separator line, and at least five buttons below
#       set global button object variables as you go
#       set button fill color to light gray
#       draw button text for each button (bottom three will be blank)
#       draw a vertical separator line between menu and image space
#
#   handleKeys:
#       O  -> loadImage()
#       S  -> saveImage()
#
#   handleClicks:
#       call buttonClicked()
#       take action based on return value (see global constants)
#       0           -> do nothing
#       LOADIMAGE   -> loadImage()
#       SAVEIMAGE   -> saveImage()
#       Quit        -> quit
#       GRAYSCALE   -> toggle fill; grayscale()
#       NEGATIVE    -> toggle fill; negative()
#       Other Effects toggle fill and call appropriate user-defined functions
#
#   buttonClicked:
#       test to see if pt is on a button; return appropriate global constant (or zero)
#           if ptX is within x coords AND ptY is within y coords for this button return global var for button
#           otherwise, return 0
#
#   loadImage:
#       get the image file using askopenfilename from tkinter.filedialog
#       if no selection, return
#       open the file
#       get width and height of image and store to global variables
#       display image
#
#   saveImage:
#       save image using asksavefilename from tkinter.filedialog
#       if canceled, return
#       save the file
#
#   grayscale:
#       if already grayscale
#           revert to original pixels
#       otherwise
#           save state
#           convert pixels to grayscale
#               using image width and height, get pixel rgb values and set to grayscale
#       display image
#
#   negative:
#       convert pixels to color negative
#           using image width and height, get pixel rgb values and set to color negative
#       display image
#
#   other effects:
#       if effect already applied
#           revert to original pixels
#       otherwise
#           save state
#           convert pixels to effect
#               using image width and height, get pixel rgb values and set to effect
#       display image


from graphics import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from math import ceil

#   global variables: button objects, button constant values (e.g. LOADIMAGE = 0), image height and width, win
buttonLoad = Rectangle(Point(0,0), Point(1,1)); LOADIMAGE = 1; buttonLoadActive = 0
buttonSave = Rectangle(Point(0,0), Point(1,1)); SAVEIMAGE = 2; buttonSaveActive = 0
buttonQuit = Rectangle(Point(0,0), Point(1,1)); QUIT = 3; buttonQuitActive = 0
buttonGray = Rectangle(Point(0,0), Point(1,1)); GRAYSCALE = 4; buttonGrayActive = 0; isGrayscale = False
buttonNeg = Rectangle(Point(0,0), Point(1,1)); NEGATIVE = 5; buttonNegActive = 0; isNegative = False
buttonShrink = Rectangle(Point(0,0), Point(1,1)); SHRINK = 6; buttonShrinkActive = 0; isShrunk = False
buttonOther2 = Rectangle(Point(0,0), Point(1,1)); OTHER2 = 7; buttonOther2Active = 0; isOther2 = False
buttonOther3 = Rectangle(Point(0,0), Point(1,1)); OTHER3 = 8; buttonOther3Active = 0; isOther3 = False
buttonIdleFill = '#cccccc'; buttonActiveFill = '#999999'

# create GraphWin
win = GraphWin('Image Manipulation', 1000, 800)
imgAreaW = win.getWidth() - 200; imgAreaH = win.getHeight()
midX = imgAreaW / 2; midY = imgAreaH / 2
buttonHeight = 30; buttonWidth = 180; buttonSep = 10; menuLeft = win.getWidth() - 200
img = Image(Point(midX, midY), 800, 800); imgHeight = 0; imgWidth = 0
imgOrig = img

def main():
    # call drawMenu()
    drawMenu()

    # enter into event loop, looking for mouse clicks and key presses
    while True:
        # key press: call handleKeys()
        key = win.checkKey()
        if key == "Escape":  # loop exit
            break

        if key:
            handleKeys(key)

        # mouse clicks: call handleClicks()
        pt = win.checkMouse()
        if pt:
            if not handleClicks(pt):
                break

    win.close()

def drawMenu():
    # at top of program, define global variables for button locations (they get set here)
    global buttonLoad, buttonSave, buttonQuit, buttonGray, buttonNeg, buttonShrink, buttonOther2, buttonOther3

    # set standard height, width, and separation space for buttons
    # these are global variables

    # draw three buttons at top, a separator line, and at least five buttons below
    # set global button object variables as you go
    # set button fill color to light gray
    # draw button text for each button (bottom three will be blank)
    # draw a vertical separator line between menu and image space
    Line(Point(menuLeft, 0), Point(menuLeft, win.getHeight())).draw(win)

    # Load Image button
    topLeft = Point(menuLeft + buttonSep, buttonSep)
    botRight = Point(menuLeft + buttonSep + buttonWidth, buttonSep + buttonHeight)
    buttonLoad = Rectangle(topLeft, botRight)
    buttonLoad.setFill(color=buttonIdleFill)
    buttonLoad.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Load Image').draw(win)

    # Save Image button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonSave = Rectangle(topLeft, botRight)
    buttonSave.setFill(color=buttonIdleFill)
    buttonSave.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Save Image').draw(win)

    # Quit button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonQuit = Rectangle(topLeft, botRight)
    buttonQuit.setFill(color=buttonIdleFill)
    buttonQuit.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Quit').draw(win)

    # Horizontal separator line
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonSep)
    Line(Point(topLeft.getX() - buttonSep, topLeft.getY()),
         Point(botRight.getX() + buttonSep ,botRight.getY())).draw(win)

    # Grayscale button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonGray = Rectangle(topLeft, botRight)
    buttonGray.setFill(color=buttonIdleFill)
    buttonGray.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Grayscale').draw(win)

    # Negative button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonNeg = Rectangle(topLeft, botRight)
    buttonNeg.setFill(color=buttonIdleFill)
    buttonNeg.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Negative').draw(win)

    # Other Effect 1 button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonShrink = Rectangle(topLeft, botRight)
    buttonShrink.setFill(color=buttonIdleFill)
    buttonShrink.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Shrink Image').draw(win)

    # Other Effect 2 button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonOther2 = Rectangle(topLeft, botRight)
    buttonOther2.setFill(color=buttonIdleFill)
    buttonOther2.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Other Effect 2').draw(win)

    # Other Effect 3 button
    topLeft = Point(topLeft.getX(), topLeft.getY() + buttonHeight + buttonSep)
    botRight = Point(botRight.getX(), botRight.getY() + buttonHeight + buttonSep)
    buttonOther3 = Rectangle(topLeft, botRight)
    buttonOther3.setFill(color=buttonIdleFill)
    buttonOther3.draw(win)
    Text(Point(topLeft.getX() + (botRight.getX() - topLeft.getX()) / 2,
               topLeft.getY() + (botRight.getY() - topLeft.getY()) / 2), 'Other Effect 3').draw(win)

def handleKeys(key):
    """
    Handles keys pressed to execute menu options (except ESC)
    :param key: str -> key that was pressed
    :return: None
    """
    # O  -> loadImage()
    if key == "o" or key == "O":
        loadImage()

    # S  -> saveImage()
    if key == "s" or key == "S":
        saveImage()

def handleClicks(pt):
    """
    Handles valid mouse clicks, executing button actions
    :param pt: Point -> location of mouse click as a Point object
    :return: int -> 0 if Quit button clicked; otherwise 1
    """
    global buttonLoadActive, buttonSaveActive, buttonQuitActive, buttonGrayActive, \
        buttonNegActive, buttonShrinkActive, buttonOther2Active, buttonOther3Active
    # call buttonClicked()
    clickResult = buttonClicked(pt)
    print(['', 'LOAD', 'SAVE', 'QUIT', 'GRAY', 'NEG', 'O1', 'O2', 'O3'][clickResult])
    # take action based on return value (see global constants)
    # 0           -> do nothing
    # LOADIMAGE   -> loadImage()
    # SAVEIMAGE   -> saveImage()
    # Quit        -> quit
    # GRAYSCALE   -> toggle fill; grayscale()
    # NEGATIVE    -> toggle fill; negative()
    # Other Effects toggle fill and call appropriate user-defined functions
    if clickResult == LOADIMAGE:
        buttonLoadActive = buttonFillToggle(buttonLoad, buttonLoadActive)
        loadImage()
        buttonLoadActive = buttonFillToggle(buttonLoad, buttonLoadActive)
    if clickResult == SAVEIMAGE:
        buttonSaveActive = buttonFillToggle(buttonSave, buttonSaveActive)
        saveImage()
        buttonSaveActive = buttonFillToggle(buttonSave, buttonSaveActive)
    if clickResult == QUIT:
        buttonQuitActive = buttonFillToggle(buttonQuit, buttonQuitActive)
        return 0
    if clickResult == GRAYSCALE:
        buttonGrayActive = buttonFillToggle(buttonGray, buttonGrayActive)
        grayscale()
    if clickResult == NEGATIVE:
        buttonNegActive = buttonFillToggle(buttonNeg, buttonNegActive)
        negative()
    if clickResult == SHRINK:
        buttonShrinkActive = buttonFillToggle(buttonShrink, buttonShrinkActive)
        shrink()
    if clickResult == OTHER2:
        buttonOther2Active = buttonFillToggle(buttonOther2, buttonOther2Active)
        other2()
    if clickResult == OTHER3:
        buttonOther3Active = buttonFillToggle(buttonOther3, buttonOther3Active)
        other3()
    return 1

def buttonClicked(pt):
    """
    Checks to see if a button was clicked
    :param pt: Point -> location of mouse click as a Point object
    :return: int -> global constant matching button clicked; zero if none
    """
    # test to see if pt is on a button; return appropriate global constant (or zero)
    #     if ptX is within x coords AND ptY is within y coords for this button return global var for button
    #     otherwise, return 0
    buttonLoadCenter = buttonLoad.getCenter()
    buttonSaveCenter = buttonSave.getCenter()
    buttonQuitCenter = buttonQuit.getCenter()
    buttonGrayCenter = buttonGray.getCenter()
    buttonNegCenter = buttonNeg.getCenter()
    buttonShrinkCenter = buttonShrink.getCenter()
    buttonOther2Center = buttonOther2.getCenter()
    buttonOther3Center = buttonOther3.getCenter()

    retVal = 0

    if buttonLoadCenter.getX() - buttonWidth / 2 < pt.getX() < buttonLoadCenter.getX() + buttonWidth / 2 and \
        buttonLoadCenter.getY() - buttonHeight / 2 < pt.getY() < buttonLoadCenter.getY() + buttonHeight / 2:
        retVal =  LOADIMAGE

    elif buttonSaveCenter.getX() - buttonWidth / 2 < pt.getX() < buttonSaveCenter.getX() + buttonWidth / 2 and \
        buttonSaveCenter.getY() - buttonHeight / 2 < pt.getY() < buttonSaveCenter.getY() + buttonHeight / 2:
        retVal = SAVEIMAGE

    elif buttonQuitCenter.getX() - buttonWidth / 2 < pt.getX() < buttonQuitCenter.getX() + buttonWidth / 2 and \
        buttonQuitCenter.getY() - buttonHeight / 2 < pt.getY() < buttonQuitCenter.getY() + buttonHeight / 2:
        retVal = QUIT

    elif buttonGrayCenter.getX() - buttonWidth / 2 < pt.getX() < buttonGrayCenter.getX() + buttonWidth / 2 and \
        buttonGrayCenter.getY() - buttonHeight / 2 < pt.getY() < buttonGrayCenter.getY() + buttonHeight / 2:
        retVal = GRAYSCALE

    elif buttonNegCenter.getX() - buttonWidth / 2 < pt.getX() < buttonNegCenter.getX() + buttonWidth / 2 and \
        buttonNegCenter.getY() - buttonHeight / 2 < pt.getY() < buttonNegCenter.getY() + buttonHeight / 2:
        retVal = NEGATIVE

    elif buttonShrinkCenter.getX() - buttonWidth / 2 < pt.getX() < buttonShrinkCenter.getX() + buttonWidth / 2 and \
        buttonShrinkCenter.getY() - buttonHeight / 2 < pt.getY() < buttonShrinkCenter.getY() + buttonHeight / 2:
        retVal = SHRINK

    elif buttonOther2Center.getX() - buttonWidth / 2 < pt.getX() < buttonOther2Center.getX() + buttonWidth / 2 and \
        buttonOther2Center.getY() - buttonHeight / 2 < pt.getY() < buttonOther2Center.getY() + buttonHeight / 2:
        retVal = OTHER2

    elif buttonOther3Center.getX() - buttonWidth / 2 < pt.getX() < buttonOther3Center.getX() + buttonWidth / 2 and \
        buttonOther3Center.getY() - buttonHeight / 2 < pt.getY() < buttonOther3Center.getY() + buttonHeight / 2:
        retVal = OTHER3

    win.checkMouse()
    return retVal

def buttonFillToggle(button, buttonFillActive):
    """
    Toggles button fill color when clicked
    :param button: Rectangle -> button as a Rectangle object
    :param buttonFillActive: boolean -> current state of button
    :return: boolean -> toggled state for button
    """
    if buttonFillActive:
        button.setFill(color=buttonIdleFill)
        return False
    button.setFill(color=buttonActiveFill)
    return True

def loadImage():
    """
    Loads a user-specified image file from disk
    :return: None
    """
    global img, imgHeight, imgWidth, imgOrig
    img.undraw()

    # get the image file using askopenfilename from tkinter.filedialog
    imgFile = askopenfilename(filetypes=(("GIF files", "*.gif"), ("All files", "*.*")))

    # if no selection, return
    if not imgFile:
        return

    # open the file
    img = Image(Point(midX, midY), imgFile)

    # get width and height of image and store to global variables
    imgWidth = img.getWidth(); imgHeight = img.getHeight()

    if imgWidth > imgAreaW or imgHeight > imgAreaH:
        scaleImg(max(imgWidth / imgAreaW, imgHeight / imgAreaH))

    imgOrig = img.clone()

    # display color image
    img.draw(win)

def saveImage():
    """
    Saves the image to disk with user-specified path
    :return: None
    """
    global img
    # save image using asksavefilename from tkinter.filedialog
    imgNew = asksaveasfilename()

    # if canceled, return
    # save the file
    if imgNew:
        img.save(imgNew)


def scaleImg(factor):
    global img, imgWidth, imgHeight

    factor = ceil(factor)

    # imgTmp = Image(Point(midX, midY), imgAreaW, imgAreaH)
    imgTmp = Image(Point(midX, midY), imgWidth // factor, imgHeight // factor)
    inc = int((imgHeight / factor) / 100)
    pbar = ProgressBar(win, x=300, y=750, length=200, width=8,
                       max_val=imgHeight // factor, show=True,
                       place='B', msg='Scaling image...', msgPlace='T')
    pbar.draw(win)
    for row in range(imgHeight // factor):
        for col in range(imgWidth // factor):
            # print(row, col, end='\b' * (len(str(row)) + len(str(col)) + 1))
            c = img.getPixel(col * factor, row * factor)
            imgTmp.setPixel(col, row, color_rgb(c[0], c[1], c[2]))
        if row % inc == 0:
            pbar.update(row)
    pbar.update(imgHeight // factor)
    pbar.undraw()

    img = imgTmp.clone()
    # img.setAnchor(Point(midX, midY))
    imgWidth = img.getWidth(); imgHeight = img.getHeight()


def grayscale():
    """
    Converts image to grayscale (or back to previous state if already grayscale)
    :return: None
    """
    global img, imgOrig, isGrayscale
    # if already grayscale
    if isGrayscale:
        # revert to original pixels
        img = imgOrig.clone()
        isGrayscale = False

    # otherwise
    else:
        # save state
        imgOrig = img.clone()

        # convert pixels to grayscale
        #     using image width and height, get pixel rgb values and set to grayscale
        inc = int(imgWidth / 100)
        pbar = ProgressBar(win, x=300, y=750, length=200, width=8, max_val=imgWidth, show=True, place='B')
        pbar.draw(win)
        for i in range(imgWidth):
            for j in range(imgHeight):
                rgb = img.getPixel(i, j)
                grayAvg = int(sum(rgb) / 3)
                grayLum = int(round(0.21 * rgb[0] + 0.72 * rgb[1] + 0.07 * rgb[2]))
                grayLit = int((max(rgb) + min(rgb)) / 2)
                gray = grayLum
                img.setPixel(i, j, color_rgb(gray, gray, gray))
            if i % inc == 0:
                pbar.update(i)
        pbar.update(imgWidth)
        pbar.undraw()
        isGrayscale = True

    # display grayscale image
    img.undraw()
    img.draw(win)

def negative():
    """
    Converts image to color-negative
    :return: None
    """
    global img
    # convert pixels to color negative
    #     using image width and height, get pixel rgb values and set to color negative
    inc = int(imgWidth / 100)
    pbar = ProgressBar(win, x=300, y=750, length=200, width=8, max_val=imgWidth, show=True, place='B')
    pbar.draw(win)
    for i in range(imgWidth):
        for j in range(imgHeight):
            rgb = img.getPixel(i, j)
            negR = 255 - rgb[0]; negG = 255 - rgb[1]; negB = 255 - rgb[2]
            img.setPixel(i, j, color_rgb(negR, negG, negB))
        if i % inc == 0:
            pbar.update(i)
    pbar.update(imgWidth)
    pbar.undraw()

    # display color negative image
    img.undraw()
    img.draw(win)

#   other effects:
#       if effect already applied
#           revert to original pixels
#       otherwise
#           save state
#           convert pixels to effect
#               using image width and height, get pixel rgb values and set to effect
#       display image


    # display color negative image
    img.undraw()
    img.draw(win)

def shrink():
    """
    Replaces img with one half its size
    :return: None
    """
    global img, imgOrig, isShrunk
    # if already grayscale
    if isShrunk:
        # revert to original pixels
        img = imgOrig.clone()
        isShrunk = False

    # otherwise
    else:
        # save state
        imgOrig = img.clone()
        imgNew = Image(Point(midX, midY), 400, 400)

        # convert pixels to grayscale
        #     using image width and height, get pixel rgb values and set to grayscale
        inc = int(imgWidth / 100)
        pbar = ProgressBar(win, x=300, y=750, length=200, width=8, max_val=imgWidth, show=True, place='B')
        pbar.draw(win)
        i = 0; iNew = 0
        while i < imgWidth:
            j = 0; jNew = 0
            while j < imgHeight:
                rgb = img.getPixel(i, j)
                imgNew.setPixel(iNew, jNew, color_rgb(rgb[0], rgb[1], rgb[2]))
                j += 2; jNew += 1
            if i % inc == 0:
                pbar.update(i)
            i += 2; iNew += 1
        pbar.update(imgWidth)
        pbar.undraw()
        isShrunk = True
        img.undraw()
        img = imgNew

    # display shrunk image
    #img.undraw()
    img.draw(win)


def other2():
    pass

def other3():
    pass

class ProgressBar:
    # bar_win = ''
    # bar_length = 0; bar_width = 0   # in pixels
    # bar_x = 0; bar_y = 0
    # bar_max = 0                     # maximum passed value
    # show_text = False

    # text_placement options:
    #
    # TL     T     TR
    # L  bar  here  R
    # BL     B     BR
    #
    # blank means no text (default)
    # text_placement = ''

    # bar_rect = Rectangle(Point(0,0), Point(0,0))
    # bar_pbar = Rectangle(Point(0,0), Point(0,0))
    # bar_text = Text(Point(0,0), '')

    def __init__(self, window, x=0, y=0, length=0, width=0, max_val=0, show=False, place='', msg='', msgPlace=''):
        self.win = window
        self.bar_x = x
        self.bar_y = y
        self.bar_length = length
        self.bar_width = width
        self.bar_max = max_val
        self.show_text = show
        self.text_placement = place
        self.msg = msg
        self.msgPlace = msgPlace

        self.bar_rect = Rectangle(Point(x, y), Point(x + length, y + width))
        self.bar_rect.setOutline('black')
        self.bar_rect.setFill('white')
        self.bar_pbar = Rectangle(Point(x+2, y+2), Point(x+3, y+width-2))
        self.bar_pbar.setOutline('gray')
        self.bar_pbar.setFill('gray')

        if show:
            if place == 'TL':
                self.bar_text = Text(Point(x, y - 20), '0%')
            if place == 'T':
                self.bar_text = Text(Point(x + length / 2, y - 20), '0%')
            if place == 'TR':
                self.bar_text = Text(Point(x + length - 15, y - 20), '0%')
            if place == 'R':
                self.bar_text = Text(Point(x + length + 5, y), '0%')
            if place == 'BR':
                self.bar_text = Text(Point(x + length - 15, y + 20), '0%')
            if place == 'B':
                self.bar_text = Text(Point(x + length / 2, y + 20), '0%')
            if place == 'BL':
                self.bar_text = Text(Point(x, y + 20), '0%')
            if place == 'L':
                self.bar_text = Text(Point(x - 15, y + width / 2), '0%')

        if msg:
            if msgPlace == 'TL':
                self.bar_msg = Text(Point(x, y - 20), msg)
            if msgPlace == 'T':
                self.bar_msg = Text(Point(x + length / 2, y - 20), msg)
            if msgPlace == 'TR':
                self.bar_msg = Text(Point(x + length - 15, y - 20), msg)
            if msgPlace == 'R':
                self.bar_msg = Text(Point(x + length + 5, y), msg)
            if msgPlace == 'BR':
                self.bar_msg = Text(Point(x + length - 15, y + 20), msg)
            if msgPlace == 'B':
                self.bar_msg = Text(Point(x + length / 2, y + 20), msg)
            if msgPlace == 'BL':
                self.bar_msg = Text(Point(x, y + 20), msg)
            if msgPlace == 'L':
                self.bar_msg = Text(Point(x - 15, y + width / 2), msg)

    # def set_window(self, arg):
    #     if arg:
    #         self.win = arg
    #
    # def set_x(self, arg):
    #     if arg:
    #         self.bar_x = arg
    #
    # def set_y(self, arg):
    #     if arg:
    #         self.bar_y = arg
    #
    # def set_bar_length(self, arg):
    #     if arg:
    #         self.bar_length = arg
    #
    # def set_bar_width(self, arg):
    #     if arg:
    #         self.bar_width = arg
    #
    # def set_bar_max(self, arg):
    #     if arg:
    #         self.bar_max = arg
    #
    # def set_show_text(self, arg):
    #     if arg:
    #         self.show_text = arg
    #
    # def set_text_placement(self, arg):
    #     if arg:
    #         self.text_placement = arg

    def get_x(self):
        return self.bar_x

    def get_y(self):
        return self.bar_y

    def get_bar_length(self):
        return self.bar_length

    def get_bar_width(self):
        return self.bar_width

    def get_show_text(self):
        return self.show_text

    def get_text_placement(self):
        return self.text_placement

    def draw(self, window):
        self.bar_win = window
        self.bar_rect.draw(self.bar_win)
        if self.show_text:
            self.bar_text.draw(self.bar_win)
        if self.msg:
            self.bar_msg.draw(self.bar_win)

    def undraw(self):
        self.bar_rect.undraw()
        self.bar_pbar.undraw()
        if self.show_text:
            self.bar_text.undraw()
        if self.msg:
            self.bar_msg.undraw()

    def update(self, val):
        pct = val / self.bar_max
        self.bar_oldbar = self.bar_pbar
        self.bar_pbar = Rectangle(self.bar_pbar.getP1(),
                                  Point(self.bar_x + int(pct * (self.bar_length-4)), self.bar_y+self.bar_width-2))
        self.bar_pbar.setOutline('gray')
        self.bar_pbar.setFill('gray')
        self.bar_oldbar.undraw()
        self.bar_pbar.draw(self.bar_win)
        if self.show_text:
            self.bar_text.setText(str(int(pct * 100)) + '%')
            # self.bar_text.undraw()
            # self.bar_text.draw(self.bar_win)
            update()

if __name__ == '__main__':
    main()

def sepia():
    """
    Converts image to sepia
    :return: None
    """
    global img
    # convert pixels to color negative
    #     using image width and height, get pixel rgb values and set to color negative
    for i in range(imgWidth):
        for j in range(imgHeight):
            rgb = img.getPixel(i, j)
            rgb[0] = int(min(rgb[0] * 0.393 + rgb[1] * 0.769 + rgb[2] * 0.189, 255))
            rgb[1] = int(min(rgb[0] * 0.349 + rgb[1] * 0.686 + rgb[2] * 0.168, 255))
            rgb[2] = int(min(rgb[0] * 0.272 + rgb[1] * 0.534 + rgb[2] * 0.131, 255))
            img.setPixel(i, j, color_rgb(rgb[0], rgb[1], rgb[2]))

