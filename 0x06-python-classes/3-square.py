#!/usr/bin/python3
""" class Square definition """


class Square:
    """ presenting a square """

    def __init__(self, size=0):

        """Initializes the data."""

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """ method that returns the area of the square """
        return self.__size ** 2
