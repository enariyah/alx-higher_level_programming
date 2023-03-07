#!/usr/bin/python3
for i in range(ord(chr(122)), ord(chr(97)) - 1, -2):
    print("{:c}{:s}".format(i, chr(i - 33)), end="")
