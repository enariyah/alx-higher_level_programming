#!/usr/bin/python3
""" class Square definition """


class Square:
    """ presenting a square """

    def __init__(self, size=0):

        """Initializes the data."""

        self.__size = size

    @property
    def size(self):
        """ retrive the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets a size for a value """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):

        """ method that returns the area of the square """
        return self.__size ** 2
