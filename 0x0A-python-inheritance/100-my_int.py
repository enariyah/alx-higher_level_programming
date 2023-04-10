#!/usr/bin/python3
"""It is not allowed to import any module"""


class MyInt(int):
    """ my int class"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
