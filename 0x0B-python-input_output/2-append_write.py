#!/usr/bin/python3
""" Module 2-read_lines. """


def append_write(filename="", text=""):
    """Append string at the end """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
