from os import path, walk
from pathlib import Path as PathLibPath
from .pastas import PastaFile
from .strings import DOTJSON, ENCODING, WRITING, DONE
from .bindgenerator import generate_binds_str


class Combiner(object):

    def __init__(self, pastapath):
        self.pastapath = pastapath

    def combine(self, configpath):
        '''Combine all .json files in pastapath to configpath'''
        pastafiles = self._get_pasta_files()
        self._write_to_config(pastafiles, configpath)

    def _get_pasta_files(self):
        '''Find all .json files in the path provided and '''
        pastafiles = []

        for subdir, dirs, files in walk(self.pastapath):
            for filename in files:
                filepath = path.join(subdir, filename)
                pathcheck = PathLibPath(filepath)

                if (pathcheck.suffix == DOTJSON):
                    pastafile = PastaFile(filepath)
                    pastafiles.append(pastafile)

        return pastafiles

    def _write_to_config(self, pastafiles, configpath):
        '''Write all pastas to the config'''

        with open(configpath, 'w+', encoding=ENCODING) as config:
            filecount = 0

            for file in pastafiles:
                filecount += 1

                print(WRITING.format(filecount, len(pastafiles)))

                pastacollection = file.get_pastacollection()

                binds = generate_binds_str(pastacollection)

                config.write(binds)

            print(DONE)
