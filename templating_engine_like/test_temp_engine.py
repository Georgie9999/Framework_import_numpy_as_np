import template_engine

if __name__ == '__main__':
    temp = template_engine.TemplateEngine()

    temp.set_template_from_html('../templates/first_html.html')
    temp.set_parameters(name="mem", lastname="cringe")
    temp.set_parameters(name="mem", lastname="cringe", score=90)

    print(temp.template)
    print(temp.parameters)
    temp.if_dealing()

    temp.eval_if_statement("if len(name) < 5")

    temp.replace_substitutions()
    print(temp.template)