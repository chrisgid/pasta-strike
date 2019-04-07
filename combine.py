from py import bindgenerator, strings, pastas, PastaFile
from os import path, walk
from pathlib import Path as PathLibPath

'''
This script combines all copypastas
in /split to pasta-strike.cfg
'''

if __name__ == '__main__':

    currentpath = path.dirname(__file__)
    splitpath = path.join(currentpath, strings.PASTADIR)
    outputpath = path.join(currentpath, strings.PASTA_STRIKE_CFG)

    splitfiles = []

    # Find all .json files in /split
    for subdir, dirs, files in walk(splitpath):

        for filename in files:

            filepath = path.join(subdir, filename)
            pathcheck = PathLibPath(filepath)

            if (pathcheck.suffix == strings.DOTJSON):

                pastafile = PastaFile(filepath)
                splitfiles.append(pastafile)

    # Write to config
    with open(outputpath, 'w+', encoding=strings.UTF_8) as config:

        filecount = 1

        for file in splitfiles:

            print(strings.WRITING.format(filecount, len(splitfiles)))
            filecount += 1

            pastacollection = file.get_pastacollection()

            binds = bindgenerator.generate_binds_str(pastacollection)

            config.write(binds)

        print(strings.DONE)
