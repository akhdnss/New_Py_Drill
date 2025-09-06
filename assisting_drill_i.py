phonebook = {}
while True: 
    input_name = input("name: ")
    if input_name == "done" or input_name == "quit": 
        print(f'current: {phonebook} ')
        break
    input_number = input("number: ")
    phonebook.setdefault(input_name, input_number)
print(phonebook)