#!/usr/bin/python3
"""fetches url with requests package"""


if __name__ == '__main__':
    import requests

    resp = req.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))