#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    avlen = len(sys.argv)
    addition = 0
    for i in range(1, avlen):
        addition += int(sys.argv[i])
    print("{}".format(addition))
