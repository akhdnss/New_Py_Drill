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
# pattern = re.compile(r'\d{3}')
# match = re.findall(pattern, "the number is 123, 456, and 789")
# print(match)

# #drill iv
# string = "Hello_World! 123."
# pattern = re.compile(r'\D')
# match = re.search(pattern, string )

# print(match)

#NEW DRILL i
# pattern = re.compile(r'\d{4}')
# match = pattern.search("My pin code is 1234. ")
# print(match.group())


# NEW DRILL ii
# string = 'Your order number is ABC-123-XYZ'
# pattern = re.compile(r'([A-Z]{3})-([0-9]{3})-([A-Z]{3})')
# match = pattern.search(string)
# print(match.groups())

#NEW DRILL III
# string = 'The numbers are 123, 456, and 789.'
# type_list = re.findall(r'\d{3}', string)
# type_tuples = re.findall(r'(\d{3})', string)

# print(f'tuples: {type_tuples} | list or str: {type_list} ')

# #NEW DRILL IV
# string = "Hello_world! 123"
# pattern = re.compile(r'(\w+)')
# match = re.findall(pattern, string)
# print(f'all words found: {match}')
# whitespace_pattern = re.compile(r'(\s+)')
# all_whitespace = re.findall(whitespace_pattern, string)
# print(f'all whitespace found: {all_whitespace} ')
# nondigit_pattern = re.compile(r'(\D+)')
# all_non_digit = re.findall(nondigit_pattern, string)
# print(f'all non digit values: {all_non_digit}')

# # NEW DRILL V
# string = "The movie features Batman and Superman."
# pattern = re.compile(r'Batman|Superman')
# pattern_i = re.compile(r'man|woman')
# match = re.findall(pattern, string)
# match_i = re.findall(pattern_i, string)
# string_ii = "I am a hero and a heroine."
# pattern_ii = re.compile(r'hero(ine|)')
# pattern_iii = re.compile(r'ine|')
# match_iii = re.findall(pattern_iii, string_ii)
# match_ii = re.findall(pattern_ii, string_ii)
# print(match, match_ii, match_i, match_iii)

# ## NEW DRILL VI
# string = 'John F. Kennedy was president'
# string_ii = 'John was his first name'
# pattern = re.compile(r'John|John F')
# pattern_ii = re.compile(r'John( F\.?)?')
# match_i = re.findall(pattern, string)
# match_ii = re.findall(pattern, string_ii)
# match_iii = re.findall(pattern_ii, string)
# match_iv = re.findall(pattern_ii, string_ii)

# print(match_i, match_ii, match_iii, match_iv)

#question
#q1 return the splitted string between "Hello" and "World"
#q2 return the splitted string "Camel", "Case", and "Split"
#q3 because it doesnt check the previous letter (should've used (?<=) )
#q4 (?=[1-9]) (?<=[a-z]) 
#q5 no because ^ is a negation. so it would NOT match any lowercase in the string
#q6 it splits the semicolon, spaces, and comma
#q7 the diff is the second code checks the privous condition if its a lowercase (idk the difference of each output tho)
#q8 splits between the digit and upper capital words (previously checked if the condition is digit by using (\d) and after by using [a-z])
#q9 the output = ["Hello", "WORLD"]
#q10 below:
# target = "fooBARbazQUX"
# pattern = r'(?<=[a-z])(?=[A-Z])'
# value = re.split(pattern, target)
# print(value)


## quiz 2
#q1
result = re.match(r'^[a-z]', "apple")
print(result.group() if result else None)