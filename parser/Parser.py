from urllib.parse import urlparse
import re


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

temp = Parser()
result = temp.parse_path('/all/{temp}/{temp2}')
print(result)

res2 = temp.parser_url('http://www.cwi.nl/%7Eguido/Python.html')
print(res2)

