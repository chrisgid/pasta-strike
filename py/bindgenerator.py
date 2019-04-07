from .strings import ALIAS, SAY, END


def generate_binds_str(pastacollection):
    binds = []

    for pasta in pastacollection.pastas:
        binds.extend(generate_binds(pasta))

    return ''.join(binds)


def generate_binds(pasta):
    binds = []

    if len(pasta.values) == 1:
        binds.append(_generate_single(pasta.alias, pasta.values[0]))
    elif len(pasta.values) > 1:
        binds.extend(_generate_multi(pasta))

    return binds


def _generate_multi(pasta):
    binds = []

    for i in range(len(pasta.values)):
        alias = pasta.alias + str(i + 1)
        value = pasta.values[i]
        binds.append(_generate_single(alias, value))

    return binds


def _generate_single(alias, value):
    return '{}{}{}{}{}'.format(ALIAS, alias, SAY, value, END)
