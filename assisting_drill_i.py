all_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'sandwiches': 3, 'apples': 2, 'cups': 20},
    'Carol': {'cups': 12, 'sandwiches': 5, 'plates': 2},
    'David': {'forks': 10, 'knives': 8, 'plates': 4}
}

# def print_items(guest): 

for guest, items in all_guests.items(): 
    #print(f'GUEST NAME: {guest}')
    for item, count in items.items(): 
        # print(f'item: {item} | count: {count} ')
        print(f'guest name: {guest} brought {item} with {count} quantity')