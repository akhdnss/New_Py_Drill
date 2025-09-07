import re
string = "Hello World world hello hell helloooo worlddd world"
# result = re.findall("orld", string)
# print(f'result: {result}')

# result_ii = re.search(r'Hello', string)
# if result_ii:
#     print(f'found: {result_ii.group()}')
# else:
#     print(f'not found')

result_iii = re.split(" ", string)
print(result_iii)
result_iv = re.split(r'\sS', string)
print(f"result_iv : {result_iv}")