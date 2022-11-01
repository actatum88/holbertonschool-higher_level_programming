#!/usr/bin/python3
"""Fetches status from Holberton Intranet"""

if __name__ == '__main__':
    import urllib.request
    
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(str(html)))
        print('\t- utf8 content: {}'.format(response.read().decode('utf8')))
    