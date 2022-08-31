#!/usr/bin/python3
for x in range(9):
    for y in range(x + 1, 10):
        if x == 8:
            print("{}{}".format(x, y), end="\n")
        else:
            print("{}{}".format(x, y), end=", ")
