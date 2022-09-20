#!/usr/bin/python3
""" Module 0-read_file.py """


def read_file(filename=""):
    """ Reads a text file and prints to stdout. utf-8 is standard if encoding is not specific. """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
