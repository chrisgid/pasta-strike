from .jsonproperties import *
from .strings import ENCODING
from pathlib import Path
import json


class PastaFile(object):

    def __init__(self, path):
        self.filepath = Path(path)

    def get_pastacollection(self):
        pastacollection = None

        with self.filepath.open(mode='r', encoding=ENCODING) as file:
            pastacollection = json.loads(file.read(), object_hook=self._json_object_hook)

        return pastacollection

    def _json_object_hook(self, obj):
        if GROUP_PROPERTY in obj:
            group = obj[GROUP_PROPERTY]
            subgroup = obj[SUBGROUP_PROPERTY]

            return PastaCollection(group, subgroup, obj[PASTAS_PROPERTY])

        if ALIAS_PROPERTY in obj:
            return Pasta(obj[ALIAS_PROPERTY], obj[VALUES_PROPERTY])


class PastaCollection(object):

    def __init__(self, group, subgroup, pastas):

        self.group = group
        self.subgroup = subgroup
        self.pastas = pastas


class Pasta(object):

    def __init__(self, alias, values):

        self.alias = alias
        self.values = values
