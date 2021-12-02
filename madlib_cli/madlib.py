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
    # regex built based off of answers from https://stackoverflow.com/questions/3335562/regex-to-select-everything-between-two-characters
    # original idea was to use {(\w{1,} ?)*} however this did not account for prompts containing punctuation or numbers
    # regex matches any characters between { and }, the ? makes it so that the match ends after the next closing curly bracket rather than the last closing curly in given string
    regex = r'{.*?}'
    stripped = re.sub(regex,'{}',file_contents)
    parts = re.findall(regex, file_contents)
    stripped_parts = []
    for prompt in parts:
        prompt = re.sub(r'{|}','',prompt)
        stripped_parts.append(prompt)
    stripped_parts = tuple(stripped_parts)
    return stripped,stripped_parts
        
