import re
def drill_1(string): 
    result = re.findall(r'\b\w{3}\b', string)
    return result
def drill_2(string): 
    return re.findall(r'\b\w{2,4}\b', string)
def drill_3(string): 
    return re.findall(r'\w+\d+\b', string) 
def drill_4(string): 
    return re.findall(r'\w+s?\b', string)
def drill_5(string): 
    return f" first result: {re.findall(r'(.)\1+', string)} | second result: {re.findall(r'\b\w*(.)\1+\w*\b')} " 
print(drill_5("look at the baloon"))