import string
from pathlib import Path
from .strings import KEY_MIN_LEN

class Adder(object):
    """description of class"""

    def __init__(self, splitpath):
        self.path = Path(splitpath)

    def add(key, value):
        if len(key) < KEY_MIN_LEN:
            raise ValueError('Key length should be {} characters in length minimum'.format(KEY_MIN_LEN))

        # Assume .json files are listed [#,a,b...,z] (for now)
        azlist = list(string.ascii_lowercase)

        if key[0] in azlist:
            pass

# TESTING
if __name__ == '__main__':
    print('hello')
    print(s)
    adder = Adder('C:\Repositories\pasta-strike\split\c.json|||//""')