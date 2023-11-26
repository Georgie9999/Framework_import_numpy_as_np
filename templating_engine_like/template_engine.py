from bs4 import BeautifulSoup
import re


class TemplateEngine:
    def __init__(self):
        self.template = ""
        self.parameters = {}

    def set_template_from_html(self, file_name: str):
        with open(file_name, 'r') as f:
            self.template = "".join(line.strip() for line in f)
            self.template = "".join(line.strip() for line in self.template)

    def set_template_from_str(self, str_template: str):
        self.template = str_template

    def set_parameters(self, **kwargs):
        self.parameters = kwargs

    def get_rendered(self):
        self.for_dealing()
        self.replace_substitutions()
        return self.template

    def replace_substitutions(self):
        for key in self.parameters:
            sub_str1 = "{{" + f"{key}" + "}}"
            sub_str2 = "{" + f"{key}" + "}"
            self.template = re.sub(sub_str1, str(self.parameters[key]), self.template, count=0)
            self.template = re.sub(sub_str2, str(self.parameters[key]), self.template, count=0)

    def if_dealing(self):
        pass

    def for_dealing(self):
        while self.template.find("{%for") != -1:
            for_start = self.template.find("{%for")
            for_end = self.template.find("%}", for_start)
            result_for_string = self.template[for_start:for_end].split("in")
            value_in_for = result_for_string[0][5:]
            key_array = result_for_string[-1]
            for_string = self.template[for_end: self.template.find("{%endfor%}")][2:]
            result_string = ""
            sub_str = "{{" + f"{value_in_for}" + "}}"
            for x in self.parameters[key_array]:
                new_string = re.sub(sub_str, x, for_string, count=0)
                result_string += new_string
            self.template = self.template.replace(
                self.template[for_start: self.template.find("r%}", for_start) + 3], result_string)
            del self.parameters[key_array]

