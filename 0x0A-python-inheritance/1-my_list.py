#!/usr/bin/python3
"""list in acssending order"""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        """print in acsending and sort"""

        if issubclass(MyList, list):
            print(sorted(self))
