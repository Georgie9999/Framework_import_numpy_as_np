import re

class Parser:
    def __init__(self):
        self.dict_parser = {}
    def parse_path(self, path) -> dict:
        self.dict_parser['path_from_root'] = re.findall('/(.*?)/', path)
        self.dict_parser['params'] = set(re.findall("{(.*?)}", path))
        return self.dict_parser
    

temp = Parser()
result = temp.parse_path('/all/{temp}/{temp2}')

print(result)

