import re

# text = "<span>one</span><span>two</span><span>three</span>"
# result = re.findall(r'<.*?>', text)
# result_ii = re.findall(r'<.*>', text)

# print(f'non greedy: {result}\ngreedy: {result_ii}')

# text = "cat dog bird aa aaaa a"
# result = re.findall(r'(?:[bcd]\w+|a+)', text)

# print(result)

# text = "emails: john.doe@example.com, jane_doe@mail.org"
# result = re.finditer(r'([\w.]+)@(\w+\.\w+)', text)

# # print(f'username: {result.group(1)} | domain: {result.group(2)}')
# for x in result:
#     print(f'username: {x.group(1)} | domain: {x.group(2)} ')

text1 = "Hello amazing World"
text2 = "Hello World!"
# pattern = re.compile(r'^hello',re.IGNORECASE) and re.compile(r'world?', re.IGNORECASE)
# result = bool(pattern.search(text1))
# result_ii = bool(pattern.search(text2))
## advanced: result = bool(re.search(r'^Hello', text1, re.IGNORECASE) and re.search(r'World$', text1, re.IGNORECASE))
result = bool(re.search(r'^hello', text1, re.IGNORECASE) and re.search(r'world$', text1, re.IGNORECASE))
result_ii = bool(re.search(r'^hello', text2, re.IGNORECASE) and re.search(r'world$', text2, re.IGNORECASE))
print(f'result from text 1: ({text1}) is {result} ')
print(f'result from text 2: ({text2}) is {result_ii} ')

# text = "color colour aa aaa a"
# result = re.findall(r'(?:colou?r|a+)', text)
# print(result)