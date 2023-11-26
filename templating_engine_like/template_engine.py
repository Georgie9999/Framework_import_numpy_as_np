from bs4 import BeautifulSoup
import re


class TemplateEngine:
    def __init__(self):
        self.template = ""
        self.parameters = {}

    def set_template_from_html(self, file_name: str):
        with open(file_name, 'r') as f:
            self.template = "".join(line.strip() for line in f)

    def set_template_from_str(self, str_template: str):
        self.template = str_template

    def set_parameters(self, **kwargs):
        self.parameters = kwargs

    def get_rendered(self):
        pass

    def replace_substitutions(self):
        for key in self.parameters:
            sub_str = "{{" + f"{key}" + "}}"
            self.template = re.sub(sub_str, self.parameters[key], self.template, count=0)

        return self.template

    def if_dealing(self):
        pass

    def for_dealing(self):
        pass
