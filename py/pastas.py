from .strings import DOTJSON, UTF_8
from pathlib import Path
import json


class PastaFile(object):

    def __init__(self, path):
        self.filepath = Path(path)

    def get_pastacollection(self):
        pastacollection = None

        with self.filepath.open(mode='r', encoding=UTF_8) as file:
            pastacollection = json.loads(file.read(), object_hook=self._json_object_hook)

        return pastacollection

    def _json_object_hook(self, obj):
        if 'group' in obj:
            group = obj['group']
            subgroup = obj['subgroup']

            return PastaCollection(group, subgroup, obj['pastas'])

        if 'alias' in obj:
            return Pasta(obj['alias'], obj['values'])


class PastaCollection(object):

    def __init__(self, group, subgroup, pastas):

        self.group = group
        self.subgroup = subgroup
        self.pastas = pastas


class Pasta(object):

    def __init__(self, alias, values):

        self.alias = alias
        self.values = values
