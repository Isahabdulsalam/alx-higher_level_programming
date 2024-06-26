#!/usr/bin/python3
"""Script to fetches the URL: https://intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(content)))
        print('\t- content: {_content}'.format(_content=content))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_content))
