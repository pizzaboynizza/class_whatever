# /n spare rows in the csv





contact = []
# open csv contact withopen as file
with open("contact.csv", 'r') as file:
    #split the lines in the file
    lines = file.read().split('\n')
    
    con2 = []
    key = lines[0].split(',')

  
    contact.append(lines[0].split(','))
    contact.append(lines[1].split(','))
    contact.append(lines[2].split(','))    
    
      
    for thing in contact:
        #zip the leys with values and looping thought them
        con = dict(zip(contact[0],thing))
        con2.append(con)
    del con2[0]

# This is a fuc to add a new contact to the csv
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
        con2.append({'name':name, 'game':game,'pet':pet})

# this is how you look up a name in the csv file
def retrieve():
    ret = input("Name: ")
    for eve in con2:
        if eve['name'] == ret:
            print(eve)                 

#how to update a contact within the csv
def update_contact():
    print("Update a contact,Pick what one you want to update Name, Game and Pet")
    up = input("Who do you want to update? ")
    change = input("What do you want to update?: ")
    new_change = input("What is the new info? ")
# running a for loop to look thought each item in the list of dic to compaire the names with the keys
    for duck in con2:
        if duck['name'] == up:
            if change in duck:
                duck[change] = new_change

# how to delete a contact with in the csv
def delete():
    print("What contact do you want to delete?")
    dele = input("Who do you want to delete? ")
    for life in con2:
        if life['name'] in dele:
            con2.remove(life)


while True:
#this loop thought the whole loop
    print("Create a record: c","Retrieve a record: r","Update a record: u","Delete a record: d")
    print(f"This is the curret address book {con2}")   
    user = input("What do you want to do?" )
    

    if user == 'c':
        add_contact()
        print('Create a record')
    elif user == 'r':
        retrieve()
        print('Retrive a record')
    elif user == 'u':
        update_contact()
        print('Update a record')
    elif user == 'd':
        delete()
        print("Delete a record")
    elif user == 'no':
        break
        


with open("contact.csv", 'w') as file:
    newcon = []
    djoin = []
    jd = []
    done = []
    newcon.append(list(con2[0].keys()))
    
    for x in con2:
        newcon.append(list(x.values()))

    for g in newcon:
        jd = ','.join(g)
        djoin.append(jd)


    done = '\n'.join(djoin)
    print(done)

    file.write(done)







  
   



