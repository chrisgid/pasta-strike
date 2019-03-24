from .strings import DOTJSON, UTF_8
from pathlib import Path
import json

class JsonFile(object):

    def __init__(self, path):

        self.path = Path(path)
        self._validate_path()


    def _validate_path(self):

        if not (self.path.exists()):
            raise FileNotFoundError('"{}" does not exist.'.format(self.path))

        if not (self.path.is_file()):
            raise ValueError('"{}" is not a file.'.format(self.path))

        if self.path.suffix != DOTJSON:
            raise ValueError('File is not of type {}'.format(DOTJSON))


    def _validate_data(self, data_dictionary):

        for key, value in data_dictionary.items():
            if not isinstance(value, (list, str)):
                    raise ValueError('JSON values must be strings or string arrays')


    def get_data(self):

        json_dictionary = None

        with self.path.open(mode='r', encoding=UTF_8) as file:
            json_dictionary = json.loads(file.read(), encoding=UTF_8)

        if not isinstance(json_dictionary, dict):
            raise ValueError('JSON is incorrectly formatted')

        self._validate_data(json_dictionary)

        return json_dictionary