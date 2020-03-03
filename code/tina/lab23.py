# /n spare rows in the csv





contact = []
with open("contact.csv", 'r') as file:
    lines = file.read().split('\n')
    
    con2 = []
    key = lines[0].split(',')

  
    contact.append(lines[0].split(','))
    contact.append(lines[1].split(','))
    contact.append(lines[2].split(','))    
    
      
    for thing in contact:
        con = dict(zip(contact[0],thing))
        con2.append(con)
    del con2[0]



# print("this is con2", con2)


def add_contact():
    name = input("Name: ")
    game = input("Game: ")
    pet = input("Pet: ")
    add = False
    for contact in con2:
        if contact == con2:
            print('Name already there')
        elif contact['name'] == name:
            print('Name Added')
        else:
            add = True
    if add:
        con2.append({name:'name', game:'game',pet:'pet'})
   


def retrieve():
    ret = input("Name: ")
    for eve in con2:
        if eve['name'] == ret:
            print(eve)
        
         
            
def update_contact():
    print("Update a contact, Name-Game-Pet")
    up = input("Who do you want to update? ")
    change = input("What do you want to update?: ")
    new_change = input("What is the new info? ")

    for duck in con2:
        if duck['name'] == up:
            if change in duck:
                duck[change] = new_change



print("Create a record: c","Retrieve a record: r","Update a record: u","Delete a record: d")   
user = input("What do you want to do?" )


while True:
    if user == 'c':
        add_contact()
        print('Create a record')
        print(con2)
        break


    elif user == 'r':
        retrieve()
        print('Retrive a record')
        break


    elif user == 'u':
        update_contact()
        print('Update a record')
        print(con2)
        break



    elif user == 'd':
        print("Delete a record")
        break



    
# def add_contact():
#     name = input("Name: ")
#     game = input("Game: ")
#     pet = input("Pet: ")
#     add = False
#     for i in con2:
#         if i.lower() == name.lower():
#             print('Name already there')
#         elif con2[i]['name'].lower() == name.lower():
#             print('Name Added')
#         else:
#             add = True
#     if add:
#         con2.append({name:'name', game:'game',pet:'pet'})
   


# def retrieve(record):
#     pass


# def update(update):
#     pass


# def delete(delete):
#     pass

