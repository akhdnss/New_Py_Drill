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


result = re.match(r'^[a-z]', "apple")
print(result.group())