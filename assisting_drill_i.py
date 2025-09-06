adress_book = {"john":{"phone":5555, "email":"@gmail.com"}, 
               "jane":{"phone":9999, "email": "@yahoo.com"}} 

#print(f'initial: {adress_book} ')
#for x, y in adress_book.items(): 
    #print(f'x: {x} | y: {y} ')

for x in adress_book.get("john"): 
    # print(type(x))
    print(adress_book["john"][x])


