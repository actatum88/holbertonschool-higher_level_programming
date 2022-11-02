#!/usr/bin/python3
"""takes a url and email from args to do a POST request"""
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    email = request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
