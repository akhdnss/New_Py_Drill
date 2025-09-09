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

# string = 'ID: abc, ID: 1234, ID: 567890'
# result = re.findall(r'\b\w{3,5}\b', string)
# print(result)

# string = '12-345 123-4567 1-23 123-456'
# result = re.findall(r'\b(\d{2}-\d{3})\b', string)
# print(result)

# string = 'Prices: $5, $100, $25.50, $2.'
# # result = re.findall(r'\b([$0-9]{1,2})\b', string)
# result = re.findall(r'\b\$\d{1,2}\b', string)
# print(result)

##DRILL SET III

# string = 'The quote is "Hello, world!" and "Goodbye, world!"'
# # result = ### dont know yet, might need some hint in drill set iii
# result = re.findall(r'"(.*?)"', string)

# string = '1234-5678-9012-3456 and 1234567890123456'
# # result = re.findall(r'\d{4}-?\d{4}-?\d{4}-?\d{4}', string)

# result = re.findall(r'(?:\d{4}-?){4}', string)

# result_ii = re.findall(r'(\d{4}-?){4}', string)
# print(result_ii)

# string = "cat car cup ice cream cycle"
# result = re.findall(r'c', string)

# string = "hello"
# result = re.findall(r'.', string)


# string = "Room 101, Room 202B, Room-303!"
# result = re.findall(r'\d{3}', string)
# result_ii = re.findall(r'Room[- ]\d{3}[A-Z]?', string)
# print(f'result_ii: {result_ii}') 



# string = "Items: A-123, B-99X, C-4567, D-88, E-100A"
# result = re.findall(r'\d{1,5}', string)
# result_ii = re.findall(r'[A-Z]-\d{1,5}[A-Z]?', string)
# print(result_ii)


# string = "run runner running ran run! fucking"
# result = re.findall(r'\brun\b', string)
# result_ii = re.findall(r'\w+ing', string)
# print(f'result ii: {result_ii}')

# import re

string = "Hello world. Regex is fun! Do you agree?"
result = re.findall(r'(^.+)', string)


print(f'result: {result}')
