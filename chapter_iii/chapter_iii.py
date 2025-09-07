# import re
# String = 'The year is 2025, not 19999 or 25.'
# result = re.findall(r'(\w{4})', String)
# print(result)

import re
String = "apple banana cherry"
result = re.findall(r'\w{5}', String)
print(result)