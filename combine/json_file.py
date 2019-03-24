import json
from pathlib import Path

UTF_8 = 'UTF-8'
DOTJSON = '.json'

class JsonFile(object):

    def __init__(self, path):

        self.path = Path(path)
        self._validate_path(self.path)


    def _validate_path(self, path):

        if not (path.exists()):
            raise FileNotFoundError('"{}" does not exist.'.format(path))

        if not (path.is_file()):
            raise ValueError('"{}" is not a file.'.format(path))

        if path.suffix != DOTJSON:
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