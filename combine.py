from py import generate
from py import strings
from py import JsonFile
from os import path, walk
from pathlib import Path as PathLibPath

''' 
This script combines all copypastas
in /split to pasta-strike.cfg
'''

if __name__ == '__main__':

    currentpath = path.dirname(__file__)
    splitpath = path.join(currentpath, strings.SPLIT)
    outputpath = path.join(currentpath, strings.PASTA_STRIKE_CFG)

    splitfiles = []

    # Find all .json files in /split
    for subdir, dirs, files in walk(splitpath):

        for filename in files:

            filepath = path.join(subdir, filename)
            pathcheck = PathLibPath(filepath)

            if (pathcheck.suffix == strings.DOTJSON):

                jsonfile = JsonFile(filepath)
                splitfiles.append(jsonfile)


    ## Write to config
    with open(outputpath, 'w+', encoding=strings.UTF_8) as config:

        filecount = 1

        for file in splitfiles:

            print(strings.WRITING.format(filecount, len(files)))
            filecount += 1

            dictionary = file.get_data()

            for key, value in dictionary.items():

                if isinstance(value, list):

                    keyvals = generate.keyvals(key, value)
                    aliases = generate.aliases(keyvals)
                    config.write(aliases)

                elif isinstance(value, str):

                    alias = generate.alias(key, value)
                    config.write(alias)

        print(strings.DONE)