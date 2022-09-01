#!/usr/bin/python3
from sys import argv
__name__ == "__main__"
if len(argv) == 1:
    print("0 arguments.")
else:
    s = "arguments"
    print("{} {}:".format(len(argv) - 1, s[:-1] if len(argv) == 2 else s))
    for x in range(1, len(argv)):
        print("{}: {}".format(x, argv[x]))
