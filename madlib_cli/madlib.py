import re


def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error


def parse_template(string):
    pieces = tuple(re.findall(r"{([^{}]*)}", string))
    for x in pieces:
        string = string.replace(x, "")
    return string, pieces


def merge(stripped, inputs):
    return stripped.format(*inputs)


welcome = """
Mad Libs: Enter words when prompted to complete the story.
"""

print(welcome)


script = read_template("assets/madlib.txt")
empty_string, parts = parse_template(script)
filled_list = []
for i in parts:
    user_input = input(f" Enter {i} > ")
    filled_list.append(user_input)
result = merge(empty_string, filled_list)
print(result)
with open('assets/result.txt', 'w') as writer:
    writer.write(result)