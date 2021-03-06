import re

TEMPLATE_PATH = 'assets/dark_and_stormy_night_template.txt'

OUTPUT_PATH = 'assets/completed_madlib.txt'

FORBIDDEN_CHARS = ('\"{\"','\"}\"')

GREETING = '''Welcome to Madlib CLI!
You will be prompted to enter a series of words in the terminal.
Have fun!'''
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

def get_match_locations(file_contents):
    '''
    Takes in a string as input, returns an iterable containing Match objects
    '''
    part_matches = re.finditer(PROMPT_REGEX, file_contents)
    return part_matches

def strip_template(file_contents):
    '''
    Takes in a string as input, returns same string but with the prompts stripped
    '''
    stripped = re.sub(PROMPT_REGEX,PROMPT_WRAPPER,file_contents)
    return stripped

def parse_template(file_contents):
    '''
    Parses input string, returns a tuple containing the stripped input string
    and a tuple containg the prompts in the order that they were stripped
    '''
    stripped = strip_template(file_contents)
    parts = get_match_locations(file_contents)
    stripped_parts = []
    for prompt in parts:
        #prompt = re.sub(PROMPT_WRAPPER_REGEX,'',file_contents[prompt.start():prompt.end()])
        prompt = re.sub(PROMPT_WRAPPER_REGEX,'',prompt.group())
        #print(prompt)
        stripped_parts.append(prompt)
    stripped_parts = tuple(stripped_parts)
    return stripped,stripped_parts
        
#parse_template('assets/dark_and_stormy_night_template.txt')
def merge(stripped_template,answers):
    '''
    Merges the stripped template string with answers given by the user
    '''
    parts = tuple(get_match_locations(stripped_template))
    for i in range(len(parts)):
        stripped_template = re.sub(PROMPT_REGEX,answers[i],stripped_template,1)
    return stripped_template

def play(path):
    try:
        file_contents = read_template(path)
        print(GREETING)
        parsed_template = parse_template(file_contents)
        answers = []
        for i in range(len(parsed_template[1])):
            user_in = input(f'Please enter a(n) {parsed_template[1][i]}:\n> ')
            while not len(re.findall(PROMPT_WRAPPER_REGEX,user_in)) == 0:
                message = 'Answer cannot contain '
                for i in range(len(FORBIDDEN_CHARS) - 1):
                    message += f' {FORBIDDEN_CHARS[i]} or'
                message += f' {FORBIDDEN_CHARS[len(FORBIDDEN_CHARS) - 1]}'
                print(message)
                user_in = input(f'Please enter a(n) {parsed_template[1][i]}:\n> ')
            answers.append(user_in)
        output = merge(parsed_template[0],answers)
        print(output)
        with open(OUTPUT_PATH,'w') as f:
            f.write(output)
    except FileNotFoundError:
        print('File Not Found.')
    except: 
        print('Something went wrong.')
play(TEMPLATE_PATH)