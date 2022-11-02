#!/bin/bash/python3

"""catches errors from requests"""
import urllib.request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))