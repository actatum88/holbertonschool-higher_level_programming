#!/usr/bin/python3
""" Module 2-read_lines. """


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns number of characters added."""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
