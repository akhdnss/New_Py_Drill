import re
# # text = "one two three four"
# # result = re.split(r' ', text)
# # print(result)

# # text = "apple,banana;grape,orange"
# # result = re.split(r'[,|;]', text) wrong! you dont need | inside the charachter class: []
## result = re.split(r',|;, text) OR re.split(r'[,;], 'text)
# # print(result)

# # text = "word1     word2  word3"
# # result = re.split(r' +| ', text) WORKS BUT
# # result = re.split(r' +', text) is more simplified
# # print(result)

# # text = "apple1banana2grape3"
# # result = re.split(r'\d', text)
# # print(result)

# text = "abc123@#def!"
# result = re.split(r'\D', text)
# print(result)

# text = "abc123@#def!"
# result = re.split(r'[^a-zA-Z]+', text)
# print(result)

# text = "Hello, world! How are you? I'm fine."
# result = re.split(r'[,!?.]', text)
# print(result)

# text = "a1b22c333d4444e"
# result = re.split(r'\d+', text)
# print(result)

# text = "camelCaseTestString"
# results = re.split(r'(?<=[a-z])(?=[A-Z])', text)
# print(results)

# text = 'PascalCase'
# result = re.split(r'(?<=[a-z])(?=[A-Z])', text)
# print(result)

text = "parseHTTPResponse"
result = re.split(r'(?=[A-Z])(?=[A-Z]{4})(?<=[a-z])', text)
print(result)