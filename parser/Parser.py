import json
from urllib.parse import urlparse
import re

import requests


class Parser:
    def __init__(self):
        self.dict_parser = {}
    def parse_path(self, path: str) -> dict:
        self.dict_parser['path_from_root'] = re.findall('/(.*?)/', path)
        self.dict_parser['params'] = set(re.findall("{(.*?)}", path))
        return self.dict_parser
    def parser_url(self, url_path: str):
        result = urlparse(url_path)
        return result

    def parse_data_model(self, byte_str, obj):
        body = json.loads(byte_str.decode())
        for key, _ in obj.__dict__.items():
            if not key.startswith("__") and not key.endswith("__"):
                if body[key]:
                    setattr(obj, key, body[key])
        return obj

if __name__ == "__main__":
    temp = Parser()
    result = temp.parse_path('/all/{temp}/{temp2}')
    print(result)

    res2 = temp.parser_url('http://www.cwi.nl/%7Eguido/Python.html')
