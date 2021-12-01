import re

def merge():
    pass

def read_template(path):
    """
    Takes in a file path and returns the file contents as a string
    """

    with open(path,'r') as f:
        contents = f.read()
        return contents

def parse_template(file_contents):
    regex = r'{.*?}'
    return re.sub(regex,'{}',file_contents)

print(parse_template(read_template('assets/dark_and_stormy_night_template.txt')))