import re
#drill set 1

# string = 'The year is 2025, not 19999 or 25.'
# pattern = re.findall(r'\b\d{4}\b', string)
# print(pattern) 

# string = 'apple banana cherry'
# result = re.findall(r'\b\w{5}\b', string)
# print(result)

# string = 'Call me at 5551234567 or 12345.'
# result = re.findall(r'\b\d{10}\b', string)
# print(result) 

# string = 'one two three four five six'
# result = re.findall(r'\b[a-z]{3}\b', string)
# print(result)

# string = 'xxx xx xxxxxxx'
# result = re.findall(r'\b[x]{6}\b', string)
# print(result)

## DRILL SET 2

# string = 'The codes are 12, 345, 6789, and 12345.'
# result = re.findall(r'\b\d{2,4}\b', string)
# print(result)

# string = 'ant bear caterpillar elephant.'
# result = re.findall(r'\b\w{5,7}\b', string)
# print(result)

string = 'ID: abc, ID: 1234, ID: 567890'
result = re.findall(r'\b\w{3,5}\b', string)
print(result)