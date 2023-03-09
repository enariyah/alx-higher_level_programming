#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    avlen = len(sys.argv)
    if avlen == 1:
        print("0 arguments.")
    elif avlen == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(avlen - 1))
    for i in range(1, avlen):
        print("{}: {}".format(i, sys.argv[i]))
