class TemplateEngine:
    def __init__(self):
        self.template = ""

    def set_template_from_html(self, file_name: str):
        pass

    def set_template_from_str(self, str_template: str):
        self.template = str_template

    def set_parameters(self, **kwargs):
        pass

    def get_rendered(self):
        pass

    def replace_substitutions(self):
        pass

    def if_deaing(self):
        pass

    def for_dealing(self):
        pass