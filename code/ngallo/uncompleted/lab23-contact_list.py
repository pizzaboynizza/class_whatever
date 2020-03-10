while True:

    def get_data():
        list_of_contacts = []
        with open('contacts.csv', 'r') as file:
            text = file.read().split('\n')
        for line in range(1,len(text)):
            header = text[0]
            header = header.split(',')
            names = text[line]
            names = names.split(',')
            list_of_contacts.append(dict(zip(header, names)))
        return list_of_contacts

    ## function to create a contact:
    def create():
        question_create = input("Would you like to add a new contact? ")
        if question_create == 'yes':
            new_contact_name = input("Enter a new name to append to your contact list: ")
            new_contact_mountain = input("Enter your favorite mountain? ")
            new_contact_color = input("Enter your favorite color? ")
            new_contact = {"name":new_contact_name, "favorite mountain":new_contact_mountain, "favorite color":new_contact_color}
            return new_contact
        elif question_create == 'no':
            print("alright then, keep your secrets!  ")
            
        else: 
            print("Try 'yes' or 'no'")

    def start():
        print("**********Hello, welcome to your contact list***********\n")
        data = get_data()
        person = create()
        if person: 
            data.append(person)
        contact = retrieved(data)
        if contact:
            print(f"here is {contact['name']}\'s data: {contact}")

    def retrieved(data):
        question_retrieved = input("Would you like to lookup a contact? ")
        if question_retrieved == 'yes':
            input_to_call_dictionary_data = input("Who\'s data would you like to look up? ")
            for contact in data:
                if contact['name'] == input_to_call_dictionary_data: 
                    return contact
        elif question_retrieved == 'no':
            print("alright then, I'll keep my secrets! ")
        else: 
            print("Try 'yes' or 'no'")
    start()
# function to retrieve data:
    # def update(line):
    #     question_update = input("Would you like to make an update to a contact? ")
    #     if question_update == 'yes':
    #         update_contact = input("Who\'s contact would you like to change? ")
    #         update(line)
    #     elif question_update == 'no':
    #         print("okay, no changes to be made.")
    #     else:
    #         print("Try 'yes' or 'no'")
    #         update(line)
    # update(line)


    # def delete(line):
    #     question_delete = input("Are there any deletions you'd like to make? ")
    #     if question_delete == 'yes':
    #         delete_contact = input("Who\'s contact information would you like to delete? ")
    #         delete(line)
    #     elif question_delete == 'no':
    #         print("No changes to be made")
    #     else:
    #         print("Try 'yes' or 'no'")
    #         delete(line)
    # delete(line)


'''
Lab 23: Contact List
Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
Note: There is a csv library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.

Version 2
Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
Version 3
When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.
'''

