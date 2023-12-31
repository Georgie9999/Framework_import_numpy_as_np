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
            self.template = re.sub(sub_str1, self.parameters[key], self.template, count=0)
            self.template = re.sub(sub_str2, self.parameters[key], self.template, count=0)

    def extract_if(self, pos: int):
        i = pos

        while not (self.template[i] == '%' and self.template[i + 1] == '}'):
            i += 1

        pos_end_if = i
        if_statement = self.template[pos + 2:pos_end_if]

        pos_end_if_true_data = self.template.find("{% else %}", i)
        if_true_data = self.template[pos_end_if+2:pos_end_if_true_data]

        i = pos_end_if_true_data + 9
        pos_start_else_data = i

        pos_end_else_data = self.template.find("{% endif %}")
        else_data = self.template[pos_start_else_data+1:pos_end_else_data]

        i = pos_end_else_data
        endif_pos = i + 11

        return if_statement, if_true_data, else_data, endif_pos

    def eval_if_statement(self, if_statement):
        if_statement = if_statement[2:]
        res = eval(if_statement, self.parameters)
        return res

    def if_dealing(self):
        f = True
        while(f):
            f = False
            for i in range(len(self.template) - 3):
                if self.template[i] == '{' and self.template[i + 1] == '%' and self.template[i + 3] == 'i':
                    f = True
                    if_statement, if_true_data, else_data, endif_pos = self.extract_if(i + 1)
                    print('state: ', if_statement, if_true_data, else_data, endif_pos, sep='\n')
                    if self.eval_if_statement(if_statement):
                        self.template = self.template.replace(else_data, "", i)
                        endif_pos -= len(else_data)
                    else:
                        self.template = self.template.replace(if_true_data, "", i)
                        endif_pos -= len(if_true_data)
                    self.template = self.template.replace("{% " + if_statement + "%}", "", i)
                    i = endif_pos
                    break

        self.template = self.template.replace("{% endif %}", "")
        self.template = self.template.replace("{% else %}", "")

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

