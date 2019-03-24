from .strings import ALIAS, SAY, END


def alias(key, value):
    return '{}{}{}{}{}'.format(ALIAS, key, SAY, value, END)


def aliases(dictionary):
    aliases = []
    
    for key, value in dictionary.items():
        aliases.append(alias(key, value))

    return ''.join(aliases)


def keyvals(key, values):

    dictionary = {}

    for i in range(len(values)):
        newkey = key + str(i + 1)
        dictionary[newkey] = values[i]

    return dictionary