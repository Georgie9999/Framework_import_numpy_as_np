import template_engine

if __name__ == '__main__':
    temp = template_engine.TemplateEngine()

    temp.set_template_from_html('../templates/first_html.html')
    temp.set_parameters(name="mem", lastname="cringe", score=90)
    final = temp.get_rendered()
    print(final)
    # print(temp.template)
    # print(temp.parameters)
    # temp.if_dealing()
    #
    # temp2 = template_engine.TemplateEngine()
    #
    # temp2.set_template_from_html('../templates/second_html.html')
    # temp2.set_parameters(test_name="mem", students=["Ivan", "Masha", "Nikolay"], score="1")
    # print(temp2.template)
    # final = temp2.get_rendered()
    # print(final)
