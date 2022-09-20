#!/usr/bin/python3
""" 0 Read File """


def read_file(filename=""):
    """ Read a file """
    with open(filename, encoding="utf=8") as myFile:
        print(myFile.read(), end="")
