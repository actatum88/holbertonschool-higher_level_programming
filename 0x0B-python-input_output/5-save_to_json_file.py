#!/usr/bin/python3
""" Module 5-save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON representation (dump) """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)