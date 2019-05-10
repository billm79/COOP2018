# button.py
from graphics import *
from time import sleep


class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """
        Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit')
        :param win: GraphWin -> graphics window object
        :param center: Point -> point object for center of button
        :param width: int/float -> width for button
        :param height: int/float -> height for button
        :param label: str -> button label
        """

        self.win = win
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.draw_shadow()
        self.rect.draw(self.win)
        self.label = Text(center, label)
        self.label.draw(self.win)
        self.deactivate()

    def clicked(self, p):
        """
        Determines if button was clicked
        :param p: Point -> point object for location of mouse click
        :return: boolean -> true if button active and p is inside
        """
        if (self.active and
                        self.xmin <= p.getX() <= self.xmax and
                        self.ymin <= p.getY() <= self.ymax):
            self.shadow_out1.undraw()
            self.shadow_out2.undraw()
            self.draw_depressed()
            return True
        else:
            return False

    def getLabel(self):
        """
        :return: str -> label of button
        """
        return self.label.getText()

    def activate(self):
        """
        Sets button to 'active.'
        """
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """
        Sets button to 'inactive.'
        """
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def draw_shadow(self):
        """Shadow for button when not pressed"""
        b = self.rect
        p1 = Point(b.getP2().getX()+2, b.getP1().getY()+2)      # top right outside shadow point
        p2 = Point(b.getP2().getX()+2, b.getP2().getY()+2)      # bottom right outside shadow point
        p3 = Point(b.getP1().getX()+2, b.getP2().getY()+2)      # bottom left outside shadow point
        self.shadow_out1 = Line(p1, p2)
        self.shadow_out1.setFill('black')
        self.shadow_out1.setWidth(2)
        self.shadow_out2 = Line(p3, p2)
        self.shadow_out2.setFill('black')
        self.shadow_out2.setWidth(2)
        self.shadow_out1.draw(self.win)
        self.shadow_out2.draw(self.win)


    def draw_depressed(self):
        """Depressed buttons lose the outside shadow and get an inside shadow"""
        b = self.rect
        p1 = Point(b.getP1().getX()+3, b.getP1().getY()+3)      # top left inside shadow point
        p2 = Point(b.getP1().getX()+3, b.getP2().getY()-0)      # bottom left inside shadow point
        p3 = Point(b.getP2().getX()-0, b.getP1().getY()+3)      # top right inside shadow point
        shadow_in1 = Line(p1, p2)
        shadow_in1.setFill('darkgrey')
        shadow_in1.setWidth(2)
        shadow_in2 = Line(p1, p3)
        shadow_in2.setFill('darkgrey')
        shadow_in2.setWidth(2)
        self.shadow_out1.undraw()
        self.shadow_out2.undraw()
        b.move(1, 1)
        shadow_in1.draw(self.win)
        shadow_in2.draw(self.win)
        sleep(0.07)
        shadow_in1.undraw()
        shadow_in2.undraw()
        b.move(-1, -1)
        self.shadow_out1.draw(self.win)
        self.shadow_out2.draw(self.win)


class ButtonWithCoords(Button):
    def __init__(self, win, center, width, height, label, coordX, coordY):
        super().__init__(win, center, width*coordX, height*coordY, label)
