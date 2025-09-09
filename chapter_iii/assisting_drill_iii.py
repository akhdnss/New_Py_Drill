import re
# DRILL I 
# string = "I have an apple and a banana"
# pattern = re.compile(r'(apple|banana)')
# match = pattern.findall(string)
# print(match) 

# string = "I love Python and also love python"
# pattern = re.compile(r'(Python|python)')
# match = pattern.findall(string)
# print(match)

# string = "My pets are a dog, a cat, and a bird."
# pattern = re.compile(r'(cat|dog|bird)')
# match = pattern.findall(string)
# print(match)

##DRILL II
# string = "The American color is red."
# string_ii = "The British colour is red."
# pattern = re.compile(r'(colo(u)r|)')
# match = pattern.findall(string)


# result = re.match(r'^[a-z]', "apple")
# print(result.group())

# string = "Learning Python Regex is fun"
# result = re.findall(r'python', string, re.IGNORECASE)

# result = re.findall(r'\d+', "I have 12 apples and 30 oranges")

# result = re.sub(r'[aiueo]',"*", "Hello World")

# result = re.search(r'(end$)', "Start middle End", re.IGNORECASE)
# result_ii = re.search(r'^start', "Start Middle End", re.IGNORECASE) 
# print(result, result_ii) ###is there other method to match two conditions in one line of code

# result = re.findall(r'[cbd]\w+', "bat cat dog mat.")

# result = re.findall(r'(gray|grey)|(a+)', "gray grey aa aaaa a")

# result = re.search(r'(\w+)@(\w+\.\w+)', "contact: john.doe@example.com")

result = re.findall(r'<(.*)>',"<p>first</p><p>second</p>" )


print(result)

