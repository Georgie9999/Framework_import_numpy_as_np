from bs4 import BeautifulSoup


class TemplateEngine:
    def __init__(self):
        self.template = ""

    def set_template_from_html(self, file_name: str):
        with open(file_name, 'r') as f:
            self.template = "".join(line.strip() for line in f)

    def set_template_from_str(self, str_template: str):
        self.template = str_template

    def set_parameters(self, **kwargs):
        pass

    def get_rendered(self):
        pass

    def replace_substitutions(self):
        pass

    def if_dealing(self):
        pass

    def for_dealing(self):
        pass
