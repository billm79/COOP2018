# shadowtext.py

from graphics import *

class ShadowText(Text):
    """
    ShadowText class for creating shadow for Text. Inherits from Text
    """
    def __init__(self, txtobj, fill='black', offset_x=2, offset_y=2):
        """
        Set some instance variables before calling superclass constructor
        :param txtobj: Text -> text object needing a shadow
        :param fill: str -> fill color
        :param offset_x: int/float -> shadow offset in x direction
        :param offset_y: int/float -> shadow offset in y direction
        """
        self.obj = txtobj.clone()               # clone the original Text object
        self.center = self.obj.getAnchor()
        self.text = self.obj.getText()
        self.obj.setFill(fill)
        self.offsetX = offset_x
        self.offsetY = offset_y
        Text.__init__(self, self.center, self.text)

    def draw(self, win):
        """
        Overrides Text.draw()
        :param win: GraphWin -> window in which to draw text shadow
        """
        self.obj.move(self.offsetX, self.offsetY)
        self.obj.draw(win)
