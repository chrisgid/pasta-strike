import string
from pathlib import Path
from .strings import KEY_MIN_LEN

class Adder(object):
    '''Adds new pastas to the list of .json files'''

    def __init__(self, pastapath):
        self.path = Path(pastapath)

    def add(self, key, value):
        if len(key) < KEY_MIN_LEN:
            raise ValueError('Key length should be {} characters in length minimum'.format(KEY_MIN_LEN))

        # Assume .json files are listed [#,a,b...,z] (for now)
        azlist = list(string.ascii_lowercase)

        if key[0] in azlist:
            pass

# TESTING
if __name__ == '__main__':
    print('hello')
    adder = Adder('C:\Repositories\pasta-strike\split\c.json|||//""')