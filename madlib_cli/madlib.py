import re

# regex built based off of answers from https://stackoverflow.com/questions/3335562/regex-to-select-everything-between-two-characters
# original idea was to use {(\w{1,} ?)*} however this did not account for prompts containing punctuation or numbers
# regex matches any characters between { and }, the ? makes it so that the match ends after the next closing curly bracket rather than the last closing curly in given string
PROMPT_REGEX = r'{.*?}'

PROMPT_WRAPPER = '{}'

PROMPT_WRAPPER_REGEX = r'{|}'


def read_template(path):
    """
    Takes in a file path and returns the file contents as a string
    """

    with open(path,'r') as f:
        contents = f.read()
        return contents

def parse_template(path):
    file_contents = read_template(path)
    stripped = re.sub(PROMPT_REGEX,PROMPT_WRAPPER,file_contents)
    parts = re.finditer(PROMPT_REGEX, file_contents)
    stripped_parts = []
    for prompt in parts:
        prompt = re.sub(PROMPT_WRAPPER_REGEX,'',file_contents[prompt.start():prompt.end()])
        print(prompt)
        stripped_parts.append(prompt)
    stripped_parts = tuple(stripped_parts)
    return stripped,stripped_parts
        
parse_template('assets/dark_and_stormy_night_template.txt')
def merge(stripped_template,answers):
    pass