# cdieview.py

from dieview import DieView


class ColorDieView(DieView):
    """
    Implementation of a DieView with changeable forground color
    Illustrates inheritance
    """

    def setValue(self, value):
        """
        Overrides DieView.setValue(), saving value locally first, then calling DieView.setValue()
        :param value: int -> value to set for die
        """
        self.value = value      # remember this value
        DieView.setValue(self, value) # call setValue from parent class

    def setColor(self, color):
        """
        Sets foreground color of die
        :param color:
        """
        self.foreground = color
        self.setValue(self.value)

