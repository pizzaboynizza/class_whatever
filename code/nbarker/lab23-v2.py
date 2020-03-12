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

# def opener(file):
#     contacts_list = []
#     with open(contacts, 'r') as file:
#         text = file.read()
#         lines = text.split('\n')
#         header = lines[0].split(',')
#     for i in range(1, len(lines)):
#         row = lines[i].split(',')
#         print(row)
#         contact = dict(zip(header,row)) 
#         contacts_list.append(contact)
#     print(contact[0])
#     print("These are the contact keys:", contact.keys())
#     print("THese are the contact values:", contact.values())
#     print(contact)
#     print(contacts)
#     return contacts_list

'''
first_name,favorite_fruit,favorite_color
matthew,melons,maroon
ken,kiwi,key_lime
on,rasberries,red
'''

contacts = [{'first_name': 'matthew', 'favorite_fruit': 'melons', 'favorite_color': 'maroon'}, {'first_name': 'ken', 'favorite_fruit': 'kiwi', 'favorite_color': 'key_lime'}, {'first_name': 'ron', 'favorite_fruit': 'rasberries', 'favorite_color': 'red'}]

def print_contact():
    '''
    pretty prints contact
    '''
    print("Let's find someone to print!")
    to_print = input("Who would you like to search for?").lower()
    snippersnapper = next(item for item in contacts if item["first_name"] == to_print)
    print(snippersnapper)

def add_new_contact():     #______________Version 2 (add new entry)
    print("For your new contact: ")    
    first_name = input("Please enter the first name of your new contact:")
    favorite_fruit = input("Please enter the favorite fruit of your new contact:") 
    favorite_color = input("Please enter the favorite color of your new contact:")
    dict2 = [first_name, favorite_fruit, favorite_color]
    print(dict2)
    result = dict(zip(contact, dict2))
    contacts.append(result)

def update_contact(): #____________________updating a contact
    print("Let's find someone to retrieve!")
    from_above = input("Who would you like to search for?").lower()
    snippersnapper = next(item for item in contacts if item["first_name"] == from_above)
    print(snippersnapper)
    if from_above not in contacts:
       add_new_contact()
    else:
        first_name = input("Please enter the first name of the contact to update:")
        favorite_fruit = input("Please enter the updated favorite fruit:")
        favorite_color = input("Please enter the updated favorite color:")
        dict_new = [first_name, favorite_fruit, favorite_color]
        update_result = dict(zip(contact, dict_new))
        contacts.update(update_result)

def delete_contact():
    #_____________________deleting a contact
    print("Let's delete a contact!")
    who_to_delete = input("Who shall we delete?")
    if who_to_delete in dict_values:
        try: contacts.pop(who_to_delete)
        except ValueError:
            print("That entry is not on the list")
    
def retrieve_contact():
    #________________retrieve_contact
    print("Let's find someone to retrieve!")
    from_above = input("Who would you like to search for?").lower()
    snippersnapper = next(item for item in contacts if item["first_name"] == from_above)
    print(snippersnapper)

work = True
#work is True
while work is True:
    print('1. look up a record')
    print('2. update a record')
    print('3. delete a record')
    print('4. print a record')
    print('5. exit')
    action = input("What would you like to do?: ")
    if action == '1':
        retrieve_contact()
    elif action == '2':
        update_contact()
    elif action == '3':
        delete_contact()
    elif action == '4':
        print_contact()
    elif action == '5': 
        work = False
        print("Goodbye!")
        break

