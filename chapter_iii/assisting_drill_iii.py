import re
#drill i
# pattern = re.compile(r'\d{4}')
# match = pattern.search("my pin is 3333")
# print(f'match: {match.group()} ')

#drill ii
# string = "Your order number is ABC-123-XYZ"
# pattern = re.compile(r'([A-Z]{3})-([0-9]{3})-([A-Z]{3})')
# match = pattern.search(string)
# print(match.group(), "GROUP 1")
# print(match.group(2), "GROUP 2")
# print(match.groups(), "match groups")

# drill iii
pattern = re.compile(r'\d{3}')
match = re.findall(pattern, "the number is 123, 456, and 789")
print(match)