def drill_1():
    car_details = {""
    "make":"honda",
    "model":"civic",
    "year": "2022"
    }

    print(f'car details: {car_details}') # 1. 

    print(f'model: {car_details["model"]} ') #2

    car_details["color"] = "blue" #3

    car_details["year"] = "2023" #4

    print(f'updated: {car_details} ')

def drill_2(): 
    alex_bag = ['hat', 'sunglasses', 'towel']
    ben_bag = ['sunglasses', 'towel', 'hat ']
    if alex_bag == ben_bag: 
        result = True
        print(f'result: {result}')
    else:
        result = False
        print(f'result: {result}')

    alex_gear = {"hat":1, "sunglasses":1, "towel":1}
    ben_gear = {"sunglasses":1, "towel":1, "hat":1}
    if alex_gear == ben_gear: 
        result = True
        print(f'result: {result}')
    else:
        result = False
        print(f'result: {result}')
    #i think it's because dict is pre - ordered and has some value to check with

def drill_3(): 
    car_details = {""
    "make":"honda",
    "model":"civic",
    "year": "2022"
    }
    for key, value in car_details: 
        print(f'key: {key} | value: {value} ')
def drill_4(): 
    student_score = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    value = student_score.get('Alice')
    value_ii = student_score.get('David')
    print(f'value_i: {value} | value_ii: {value_ii} ')
    #as far is i know, get.() function is only better bcs of error handling

def drill_5(): 
    word_counts = {}
    initial_sentence = "The quick brown fox jumps over the lazy dog."
    sen_split = initial_sentence.split()
    for word in sen_split: 
        print(f'word: {word}')
        word_counts.setdefault(word, 0)
        word_counts[word] = word_counts[word] + 1
    print(f'word count: {word_counts}')   
#drill_5()

def drill_6():
    inv = {'sword': 1, 'potion': 5}
    def add_item(inventory, item_name, quantity): 
        if item_name not in inventory: 
            #inventory.setdefault(item_name,quantity)
            #inventory[item_name] = inventory[item_name] + 1
            inventory[item_name] = 1
        else: 
            #inventory[item_name] = inventory[item_name] + 1
            inventory[item_name] += 1
        return inventory.setdefault(item_name, quantity)
    usr_input = "potion"
    usr_quantity = 3
    usr_input_ii = "shield"
    usr_quantity_ii = 1
    add_item(inv, usr_input, usr_quantity)
    add_item(inv, usr_input_ii, usr_quantity_ii)
    print(f'inventory: {inv}')

drill_6()



