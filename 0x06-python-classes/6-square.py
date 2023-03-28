#!/usr/bin/python3
""" class Square definition """


class Square:
    """ presenting a square """

    def __init__(self, size=0, position=(0, 0)):

        """Initializes the data."""

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ retrive position """
        return self.__position

    @position.setter
    def position(self, value):
        """ set postion for a value """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """ method that returns the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ prints stdout with # character """
        if self.__size == 0:
            print()
        for p in range(0, self.__position[1]):
            print()
        for s in range(0, self.__size):
            for p in range(0, self.position[0]):
                print(" ", end="")
            print(self.__size * '#')
