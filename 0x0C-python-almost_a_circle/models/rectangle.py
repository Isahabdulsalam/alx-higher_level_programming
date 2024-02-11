#!/usr/bin/python3

from base import Base

class Rectangle(Base):
    """ Defining the rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            self._width = value

        @property
        def height(self):
            return self._height

        @width.setter
        def height(self, value):
            self._height = value

        @property
        def x(self):
            return self._x

        @x.setter
        def width(self, value):
            self._x = value

        @property
        def y(self):
            return self._y
        @width.setter
        def y(self, value):
            self._y = value
