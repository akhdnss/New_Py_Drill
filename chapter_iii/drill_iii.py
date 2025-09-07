import re
def drill_1():
    pattern = re.compile(r'\d{4}')
    match = pattern.search("my pin code is 1234. ")
    print(match)

