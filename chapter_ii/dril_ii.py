def drill_i(): 
    num_i = "hello, who's there"
    num_ii = r"it's a beautiful day, isn't it? "
    print(num_ii)
    num_iii = "test, since i dont wanna waste time writing poem, \nI'm just gonna write this"

def drill_2(): 
    s = "Python programming"
    print(f'first index: {s[0]}')
    print(f'last index: {s[-1]}')
    print(f'first word: {s[:6]}')
    print(f'last word: {s[6:]}')
    print(f'gram: {s[10:-4]}')
# drill_2()

def drill_3(usr_word, usr_sentence):
    value = False
    if usr_word in usr_sentence.split(): 
        value = True
    return value

def drill_4(item_name, price): 
    # item_name = "laptop"
    # price = 999.99
    print("the item, {} costs ${}".format(item_name, price))
    print("the item %s costs $%s"%(item_name, price))


def drill_5(usr_name): 
    converted_up = usr_name.upper()
    converted_down = usr_name.lower()
    print(usr_name.isupper())
    print(f'converted up: {converted_up}, converted down: {converted_down} ')

# drill_5("Hello")

def drill_6(age, password): 
    value = age.isdecimal()
    if value == True:
        print(f'the age is valid')
    else:
        print(f'invalid! ')
    value_ii = password.isalnum()
    if value_ii == True: 
        print(f'the password is valid! ')
    else: 
        print(f'invalid! ')

# drill_6("10", "hello123")

def drill_7(list_of_words):
    join_method = ' '.join(list_of_words)
    split_method = join_method.split()
    split_method_ii = join_method.split(",")
    print(f'1. {join_method} | 2. {split_method} | 3. {split_method_ii}')

# drill_7(["apple","banana", "orange"]) 

def drill_8(string): 
    print(string.rjust(15))
    print(string.ljust(15))
    print(string.center(15, "*"))
    # rando = "*"

# drill_8("hello")

def drill_9(string): 
    print(f'stripped: {string.strip()}')
    print(f'lstripped: {string.lstrip()}')
    print(f'rstripped: {string.rstrip()}')
    print(f'stripsen: {string.strip("x")}')

def dril_10(): 