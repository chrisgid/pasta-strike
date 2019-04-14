from py import strings, Combiner
from os import path

'''Combines all copypastas in /pastas to pasta-strike.cfg'''


def main():
    currentpath = path.dirname(__file__)
    pastapath = path.join(currentpath, strings.PASTADIR)
    outputpath = path.join(currentpath, strings.PASTA_STRIKE_CFG)

    combiner = Combiner(pastapath)
    combiner.combine(outputpath)


if __name__ == '__main__':
    main()
