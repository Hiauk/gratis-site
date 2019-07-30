from template import createPage
from distutils.dir_util import copy_tree
import os

fromDirectory = "css"
toDirectory = "output/css"

copy_tree(fromDirectory, toDirectory)

for filename in os.listdir('pages'):
    with open('pages/' + filename) as f:
        lines = f.read().splitlines()

    parsed = []
    for line in lines:
        item = line.split()
        if len(item) > 0:
            if item[0] == '#':
                parsed.append('<h1>' + line.replace('# ', '') + '</h1>')
            elif item[0] == '##':
                parsed.append('<h2>' + line.replace('## ', '') + '</h2>')
            elif item[0] == '###':
                    parsed.append('<h3>' + line.replace('### ', '') + '</h3>')
            elif item[0] == '####':
                    parsed.append('<h4>' + line.replace('#### ', '') + '</h4>')
            elif item[0] == '#####':
                    parsed.append('<h5>' + line.replace('##### ', '') + '</h5>')
            elif item[0] == '+':
                parsed.append('<li>' + line.replace('+ ', '') + '</li>')
            else:
                parsed.append('<p>' + line + '</p>')

    output_html = createPage(parsed)
    filename = 'output/' + filename + ".html"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write(output_html)
