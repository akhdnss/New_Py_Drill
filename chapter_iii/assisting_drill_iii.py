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

## DRILL 2 optional quantifier
# string_i = 'The American color is red. '
# string_ii = 'The British colour is red. '
# pattern = re.compile(r'(colou?r)')
# match_american = pattern.findall(string_i)
# match_british = pattern.findall(string_ii)
# print(f'american: {match_american} | british: {match_british} ')

# string = "My favourite word is regex. "
# string_ii = "My favorite word is regex. "
# pattern = re.compile(r'(favou?rite)')
# first_match = pattern.findall(string)
# second_match = pattern.findall(string_ii)
# print(f'first match: {first_match} | second match: {second_match} ')

#first_num = "415-555-1234"
#pattern = re.compile(r'()') i dont know it yet

string = 'The users are Alice, Bob, and Alice7.'
pattern = re.compile(r'(Alice|Bob)')
print(f'updated: {pattern.findall(string)}')
