import template_engine

if __name__ == '__main__':
    temp = template_engine.TemplateEngine()

    temp.set_template_from_html('../templates/first_html.html')
    print(temp.template)
