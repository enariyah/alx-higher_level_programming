#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        val = fct(*args)
    except ZeroDivisionError:
        val = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        val = None
        sys.stderr.write("Exception: list index out of range\n")
    return val
