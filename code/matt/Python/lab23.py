"""
Version 1
    Let's build a program to manage a list of contacts. 
    To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. 
    Headers might consist of name, favorite fruit, favorite color. 
    Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. 
    The text in the header represents the keys, the text in the other lines represent the values.
"""
# def call_contacts():
with open('contacts.csv', 'r') as file:
    lines = file.read().split("\n")

contact = []
contact_actually = []
key = lines[0].split(",")

for line in lines:
    line.split(",")
    contact.append(line)

for thing in contact:
    split_thing = thing.split(",")
    workplease = dict(zip(key, split_thing))
    contact_actually.append(workplease)
del contact_actually[0]
"""
Version 2
    Implement a CRUD REPL

    Create a record: ask the user for each attribute, add a new contact to your contact 
        list with the attributes that the user entered.
    Retrieve a record: ask the user for the contact's name, find the user 
        with the given name, and display their information
    Update a record: ask the user for the contact's name, then for which attribute 
        of the user they'd like to update and the value of the attribute they'd like to set.
    Delete a record: ask the user for the contact's name, remove the contact with the given 
        name from the contact list.
    """


def welcome():
    while True:
        user_input = input(f"""Enter the number of the action to perform:
    1: Create a new Contact
    2: Retrieve a specific record (by Name)
    3: Update a specific record (by Name)
    4: Delete a specific record (by Name)
    5: Exit
Your option: """)
        if user_input == "1":
            contact_add()
        elif user_input == "2":
            contact_retrieve()
        elif user_input == "3":
            contact_update()
        elif user_input == "4":
            contact_delete()
        elif user_input == "5":
            print("Okay, bye.")
            # contact_exit()
            break
        else:
            print("something went wrong. try again.")



def name_input():
    nametest = ""
    while nametest.lower() not in ["yes", "y"]:
        name_input = input("Enter Contact name: ")
        nametest = input(f"The contact's name is {name_input}. Is this correct? (Yes or No): ")
        if nametest.lower() in ["yes", "y"]:
            print(f"Adding {name_input}.")
            return name_input
        else:
            print("Try Again.")


def game_input():
    gametest = ""
    while gametest.lower() not in ["yes", "y"]:
        game_input = input("Enter Contact's Favorite Game: ")
        gametest = input(f"Their favorite game is {game_input}. Is this correct? (Yes or No): ")
        if gametest.lower() in ["yes", "y"]:
            print(f"Adding {game_input}.")
            return game_input
        else:
            print("Try Again.")


def color_input():
    colortest = ""
    while colortest.lower() not in ["yes", "y"]:
        color_input = input("Enter Contact's Favorite Color: ")
        colortest = input(f"The contact's favorite color is {color_input}. Is this correct? (Yes or No): ")
        if colortest.lower() in ["yes", "y"]:
            print(f"Their favorite color is {color_input}.")
            return color_input
        else:
            print("Try again.")


def infected_input():
    infectedtest = ""
    while infectedtest.lower() not in ["yes", "y"]:
        infected_input = input("Is this Contact infected? (Yes or No): ")
        infectedtest = input(f"You entered {infected_input}. Is this correct? (Yes or No): ")
        if infectedtest.lower() in ["yes", "y"]:
            print(f"Adding {infected_input} to their infection status.")
            return infected_input
        else:
            print("Try again.")


def contact_add():
    print("Adding a Contact:")
    contact = [name_input(),game_input(),color_input(),infected_input()]
    new_contact = dict(zip(key, contact))
    contact_actually.append(new_contact)


def contact_retrieve():
    lookup = input("Enter contact name to look up: ")
    for name in contact_actually:
        if name["name"] in lookup:
            print(name)


def contact_delete():
    lookup = input("Enter contact name to delete: ")
    for name in contact_actually:
        if name["name"] in lookup:
            delete_test = input(f"You are about to delete {lookup}. Are you sure? (Y/N): ")
            
    if delete_test.lower() in ["yes", "y"]:
        for name in contact_actually:
            if name["name"] in lookup:
                contact_actually.remove(name)


def contact_update():
    lookup = input("Enter contact name to update: ")
    for name in contact_actually:
        if name["name"] in lookup:
            update_test = input(f"You want to update {name}. Is this correct? (Y/N): ")
            if update_test.lower() in ["yes", "y"]:
                update_item = input(f"""Items available to update for {name}:
        1. Name
        2. Favorite Game
        3. Favorite Color
        4. Infected Status
        5. Exit (Done)
Enter the number for the item you wish to update: """)
                if update_item == "1":
                    name["name"] = input("Type their new Name: ")
                elif update_item == "2":
                    name["favorite game"] = input("Type their new Favorite Game: ")
                elif update_item == "3":
                    name["favorite color"] = input("Type their new Favorite Color: ")
                elif update_item == "4":
                    name["infected?"] = input("Enter their current Infected Status (Yes/No): ")
                elif update_item == "5":
                    print("Okay, bye.")
                else:
                    print("something went wrong. try again.")
            print(f"Contact is now {name}")


welcome()
# contact_add()
# contact_retrieve()
# contact_delete()
# contact_update()


list_keys = []
list_keys.append(list(contact_actually[0].keys()))

for x in contact_actually:
    list_keys.append(list(x.values()))

unit_out = []
for blah in list_keys:
    unit_out.append(",".join(blah))

lines_out = "\n".join(unit_out)
with open('contacts.csv', 'w') as contact_list_file:
    contact_list_file.write(lines_out)