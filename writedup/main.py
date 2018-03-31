import argparse
import os

from docxtpl import DocxTemplate, Listing
from jinja2 import Environment, meta

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',
                    help='Path of the docx file.')

jinja_env = Environment()

def main():
    args = parser.parse_args()
    file_path = os.path.abspath(args.file)
    assert os.path.exists(os.path.abspath(file_path)), "file doesn't exist"

    tpl = DocxTemplate(file_path)
    ast = jinja_env.parse(tpl.patch_xml(tpl.get_xml()))
    variables = meta.find_undeclared_variables(ast)

    print("Variables: ", variables)

    context = {}

    for variable in variables:
        print("Enter value of variable {}({})".format(
            variable,
            variable.replace('_', '')))
        line = input("> ")
        lines = []
        while line != 'end':
            lines.append(line)
            line = input("> ")

        line = '\n'.join(lines)
        context[variable] = Listing(line)

    print("context: ", context)
    tpl.render(context)
    tpl.save("generated.docx")

if __name__ == '__main__':
    main()
