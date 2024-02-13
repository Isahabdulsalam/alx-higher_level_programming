#!/usr/bin/python3

from base import Base

class Rectangle(Base):
    """ Defining the rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing new rectangle """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width function """
        return self.__width

    @property
    def height(self):
        """ height function """
        return self.__height

    @property
    def x(self):
        """ x function """
        return self.__x

    @property
    def y(self):
        """ y function """
        return self.__y

    @width.setter
    def width(self, value):
        """ function width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ function height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ function x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ function y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def area(self):
            """ function area """
            return self.width * self.height
    @property
    def display(self):
        """ print the rectangle using '#' character"""
        if self.width == 0 or self.width == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wid in range(self.width)]
            print("")
