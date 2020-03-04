'''
Nick Barker
3/2/2020-3/4/2020
3:30am


Implement a CRUD REPL
#with extra CRUD

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''
from operator import itemgetter

def opener(path):
    contacts = []
    with open(path, 'r') as file:
        text = file.read()
    lines = text.split('\n')
    header = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(header,row)) 
        contacts.append(contact)
    #print("This is contacts:", contacts)
    #print("This is conTACT:", contact)
    #print("This is the MFING HEADER:", header)
    return contacts, contact, header

contacts, contact, header = opener('contacts.csv')

dict_values = ['matthew', 'melons', 'maroon', 'ken', 'kiwi', 'key_lime', 'ron', 'rasberries', 'red']

def add_new_contact():
#______________Version 2 (add new entry)
    print("For your new contact: ")    
    first_name = input("Please enter the first name of your new contact:")
    favorite_fruit = input("Please enter the favorite fruit of your new contact:") 
    favorite_color = input("Please enter the favorite color of your new contact:")
    dict2 = [first_name, favorite_fruit, favorite_color]
    print(dict2)
    result = dict(zip(contact, dict2))
    contacts.append(result)

add_new_contact()

print(contacts)

def update_contact():
#____________________updating a contact
    print("Let's change some info!")
    already_in = input("Who would you like to update?")
    if already_in not in dict_values:
       add_new_contact()
    else:
        first_name = input("Please enter the first name of the contact tupdate:")
        favorite_fruit = input("Please enter the updated favorite fruit:")
        favorite_color = input("Please enter the updated favorite color:")
        dict_new = [first_name, favorite_fruit, favorite_color]
        update_result = dict(zip(contact, dict_new))
        contacts.append(update_result)

update_contact()

print(contacts)

def delete_contact():
    #_____________________deleting a contact
    print("Let's delete a contact!")
    who_to_delete = input("Who shall we delete?")
    if who_to_delete in dict_values:
        try:contacts.remove(who_to_delete)
        except ValueError:
            print("That entry is not on the list")
    

delete_contact()

def retrieve_contact():
    #________________retrieve_contact
    print("Let's find a pirate!")
    who_to_find = input("Who shall we find?")
    if who_to_find in contacts:
        print()

print('*****')
print([(k, contact[k]) for k in contacts]) 


def endgame():
    while True:
        action = user_input("What would you like to do?: ")
    print('1. look up a record')
    print('2. update a record')
    print('3. delete a record')
    print('4. exit')
        if action == '1':
            retrieve_contact()
        elif action == '2':
            update_contact()
        elif action == '3':
            delete_contact()
        elif action == '4':
            break
        else:
            print("this was the worst lab ever")



